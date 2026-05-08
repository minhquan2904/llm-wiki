---
title: "Apache Kafka"
source: "compiled"
date_added: 2026-04-23
tags: [tool, message-broker, data-streaming, distributed-systems]
aliases: [Kafka]
status: reviewed
related:
  - "[[rabbitmq]]"
  - "[[kafka-vs-rabbitmq]]"
  - "[[kafka-replication]]"
  - "[[kafka-connect]]"
  - "[[kafka-streams]]"
  - "[[kafka-producer]]"
  - "[[kafka-consumer]]"
  - "[[kafka-mirrormaker]]"
  - "[[kafka-administration]]"
  - "[[kafka-monitoring]]"
summary: "Nền tảng xử lý luồng sự kiện phân tán, nổi bật với thông lượng cao và khả năng lưu trữ dữ liệu thời gian thực."
---

## Tổng Quan

Apache Kafka là một nền tảng xử lý luồng sự kiện (event streaming platform) phân tán, mã nguồn mở, được thiết kế cho các ứng dụng yêu cầu xử lý dữ liệu với thông lượng khổng lồ, độ trễ thấp và khả năng mở rộng cao. Ban đầu được phát triển tại LinkedIn bởi Jay Kreps, Neha Narkhede và Jun Rao để giải quyết vấn đề xử lý dữ liệu thời gian thực, Kafka sau đó được mở mã nguồn vào năm 2011 dưới sự quản lý của Apache Software Foundation.

Kafka thường được mô tả là "distributed commit log" — một hệ thống lưu trữ bền vững và có thứ tự, cho phép replay dữ liệu để tái tạo trạng thái hệ thống. LinkedIn sử dụng Kafka xử lý hơn một nghìn tỷ message mỗi ngày (tính đến 2015).

## Kiến Trúc Cốt Lõi

Kiến trúc của Kafka xoay quanh một dịch vụ nhật ký lưu trữ (commit log) phân tán và được sao chép. Các thành phần cơ bản bao gồm:

**Brokers** — Các máy chủ lưu trữ và quản lý dữ liệu. Một tập hợp các Brokers tạo thành một Cluster. Mỗi broker đăng ký danh tính qua ephemeral node trên ZooKeeper; khi broker ngừng hoạt động, node biến mất và cluster được thông báo tự động.

**Topics và Partitions** — Topics là danh mục logic nơi dữ liệu được xuất bản. Topics được chia nhỏ thành các partition, cho phép xử lý song song và mở rộng theo chiều ngang. Mỗi partition được lưu trữ dưới dạng các **segment** (mặc định 1 GB hoặc 1 tuần dữ liệu, tùy giới hạn nào đạt trước). Segment đang ghi gọi là active segment và không bao giờ bị xóa.

**Producers** — Các thực thể đẩy (publish) dữ liệu vào Kafka. Client xác định broker đích qua metadata request, sau đó gửi produce request trực tiếp tới Leader replica của partition tương ứng.

**Consumers và Consumer Groups** — Các thực thể đọc dữ liệu. Consumer Group cho phép chia sẻ tải tiêu thụ dữ liệu trên nhiều tiến trình. Consumer chỉ đọc được message đã committed — tức đã replicate tới tất cả in-sync replica.

**Leaders và Followers** — Cơ chế [[kafka-replication]] trong đó Leader xử lý đọc/ghi, Followers sao chép dữ liệu thụ động. Chỉ các in-sync replica đủ tư cách trở thành Leader mới khi Leader hiện tại gặp sự cố.

## Lưu Trữ Vật Lý

Kafka sử dụng định dạng message giống nhau trên đĩa và trên đường truyền, cho phép tối ưu hóa **zero-copy** — gửi dữ liệu từ filesystem cache thẳng tới network channel mà không qua buffer trung gian. Mỗi partition duy trì **index** ánh xạ offset tới vị trí trong segment file, giúp Consumer bắt đầu đọc từ bất kỳ offset nào một cách nhanh chóng.

Hai chính sách retention được hỗ trợ: **delete** (xóa message cũ hơn thời gian retention) và **compact** (giữ lại giá trị mới nhất cho mỗi key). Log compaction hoạt động bằng cách chia log thành phần "clean" (đã compact) và "dirty" (chưa compact), sử dụng in-memory offset map 24 byte/entry để xác định message nào cần giữ.

## Xử Lý Request

Broker sử dụng kiến trúc đa luồng: **acceptor thread** nhận kết nối, **network threads** (processor) đặt request vào request queue và gửi response, **IO threads** xử lý request thực tế. Hai loại request chính là **Produce request** (ghi message) và **Fetch request** (đọc message). Client định tuyến request thông qua metadata cache chứa thông tin về partition leader, được refresh định kỳ qua `metadata.max.age.ms`.

