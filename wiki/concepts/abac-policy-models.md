---
title: "Mô hình Chính sách ABAC: Logic-Formula và Liệt kê"
source: "compiled"
date_added: 2026-04-23
tags: [concept, abac, policy]
aliases: [ABAC Policy Models, Logic-Formula, Enumerated Policy]
status: draft
related:
  - "[[attribute-based-access-control]]"
summary: "Hai phương pháp biểu diễn chính sách trong ABAC: sử dụng biểu thức logic và liệt kê mối quan hệ."
---

## Định Nghĩa

Trong mô hình [[attribute-based-access-control]], cách thức hệ thống hiểu và xử lý các quy tắc cấp quyền phụ thuộc vào mô hình biểu diễn chính sách. Hiện tại, có hai kỹ thuật chủ đạo để cấu trúc chính sách này: mô hình biểu diễn bằng công thức logic (Logic-Formula) và mô hình liệt kê quan hệ (Enumerated). Cả hai cách tiếp cận đều quyết định tốc độ và độ phức tạp của quá trình kiểm tra quyền hạn trước khi hệ thống cấp luồng truy cập.

## Mô hình Logic-Formula

Mô hình này xác định quyền thông qua các công thức toán hạng kết nối các thuộc tính. Nó sử dụng các mệnh đề logic cơ bản (AND, OR, NOT) hoặc các toán tử so sánh (≥, ≠) để thiết lập một hàng rào điều kiện. 

Ví dụ, một mệnh đề: `Role = "Doctor" AND Target_Ward = Subject_Ward` yêu cầu hệ thống đọc giá trị của thuộc tính để cấp quyền ngay tại thời điểm thực thi.
- **Ưu điểm:** Khả năng biểu diễn mạnh mẽ, bao quát được các yêu cầu kinh doanh phức tạp chỉ trong một câu lệnh duy nhất.
- **Nhược điểm:** Tiêu tốn nhiều tài nguyên xử lý và rất khó để kiểm tra tính toàn vẹn của một chính sách trước khi đưa vào vận hành thực tế. Nó buộc hệ thống phải gán đầy đủ giá trị của tất cả thuộc tính mới có thể đưa ra kết luận.

## Mô hình Liệt kê (Enumerated)

Khác với việc tạo ra quy tắc logic, mô hình này quy định quyền bằng cách vạch sẵn các mối liên kết (đồ thị) chứa đựng hoặc liên kết giữa các tên định danh thuộc tính. Những hệ thống như kiểm soát dựa trên nhãn mác hoặc mô hình [[next-generation-access-control]] (thông qua uai, opsi, oai) là ứng dụng tiêu biểu.

- **Ưu điểm:** Cho phép các thuật toán xử lý đối chiếu một cách hiệu quả. Việc phân tích và kiểm thử độc lập đối với từng người dùng hoặc từng đối tượng được tiến hành dễ dàng bằng cách duyệt qua các liên kết đã định sẵn.
- **Nhược điểm:** Khi số lượng thuộc tính và liên kết chéo gia tăng, sơ đồ tổ chức liệt kê có thể rơi vào trạng thái bùng nổ độ phức tạp, gây khó khăn cho việc quản trị tổng thể.

## Liên Hệ / Ứng Dụng

Việc lựa chọn giữa Logic-Formula hay Liệt kê không phải là một quyết định cứng nhắc mà phụ thuộc vào ưu tiên thiết kế. Nếu một cơ sở dữ liệu đòi hỏi tốc độ kiểm tra các liên kết lớn trước quá trình cấp quyền, mô hình Liệt kê sẽ thể hiện hiệu suất cao. Ngược lại, nếu một hệ thống phân tán đòi hỏi các quy tắc biến động liên tục mà không thể dự đoán trước sơ đồ liên kết, Logic-Formula là cấu trúc bắt buộc để thể hiện sự linh hoạt.

## Nguồn Tham Khảo
- `raw/articles/LogicalFormulaandEnumerated.md`
