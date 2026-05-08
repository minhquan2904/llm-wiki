---
title: "Kafka Monitoring"
source: "compiled"
date_added: 2026-05-08
tags: [concept, kafka, monitoring, observability, jmx, metrics]
aliases: [Kafka Monitoring, Giám sát Kafka, Kafka Metrics]
status: reviewed
related:
  - "[[apache-kafka]]"
  - "[[kafka-replication]]"
  - "[[kafka-administration]]"
  - "[[kafka-consumer]]"
summary: "Hệ thống giám sát Apache Kafka — bao gồm các chỉ số JMX quan trọng của broker, giám sát consumer lag và chiến lược end-to-end monitoring."
---

## Định Nghĩa

Kafka Monitoring là tập hợp các phương pháp và chỉ số (metrics) dùng để giám sát sức khỏe và hiệu năng của một cụm [[apache-kafka]]. Kafka phơi bày metrics qua giao diện JMX (Java Management Extensions). Hệ thống giám sát hiệu quả bao gồm ba lớp: broker metrics, host-level metrics và client metrics.

## Chỉ Số Broker Quan Trọng

**`UnderReplicatedPartitions`** — Số partition có bản sao không đồng bộ (not in ISR). Giá trị khác 0 kéo dài là tín hiệu cảnh báo nghiêm trọng, có thể do broker quá tải, network bottleneck hoặc disk failure. Đây là "chỉ số vàng" cần alert ngay.

**`ActiveControllerCount`** — Số lượng controller trên mỗi broker. Chính xác phải bằng 1 trên đúng một broker trong cluster và bằng 0 trên tất cả broker còn lại. Nếu tổng cluster khác 1, cluster đang ở trạng thái bất thường.

**`RequestHandlerAvgIdlePercent`** — Phần trăm thời gian rảnh của IO thread pool. Khi giảm xuống dưới 20%, broker đang quá tải và cần scale hoặc giảm tải.

**`AllTopicsMessagesInPerSec`** và **`AllTopicsBytesInPerSec`** / **`AllTopicsBytesOutPerSec`** — Thông lượng message và byte đầu vào/đầu ra. Dùng để baseline traffic pattern và phát hiện spike bất thường.

**Request Latency** — Thời gian xử lý request (`Produce`, `FetchConsumer`, `FetchFollower`). Theo dõi percentile 99th thay vì average để phát hiện tail latency.

**Partition Count** và **Leader Count** — Số partition và số partition mà broker đang làm leader. Phân bổ đều giữa các broker là dấu hiệu cụm khỏe mạnh.

## Giám Sát Cấp Hệ Điều Hành

**CPU** — Kafka tốn CPU cho nén/giải nén message. Theo dõi `user` CPU (xử lý ứng dụng) tách biệt với `system` CPU (kernel I/O).

**Disk** — Theo dõi I/O utilization và throughput. Kafka phụ thuộc nặng vào sequential disk write; latency disk cao trực tiếp ảnh hưởng produce latency.

**Network** — Giám sát bandwidth sử dụng trên mỗi NIC. Kafka nhân bản dữ liệu qua network cho cả replication lẫn consumer fetch.

**JVM** — Garbage Collection pause là nguồn latency spike phổ biến. Sử dụng G1GC với `MaxGCPauseMillis=20ms` là cấu hình khuyến nghị. Theo dõi full GC frequency.

## Giám Sát Consumer Lag

Consumer lag là khoảng cách giữa offset mới nhất trên partition (log-end offset) và offset đã commit bởi [[kafka-consumer]]. Lag tăng liên tục nghĩa là consumer không theo kịp producer.

Kafka cung cấp `kafka-consumer-groups.sh --describe` để kiểm tra lag theo group. Tuy nhiên, công cụ tốt hơn là **Burrow** (LinkedIn) — hệ thống giám sát lag chuyên dụng đánh giá trạng thái consumer dựa trên xu hướng lag (tăng/giảm/ổn định) thay vì ngưỡng tuyệt đối. Burrow phân loại consumer thành các trạng thái: OK, WARNING, ERROR, STOP, STALL.

Không nên dựa vào metrics consumer-side (`records-lag-max`) để giám sát vì khi consumer crash, metric biến mất hoàn toàn.

## End-to-End Monitoring

Giám sát end-to-end đo thời gian từ lúc message được produce đến lúc consumer nhận được. Công cụ **Kafka Monitor** (LinkedIn) tạo synthetic message giả, gửi qua pipeline hoàn chỉnh và đo latency/availability thực tế. Đây là lớp giám sát bổ sung cho các chỉ số broker — phát hiện vấn đề mà metric nội bộ không thấy được (VD: permission issue, network partition giữa client và broker).

## Chiến Lược Cảnh Báo

Phân tầng cảnh báo theo mức độ nghiêm trọng:

**Critical** — `UnderReplicatedPartitions > 0` kéo dài, `ActiveControllerCount != 1`, disk I/O error.

**Warning** — Consumer lag tăng liên tục, `RequestHandlerAvgIdlePercent < 20%`, partition count mất cân bằng giữa broker.

**Info** — Traffic spike bất thường, thay đổi cấu hình topic, broker restart.

## Nguồn Tham Khảo

- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide*, Chapter 10 (O'Reilly, 2017)