Khi `acks=all`, produce request được lưu trong **purgatory** cho đến khi tất cả ISR xác nhận nhận message. Consumer có thể đặt giới hạn dung lượng tối thiểu (`fetch.min.bytes`) — broker chờ tích lũy đủ dữ liệu trước khi phản hồi, giảm overhead network.

## Hệ Sinh Thái Mở Rộng

**[[kafka-connect]]** — Framework tích hợp dữ liệu với kiến trúc Connector-Task-Worker, di chuyển dữ liệu giữa Kafka và các hệ thống bên ngoài (database, search engine, cloud storage) mà không cần viết code.

**[[kafka-streams]]** — Thư viện xử lý luồng sự kiện tích hợp, hỗ trợ windowing, aggregation, stream-table join và quản lý trạng thái cục bộ (local state) qua RocksDB. Chạy như ứng dụng Java thông thường, không yêu cầu cluster riêng.

**[[kafka-replication]]** — Cơ chế sao chép Leader/Follower với ISR đảm bảo tính bền vững và sẵn sàng. Cấu hình `replication.factor`, `min.insync.replicas` và `acks` cho phép điều chỉnh trade-off giữa an toàn dữ liệu và hiệu suất.

## Vai Trò Trong Hệ Thống (Use Cases)

Kafka thường được sử dụng làm "xương sống" (backbone) cho liên lạc giữa các dịch vụ trong kiến trúc phân tán:

- **Data Streaming** — Nhập và xử lý khối lượng dữ liệu khổng lồ theo thời gian thực (tổng hợp nhật ký, lưu trữ dữ liệu).
- **Phân tích thời gian thực** — Cung cấp luồng dữ liệu cho các công cụ phân tích.
- **Event Sourcing** — Kiến trúc hướng sự kiện, lưu lại toàn bộ lịch sử thay đổi trạng thái.
- **Data Pipelines** — Đóng vai trò bộ đệm trung tâm giữa nguồn và đích, tách biệt thời gian và thông lượng giữa các giai đoạn pipeline.

## Cài Đặt và Hạ Tầng

Kafka yêu cầu Java 8+ và Apache ZooKeeper để lưu trữ metadata (broker registry, topic config, consumer group). ZooKeeper ensemble khuyến nghị triển khai số lẻ node (3 hoặc 5) để đảm bảo quorum; nên dùng chroot path riêng cho mỗi Kafka cluster để chia sẻ ensemble.

Lựa chọn phần cứng: **Disk throughput** ảnh hưởng trực tiếp đến produce latency — SSD cho hiệu năng tốt nhất, HDD tiết kiệm chi phí có thể bù bằng RAID hoặc nhiều mount point. **Memory** ưu tiên cho page cache (không cần heap JVM lớn — 5 GB là đủ cho hầu hết workload). **Network** thường là nút thắt chính khi có nhiều consumer và replication. Filesystem khuyến nghị: XFS với mount option `noatime`. OS tuning: `vm.swappiness=1`, `vm.dirty_background_ratio=5`.

Về GC, khuyến nghị sử dụng G1GC với `MaxGCPauseMillis=20` và `InitiatingHeapOccupancyPercent=35`. Xem thêm [[kafka-administration]] cho quy trình vận hành chi tiết.

## Lợi Thế và Hạn Chế

**Lợi Thế:**
- **Thông lượng cực cao** — Xử lý hàng triệu sự kiện mỗi giây, tối ưu qua zero-copy và batching.
- **Khả năng mở rộng ngang** — Thêm Broker vào Cluster, partition tự động phân bổ.
- **Độ bền dữ liệu** — Lưu trữ trên đĩa và sao chép đa broker; tính bền vững hoàn toàn dựa vào replication, không chờ flush xuống đĩa.
- **Luồng xử lý tích hợp** — Kafka Streams và Kafka Connect đi kèm, không cần framework bên ngoài.

**Hạn Chế:**
- **Độ phức tạp** — Cấu hình và quản lý cluster đòi hỏi kiến thức chuyên sâu về replication, ISR và retention (xem [[kafka-monitoring]]).
- **Định tuyến hạn chế** — Phụ thuộc vào Topics/Partitions, không có cơ chế định tuyến thông điệp phức tạp theo nội dung như [[rabbitmq]].
- **Hiệu suất suy giảm do nén** — Quá trình nén/giải nén luồng dữ liệu có thể ảnh hưởng đến hiệu quả xử lý tổng thể.

## Nguồn Tham Khảo

- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide* (O'Reilly, 2017)
