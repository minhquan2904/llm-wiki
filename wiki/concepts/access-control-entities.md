---
title: "Các Thực Thể Kiểm Soát Truy Cập Cơ Bản"
source: "raw/articles/Terminology.md"
date_added: 2026-04-23
tags: [concept, access-control]
aliases: [Thực thể kiểm soát truy cập, Chủ thể và Đối tượng]
status: draft
related:
  - "[[access-control-policy-enforcement]]"
summary: "Hệ thống thuật ngữ và các định nghĩa về thành tố tham gia vào mạng lưới kiểm soát quyền truy cập."
---

## Định Nghĩa

Các mô hình kiểm soát quyền hạn cổ điển được xây dựng dựa trên sự tương tác giữa một nhóm các thực thể nền tảng. Dù hệ thống ứng dụng mô hình tự do (DAC), bắt buộc (MAC) hay dựa trên vai trò (RBAC), kiến trúc của chúng đều xoay quanh việc định dạng sự tương tác giữa Chủ thể và Đối tượng.

## Các Thành Tố Cơ Bản

- **Chủ thể (Subject):** Đại diện cho người dùng, hoặc bất kỳ tiến trình hệ thống, phần mềm, thiết bị nào có thể khởi tạo hành động thay mặt người dùng. Chủ thể là các thực thể chủ động duy nhất trong hệ thống, mang theo danh tính và trạng thái để tác động hoặc truyền tải thông tin.
- **Đối tượng (Object):** Là các tài nguyên thụ động cần được bảo vệ trong hệ thống, ví dụ như tập tin, cơ sở dữ liệu, cổng mạng hoặc máy trong tổ chức.
- **Quyền truy cập (Access Right):** Quy tắc quy định phạm vi tác động mà một người dùng có thể thực hiện trên một đối tượng (ví dụ: đọc, ghi, thực thi).

## Cấu Trúc Quyền Hạn

Trong hệ thống thực tế, các quyền không chỉ áp dụng đơn thuần lên tài nguyên vật lý mà được phân tách thành các cấp độ.

1. **Quyền hạn (Privilege):** Đại diện cho một khả năng cụ thể của người dùng đối với một đối tượng được chỉ định. Tập hợp toàn bộ các đặc quyền của một người dùng tạo thành một **Bộ quyền**.
2. **Hoạt động (Operation):** Hành động thực thi chức năng trong hệ thống, được chia thành hai nhánh chính:
   - *Hoạt động tài nguyên:* Các tương tác trực tiếp lên Đối tượng (như Đọc, Ghi dữ liệu).
   - *Hoạt động quản trị:* Các hành động tác động vào hạ tầng kiểm soát, như cấp quyền, thu hồi quyền, tạo lập và sửa đổi chính sách.
3. **Quyền (Permission):** Đi liền với các loại hoạt động trên, quyền cũng được chia làm Quyền tài nguyên (cho phép tương tác với dữ liệu) và Quyền quản trị (cho phép điều chỉnh hệ thống phòng thủ).

## Ý Nghĩa Trong Triển Khai

Trong hầu hết các kiến trúc, hệ thống không lưu trữ quyền hạn dưới dạng một danh sách đơn giản gồm 3 yếu tố [Chủ thể, Hoạt động, Đối tượng]. Thay vào đó, chúng được biểu diễn thông qua cấu trúc gián tiếp như danh sách khả năng (Capability Lists), danh sách kiểm soát truy cập (ACL) hoặc gắn kết qua hệ thống các Vai trò, nhằm tối ưu hiệu năng duyệt quyền trong quá trình [[access-control-policy-enforcement|Thực thi chính sách]].

## Nguồn Tham Khảo
- `raw/articles/Terminology.md`
