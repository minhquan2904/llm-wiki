---
title: "Kafka Replication"
source: "compiled"
date_added: 2026-05-08
tags: [concept, kafka, distributed-systems, replication, fault-tolerance]
aliases: [Kafka Replication, ISR, In-Sync Replicas, Sao chép Kafka]
status: reviewed
related:
  - "[[apache-kafka]]"
  - "[[kafka-connect]]"
  - "[[kafka-streams]]"
  - "[[publish-subscribe]]"
summary: "Cơ chế sao chép dữ liệu trong Apache Kafka — nền tảng đảm bảo tính sẵn sàng và bền vững thông qua Leader/Follower, ISR và các cấu hình tin cậy."
---

## Định Nghĩa

Replication là cơ chế cốt lõi đảm bảo tính sẵn sàng (availability) và bền vững dữ liệu (durability) trong [[apache-kafka]]. Mỗi partition của một topic được sao chép thành nhiều bản (replica) và phân tán trên các broker khác nhau trong cluster. Tài liệu chính thức mô tả Kafka là "a distributed, partitioned, replicated commit log service" — replication đứng ở vị trí trung tâm của kiến trúc này.

## Leader và Follower

Mỗi partition có đúng một **Leader replica** và một hoặc nhiều **Follower replica**. Mọi yêu cầu đọc/ghi từ Producer và Consumer đều đi qua Leader để đảm bảo tính nhất quán. Follower không phục vụ yêu cầu từ client — nhiệm vụ duy nhất của chúng là sao chép dữ liệu từ Leader bằng cách gửi Fetch request, cùng cơ chế mà Consumer sử dụng.

Follower gửi Fetch request tuần tự: yêu cầu message 1, rồi message 2, rồi message 3. Khi Follower yêu cầu message 4, Leader biết rằng Follower đã nhận đủ các message trước đó. Cơ chế tuần tự này cho phép Leader theo dõi chính xác tiến trình sao chép của từng Follower.

## In-Sync Replicas (ISR)

Khái niệm ISR phân tách các replica thành hai nhóm: **in-sync** và **out-of-sync**. Một Follower được coi là in-sync khi thỏa mãn đồng thời hai điều kiện: đã gửi Fetch request trong vòng 10 giây gần nhất (mặc định `replica.lag.time.max.ms`) và đã bắt kịp message mới nhất từ Leader trong khoảng thời gian đó.

Khi Follower mất kết nối, ngừng fetch, hoặc bị tụt lại quá lâu, nó bị đánh dấu out-of-sync và không còn đủ điều kiện trở thành Leader mới khi Leader hiện tại gặp sự cố. Chỉ các in-sync replica mới đủ tư cách tham gia bầu cử Leader.

Hiện tượng replica liên tục dao động giữa trạng thái in-sync và out-of-sync thường là dấu hiệu của cấu hình garbage collection sai trên broker — JVM tạm dừng vài giây khiến broker mất kết nối tới ZooKeeper.

## Controller và Bầu Cử Leader

**Controller** là một broker đặc biệt trong cluster, ngoài chức năng broker thông thường, còn chịu trách nhiệm bầu chọn Leader cho các partition. Broker đầu tiên khởi động tạo một ephemeral node `/controller` trong ZooKeeper và trở thành Controller. Các broker khác tạo watch trên node này để được thông báo khi Controller thay đổi.

Mỗi lần Controller mới được bầu, nó nhận một **controller epoch** tăng dần qua thao tác conditional increment trên ZooKeeper. Epoch number ngăn chặn tình huống "split brain" — nếu broker nhận message từ Controller có epoch cũ hơn, message đó bị bỏ qua.

Khi Controller phát hiện broker rời cluster, nó xác định các partition cần Leader mới, chọn replica tiếp theo trong danh sách replica làm Leader, và gửi `LeaderAndIsr` request tới các broker liên quan.

## Preferred Leader và Cân Bằng Tải

Khi topic được tạo, replica đầu tiên trong danh sách replica của mỗi partition trở thành **preferred leader**. Kafka phân bổ Leader đều giữa các broker tại thời điểm tạo topic. Với cấu hình `auto.leader.rebalance.enable=true` (mặc định), cluster tự động kiểm tra và bầu lại preferred leader khi nó đang in-sync nhưng không phải Leader hiện tại, nhằm duy trì cân bằng tải.

## Cấu Hình Tin Cậy

Ba tham số cấu hình quyết định mức độ tin cậy của hệ thống:

**`replication.factor`** — Số lượng replica cho mỗi partition. Giá trị N cho phép mất N-1 broker mà không ảnh hưởng đến khả năng đọc/ghi. Khuyến nghị phổ biến là 3; các hệ thống ngân hàng đôi khi sử dụng 5. Khi có thông tin rack (`broker.rack`), Kafka phân bổ replica trên các rack khác nhau để đảm bảo sẵn sàng khi cả rack gặp sự cố.

**`min.insync.replicas`** — Số replica in-sync tối thiểu để broker chấp nhận ghi. Với giá trị 2, nếu chỉ còn 1 replica in-sync, partition trở thành read-only — Producer nhận `NotEnoughReplicasException`. Cấu hình này kết hợp với `acks=all` tạo thành lớp bảo vệ mạnh nhất cho dữ liệu.

**`unclean.leader.election.enable`** — Cho phép hoặc cấm replica out-of-sync trở thành Leader. Bật (true) ưu tiên tính sẵn sàng nhưng chấp nhận mất dữ liệu. Tắt (false) đảm bảo tính nhất quán nhưng partition có thể offline cho đến khi Leader cũ phục hồi. Hệ thống ngân hàng thường tắt tùy chọn này; hệ thống phân tích clickstream thường bật.

## Acks và Producer

Cấu hình `acks` ở phía Producer quyết định thời điểm message được coi là "ghi thành công":

- `acks=0` — Không chờ xác nhận từ broker. Thông lượng cao nhất, rủi ro mất dữ liệu cao nhất.
- `acks=1` — Leader xác nhận sau khi ghi vào partition data file. Có thể mất dữ liệu nếu Leader crash trước khi replicate.
- `acks=all` — Leader chờ tất cả ISR nhận message trước khi xác nhận. An toàn nhất nhưng chậm nhất.

Kafka không chờ dữ liệu flush xuống đĩa — tính bền vững hoàn toàn dựa vào replication.

## Commit và Khả Năng Đọc

Consumer chỉ đọc được các message đã **committed** — tức đã được ghi vào tất cả in-sync replica. Message chưa replicate đầy đủ được coi là "unsafe" và không hiển thị cho Consumer. Nếu Leader crash trước khi replicate, message chỉ tồn tại trên Leader sẽ biến mất mà Consumer không bao giờ biết đến — đảm bảo tính nhất quán cho toàn hệ thống.

Cơ chế này cũng đồng nghĩa: nếu replication chậm, Consumer sẽ chậm nhận message mới. Độ trễ tối đa bị giới hạn bởi `replica.lag.time.max.ms`.

## Nguồn Tham Khảo

- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide* (O'Reilly, 2017), Chapter 5: Kafka Internals
- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide* (O'Reilly, 2017), Chapter 6: Reliable Data Delivery
