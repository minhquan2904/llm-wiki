---
title: "Mô Hình Tổ Chức Và Vòng Đời Người Dùng NGAC"
source: "raw/ngac/ngac_system/organization-structure.md, raw/ngac/ngac_system/user-lifecycle.md"
date_added: 2026-05-04
tags: [concept, ngac, organization, identity]
aliases: [NGAC Organization Model, User Lifecycle]
status: reviewed
related:
  - "[[ngac-permission-graph]]"
  - "[[ngac-microservices-architecture]]"
summary: "Cách hệ thống NGAC tổ chức người dùng, Workspace, Department và vòng đời định danh qua JWT."
---

## Định Nghĩa

Mô hình tổ chức trong hệ thống NGAC là cách ánh xạ cấu trúc của một công ty/doanh nghiệp ngoài đời thực (bao gồm không gian làm việc, phòng ban, và vai trò) vào trong đồ thị quyền hạn (Permission Graph). Điều này tạo ra ranh giới dữ liệu an toàn giữa các nhóm (Tenants) và định hình hành trình của người dùng từ lúc đăng ký đến khi tương tác với hệ thống.

## Cấu Trúc Tổ Chức (Organizational Structure)

Hệ thống không sử dụng các khái niệm "Role" cứng nhắc (như Admin, User, Viewer). Thay vào đó, quyền được xác định bởi vị trí của người dùng trong cây tổ chức:

### Workspace (Không Gian Làm Việc)
Là đơn vị tổ chức cao nhất, đại diện cho một công ty. Dữ liệu giữa các Workspace được cách ly hoàn toàn.
- Khi tạo Workspace, một **Policy Class (PC)** gốc được sinh ra.
- Hệ thống tự động thiết lập 3 nhóm tài nguyên (OA): Quản lý (Mgmt), Tài liệu (Documents), và Kênh chat (Channels).
- 2 nhóm người dùng (UA) được khởi tạo: **Owners** (Chủ sở hữu - có toàn quyền) và **Members** (Thành viên - có quyền đọc/ghi cơ bản).

### Department (Phòng Ban)
Phòng ban chia nhỏ Workspace và có thể lồng nhau (Nested).
- Mỗi phòng ban tạo ra một nhóm **Thành viên phòng ban (UA)** và một nhóm **Trưởng phòng (Chief UA)** lồng bên trong.
- Trưởng phòng tự động kế thừa quyền của thành viên và có thêm quyền quản lý trên tài nguyên riêng của phòng ban đó.

## Vòng Đời Người Dùng (User Lifecycle)

Hành trình của người dùng được gắn kết chặt chẽ với "Node quyền" NGAC của họ:

1. **Đăng ký (Registration):** Khi tạo tài khoản, bên cạnh lưu thông tin cơ bản, hệ thống sinh ra một **Node quyền (U)** duy nhất. Node này là "chìa khóa" định danh cho mọi kiểm tra quyền sau này. Ban đầu, Node U được gán vào nhóm `PublicUsers`.
2. **Đăng nhập (Authentication):** Sau khi xác thực thành công, hệ thống cấp một **JWT Token**. Token này chứa không chỉ User ID mà cả **NGAC Node ID** và thông tin Workspace mặc định (Tenant).
3. **Phân quyền (Assignment):** Khi người dùng được mời vào Workspace hoặc gán vào phòng ban, Node U của họ sẽ được tạo cạnh (Edge) liên kết tới các nhóm UA tương ứng trong đồ thị NGAC.
4. **Kết nối Realtime:** Trình duyệt tự động mở kết nối WebSocket, gửi JWT Token trong vòng 5 giây đầu để xác thực. Server theo dõi kết nối này để phát sự kiện Presence (Online/Offline) và gửi thông báo. Một người dùng có thể mở nhiều tab (nhiều kết nối), hệ thống chỉ đánh dấu Offline khi kết nối cuối cùng bị đóng.

## Liên Hệ / Ứng Dụng

Cơ chế này mang lại lợi ích lớn trong môi trường Multi-tenant:
- Quản lý vòng đời chặt chẽ: Việc thu hồi quyền của một người dùng chỉ đơn giản là cắt đứt các cạnh (Assignment) nối từ Node U của họ tới các nhóm UA, khiến quyền có hiệu lực thay đổi tức thì.
- Giao tiếp bảo mật: Mọi request HTTP và WebSocket đều mang theo JWT chứa `ngac_node_id`, giúp Policy Service dễ dàng truy vết và cấp quyền động mà không cần truy vấn phức tạp vào database người dùng.

## Nguồn Tham Khảo
- `raw/ngac/ngac_system/organization-structure.md`
- `raw/ngac/ngac_system/user-lifecycle.md`
