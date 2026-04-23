---
title: "Attribute-Based Access Control (ABAC)"
source: "compiled"
date_added: 2026-04-23
tags: [concept, abac, access-control]
aliases: [ABAC, Kiểm soát truy cập dựa trên thuộc tính]
status: draft
related:
  - "[[abac-architecture]]"
  - "[[abac-attribute-management]]"
  - "[[abac-vs-rbac]]"
summary: "Mô hình kiểm soát truy cập linh hoạt xác định quyền bằng cách đánh giá các thuộc tính của chủ thể, đối tượng và môi trường."
---

## Định Nghĩa

Kiểm soát truy cập dựa trên thuộc tính (Attribute-Based Access Control - ABAC) là một mô hình thiết lập chính sách phân quyền thông qua việc đánh giá các **thuộc tính**. Mô hình này không dựa trên định danh cụ thể hay vai trò cứng nhắc mà tính toán quyền quyết định dựa trên ba nhóm thuộc tính chính: chủ thể (người yêu cầu), đối tượng (tài nguyên), và môi trường (bối cảnh yêu cầu). 

Khác với các hệ thống liệt kê quyền hạn bằng bảng phân quyền cố định, hệ thống này tự động xác định khả năng truy cập tài nguyên khi giá trị thuộc tính thỏa mãn các quy tắc logic hệ quản trị đặt ra.

## Cơ Chế Nhận Diện Và Đánh Giá

Cơ chế phân quyền này hoạt động phụ thuộc vào việc cấu trúc các thực thể dưới định dạng các nhóm trường thông tin.

- **Chủ thể (Subject):** Cung cấp hồ sơ chi tiết đối tượng gửi đi yêu cầu, thông qua các trường mang tính thẻ người dùng như chức danh, bộ phận trực thuộc, các cấp độ chứng chỉ.
- **Đối tượng (Object):** Chỉ định thuộc tính của tài sản dữ liệu được yêu cầu (ví dụ: hồ sơ bệnh lý, dự án kinh doanh), đính kèm với mức độ nhạy cảm hoặc định danh chuyên mục tài liệu.
- **Môi trường (Environment):** Yếu tố khách quan độc lập với vai trò người sử dụng như cấu trúc khung giờ làm việc, địa chỉ IP mạng nội bộ hoặc đo thị phần vị trí thiết bị.

Một chính sách quản trị được vận hành bằng biểu thức liên kết các dữ liệu này lại với nhau nhằm cấp hoặc ngăn chặn các hành vi cụ thể (read/write/delete). 

## Quy Trình Xử Lý Yêu Cầu

Tiến trình truy vấn cấp quyền trong hệ thống phân tán được vận hành qua nhiều nhịp cơ chế tương tác với các node theo khung [[abac-architecture]].

Khi nhận được một phiên truy vấn mới, hệ thống chủ động mở tiến trình lấy mẫu thuộc tính từ các nguồn danh tính liên kết khác. Nó so khớp dữ liệu thời gian thực giữa các thuộc tính của tác tử với khung chính sách. Nếu điều kiện đáp ứng tuyệt đối các quy định thiết lập (chẳng hạn: nhân sự kế toán tại công ty yêu cầu lấy sao kê trên mạng tại công ty trong giờ làm theo ca), cổng sẽ mở kết nối truy xuất với tài nguyên tương ứng. Suốt quy trình này, từng yếu tố được đánh dấu lại giúp quản trị viên nâng cao hiệu năng trong việc xem xét các kịch bản kiểm toán tương lai.

Sự toàn vẹn của mô hình phần lớn nằm ở mức độ hoàn thiện của [[abac-attribute-management]] (quản lý chất lượng thuộc tính phân tán) để tránh cấp sai vì giá trị sai lệch.

## Liên Hệ / Ứng Dụng

Cơ chế logic cho phép các tổ chức xây dựng một khối quy định đồ sộ với độ bảo mật cao. Ngành y tế dùng cách thức này để giới hạn việc xem và tinh chỉnh thông tin điện tử lâm sàng chỉ dành cho bác sỹ chủ trị đúng khoa làm việc. Đối với môi trường giao dịch trực tuyến, các luật kiểm soát chặn hoàn toàn các tiến trình đáng ngờ liên kết từ hành vi thao tác phi chuẩn so với môi trường thông thường.

Mô hình thiết lập này không cần phải thay đổi số lượng nhóm vai trò như một môi trường rườm rà. Nó dễ dàng chia sẻ nguồn lực dữ liệu giữa các cá nhân thuộc phạm vi hoạt động khác biệt như một đối tác công nghệ độc lập mà không dẫn đến vấn đề thiết lập account hệ thống như cấu trúc [[abac-vs-rbac]].

## Nguồn Tham Khảo
- `raw/articles/intro.md`
- `raw/articles/HowABACWork.md`
- `raw/articles/Using.md`
