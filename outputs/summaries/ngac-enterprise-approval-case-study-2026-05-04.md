---
title: "Case Study: Giải bài toán Phê duyệt Doanh nghiệp với Hybrid NGAC"
source: "compiled"
date_added: 2026-05-04
tags: [summary, ngac, architecture, case-study]
aliases: [NGAC Enterprise Approval, Bài toán NGAC cho doanh nghiệp]
status: reviewed
related:
  - "[[ngac-practical-implementation]]"
  - "[[ngac-permission-graph]]"
  - "[[ngac-database-design]]"
summary: "Phân tích cách ứng dụng kiến trúc Hybrid NGAC để giải quyết bài toán hiệu năng khi xử lý hàng trăm lệnh chờ duyệt cho hàng nghìn người dùng trong môi trường doanh nghiệp."
---

## Context

Bài toán đặt ra: *Làm thế nào để áp dụng NGAC vào môi trường doanh nghiệp quy mô lớn (ví dụ: hàng nghìn User) với nhu cầu xử lý hàng trăm lệnh chờ duyệt cho mỗi người, yêu cầu phản hồi nhanh chóng và hỗ trợ phân trang (pagination)?*

Việc bê nguyên xi lý thuyết đồ thị gốc của NGAC vào hệ thống sẽ gặp bế tắc về hiệu năng (Graph Traversal quá tải khi đồ thị phình to). Để xử lý mượt mà, hệ thống thực tế áp dụng kiến trúc **Hybrid NGAC**, chia bài toán thành 3 luồng xử lý riêng biệt giữa Đồ thị In-memory và Cơ sở dữ liệu quan hệ (SQL).

## Phân Tích Luồng Xử Lý

### 1. Phía Đồ Thị NGAC (Quản lý hàng nghìn User)
Trong In-memory Graph, hệ thống **tuyệt đối không biến "Lệnh chờ duyệt" thành một Node (Object)**. Đồ thị lúc này cực kỳ tinh gọn, chỉ chứa:
- Nút người dùng (U) và Nhóm chức danh/Phòng ban (UA).
- Các vùng dữ liệu không gian làm việc (OA) và Chính sách (PC).

Nhờ việc lược bỏ Object Node, với vài nghìn User, đồ thị chỉ có vài nghìn nút, chiếm một lượng RAM rất nhỏ (thường <1MB). Tốc độ duyệt đồ thị để trả lời câu hỏi *"User A có quyền duyệt B không?"* (NGAC Guard) diễn ra chưa tới một mili-giây. Mọi thay đổi luân chuyển nhân sự chỉ là việc vẽ lại các cạnh (Assignment) giữa các nút U và UA.

### 2. Quá Trình Sinh Lệnh Duyệt (Resolve & Denormalize)
Khi một "Lệnh" (ví dụ: Xin nghỉ phép, Đề xuất thanh toán) được tạo ra:
1. API sẽ gọi NGAC Graph (đóng vai trò Guard) và hỏi: *"Ai có quyền `[approve]` đối với Vùng dữ liệu (Scope OA) của lệnh này?"*
2. Đồ thị NGAC sẽ duyệt ngược từ OA lên UA và tìm ra chính xác các cá nhân (U) có thẩm quyền.
3. Thay vì giữ kết quả sự vụ này trong Graph, hệ thống sẽ **phi chuẩn hóa (Denormalize)** và ghi kết quả này vào cơ sở dữ liệu quan hệ (RDBMS), cụ thể là lưu vào bảng phi chuẩn hóa (ví dụ: `approval_assignments` với các trường `ticket_id, user_id, status`).

### 3. Phía SQL (Truy vấn hàng trăm Lệnh chờ duyệt)
Khi hàng nghìn người dùng cùng lúc mở màn hình *"Danh sách lệnh chờ duyệt của tôi"*, hệ thống **không đụng tới đồ thị NGAC**.
- API sẽ query thẳng vào SQL: `SELECT * FROM approvals JOIN approval_assignments WHERE user_id = {current_user}`.
- Do dữ liệu nằm ở CSDL quan hệ, các tính năng như Phân trang (Pagination), Sắp xếp (Sorting), Lọc (Filtering) sẽ tận dụng sức mạnh của Index trong SQL, mang lại độ trễ cực thấp (O(log N)).

## Xử Lý Bất Đồng Bộ Khi Đổi Nhân Sự (Reconciliation)

Một thách thức của Hybrid NGAC là khi nhân sự thay đổi (VD: Trưởng phòng cũ nghỉ việc, người mới lên thay):
- **Trên NGAC Graph:** Cập nhật ngay lập tức (Xóa cạnh cũ, nối cạnh mới). Người mới lập tức có quyền duyệt các lệnh sinh ra từ thời điểm này.
- **Trên SQL:** Các lệnh chưa duyệt cũ vẫn đang "gắn" với `user_id` của người cũ (Stale Data). Một tiến trình ngầm (Reconciliation Worker) sẽ được kích hoạt để quét các lệnh chưa duyệt trong bảng `approval_assignments`, dùng NGAC xác định lại người duyệt mới, và re-assign tự động sang `user_id` mới. Các lệnh đã duyệt trong quá khứ được giữ nguyên giá trị lịch sử kiểm toán.

## Kết Luận

Kiến trúc Hybrid NGAC chứng minh sự thành công bằng cách **tách bạch vai trò**:
- Dùng **NGAC Graph** làm cỗ máy tính toán rule logic (Resolution Engine).
- Dùng **SQL Database** làm bộ đệm hiển thị danh sách (List/Store Engine).

## Nguồn Tham Khảo
- [[ngac-practical-implementation]]
- [[ngac-database-design]]
- [[ngac-permission-graph]]
