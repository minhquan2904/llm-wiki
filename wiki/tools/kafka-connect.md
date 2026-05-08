---
title: "Kafka Connect"
source: "compiled"
date_added: 2026-05-08
tags: [tool, kafka, data-pipeline, etl, kafka-connect]
aliases: [Kafka Connect, Connect API]
status: reviewed
related:
  - "[[apache-kafka]]"
  - "[[kafka-replication]]"
  - "[[kafka-streams]]"
  - "[[message-broker]]"
summary: "Framework tích hợp dữ liệu của Apache Kafka, cung cấp kiến trúc Connector-Task-Worker để di chuyển dữ liệu giữa Kafka và các hệ thống bên ngoài."
---

## Tổng Quan

Kafka Connect là một thành phần của [[apache-kafka]], cung cấp phương thức có cấu trúc và mở rộng được để di chuyển dữ liệu giữa Kafka và các hệ thống lưu trữ bên ngoài. Ra đời từ phiên bản 0.9, Connect giải quyết các bài toán tích hợp dữ liệu mà trước đây mỗi tổ chức phải tự xây dựng: quản lý cấu hình, lưu trữ offset, song song hóa, xử lý lỗi và hỗ trợ nhiều định dạng dữ liệu.

Giá trị cốt lõi của Kafka trong data pipeline là vai trò bộ đệm lớn (giant buffer) giữa các giai đoạn của pipeline, giúp tách biệt (decouple) Producer và Consumer cả về thời gian lẫn thông lượng. Producer có thể ghi real-time trong khi Consumer xử lý theo batch hàng giờ, hoặc ngược lại.

## Kiến Trúc

Kafka Connect vận hành dưới dạng cluster các **worker process**. Mỗi worker chạy các **connector plugin** — thư viện chịu trách nhiệm di chuyển dữ liệu thực tế. Kiến trúc bao gồm ba lớp:

**Connectors** — Đại diện logic cho một tác vụ tích hợp. Có hai loại: **Source connector** đọc dữ liệu từ hệ thống bên ngoài vào Kafka, và **Sink connector** ghi dữ liệu từ Kafka ra hệ thống bên ngoài. Connector được tạo và quản lý qua REST API.

**Tasks** — Đơn vị thực thi song song. Mỗi Connector khởi tạo một hoặc nhiều Task để chia nhỏ công việc và tận dụng tài nguyên CPU hiệu quả hơn. Source task đọc dữ liệu và chuyển thành Connect data object; Sink task nhận object và ghi vào hệ thống đích.

**Converters** — Lớp chuyển đổi định dạng giữa Connect data object và dữ liệu lưu trong Kafka. JSON converter đi kèm Apache Kafka; Avro converter do Confluent Schema Registry cung cấp. Cấu hình `key.converter` và `value.converter` cho phép chọn định dạng lưu trữ trong Kafka độc lập với loại connector sử dụng.

## Standalone và Distributed Mode

Connect hỗ trợ hai chế độ vận hành:

**Standalone mode** (`bin/connect-standalone.sh`) — Tất cả connector và task chạy trên một worker duy nhất. Phù hợp cho phát triển, gỡ lỗi, hoặc khi connector cần gắn với máy cụ thể (ví dụ: syslog connector lắng nghe trên port xác định).

**Distributed mode** (`bin/connect-distributed.sh`) — Nhiều worker chia sẻ cùng `group.id` tạo thành cluster. Connector và task được phân bổ tự động giữa các worker. Khi một worker gặp sự cố hoặc connector bị xóa, các task được rebalance sang worker còn lại. Chế độ này là tiêu chuẩn cho production.

## Khi Nào Dùng Connect vs Producer/Consumer API

**Connect** phù hợp khi kết nối Kafka với datastore mà bạn không viết code hoặc không muốn sửa đổi code. Connect cung cấp sẵn quản lý offset, song song hóa, xử lý lỗi, hỗ trợ nhiều kiểu dữ liệu và REST API chuẩn.

**Producer/Consumer API** phù hợp khi bạn kiểm soát code ứng dụng và muốn đẩy/kéo dữ liệu trực tiếp từ logic nghiệp vụ. Viết một ứng dụng nhỏ kết nối Kafka với datastore có vẻ đơn giản, nhưng xử lý đúng các vấn đề về kiểu dữ liệu, cấu hình và khôi phục offset thường phức tạp hơn dự kiến.

## Vai Trò Trong Data Pipeline

Khi thiết kế data pipeline, hai triết lý phổ biến là **ETL** (Extract-Transform-Load) và **ELT** (Extract-Load-Transform). ETL biến đổi dữ liệu trong pipeline, tiết kiệm lưu trữ nhưng hạn chế khả năng sử dụng dữ liệu gốc ở downstream. ELT (còn gọi là data-lake architecture) giữ nguyên dữ liệu gốc và dồn xử lý về hệ thống đích, tối đa hóa tính linh hoạt.

Kafka Connect hỗ trợ cả hai mô hình. Với Kafka làm trung gian, pipeline đạt được: tách biệt thời gian (Producer real-time, Consumer batch), khả năng mở rộng độc lập (thêm Consumer/Producer không ảnh hưởng bên kia), và đảm bảo at-least-once delivery mặc định — kết hợp với datastore có unique key hoặc transactional model để đạt exactly-once.

## Lợi Thế và Hạn Chế

**Lợi Thế:**
- Hệ sinh thái connector phong phú (JDBC, Elasticsearch, S3, HDFS, Debezium CDC)
- Quản lý offset tự động, đảm bảo khôi phục từ điểm dừng khi sự cố
- REST API chuẩn hóa cho quản lý và giám sát
- Hỗ trợ schema evolution thông qua Schema Registry

**Hạn Chế:**
- Yêu cầu cơ sở hạ tầng riêng cho Connect cluster trong production
- Gỡ lỗi connector phức tạp hơn so với ứng dụng Producer/Consumer thuần
- Một số connector community có chất lượng không đồng đều

## Nguồn Tham Khảo

- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide* (O'Reilly, 2017), Chapter 7: Building Data Pipelines
