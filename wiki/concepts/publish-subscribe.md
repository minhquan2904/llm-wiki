---
title: "Publish/Subscribe (Pub/Sub)"
source: "compiled"
date_added: 2026-04-23
tags: [concept, system-design, messaging-pattern]
aliases: [Pub/Sub, Mô hình Pub-Sub, Publish-Subscribe]
status: draft
related:
  - "[[message-broker]]"
  - "[[apache-kafka]]"
summary: "Mô hình giao tiếp bất đồng bộ trong đó người gửi phát thông điệp vào các chủ đề mà không cần chỉ định người nhận cụ thể."
---

# Publish/Subscribe (Pub/Sub)

## Định Nghĩa

Publish/Subscribe (thường gọi tắt là Pub/Sub) là một mô hình giao tiếp tin nhắn bất đồng bộ, trong đó các đối tượng gửi tin nhắn (Publishers) không lập trình để gửi tin nhắn trực tiếp đến các đối tượng nhận cụ thể (Subscribers). Thay vào đó, Publishers phân loại các tin nhắn vào các chủ đề (topics) hoặc kênh (channels) mà không cần biết có những Subscribers nào đang lắng nghe. Ngược lại, Subscribers biểu thị sự quan tâm đến một hoặc nhiều topics và chỉ nhận những tin nhắn phù hợp với chủ đề đó, mà không cần biết Publishers là ai.

## Cơ Chế Hoạt Động

Mô hình Pub/Sub cho phép tách rời (decouple) hoàn toàn giữa bên tạo dữ liệu và bên tiêu thụ dữ liệu:

- **Publishers**: Cứ đẩy sự kiện/tin nhắn vào một `Topic` mỗi khi có thay đổi trạng thái hoặc dữ liệu mới.
- **Topic/Channel**: Kênh phân phối thông điệp. Nó giống như một đài phát thanh phát sóng trên một tần số nhất định.
- **Subscribers**: "Dò đài" (subscribe) vào các `Topic` quan tâm. Mỗi khi có tin nhắn mới trên Topic, hệ thống trung gian sẽ phân phối (broadcast) tin nhắn đó đến toàn bộ Subscribers.

## So Sánh với Message Broker Truyền Thống

Trong khi các [[message-broker]] truyền thống (như RabbitMQ) thường thiên về việc đảm bảo tin nhắn đến tay một consumer duy nhất một cách an toàn (Point-to-Point), thì hệ thống Pub/Sub nhấn mạnh vào việc **phân phối một thông điệp cho nhiều consumer cùng lúc**. 

Tuy nhiên, các hệ thống Pub/Sub hiện đại có thể không cung cấp khả năng chuyển tiếp tin nhắn được đảm bảo (guaranteed delivery) phức tạp như message brokers, nhưng bù lại mang đến khả năng mở rộng (scalability) và linh hoạt (flexibility) vượt trội.

## Liên Hệ / Ứng Dụng

Mô hình này là nền tảng cốt lõi của các hệ thống Event Streaming như [[apache-kafka]], được ứng dụng rộng rãi trong:
- **Hệ thống theo dõi thời gian thực**: Ví dụ ứng dụng gọi xe (tài xế phát tọa độ vào topic, ứng dụng người dùng subscribe để xem vị trí).
- **Log Aggregation**: Đẩy toàn bộ log của hệ thống vào một topic trung tâm để các công cụ phân tích subscribe và xử lý.
- **Kiến trúc hướng sự kiện (Event-driven Architecture)**: Các microservices giao tiếp và phản ứng với các sự kiện của nhau thông qua cơ chế Pub/Sub.
