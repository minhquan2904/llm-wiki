---
title: "Kiến Trúc Microservices Của Hệ Thống NGAC"
source: "raw/ngac/ngac_system/overview.md, raw/ngac/ngac_system/system-architecture.md"
date_added: 2026-05-04
tags: [concept, ngac, microservices, system-design]
aliases: [NGAC Microservices Architecture]
status: reviewed
related:
  - "[[ngac-architecture]]"
  - "[[ngac-practical-implementation]]"
summary: "Cấu trúc microservices của nền tảng dựa trên NGAC, bao gồm API Gateway, gRPC, Event-Driven với Kafka và Redis."
---

## Định Nghĩa

Kiến trúc Microservices của hệ thống NGAC (trong bối cảnh dự án Enterprise) là một hệ sinh thái các dịch vụ phân tán, được thiết kế để xử lý khối lượng lớn truy cập đồng thời đảm bảo kiểm soát quyền hạn chặt chẽ qua NGAC. Trái ngược với kiến trúc Monolithic, hệ thống này tách biệt rõ ràng trách nhiệm của từng service, sử dụng API Gateway làm cổng giao tiếp và Event Bus để đồng bộ dữ liệu bất đồng bộ.

## Các Lớp Kiến Trúc (Architecture Layers)

### 1. API Gateway (Traefik)
Traefik đóng vai trò là điểm vào duy nhất (Single Entry Point) cho toàn bộ request từ Client (Web/Mobile).
- Nó thực hiện phân giải URL (Routing) để định tuyến request tới đúng dịch vụ (VD: `/api/v1/auth/*` chuyển tới Auth Service).
- Traefik cũng hỗ trợ Load Balancing, tự động phân phối tải giữa các bản sao (replicas) của cùng một dịch vụ, giúp hệ thống mở rộng ngang (Horizontal Scaling) dễ dàng.

### 2. Các Dịch Vụ Cốt Lõi (Core Services)
Hệ thống bao gồm khoảng 10 microservices, được viết bằng Golang để tối ưu hiệu năng:
- **Policy Service:** "Bộ não" của hệ thống, chứa NGAC Engine. Mọi dịch vụ khác đều phải gọi Policy Service để kiểm tra quyền trước khi thực hiện hành động.
- **Auth Service:** Xử lý xác thực (Login/Register), cấp phát JWT token, và quản lý session.
- **Workspace Service:** Quản lý cấu trúc tổ chức (Tenant, Department, User Groups).
- **Messaging Service:** Quản lý kênh chat, tin nhắn và kết nối realtime qua WebSocket.
- **Asset / Approval Service:** Quản lý tài sản vật lý và quy trình phê duyệt (Workflow).
- **Drive Service:** Quản lý lưu trữ tệp tin và thư mục trên đám mây (S3).

## Giao Tiếp Giữa Các Dịch Vụ (Inter-Service Communication)

Để các dịch vụ hoạt động trơn tru, hệ thống áp dụng nhiều cơ chế giao tiếp khác nhau tùy thuộc vào ngữ cảnh:

### Giao Tiếp Đồng Bộ (Synchronous - gRPC)
- Khi một dịch vụ cần kết quả trả về ngay lập tức để tiếp tục xử lý (VD: Messaging Service hỏi Policy Service xem User A có quyền gửi tin nhắn không), hệ thống sử dụng **gRPC**.
- gRPC dùng Protobuf (Protocol Buffers) để truyền tải dữ liệu dạng nhị phân, mang lại tốc độ nhanh hơn nhiều so với JSON/REST và tích hợp sẵn cơ chế kiểm tra kiểu dữ liệu (Type Safety).

### Giao Tiếp Bất Đồng Bộ (Asynchronous - Kafka/Redpanda)
- Đối với các tác vụ không cần phản hồi ngay (Fire-and-forget), hệ thống sử dụng kiến trúc Event-Driven thông qua **Kafka (hoặc Redpanda)**.
- Ví dụ: Khi một yêu cầu mua hàng được duyệt, Approval Service sẽ "phát" (publish) sự kiện lên Kafka. Messaging Service "nghe" (consume) sự kiện này và tự động tạo thông báo gửi cho người dùng mà không làm chậm quá trình duyệt của Approval Service.

### Giao Tiếp Thời Gian Thực (Realtime - Redis & WebSocket)
- Kết nối từ Server tới Client được duy trì qua WebSocket để đẩy thông báo và tin nhắn mới ngay lập tức.
- Để đồng bộ hóa trạng thái giữa nhiều instance của Messaging Service, hệ thống sử dụng **Redis Pub/Sub**. Khi Server A nhận tin nhắn mới, nó đẩy lên Redis, Server B nhận từ Redis và chuyển tiếp cho các Client đang kết nối với Server B.

## Cơ Chế Quản Lý Dữ Liệu (Data Management)

Hệ thống áp dụng triệt để nguyên tắc **Database-per-service**:
- Mỗi microservice sở hữu một Database (PostgreSQL) riêng biệt. Không có dịch vụ nào được phép truy cập trực tiếp vào DB của dịch vụ khác.
- Việc này ngăn chặn tình trạng thắt cổ chai ở cơ sở dữ liệu dùng chung và tránh các truy vấn chéo phức tạp làm sập hệ thống.
- Khi cần dữ liệu từ dịch vụ khác, các dịch vụ phải gọi gRPC hoặc lắng nghe sự kiện từ Kafka.

Mọi thực thể (User, Channel, File, Request) trong các database riêng lẻ đều có một cột quan trọng: `ngac_node_id`. Cột này đóng vai trò như một mỏ neo (anchor), liên kết thực thể nghiệp vụ với đồ thị quyền hạn tập trung tại Policy Service.

## Nguồn Tham Khảo
- `raw/ngac/ngac_system/overview.md`
- `raw/ngac/ngac_system/system-architecture.md`
