---
title: "Apache Kafka"
source: "compiled"
date_added: 2026-04-23
tags: [tool, message-broker, data-streaming]
aliases: [Kafka]
status: draft
related:
  - "[[rabbitmq]]"
  - "[[kafka-vs-rabbitmq]]"
summary: "Nền tảng xử lý luồng sự kiện phân tán, nổi bật với thông lượng cao và khả năng lưu trữ dữ liệu thời gian thực."
---

# Apache Kafka

## Tổng Quan

Apache Kafka là một nền tảng xử lý luồng sự kiện (event streaming platform) phân tán, mã nguồn mở, được thiết kế cho các ứng dụng yêu cầu xử lý dữ liệu với thông lượng khổng lồ, độ trễ thấp và khả năng mở rộng cao. Ban đầu được phát triển tại LinkedIn bởi Jay Kreps, Neha Narkhede và Jun Rao để giải quyết vấn đề xử lý dữ liệu thời gian thực, Kafka sau đó được mở mã nguồn vào năm 2011 dưới sự quản lý của Apache Software Foundation.

## Kiến Trúc Cốt Lõi

Kiến trúc của Kafka xoay quanh một dịch vụ nhật ký lưu trữ (commit log) phân tán và được sao chép. Các thành phần cơ bản bao gồm:
- **Brokers**: Các máy chủ lưu trữ và quản lý dữ liệu. Một tập hợp các Brokers tạo thành một Cluster.
- **Topics**: Danh mục hoặc kênh logic nơi dữ liệu được xuất bản.
- **Partitions**: Topics được chia nhỏ thành các phân vùng, cho phép dữ liệu được xử lý song song và mở rộng theo chiều ngang.
- **Producers**: Các thực thể đẩy (publish) dữ liệu vào Kafka.
- **Consumers & Consumer Groups**: Các thực thể đọc dữ liệu. Các Consumer Group cho phép chia sẻ tải tiêu thụ dữ liệu trên nhiều tiến trình.
- **Leaders & Followers**: Cơ chế sao chép (replication) trong đó một Leader xử lý đọc/ghi, còn các Followers sao chép dữ liệu thụ động để dự phòng lỗi.

## Vai Trò Trong Hệ Thống (Use Cases)

Kafka thường được sử dụng làm "xương sống" (backbone) cho liên lạc giữa các dịch vụ trong kiến trúc phân tán:
- **Data Streaming**: Nhập và xử lý khối lượng dữ liệu khổng lồ theo thời gian thực (ví dụ: tổng hợp nhật ký, lưu trữ dữ liệu).
- **Phân tích thời gian thực**: Cung cấp luồng dữ liệu cho các công cụ phân tích.
- **Event Sourcing**: Kiến trúc hướng sự kiện, lưu lại toàn bộ lịch sử thay đổi trạng thái của hệ thống.

## Lợi Thế và Hạn Chế

**Lợi Thế:**
- **Thông lượng cực cao**: Có khả năng xử lý hàng triệu sự kiện mỗi giây.
- **Khả năng mở rộng ngang**: Dễ dàng thêm Broker vào Cluster.
- **Độ bền dữ liệu**: Lưu trữ trên đĩa cứng và sao chép đa cụm, đảm bảo an toàn dữ liệu ngay cả khi node bị hỏng.
- **Luồng xử lý tích hợp**: Cung cấp Kafka Streams cho xử lý thời gian thực.

**Hạn Chế:**
- **Độ phức tạp**: Cấu hình và quản lý cụm phân tán đòi hỏi kiến thức chuyên sâu.
- **Định tuyến hạn chế**: Phụ thuộc vào Topics/Partitions, không có cơ chế định tuyến thông điệp phức tạp theo nội dung.
- **Hiệu suất suy giảm do nén**: Quá trình nén/giải nén luồng dữ liệu có thể ảnh hưởng đến hiệu quả xử lý tổng thể.
