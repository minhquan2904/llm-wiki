---
title: "Kafka MirrorMaker"
source: "compiled"
date_added: 2026-05-08
tags: [concept, kafka, cross-cluster, replication, mirrormaker, disaster-recovery]
aliases: [Kafka MirrorMaker, MirrorMaker, Cross-Cluster Mirroring]
status: reviewed
related:
  - "[[apache-kafka]]"
  - "[[kafka-replication]]"
  - "[[kafka-connect]]"
  - "[[kafka-administration]]"
summary: "Cơ chế sao chép dữ liệu giữa các cụm Kafka — bao gồm kiến trúc MirrorMaker, các mẫu triển khai đa cụm và chiến lược failover."
---

## Định Nghĩa

MirrorMaker là công cụ sao chép dữ liệu xuyên cụm (cross-cluster mirroring) của [[apache-kafka]]. Về bản chất, MirrorMaker là một consumer đọc message từ cụm nguồn kết hợp với một producer ghi vào cụm đích, nối với nhau qua một hàng đợi nội bộ. Cơ chế replication bên trong Kafka cluster chỉ hoạt động trong phạm vi một cluster duy nhất — MirrorMaker giải quyết nhu cầu sao chép giữa các cluster.

## Các Mẫu Kiến Trúc Đa Cụm

**Hub-and-Spoke** — Một cụm trung tâm (hub) nhận dữ liệu từ nhiều cụm cục bộ (spoke). Phù hợp khi cần tổng hợp dữ liệu tại một điểm duy nhất. Ưu điểm: đơn giản, dữ liệu được tập trung. Hạn chế: ứng dụng tại spoke không truy cập được dữ liệu từ spoke khác.

**Active-Active** — Hai hoặc nhiều cụm vừa nhận dữ liệu cục bộ vừa mirror từ cụm kia. Cung cấp redundancy và proximity cho người dùng ở nhiều vùng địa lý. Thách thức lớn nhất là xử lý xung đột (conflict) khi cùng entity được cập nhật đồng thời ở cả hai cụm, và tránh vòng lặp mirror vô hạn (circular mirroring) — thường giải quyết bằng quy ước đặt tên topic khác nhau.

**Active-Standby** — Một cụm chính (active) phục vụ toàn bộ traffic, một cụm dự phòng (standby) nhận bản sao. Khi active gặp sự cố, traffic được chuyển sang standby. Đơn giản nhất nhưng lãng phí tài nguyên standby và failover phức tạp do offset không đồng bộ.

**Stretch Cluster** — Một cluster Kafka duy nhất triển khai trên nhiều datacenter với rack-awareness. Kafka tự động replicate partition giữa các rack/DC. Ưu điểm: đồng bộ hoàn toàn, failover trong suốt. Hạn chế: yêu cầu latency thấp giữa các DC (thường ≤ 15ms), không khả thi cho khoảng cách địa lý lớn.

## Triển Khai MirrorMaker

MirrorMaker chạy như một tiến trình độc lập với consumer group đọc từ cụm nguồn. Nguyên tắc quan trọng: triển khai MirrorMaker tại cụm **đích** (remote-consuming, local-producing). Lý do: khi mất kết nối mạng, consumer bị disconnect chỉ mất khả năng đọc tạm thời, dữ liệu vẫn an toàn tại cụm nguồn. Ngược lại, remote-producing khi mất kết nối có nguy cơ tích tụ message trong buffer producer, dẫn tới mất dữ liệu khi buffer đầy.

Cấu hình đáng chú ý: tăng `linger.ms` và `batch.size` trên producer để cải thiện throughput xuyên datacenter; đặt `auto.offset.reset=earliest` trên consumer để tránh bỏ sót message khi khởi động lại.

## Giám Sát và Vận Hành

Chỉ số quan trọng nhất là **consumer lag** — khoảng cách giữa offset mới nhất trên cụm nguồn và offset đã commit bởi MirrorMaker consumer. Lag cao kéo dài chỉ ra MirrorMaker không theo kịp throughput nguồn, cần tăng số consumer thread hoặc tối ưu cấu hình. Giám sát lag kết hợp với [[kafka-monitoring]] là điều kiện tiên quyết cho vận hành cross-cluster.

## Các Giải Pháp Thay Thế

**Confluent Replicator** — Xây dựng trên [[kafka-connect]], cung cấp bảo toàn cấu hình topic, tự động tạo topic đích và giao diện quản lý. Sản phẩm thương mại.

**Uber uReplicator** — Phiên bản cải tiến MirrorMaker do Uber phát triển, giải quyết vấn đề rebalance khi thêm/bớt topic bằng cách sử dụng Apache Helix làm bộ điều phối trung tâm.

## Thách Thức Failover

Chuyển đổi dự phòng (failover) giữa các cụm Kafka là thao tác rủi ro do bản chất sao chép bất đồng bộ: (1) offset tại cụm đích không tương ứng 1:1 với offset cụm nguồn; (2) có thể xảy ra duplicate hoặc mất message trong khoảng lag; (3) consumer tại cụm mới cần chiến lược xác định offset bắt đầu — thường dùng timestamp-based seeking hoặc chấp nhận đọc lại từ earliest.

## Nguồn Tham Khảo

- Neha Narkhede, Gwen Shapira, Todd Palino — *Kafka: The Definitive Guide*, Chapter 8 (O'Reilly, 2017)3
