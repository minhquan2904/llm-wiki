---
title: "Kiến Trúc Nhắn Tin Và Realtime NGAC"
source: "raw/ngac/ngac_system/chat-flow.md, raw/ngac/ngac_system/realtime-flow.md"
date_added: 2026-05-04
tags: [concept, ngac, messaging, realtime, websocket]
aliases: [NGAC Messaging System, Realtime Events]
status: reviewed
related:
  - "[[ngac-microservices-architecture]]"
  - "[[publish-subscribe]]"
summary: "Phân tích cơ chế hoạt động của tính năng Chat và hệ thống Realtime WebSocket được bảo vệ bởi NGAC."
---

## Định Nghĩa

Hệ thống nhắn tin (Messaging) và thời gian thực (Realtime) trong môi trường NGAC đảm nhận việc phân phối thông tin, sự kiện và thông báo tới hàng ngàn client cùng lúc với độ trễ tối thiểu. Điểm khác biệt lớn nhất là mọi bản tin, từ tin nhắn chat đến thông báo phê duyệt, đều phải vượt qua đồ thị quyền NGAC trước khi được lưu trữ hoặc chuyển tiếp tới người nhận.

## Thành Phần Cốt Lõi Của Messaging

Hệ thống cung cấp 3 loại kênh giao tiếp:
1. **Workspace Channel:** Kênh chung cho toàn bộ thành viên (vd: #general).
2. **Private Channel:** Kênh kín, chỉ những người được mời mới thấy.
3. **Direct Message (DM):** Kênh riêng tư giữa 2 cá nhân, không thuộc Workspace nào mà được gắn vào `PC_Global`.

Mỗi kênh chat khi sinh ra đều được ánh xạ thành 2 Node trên đồ thị NGAC:
- **Content OA (Tài nguyên):** Chứa các đối tượng tin nhắn, file.
- **Members UA (Người dùng):** Đại diện cho những người có quyền truy cập kênh. 

Hệ thống chỉ cho phép thao tác nếu Policy Service xác nhận có đường dẫn hợp lệ từ User Node tới Content OA của kênh đó.

## Luồng Xử Lý Realtime

Kiến trúc thời gian thực vận hành dựa trên sự kết hợp của 3 công nghệ: WebSocket, Redis Pub/Sub, và Kafka Event Bus.

### 1. Phân Phối Tin Nhắn (WebSocket & Redis)
- **Gửi tin nhắn:** Khi người dùng gửi tin nhắn, HTTP Request tới Messaging Service sẽ được kiểm duyệt quyền qua NGAC. Sau khi lưu vào DB, Server gửi tin nhắn qua WebSocket (dùng định dạng Protobuf nhị phân) tới các client đang theo dõi kênh.
- **Mở Rộng (Scaling) với Redis:** Khi có nhiều Server Instances, một tin nhắn gửi tới Server A sẽ được `publish` lên kênh Redis (`channel:{id}`). Server B `subscribe` kênh này, nhận tin nhắn và đẩy xuống các client đang kết nối với nó.

### 2. Sự Kiện Liên Dịch Vụ (Kafka Event Bus)
- Các microservices khác (như Approval, Asset) không gọi WebSocket trực tiếp. Thay vào đó, chúng phát (publish) sự kiện (Events) lên Kafka.
- Messaging Service hoạt động như một Kafka Consumer. Nó lắng nghe các sự kiện (ví dụ: `ApprovalEvent`), tạo thông báo (Notification) trong Database, và sử dụng WebSocket Hub để đẩy (push) thông báo tới đúng User IDs.
- Cấu trúc bất đồng bộ (Fire-and-forget) này giúp các luồng nghiệp vụ chính không bị chậm trễ dù hệ thống thông báo có đang quá tải.

## Quản Lý Trạng Thái Kết Nối (Presence & Typing)

- **Online/Offline:** WebSocket Hub quản lý danh sách thiết bị. Khi kết nối cuối cùng của một User ngắt đi, sự kiện `PresenceEvent{offline}` được phát đi toàn hệ thống.
- **Typing Indicator:** Gửi sự kiện "đang gõ" qua giao thức ClientEnvelope, Hub tự động loại trừ người đang gõ và broadcast tới toàn bộ client khác trong kênh.
- **Thread Reply:** Khi một luồng phụ (Thread) có cập nhật mới, Server tạo một `ThreadReplyEvent` để cập nhật giao diện người dùng một cách cục bộ thay vì tải lại toàn trang.

## Nguồn Tham Khảo
- `raw/ngac/ngac_system/chat-flow.md`
- `raw/ngac/ngac_system/realtime-flow.md`
