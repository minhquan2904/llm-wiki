---
title: "Kiến trúc ABAC (PEP, PDP, PAP, PIP)"
source: "compiled"
date_added: 2026-04-23
tags: [concept, abac, architecture]
aliases: [ABAC Architecture, PEP, PDP, PAP, PIP]
status: draft
related:
  - "[[attribute-based-access-control]]"
  - "[[next-generation-access-control]]"
summary: "Cấu trúc thành phần chức năng kiểm soát vòng đời một yêu cầu truy cập trong mô hình kiểm soát dựa trên thuộc tính."
---

## Tổng Quan Kiến Trúc

Kiến trúc của mô hình [[attribute-based-access-control]] là một mạng lưới các bộ phận (point) tiếp nhận, ra quyết định và thực thi. Việc phân rã chức năng này thành các phần độc lập cho phép hệ thống triển khai kiểm soát quyền trên nhiều loại tài nguyên với sự tích hợp bảo mật sâu.

Một luồng xét duyệt cơ bản phải đi qua ít nhất bốn khối chức năng lõi để tiến hành khớp lệnh từ yêu cầu của người sử dụng với ngôn ngữ biểu diễn của hệ thống.

## Các Thành Phần Quyết Định Lõi

- **PEP (Policy Enforcement Point - Điểm Thực Thi Chính Sách):** Cơ chế cổng giao tiếp (gateway) chuyên chặn bắt yêu cầu từ ứng dụng. Đây là điểm vào, nơi hệ thống gom góp dữ liệu ban đầu để bao bọc thành một lệnh chuyển tiếp, và cũng là điểm cuối nhận lệnh đóng/mở tài nguyên nhằm ngăn chặn mọi hình thức vượt quyền ở cấp thấp nhất.
- **PDP (Policy Decision Point - Bộ Quyết Định Chính Sách):** Tổ hợp cốt lõi xử lý logic toán hạng. Nó phân tích yêu cầu do PEP gửi đến, đối chiếu bộ từ khóa thuộc loại quyền, đánh giá với tập chính sách đang vận hành và trả về một phán quyết tuyệt đối duy nhất (Allow hoặc Deny).
- **PAP (Policy Administration Point - Bộ Quản Lý Chính Sách):** Trung tâm điều khiển chính dành riêng cho quản trị viên cấu hình định dạng câu lệnh và khởi tạo vòng đời một luật truy cập. Nó biên dịch các chính sách bằng ngôn ngữ hệ thống cho chức năng của PDP.
- **PIP (Policy Information Point - Điểm Cung Cấp Thông Tin):** Cầu nối liên tục khai thác dữ liệu thuộc tính từ cơ sở hạ tầng tổ chức. Nó cung cấp cho trung tâm quyết định các trạng thái động theo thời gian thực (ví dụ như tình trạng kết nối thiết bị hay chức danh thay đổi mới nhất từ bộ phận nhân sự).

## Cơ Chế Luồng Phối Hợp Bổ Sung

Khi quy mô tăng tuyến tính, các luồng thông tin yêu cầu một kỹ thuật bổ trợ giúp tăng độ tin cậy đồng bộ và chống rò rỉ mã khi thực thi tài nguyên cấp vật lý.

Hai bộ xử lý thường trực bổ sung bao gồm:
- **Bộ Xử Lý Ngữ Cảnh (Context Handler):** Cầu nối trung gian giữa PEP và PDP có nhiệm vụ đồng bộ định dạng. Nó sẽ gỡ gói yêu cầu ban đầu, kết hợp gọi bổ sung từ PIP, sau đó dựng lại khối thông tin yêu cầu đóng gói đầy đủ và đồng nhất để giao cho hệ quyết định.
- **RAP (Resource Access Point - Điểm Truy Cập Tài Nguyên):** Cơ chế tường gác cơ sở tài nguyên vật lý cuối cùng. Sau khi nhận được tín hiệu OK từ cấp trên, RAP tương tác dữ liệu và thu thập tình trạng đọc/ghi về nền tảng. Hệ điều hành bảo vệ tài liệu chặn đứng mọi lệnh đến mà không thông qua bước xuất trình thông hành từ mô hình RAP này.

Một biến thể nâng cao bổ sung sự quản lý sự kiện trạng thái vào luồng xử lý gọi là mô hình [[next-generation-access-control]].

## Nguồn Tham Khảo
- `raw/articles/ArchitecturesandFunctionalComponents.md`
