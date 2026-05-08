---
title: "Kafka Streams"
source: "compiled"
date_added: 2026-05-08
tags: [concept, kafka, stream-processing, distributed-systems, kafka-streams]
aliases: [Kafka Streams, Kafka Streams API, Xử lý luồng Kafka]
status: reviewed
related:
  - "[[apache-kafka]]"
  - "[[kafka-replication]]"
  - "[[kafka-connect]]"
  - "[[publish-subscribe]]"
summary: "Thư viện xử lý luồng sự kiện tích hợp trong Apache Kafka — hỗ trợ topology, windowing, state management và stream-table duality."
---

## Định Nghĩa

Kafka Streams là thư viện xử lý luồng (stream processing library) được tích hợp trong [[apache-kafka]] từ phiên bản 0.10.0. Khác với các framework xử lý luồng độc lập như Apache Flink hay Spark Streaming, Kafka Streams là một thư viện Java thuần — ứng dụng sử dụng nó chạy như một tiến trình thông thường, không yêu cầu cài đặt cluster riêng. Để mở rộng, chỉ cần khởi chạy thêm instance của cùng ứng dụng.

## Mô Hình Luồng Dữ Liệu

Xử lý luồng (stream processing) là mô hình lập trình xử lý liên tục một hoặc nhiều luồng sự kiện không giới hạn (unbounded dataset). Luồng sự kiện có ba đặc tính cốt lõi: **có thứ tự** (ordered) — thứ tự sự kiện mang ý nghĩa nghiệp vụ; **bất biến** (immutable) — sự kiện đã xảy ra không thể sửa đổi, chỉ có thể ghi thêm sự kiện hủy bỏ; và **có thể phát lại** (replayable) — khả năng phát lại luồng sự kiện từ quá khứ phục vụ sửa lỗi, phân tích mới hoặc kiểm toán.

Mô hình này lấp khoảng trống giữa request-response (độ trễ mili-giây, đồng bộ) và batch processing (độ trễ hàng giờ, thông lượng cao). Phần lớn nghiệp vụ doanh nghiệp — cảnh báo giao dịch đáng ngờ, điều chỉnh giá real-time, theo dõi vận chuyển — phù hợp với mô hình xử lý liên tục, không chặn này.

## Tính Đối Ngẫu Stream-Table

Stream và Table là hai mặt của cùng một thực tế: stream ghi lại lịch sử thay đổi, table phản ánh trạng thái hiện tại. Chuyển table thành stream yêu cầu Change Data Capture (CDC) — ghi lại mọi INSERT, UPDATE, DELETE dưới dạng sự kiện. Chuyển stream thành table (gọi là **materializing**) yêu cầu áp dụng tuần tự tất cả sự kiện từ đầu đến cuối để tái tạo trạng thái tại một thời điểm.

Kafka Streams biểu diễn tính đối ngẫu này qua hai abstraction: `KStream` (luồng sự kiện) và `KTable` (bảng cập nhật liên tục). KTable duy trì bản sao cục bộ (local cache) của dữ liệu và tự động cập nhật khi nhận sự kiện thay đổi từ Kafka topic.

## Cửa Sổ Thời Gian (Windowing)

Hầu hết các phép toán trên luồng sự kiện đều là phép toán trên cửa sổ thời gian — trung bình trượt, top sản phẩm tuần này, phân vị 99 của tải hệ thống. Kafka Streams hỗ trợ ba loại cửa sổ:

**Tumbling window** — Cửa sổ cố định, không chồng lấn. Khi advance interval bằng kích thước cửa sổ (ví dụ: cửa sổ 5 phút, trượt mỗi 5 phút), mỗi sự kiện thuộc đúng một cửa sổ.

**Hopping window** — Cửa sổ chồng lấn. Advance interval nhỏ hơn kích thước cửa sổ (ví dụ: cửa sổ 5 phút, trượt mỗi 1 phút), mỗi sự kiện có thể thuộc nhiều cửa sổ.

