---
title: "Kafka Consumer"
source: "compiled"
date_added: 2026-05-08
tags: [concept, kafka, consumer, api, distributed-systems]
aliases: [Kafka Consumer, KafkaConsumer, Consumer API, Consumer Group]
status: reviewed
related:
  - "[[apache-kafka]]"
  - "[[kafka-producer]]"
  - "[[kafka-replication]]"
  - "[[kafka-streams]]"
summary: "Kiến trúc đọc thông điệp của Apache Kafka — bao gồm Consumer Group, cơ chế rebalance, quản lý offset và các chiến lược commit."
---

## Định Nghĩa

Kafka Consumer là client đọc thông điệp từ các topic trong [[apache-kafka]]. Consumer hoạt động theo mô hình pull — liên tục gọi `poll()` để lấy batch message từ broker. Cơ chế Consumer Group cho phép nhiều consumer chia sẻ tải xử lý trên cùng topic, trong khi mỗi partition chỉ được tiêu thụ bởi đúng một consumer trong group tại bất kỳ thời điểm nào.

## Consumer Group

Mỗi consumer thuộc một consumer group (xác định bởi `group.id`). Kafka tự động phân phối partition giữa các consumer trong group. Nếu topic có 4 partition và group có 2 consumer, mỗi consumer nhận 2 partition. Nếu consumer vượt quá số partition, consumer thừa sẽ nhàn rỗi (idle).

Nhiều consumer group có thể đọc cùng topic một cách độc lập — mỗi group nhận toàn bộ message. Đây là điểm khác biệt cốt lõi so với mô hình message queue truyền thống, nơi message chỉ được tiêu thụ một lần.

## Cơ Chế Rebalance

Rebalance là quá trình phân phối lại partition khi consumer gia nhập/rời khỏi group hoặc khi topic thay đổi. Trong thời gian rebalance, toàn bộ group tạm ngừng tiêu thụ — tạo ra cửa sổ không khả dụng ngắn.

Consumer duy trì liên lạc với Group Coordinator (một broker được chỉ định) qua heartbeat. Từ Kafka 0.10.1, heartbeat chạy trên thread riêng biệt, tách rời khỏi tần suất `poll()`. Nếu heartbeat không đến trong `session.timeout.ms`, coordinator coi consumer đã chết và khởi động rebalance.

Consumer đầu tiên gia nhập group trở thành Group Leader, chịu trách nhiệm tính toán bản phân công partition qua `PartitionAssignor` (Range hoặc RoundRobin), rồi gửi kết quả cho coordinator phân phối.

## Quản Lý Offset

Offset là số nguyên tăng dần đánh dấu vị trí message trong partition. Consumer theo dõi offset đã xử lý bằng cách commit vào topic nội bộ `__consumer_offsets`.

**Auto commit** (`enable.auto.commit=true`) — commit tự động theo chu kỳ `auto.commit.interval.ms` (mặc định 5 giây). Đơn giản nhưng có thể gây duplicate khi consumer crash giữa hai lần commit.

**Commit đồng bộ** (`commitSync()`) — chặn thread cho đến khi broker xác nhận. An toàn nhưng ảnh hưởng throughput.

**Commit bất đồng bộ** (`commitAsync()`) — không chặn, sử dụng callback. Không tự động retry vì offset mới hơn có thể đã commit trong lúc chờ. Chiến lược phổ biến: dùng `commitAsync()` trong poll loop, `commitSync()` trong `finally` block.

**Commit offset cụ thể** — Consumer có thể commit offset cho từng partition riêng lẻ, cho phép xử lý at-least-once chính xác hơn.

## Poll Loop

Vòng lặp `poll()` là trái tim của consumer. Mỗi lần gọi `poll()`, consumer nhận batch `ConsumerRecords`, xử lý từng record, rồi gọi lại `poll()`. Vòng lặp này cũng đảm nhiệm gửi heartbeat, tham gia rebalance và fetch dữ liệu.

Consumer phải gọi `poll()` trong khoảng `max.poll.interval.ms` — nếu vượt quá, coordinator coi consumer đã livelock và khởi động rebalance. Khi thoát, gọi `consumer.close()` để trigger rebalance ngay thay vì chờ session timeout. Phương thức `wakeup()` cho phép thread khác đánh thức consumer đang chặn trong `poll()` để thoát gracefully.

## Cấu Hình Quan Trọng

**`fetch.min.bytes`** — dung lượng tối thiểu broker tích lũy trước khi trả response. Giảm tải CPU/network cho topic ít traffic.

**`max.partition.fetch.bytes`** (mặc định 1 MB) — giới hạn dữ liệu trả về mỗi partition. Phải lớn hơn `max.message.size` trên broker.

**`session.timeout.ms`** — thời gian tối đa không heartbeat trước khi bị coi là dead. Đặt thấp giúp phát hiện lỗi nhanh, đặt cao giảm rebalance do GC pause.

**`auto.offset.reset`** — hành vi khi không có offset hợp lệ: `latest` (đọc từ mới nhất) hoặc `earliest` (đọc từ đầu).

## Nguồn Tham Khảo

- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide*, Chapter 4 (O'Reilly, 2017)
