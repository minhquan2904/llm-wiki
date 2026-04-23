---
title: "Xác thực (Authentication) và Ủy quyền (Authorization)"
source: "raw/articles/Terminology.md"
date_added: 2026-04-23
tags: [comparison, access-control]
aliases: [AuthN vs AuthZ, Authentication vs Authorization]
status: draft
related:
  - "[[access-control-policy-enforcement]]"
summary: "Phân định ranh giới giữa việc nhận diện danh tính người dùng và quá trình xét duyệt quyền hạn truy cập."
---

## Bối Cảnh

Xác thực (Authentication) và Ủy quyền (Authorization) là hai giai đoạn nền tảng tạo nên bất kỳ chu trình truy cập bảo mật nào. Dù thường xuyên bị nhầm lẫn và gọi chung dưới thuật ngữ "đăng nhập", đây thực chất là hai quy trình có chức năng, nguyên lý và thời điểm thực thi hoàn toàn khác biệt.

## Bảng So Sánh

| Tiêu chí            | Xác thực (Authentication)                     | Ủy quyền (Authorization)                                     |
| ------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| **Câu hỏi cốt lõi** | "Bạn là ai?"                                  | "Bạn được phép làm gì?"                                      |
| **Mục đích**        | Kiểm chứng danh tính (Identity) của thực thể. | Cấp hoặc từ chối quyền (Permissions) của thực thể.           |
| **Phương thức**     | Mật khẩu, sinh trắc học, thẻ từ, mã OTP.      | Danh sách kiểm soát, chính sách dựa trên vai trò/thuộc tính. |
| **Trình tự**        | Là điều kiện tiên quyết, thực hiện trước.     | Hoạt động sau khi xác thực thành công.                       |

## Phân Tích

Mối quan hệ giữa xác thực và ủy quyền có tính chất tuyến tính và phụ thuộc. 

**Xác thực** đảm bảo hệ thống đang tương tác với đúng một cá nhân cụ thể. Hệ thống yêu cầu người dùng cung cấp các bằng chứng (chứng thư số, mật khẩu) để chứng minh họ chính là thực thể mà họ tuyên bố. Tuy nhiên, việc một cá nhân chứng minh được mình là ai không đồng nghĩa với việc họ được phép làm bất cứ thứ gì trong mạng lưới.

Giai đoạn **Ủy quyền** bắt đầu ngay sau khi danh tính đã được xác thực hợp lệ. Hệ thống sẽ ánh xạ danh tính này với cơ sở dữ liệu các [[access-control-entities|Quyền truy cập]] và chính sách. Ngay cả một danh tính hợp lệ vẫn có thể bị từ chối truy cập nếu hành vi của họ vượt quá giới hạn ủy quyền cho phép. Sự thất bại của quá trình xác thực sẽ dẫn đến việc đình chỉ ngay lập tức bước ủy quyền.

## Kết Luận

Một hệ thống kiểm soát quyền hạn vững chắc phải vận hành hoàn hảo ở cả hai khâu. Một cơ chế ủy quyền phức tạp như [[attribute-based-access-control|ABAC]] sẽ vô dụng nếu khâu xác thực lỏng lẻo để lọt kẻ gian với danh tính giả. Ngược lại, xác thực sinh trắc học tiên tiến cũng không thể bảo vệ tổ chức nếu hệ thống thiếu một hàng rào ủy quyền chi tiết, dẫn đến việc cấp quyền hạn vượt mức cần thiết cho nhân viên.

## Nguồn Tham Khảo
- `raw/articles/Terminology.md`
- `raw/articles/PolicyEnforcement.md`
