---
title: "So sánh ABAC và RBAC"
source: "compiled"
date_added: 2026-04-23
tags: [comparison, abac, rbac, access-control]
aliases: [ABAC vs RBAC, So sánh ABAC và RBAC]
status: draft
related:
  - "[[attribute-based-access-control]]"
summary: "Phân tích sự khác biệt giữa mô hình kiểm soát truy cập dựa trên thuộc tính (ABAC) và dựa trên vai trò (RBAC)."
---

## Bối Cảnh

Mô hình kiểm soát truy cập dựa trên vai trò (RBAC) và dựa trên thuộc tính (ABAC) là hai phương pháp phổ biến nhất trong quản lý danh tính và quyền truy cập hiện đại. Việc lựa chọn giữa hai mô hình này quyết định kiến trúc bảo mật của tổ chức, ảnh hưởng trực tiếp đến khả năng mở rộng, độ phức tạp quản trị và mức độ chi tiết trong kiểm soát luồng dữ liệu.

## Bảng So Sánh

| Tiêu chí | ABAC (Attribute-Based) | RBAC (Role-Based) |
|----------|------------------------|-------------------|
| **Cơ sở xác định** | Thuộc tính (người dùng, tài nguyên, môi trường) | Vai trò tĩnh được gán cho người dùng |
| **Độ chi tiết** | Rất cao, linh hoạt và tinh tế | Thấp hơn, bị giới hạn ở mức vai trò |
| **Khả năng mở rộng** | Dễ dàng mở rộng bằng cách thêm thuộc tính mới | Hạn chế, yêu cầu tạo mới và cấu hình lại vai trò |
| **Quản trị** | Tập trung vào chính sách, ít vai trò cố định, đơn giản hơn ở quy mô lớn | Phức tạp khi số lượng vai trò (role explosion) tăng cao |
| **Tài nguyên tính toán** | Đòi hỏi nhiều tài nguyên hơn để đánh giá chính sách động | Hiệu suất cao, tiêu tốn ít tài nguyên tính toán hơn |

## Phân Tích

### Ưu thế của ABAC
ABAC vượt trội ở khả năng kiểm soát truy cập chi tiết thông qua việc sử dụng nhiều chiều thông tin (thời gian, vị trí, ngữ cảnh). Khi tổ chức phát triển, ABAC mở rộng linh hoạt mà không cần phải tái cấu trúc hệ thống quyền hạn. Các chính sách điều khiển trực tiếp trên thuộc tính giúp đơn giản hóa việc đối phó với các kịch bản ngoại lệ hoặc yêu cầu kiểm soát phức tạp từ môi trường đa tổ chức.

### Hạn chế của ABAC
Sự linh hoạt của ABAC đi kèm với sự phức tạp trong quá trình định nghĩa ban đầu. Các tổ chức phải thiết lập một khung quản lý thuộc tính chuẩn mực (xem [[abac-attribute-management]]). Hơn nữa, việc đánh giá hàng loạt chính sách tại thời gian thực đòi hỏi năng lực tính toán cao hơn, có thể tạo độ trễ trong các hệ thống yêu cầu phản hồi tức thời.

### Ưu thế và Hạn chế của RBAC
RBAC có lợi thế ở sự đơn giản và dễ hiểu. Việc cấp quyền theo nhóm vai trò trực quan giúp giảm tải tài nguyên hệ thống và đẩy nhanh quá trình triển khai ban đầu. Tuy nhiên, trong các hệ thống quy mô lớn có sự biến động nhân sự liên tục, RBAC dễ rơi vào tình trạng "bùng nổ vai trò" (role explosion), khi quản trị viên phải tạo ra hàng ngàn vai trò vi mô để đáp ứng các trường hợp kiểm soát đặc thù.

## Kết Luận

RBAC phù hợp cho các hệ thống quy mô nhỏ đến trung bình, có tính ổn định cao và yêu cầu bảo mật ít phức tạp. Trong khi đó, ABAC là giải pháp hiệu quả cho các tổ chức lớn, phân tán, yêu cầu kiểm soát truy cập chi tiết, linh hoạt với ngữ cảnh và có khả năng mở rộng liên tục mà không làm tăng gánh nặng quản lý vai trò.

## Nguồn Tham Khảo
- `raw/articles/ABACvsRBAC.md`
