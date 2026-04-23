---
title: "RabbitMQ"
source: "compiled"
date_added: 2026-04-23
tags: [tool, message-broker]
aliases: []
status: draft
related:
  - "[[apache-kafka]]"
  - "[[kafka-vs-rabbitmq]]"
summary: "Message broker mã nguồn mở linh hoạt, hỗ trợ nhiều giao thức và định tuyến tin nhắn phức tạp."
---

# RabbitMQ

## Tổng Quan

RabbitMQ là một Message Broker (trung gian tin nhắn) mã nguồn mở phổ biến, ban đầu được phát triển bởi Rabbit Technologies Ltd vào năm 2007. Sử dụng giao thức AMQP (Advanced Message Queuing Protocol), RabbitMQ đóng vai trò như một hệ thống bưu điện trung gian, tiếp nhận thông điệp từ người gửi và định tuyến chúng đến đúng người nhận. Được viết bằng ngôn ngữ Erlang, nó nổi tiếng với độ tin cậy cao, khả năng định tuyến linh hoạt và sự dễ dàng trong việc triển khai.

## Kiến Trúc Cốt Lõi

Khác với mô hình lưu trữ dạng nhật ký của Kafka, RabbitMQ sử dụng mô hình hàng đợi thông minh:
- **Producers**: Các đối tượng tạo và gửi tin nhắn.
- **Exchanges**: Bộ định tuyến nhận tin nhắn từ Producers và phân phối chúng dựa trên các quy tắc cấu hình.
- **Queues**: Các bộ đệm lưu trữ tin nhắn an toàn cho đến khi chúng được xử lý.
- **Bindings**: Các quy tắc liên kết giữa Exchanges và Queues.
- **Consumers**: Các đối tượng đăng ký nhận và xử lý tin nhắn từ Queues.

## Vai Trò Trong Hệ Thống (Use Cases)

RabbitMQ là sự lựa chọn tiêu chuẩn cho các mô hình trao đổi thông tin truyền thống:
- **Tích hợp ứng dụng**: Ghép nối lỏng lẻo (decoupling) các thành phần trong hệ thống phần mềm, cho phép chúng giao tiếp độc lập.
- **Microservices**: Làm lớp giao tiếp trung gian, đảm bảo thông điệp không bị mất khi một service tạm thời gián đoạn.
- **Xử lý tác vụ nền (Background Jobs)**: Đẩy các công việc nặng (xử lý file, gửi email, sao lưu) vào hàng đợi để xử lý bất đồng bộ.

## Lợi Thế và Hạn Chế

**Lợi Thế:**
- **Định tuyến phong phú**: Cơ chế Exchanges cung cấp khả năng điều hướng thông điệp phức tạp (Direct, Topic, Fanout).
- **Dễ sử dụng**: Giao diện quản lý trực quan (Management UI) và tài liệu rõ ràng, dễ tiếp cận hơn nhiều hệ thống phân tán khác.
- **Độ tin cậy cao**: Cung cấp cơ chế xác nhận (acknowledgment) đảm bảo mỗi tin nhắn đều được xử lý trước khi xóa khỏi hàng đợi.
- **Tính tương thích**: Hỗ trợ nhiều giao thức (AMQP, MQTT, STOMP) và đa dạng ngôn ngữ lập trình.

**Hạn Chế:**
- **Giới hạn thông lượng**: Hiệu suất tổng thể không thể sánh bằng các hệ thống hướng luồng dữ liệu (như Kafka) khi đối mặt với hàng triệu sự kiện/giây.
- **Không hỗ trợ phát lại (Replay)**: Tin nhắn thường bị xóa sau khi tiêu thụ thành công, không thể đọc lại trạng thái trong quá khứ một cách tự nhiên.
