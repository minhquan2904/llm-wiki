---
title: "Kafka Producer"
source: "compiled"
date_added: 2026-05-08
tags: [concept, kafka, producer, api, distributed-systems]
aliases: [Kafka Producer, KafkaProducer, Producer API]
status: reviewed
related:
  - "[[apache-kafka]]"
  - "[[kafka-consumer]]"
  - "[[kafka-replication]]"
  - "[[kafka-connect]]"
summary: "Kiến trúc và API gửi thông điệp của Apache Kafka — bao gồm mô hình ProducerRecord, ba chế độ gửi, cấu hình acks và chiến lược phân vùng."
---

## Định Nghĩa

Kafka Producer là client chịu trách nhiệm tạo và gửi thông điệp (message) tới các topic trong [[apache-kafka]]. Producer đóng gói dữ liệu thành đối tượng `ProducerRecord`, thực hiện serialization, chọn partition đích, rồi đưa message vào buffer nội bộ trước khi gửi theo batch tới broker.

## Kiến Trúc Bên Trong

Quy trình gửi message trải qua năm bước tuần tự: (1) ứng dụng tạo `ProducerRecord` gồm topic, value, key (tùy chọn) và partition (tùy chọn); (2) Serializer chuyển key/value thành byte arrays; (3) Partitioner chọn partition — nếu key tồn tại, áp dụng hash nhất quán (`murmur2`) để đảm bảo cùng key luôn rơi vào cùng partition; (4) message được thêm vào batch tương ứng trong bộ đệm bộ nhớ; (5) một thread riêng biệt gửi batch tới broker leader của partition.

Khi broker nhận message thành công, nó trả về `RecordMetadata` chứa topic, partition và offset. Nếu ghi thất bại, broker trả lỗi và producer có thể tự động retry.

## Ba Chế Độ Gửi

**Fire-and-forget** — Gọi `send()` mà không kiểm tra kết quả. Phù hợp cho dữ liệu chấp nhận mất mát (metrics, click tracking). Đạt throughput cao nhất nhưng không đảm bảo delivery.

**Synchronous** — Gọi `send().get()` để chặn thread cho đến khi nhận response. Đảm bảo biết chính xác kết quả nhưng đánh đổi throughput vì mỗi message phải chờ một network roundtrip.

**Asynchronous** — Gọi `send(record, callback)` với `Callback.onCompletion()`. Kết hợp throughput cao với khả năng xử lý lỗi — callback chạy trên thread I/O của producer khi nhận response từ broker.

## Cấu Hình Quan Trọng

**`acks`** quyết định mức độ đảm bảo delivery. `acks=0` không chờ xác nhận (throughput tối đa, có thể mất message). `acks=1` chờ leader xác nhận (cân bằng). `acks=all` chờ tất cả ISR xác nhận (an toàn nhất, xem [[kafka-replication]]).

**`retries`** và **`retry.backoff.ms`** kiểm soát hành vi retry tự động cho các lỗi tạm thời (retriable errors) như mất kết nối hay "no leader". Lỗi không thể retry (message quá lớn) được trả về ngay.

**`batch.size`** (mặc định 16 KB) và **`linger.ms`** kiểm soát batching. Producer gửi batch khi đạt kích thước hoặc hết thời gian chờ, tùy điều kiện nào đến trước. Tăng hai giá trị này cải thiện throughput nhưng tăng latency.

**`buffer.memory`** (mặc định 32 MB) giới hạn tổng bộ nhớ cho buffer. Khi buffer đầy, `send()` chặn tối đa `max.block.ms` rồi ném exception.

**`compression.type`** hỗ trợ `gzip`, `snappy`, `lz4`. Nén diễn ra ở cấp batch, giảm băng thông mạng và dung lượng lưu trữ nhưng tốn CPU.

## Serialization và Schema

Producer serialize key/value thành byte arrays trước khi gửi. Kafka cung cấp sẵn `StringSerializer`, `IntegerSerializer` và `ByteArraySerializer`. Đối với dữ liệu có cấu trúc, Apache Avro kết hợp Schema Registry là lựa chọn phổ biến — schema được lưu riêng biệt, cho phép producer và [[kafka-consumer]] tiến hóa schema độc lập (backward/forward compatibility) mà không cần phối hợp deploy.

## Chiến Lược Phân Vùng

Partitioner mặc định sử dụng hash Murmur2 trên key. Mọi message có cùng key luôn rơi vào cùng partition, đảm bảo thứ tự xử lý cho cùng entity (VD: cùng user_id). Nếu không có key, producer phân phối round-robin đều giữa các partition.

Thay đổi số lượng partition sau khi đã có dữ liệu sẽ phá vỡ mapping key-to-partition. Cần tính toán partition count phù hợp từ đầu dựa trên throughput mục tiêu.

## Nguồn Tham Khảo

- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide*, Chapter 3 (O'Reilly, 2017)
