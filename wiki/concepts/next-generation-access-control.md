---
title: "Kiểm soát truy cập thế hệ tiếp theo (NGAC)"
source: "compiled"
date_added: 2026-04-23
tags: [concept, access-control, ngac, abac]
aliases: [Next-Generation Access Control, NGAC]
status: reviewed
related:
  - "[[ngac-architecture]]"
  - "[[ngac-security-model]]"
  - "[[attribute-based-access-control]]"
  - "[[ngac-practical-implementation]]"
  - "[[ngac-database-design]]"
  - "[[ngac-permission-graph]]"
summary: "Mô hình kiểm soát truy cập (INCITS 565-2020) linh hoạt, hỗ trợ đa chính sách và quản lý sự kiện trạng thái."
---

## Định Nghĩa

Kiểm soát truy cập thế hệ tiếp theo (Next-Generation Access Control - NGAC) là một mô hình kiểm soát quyền hạn được chuẩn hóa bởi **INCITS 565-2020**. Mô hình này khắc phục các giới hạn của mô hình phân quyền truyền thống (RBAC, DAC, MAC) bằng cách cung cấp một bộ khung trừu tượng dữ liệu thống nhất dựa trên đồ thị (graph-based). NGAC cho phép thực thi đồng thời và tương thích nhiều loại chính sách truy cập khác nhau trong cùng một hệ thống.

## Đặc Trưng Cốt Lõi

Khác với các hệ thống chỉ tập trung vào việc định dạng yêu cầu truy cập, NGAC chú trọng việc quản lý cấu trúc các thuộc tính, mối quan hệ chứa đựng, và tính toàn vẹn trạng thái. Hai mảnh ghép lớn tạo nên sự hoàn chỉnh của NGAC bao gồm:

1. **[[ngac-architecture|Kiến Trúc Thực Thi]]:** Dựa trên cấu trúc phân tách luồng dữ liệu (PEP, PDP, PIP, PAP, RAP) và đặc biệt bổ sung **EPP (Event Processing Point)** để nhận diện sự kiện thời gian thực.
2. **[[ngac-security-model|Mô Hình Bảo Mật]]:** Một tập hợp toán học chuẩn hóa (Policy Elements) biểu diễn mọi tài nguyên thông qua định dạng Đồ thị phân cấp và các quan hệ cốt lõi (Assignment, Association, Prohibition, Obligation).

Việc thiết kế dưới dạng mở (open factors) cho phép tổ chức tự do định nghĩa cấu trúc định danh, giao thức truyền thông, và phương pháp mã hóa mà không bị ràng buộc vào các công nghệ cứng nhắc.

## Lợi Thế Và Hạn Chế

Ưu điểm chính của NGAC nằm ở tính **Thống nhất** và **Mở rộng**. Nó cho phép tích hợp các quy tắc quản trị trung ương song song với các thiết lập bảo mật cục bộ của từng bộ phận. Cấu trúc đồ thị giúp thuật toán giải quyết quyền truy cập chỉ ở mức độ phức tạp tuyến tính, đồng thời dễ dàng thích ứng với điện toán đám mây và môi trường phân tán.

Tuy nhiên, tính đa dạng này đồng nghĩa với việc **phức tạp trong triển khai**. Quá trình quy hoạch toàn bộ tài nguyên số thành mô hình Policy Elements của NGAC đòi hỏi sự thiết kế tỉ mỉ ngay từ ban đầu.

## Liên Hệ / Ứng Dụng

NGAC đặc biệt phù hợp trong cấu trúc doanh nghiệp hiện đại hoặc cơ quan công quyền, nơi mà dữ liệu phân tán ở nhiều hệ thống với quyền hạn khác nhau nhưng lại yêu cầu một cửa ngõ kiểm soát duy nhất. Ví dụ, một đám mây chính phủ có thể vận hành các nguyên tắc bảo mật riêng tư cục bộ tại các chi nhánh, đồng thời tuân thủ quy tắc an ninh quốc gia từ trung ương, tất cả được xử lý đồng bộ.

Trong các dự án phần mềm thực tế, việc áp dụng lý thuyết NGAC nguyên bản thường đi kèm với các điều chỉnh kiến trúc để đảm bảo hiệu năng. Xem thêm chi tiết tại:
- **[[ngac-practical-implementation|Triển Khai NGAC Thực Tế]]:** Các quyết định thiết kế mô hình lai (Hybrid Pattern) lược bỏ Object nodes để tối ưu bộ nhớ.
- **[[ngac-database-design|Thiết Kế Cơ Sở Dữ Liệu NGAC]]:** Cách ánh xạ in-memory graph thành các bảng nền tảng trên PostgreSQL.
- **[[ngac-permission-graph|Đồ Thị Quyền NGAC]]:** Phân tích đồ thị quyền áp dụng cho Workspace, Department và Approval.

## Nguồn Tham Khảo
- `raw/ngac/ngac.md` (INCITS 565-2020 standard)
- `raw/articles/NGAC.md`