**Sliding window** — Cửa sổ trượt theo từng bản ghi, không gắn với đồng hồ. Sử dụng trong join hai luồng theo khoảng thời gian.

Ba yếu tố cần xác định cho mỗi cửa sổ: kích thước (window size), tần suất cập nhật (advance interval), và thời gian cửa sổ còn chấp nhận sự kiện trễ (grace period).

## Quản Lý Trạng Thái (State Management)

Xử lý luồng trở nên phức tạp khi phép toán liên quan nhiều sự kiện — đếm, trung bình trượt, join. Kafka Streams quản lý trạng thái cục bộ (local state) bằng embedded RocksDB, đồng thời gửi mọi thay đổi trạng thái về một Kafka topic (sử dụng [[kafka-replication]] qua log compaction). Khi một instance gặp sự cố, trạng thái được khôi phục bằng cách đọc lại topic đó.

Cơ chế này giải quyết ba thách thức: **bộ nhớ** — RocksDB lưu trên đĩa, không bị giới hạn bởi RAM; **bền vững** — trạng thái được sao lưu về Kafka, khôi phục nhanh khi khởi động lại; **rebalancing** — khi partition được gán lại cho instance khác, instance mới tái tạo trạng thái từ Kafka topic.

## Các Mẫu Thiết Kế

**Single-Event Processing (Map/Filter)** — Xử lý từng sự kiện độc lập: lọc, chuyển đổi định dạng. Không cần duy trì trạng thái, dễ mở rộng và khôi phục.

**Processing with Local State** — Aggregation theo nhóm (group by). Kafka partitioner đảm bảo các sự kiện cùng key đến cùng partition, cho phép mỗi instance duy trì trạng thái chỉ cho tập con key được gán.

**Stream-Table Join** — Làm giàu sự kiện bằng dữ liệu từ bảng tham chiếu. Thay vì truy vấn database bên ngoài (tốn 5-15ms/record, không scale), ứng dụng duy trì bản sao cục bộ của bảng qua CDC stream và thực hiện lookup cục bộ.

**Stream-Stream Join (Windowed Join)** — Join hai luồng sự kiện dựa trên khóa chung và cửa sổ thời gian. Kafka Streams đảm bảo các partition tương ứng của hai topic được gán cho cùng một task.

**Reprocessing** — Kafka lưu trữ luồng sự kiện lâu dài, cho phép chạy phiên bản mới của ứng dụng song song với phiên bản cũ (consumer group mới, đọc từ offset đầu tiên), so sánh kết quả trước khi chuyển đổi.

## Kiến Trúc Topology

Mọi ứng dụng Kafka Streams xây dựng và thực thi ít nhất một **topology** — đồ thị có hướng không chu trình (DAG) của các phép biến đổi. Topology bao gồm: **Source processor** đọc dữ liệu từ topic, **Stream processor** thực hiện biến đổi (filter, map, aggregate, join), và **Sink processor** ghi kết quả vào topic đầu ra.

Ứng dụng tạo topology qua `StreamBuilder`, sau đó tạo `KafkaStreams` execution object. Khi khởi chạy, object này sinh nhiều thread, mỗi thread áp dụng topology lên các sự kiện trong luồng. Mở rộng bằng cách chạy nhiều instance — các instance tự phối hợp và phân chia partition.

## Xử Lý Thời Gian

Kafka Streams phân biệt ba khái niệm thời gian: **Event time** — thời điểm sự kiện xảy ra, quan trọng nhất cho nghiệp vụ; **Log append time** — thời điểm broker nhận sự kiện; **Processing time** — thời điểm ứng dụng xử lý sự kiện, không đáng tin cậy do phụ thuộc vào thời điểm đọc.

Sự kiện đến trễ (out-of-sequence) được xử lý bằng cách duy trì nhiều cửa sổ aggregation trong local state. Kết quả aggregation được ghi vào compacted topic — khi có sự kiện trễ, kết quả mới đơn giản ghi đè kết quả cũ cho cùng cửa sổ.

## Nguồn Tham Khảo

- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide* (O'Reilly, 2017), Chapter 11: Stream Processing
