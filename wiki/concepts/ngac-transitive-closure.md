---
title: "NGAC: Tối Ưu Hóa Bao Đóng Bắc Cầu (Transitive Closure)"
source: "compiled"
date_added: 2026-05-04
tags: [concept, ngac, graph-theory, optimization]
aliases: [Transitive Closure, Materialized Views trong NGAC, NGAC Materialization]
status: canonical
related:
  - "[[ngac-practical-implementation]]"
  - "[[ngac-database-design]]"
summary: "Cơ chế toán học bao đóng bắc cầu trong đồ thị NGAC và các chiến lược tối ưu hóa hiệu năng thông qua vật chất hóa (materialization) và phi chuẩn hóa (denormalization)."
---

# NGAC: Tối Ưu Hóa Bao Đóng Bắc Cầu (Transitive Closure)

## Định Nghĩa

Trong mô hình Next-Generation Access Control (NGAC), hệ thống xác định quyền truy cập thông qua một đồ thị có hướng không có chu trình (DAG). Trong toán học đồ thị, **bao đóng bắc cầu** (Transitive Closure) mô tả khả năng tiếp cận (reachability) – nghĩa là xác định xem có bất kỳ đường đi hợp lệ nào từ một đỉnh (User/Subject) đến một đỉnh khác (Object/Resource) hay không. Do vậy, việc quyết định một người dùng có quyền hay không về bản chất chính là bài toán tính toán bao đóng bắc cầu trên đồ thị NGAC.

**Vật chất hóa** (Materialization) và **Phi chuẩn hóa** (Denormalization) là những chiến lược kiến trúc nhằm lưu trữ trước kết quả của bao đóng bắc cầu, hoán đổi dung lượng bộ nhớ lấy tốc độ xử lý để phá vỡ các rào cản hiệu năng.

## Đánh Đổi Hiệu Năng (Performance Trade-offs)

Thuật toán tính toán bao đóng bắc cầu truyền thống thường tốn kém, độ phức tạp có thể lên tới $O(V^3)$. Nếu phải duyệt đồ thị ngay tại thời điểm thực thi (on-the-fly traversal) mỗi khi có truy vấn kiểm tra quyền, hệ thống sẽ gặp rào cản về khả năng mở rộng (scalability) ở quy mô doanh nghiệp.

Vì vậy, kiến trúc hệ thống buộc phải cân nhắc sự đánh đổi (trade-offs):
- **Đối với hệ thống Read-heavy (Nhiều truy vấn đọc):** Việc lưu trữ trước các đường đi hợp lệ (Materialized Views) cho phép thời gian kiểm tra quyền giảm xuống chỉ còn hằng số $O(1)$.
- **Đối với hệ thống Write-heavy (Nhiều cập nhật quyền):** Mỗi sự thay đổi (thêm/xóa cạnh gán) trên đồ thị gốc đều kéo theo sự vô hiệu hóa và ép buộc hệ thống phải tính toán lại hàng loạt trên đồ thị phi chuẩn hóa. Lúc này, chi phí bảo trì trở thành một gánh nặng lớn.

## Chiến Lược Tối Ưu Hóa

Thay vì phụ thuộc hoàn toàn vào một phương pháp, các hệ thống NGAC hiệu năng cao thường sử dụng các chiến lược sau:

### 1. Materialized Views (Vật chất hóa bộ đệm)
Vật chất hóa các đường dẫn tương đương với việc tạo ra một khung nhìn phi chuẩn hóa (denormalized view) chuyên dụng. Policy Decision Point (PDP) không cần phải thực hiện hành động "duyệt" đồ thị mà thay vào đó là thực hiện "tra cứu" trực tiếp trên bộ nhớ đệm (Cache). 

### 2. Cập nhật tăng dần (Incremental Updates)
Trong môi trường có tính động cao, việc tính toán lại toàn bộ bao đóng bắc cầu là bất khả thi. Khi một cạnh (Assignment) bị thay đổi, hệ thống áp dụng thuật toán tối ưu để xác định và chỉ tính toán lại riêng nhánh/mảnh đồ thị bị ảnh hưởng.

### 3. Hybrid Architecture (Kiến trúc lai)
Thay vì duy trì tính vật chất hóa trên Graph Database (Graph DB) đắt đỏ, hệ thống có thể tách biệt quyền truy cập và dữ liệu hiển thị:
- **Graph Guard:** Giữ Graph PDP làm nhiệm vụ gác cổng trả lời `YES/NO` bằng việc duyệt nhanh trong bộ nhớ (In-memory).
- **Denormalized SQL:** Phi chuẩn hóa danh sách các kết quả (ai có quyền đối với danh sách đối tượng nào) xuống một cơ sở dữ liệu quan hệ chuyên biệt. Điều này phục vụ riêng cho các truy vấn theo dạng danh sách (List) và phân trang (Pagination), vượt qua được giới hạn duyệt sâu của đồ thị truyền thống.

## Liên Hệ / Ứng Dụng

- Triển khai thuật toán Đồ thị (Graph algorithms) vào cơ sở dữ liệu quan hệ (ví dụ: Recursive CTE trong PostgreSQL).
- Thiết kế hệ thống Access Control phân tán hiệu năng cao, lấy cảm hứng từ cấu trúc Zanzibar của Google (sử dụng tuple để tạo quan hệ).

## Nguồn Tham Khảo

- Tổng hợp về kỹ thuật vật chất hóa và phi chuẩn hóa để tối ưu hóa đồ thị NGAC: `raw/articles/ngac-materialized-denormalize.md`
