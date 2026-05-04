---
title: "NGAC Database Design: Ánh Xạ Đồ Thị Quyền"
source: "raw/ngac/ngac_in_real_project/permission-db-mapping.md"
date_added: 2026-05-04
tags: [concept, ngac, database, schema, sql]
aliases: [NGAC Schema Mapping, NGAC Database Design]
status: canonical
related:
  - "[[ngac-practical-implementation]]"
  - "[[next-generation-access-control]]"
summary: "Phân tích cách ánh xạ in-memory graph của NGAC thành 3 bảng cốt lõi trong cơ sở dữ liệu quan hệ, kết nối với dữ liệu nghiệp vụ và sử dụng Recursive CTE để debug."
---

# NGAC Database Design: Ánh Xạ Đồ Thị Quyền

## Định Nghĩa

Thiết kế cơ sở dữ liệu NGAC (NGAC Database Design) là việc hiện thực hóa mô hình dữ liệu đồ thị NGAC vào một hệ quản trị cơ sở dữ liệu quan hệ (như PostgreSQL). Do NGAC hoạt động ở chế độ *in-memory graph* để đáp ứng tốc độ phản hồi tính bằng mili-giây, CSDL không dùng để tính toán quyền lúc runtime mà đóng vai trò là "Source of Truth" (Kho lưu trữ gốc) dùng để nạp đồ thị khi khởi động và ghi nhận các sự kiện thay đổi quyền. Kiến trúc này sử dụng 3 bảng nền tảng không chứa dữ liệu nghiệp vụ, thay vào đó liên kết với dữ liệu nghiệp vụ bằng khóa ngoại.

## 3 Bảng Cốt Lõi (Core Tables)

Toàn bộ đồ thị quyền được mô tả qua 3 bảng chính:

1. **`ngac_nodes`**: Lưu trữ mọi đỉnh trong đồ thị.
   - Bao gồm các cột: `id` (PK), `name` (tên mang tính gợi nhớ), `node_type` (phân loại U, UA, OA, PC), `properties` (metadata JSONB).
2. **`ngac_assignments`**: Lưu trữ các cạnh phân cấp (Containment) trong đồ thị.
   - Định nghĩa quan hệ cha-con: `child_id` (ví dụ User A) trỏ tới `parent_id` (ví dụ Phòng ban B).
   - Một bản ghi ở đây giúp nút con kế thừa toàn bộ quyền của nút cha.
3. **`ngac_associations`**: Lưu trữ các cạnh cấp quyền (Permissions).
   - Nối giữa `ua_id` (User Attribute) và `oa_id` (Object Attribute).
   - Chứa mảng `operations` như `[read, write, approve]`.

## Kết Nối Với Bảng Nghiệp Vụ (Business Tables)

Các bảng chứa logic hệ thống (Business Data) hoàn toàn không lưu thông tin phân quyền phức tạp. Chúng chỉ trỏ một khóa ngoại (Foreign Key) sang `ngac_nodes`:

- Bảng `users`: Lưu cột `ngac_node` trỏ tới node loại `U`.
- Bảng `departments`: Lưu `ngac_ua_id` trỏ tới loại `UA`.
- Bảng `drive_items` (Files/Folders): Lưu `ngac_node_id` trỏ tới `OA` (thường là OA của folder chứa nó).

Nhờ kiến trúc này, hệ thống quyền và hệ thống kinh doanh (business) được tách bạch hoàn toàn.

## Schema-per-Tenant & Bảng Phi Chuẩn Hóa (Denormalization)

Để giải quyết bài toán hiệu năng hiển thị danh sách (như tính năng liệt kê các phê duyệt đang chờ), hệ thống áp dụng kỹ thuật Denormalization và cách ly theo Tenant:

- **Schema-per-tenant**: Dữ liệu phê duyệt không lưu chung ở public schema mà lưu trong schema riêng (ví dụ: `tenant_{workspace_id}`).
- **`approval_assignments`**: Bảng này ghi nhận ai được quyền duyệt một yêu cầu cụ thể (`user_node_id`, `status`). 
- Quy trình: Hệ thống chỉ chọc vào NGAC một lần khi tạo phiếu để "dò tìm" người duyệt, sau đó ghi chú lại vào bảng này. Mọi tác vụ list/paging sau đó chỉ dùng thuần SQL mà không phải duyệt qua cây NGAC, đảm bảo độ trễ O(log N).

## Truy Vấn Đệ Quy (Recursive CTE) Để Debug

Mặc dù hệ thống không dùng SQL để kiểm tra quyền lúc runtime, các câu lệnh truy vấn SQL đệ quy (`WITH RECURSIVE`) là công cụ bắt buộc để debug và kiểm toán (audit). 

Ví dụ, khi một người dùng gặp lỗi "Access Denied", quản trị viên sẽ dùng truy vấn đệ quy để:
1. Duyệt ngược từ node User lên trên (`ngac_assignments`) để tìm xem người này đạt được tới nút Policy Class (PC) nào.
2. Duyệt ngược từ node Resource lên trên xem tài nguyên nằm ở PC nào.
3. Kiểm tra xem có chung PC hay không (Giao điểm quyền hạn - Intersection Principle).
4. Khảo sát bảng `ngac_associations` giữa các đường dẫn vừa tìm được xem có đủ `operations` hay không.

## Liên Hệ / Ứng Dụng

- Phân rã dữ liệu từ Graph Database sang RDBMS.
- Xây dựng hệ thống Audit log quyền hạn thông qua CSDL quan hệ.
- Viết kịch bản kiểm thử (Test queries) cho NGAC.

## Nguồn Tham Khảo

- Sơ đồ ánh xạ Database: `raw/ngac/ngac_in_real_project/permission-db-mapping.md`
- Các câu lệnh SQL Debug NGAC: `raw/ngac/ngac_in_real_project/permission-check-queries.md`
