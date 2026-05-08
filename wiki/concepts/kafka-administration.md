---
title: "Kafka Administration"
source: "compiled"
date_added: 2026-05-08
tags: [concept, kafka, administration, operations, cli-tools]
aliases: [Kafka Administration, Quản trị Kafka, Kafka Admin Tools]
status: reviewed
related:
  - "[[apache-kafka]]"
  - "[[kafka-replication]]"
  - "[[kafka-monitoring]]"
  - "[[kafka-mirrormaker]]"
summary: "Tổng hợp công cụ và quy trình quản trị cụm Apache Kafka — bao gồm quản lý topic, partition reassignment, consumer group và các thao tác khẩn cấp."
---

## Định Nghĩa

Kafka Administration bao gồm tập hợp các công cụ dòng lệnh (CLI) và quy trình vận hành để quản lý một cụm [[apache-kafka]] ở môi trường production. Các công cụ chính giao tiếp với cụm thông qua ZooKeeper hoặc trực tiếp với broker, hỗ trợ tạo/sửa/xóa topic, quản lý consumer group, di chuyển partition và ghi đè cấu hình.

## Quản Lý Topic

Công cụ `kafka-topics.sh` hỗ trợ bốn thao tác chính:

**Tạo topic** — Chỉ định tên, số partition và replication factor. Nếu `auto.create.topics.enable=true` trên broker, topic tự động được tạo khi producer ghi hoặc consumer đọc, nhưng môi trường production nên tắt tính năng này để kiểm soát chặt chẽ.

**Liệt kê topic** — Hiển thị danh sách toàn bộ topic trong cụm bằng `--list`.

**Mô tả topic** — `--describe` hiển thị số partition, replication factor, cấu hình override và trạng thái ISR của từng partition. Tùy chọn `--under-replicated-partitions` lọc ra các partition có bản sao bị thiếu — chỉ số cảnh báo quan trọng.

**Tăng partition** — Chỉ cho phép tăng, không giảm số partition. Nếu dữ liệu sử dụng key-based partitioning, thay đổi số partition sẽ phá vỡ mapping key-to-partition (xem [[kafka-producer]]).

## Quản Lý Consumer Group

Công cụ `kafka-consumer-groups.sh` cho phép liệt kê group, xem offset hiện tại, lag và trạng thái từng consumer. Các thao tác offset:

**Export offset** — Xuất offset hiện tại ra file CSV để backup.

**Import offset** — Nhập offset từ file CSV, cho phép rollback consumer về thời điểm trước đó (yêu cầu tất cả consumer trong group phải dừng trước).

Quản lý offset rất quan trọng trong các tình huống reprocess dữ liệu hoặc khôi phục sau sự cố.

## Cấu Hình Động

`kafka-configs.sh` cho phép thay đổi cấu hình topic và client tại runtime mà không cần restart broker:

**Override topic** — Thêm/xóa override cho từng topic (VD: `retention.ms`, `max.message.bytes`). Override được lưu trong ZooKeeper và ưu tiên hơn cấu hình mặc định của broker.

**Override client** — Áp dụng quota cho producer/consumer client ID (VD: giới hạn throughput `producer_byte_rate`, `consumer_byte_rate`).

## Partition Reassignment

Khi cần cân bằng tải giữa các broker (thêm broker mới, loại bỏ broker cũ), sử dụng `kafka-reassign-partitions.sh`:

(1) Tạo danh sách topic cần di chuyển (file JSON). (2) Chạy `--generate` để Kafka đề xuất bản phân bổ mới. (3) Chạy `--execute` để áp dụng. (4) Chạy `--verify` để kiểm tra tiến độ.

Reassignment có thể ảnh hưởng đáng kể tới hiệu năng cụm vì broker phải replicate toàn bộ dữ liệu partition sang broker đích. Nên thực hiện từng đợt nhỏ và giám sát qua [[kafka-monitoring]].

## Preferred Replica Election

Mỗi partition có danh sách replica theo thứ tự ưu tiên — replica đầu tiên là preferred leader. Sau nhiều lần failover, leader có thể không còn là preferred replica, gây phân bổ tải không đều. Chạy `kafka-preferred-replica-election.sh` để khôi phục leader về preferred replica.

Kafka broker có tùy chọn `auto.leader.rebalance.enable` tự động chạy preferred election, nhưng sách *Definitive Guide* khuyến cáo **không bật** tại production vì có thể gây chuyển leader bất ngờ dưới tải cao.

## Console Producer và Consumer

`kafka-console-producer.sh` và `kafka-console-consumer.sh` là công cụ gỡ lỗi cho phép đọc/ghi message thủ công. Hỗ trợ chỉ định serializer, formatter, tùy chọn `--from-beginning` và `--max-messages`. Có thể đọc topic nội bộ `__consumer_offsets` bằng `OffsetsMessageFormatter` để kiểm tra commit offset.

## Thao Tác Khẩn Cấp

Các thao tác nguy hiểm chỉ dùng trong tình huống đặc biệt, thao tác trực tiếp trên ZooKeeper:

**Di chuyển Controller** — Xóa znode `/controller` để buộc cluster bầu controller mới. Dùng khi controller bị treo nhưng vẫn giữ kết nối.

**Hủy Partition Move** — Xóa znode `/admin/reassign_partitions` rồi di chuyển controller để buộc cluster quên reassignment đang dở. Cần kiểm tra replication factor sau thao tác.

**Xóa Topic thủ công** — Yêu cầu tắt toàn bộ broker trước khi xóa znode topic và thư mục dữ liệu trên đĩa. Không bao giờ thực hiện khi cluster đang online.

## Nguồn Tham Khảo

- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide*, Chapter 9 (O'Reilly, 2017)
