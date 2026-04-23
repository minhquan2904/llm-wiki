---
title: "Message Broker"
source: "compiled"
date_added: 2026-04-23
tags: [concept, system-design, message-broker]
aliases: [Trạm trung chuyển tin nhắn, Trạm môi giới tin nhắn]
status: draft
related:
  - "[[publish-subscribe]]"
  - "[[rabbitmq]]"
  - "[[apache-kafka]]"
summary: "Một thành phần trung gian hỗ trợ ứng dụng giao tiếp, nhận và định tuyến dữ liệu dựa trên các quy tắc xác định trước."
---

# Message Broker

## Định Nghĩa

Message broker là một thành phần kiến trúc trung gian đứng giữa các hệ thống, dịch vụ hoặc ứng dụng phần mềm, tạo điều kiện cho chúng giao tiếp và trao đổi thông tin. Chức năng chính của message broker là tiếp nhận thông điệp từ người gửi (producers), xác thực, biến đổi (nếu cần), và định tuyến chúng đến đúng người nhận (consumers) dựa trên các quy tắc và logic được định sẵn.

## Cơ Chế Hoạt Động

Bằng cách sử dụng một message broker, các ứng dụng có thể tập trung vào chức năng cốt lõi của chúng thay vì phải lo lắng về logic kết nối và truyền tải mạng. Các thành phần chính trong cơ chế của nó bao gồm:

- **Producers**: Ứng dụng tạo và gửi dữ liệu đến broker.
- **Broker**: Tiếp nhận, giữ an toàn và định tuyến tin nhắn.
- **Consumers**: Ứng dụng nhận dữ liệu từ broker để xử lý.

Các message broker (như [[rabbitmq]]) tập trung vào việc định tuyến tin nhắn và đảm bảo tính tin cậy. Khi có lỗi xảy ra ở phía người nhận, broker có thể giữ tin nhắn trong hàng đợi cho đến khi người nhận trực tuyến trở lại để xử lý.

## Lợi Thế / Hạn Chế

**Lợi Thế:**
- **Decoupling (Ghép nối lỏng lẻo)**: Producers và Consumers không cần phải biết đến sự tồn tại của nhau.
- **Đảm bảo giao hàng (Guaranteed Delivery)**: Tin nhắn không bị mất khi một trong các dịch vụ gặp sự cố tạm thời.
- **Định tuyến linh hoạt**: Hỗ trợ nhiều kiểu nhắn tin như Request/Reply, Point-to-Point, hoặc Pub/Sub.

**Hạn Chế:**
- **Điểm nghẽn (Bottleneck)**: Có thể trở thành nút thắt cổ chai về hiệu suất nếu không được cấu hình và quản lý đúng cách.
- **Điểm lỗi duy nhất (Single Point of Failure)**: Nếu broker sập, toàn bộ giao tiếp giữa các dịch vụ sẽ bị gián đoạn (cần cấu hình cluster để khắc phục).

## Liên Hệ / Ứng Dụng

Trong các hệ thống phân tán và kiến trúc microservices hiện đại, message broker đóng vai trò thiết yếu để các service giao tiếp bất đồng bộ, xử lý các tác vụ nền tốn thời gian, hoặc điều phối các luồng dữ liệu (data streaming).
