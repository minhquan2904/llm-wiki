---
title: "So sánh DAC và MAC"
source: "raw/articles/ModelsAndPolicies.md"
date_added: 2026-04-23
tags: [comparison, access-control]
aliases: [DAC vs MAC]
status: draft
related:
  - "[[discretionary-access-control]]"
  - "[[mandatory-access-control]]"
summary: "Phân tích sự khác biệt cốt lõi giữa quản lý truy cập tự do theo người dùng (DAC) và quy tắc tập trung (MAC)."
---

## Bối Cảnh

DAC (Discretionary Access Control) và MAC (Mandatory Access Control) là hai triết lý kiểm soát quyền truy cập cổ điển, đại diện cho hai đầu thái cực của sự cân bằng giữa tính linh hoạt trong chia sẻ tài nguyên và tính nghiêm ngặt trong bảo mật hệ thống. Hiểu rõ ranh giới giữa hai mô hình này là bước đệm quan trọng trước khi tiếp cận các mô hình động như [[attribute-based-access-control]].

## Bảng So Sánh

| Tiêu chí | DAC (Kiểm soát tùy ý) | MAC (Kiểm soát bắt buộc) |
|----------|-----------------------|--------------------------|
| **Cơ quan cấp quyền** | Chủ sở hữu tài nguyên (Người dùng). | Quản trị viên trung tâm (Hệ thống). |
| **Bản chất chia sẻ** | Linh hoạt, tự do cấp hoặc thu hồi quyền. | Cứng nhắc, tuân thủ nghiêm thực nhãn bảo mật. |
| **Tính lan truyền** | Cho phép chia sẻ lại dữ liệu cho bên thứ ba. | Ngăn chặn tuyệt đối việc rò rỉ dữ liệu ngoài luồng. |
| **Nguy cơ bảo mật** | Dễ tổn thương trước mã độc (Trojan horse). | Khả năng phòng ngự toàn diện, tránh thất thoát thông tin. |
| **Độ phức tạp quản lý** | Thấp, dễ triển khai ở quy mô nhỏ. | Cao, đòi hỏi dán nhãn toàn bộ chủ thể và đối tượng. |

## Phân Tích

Sự khác biệt cốt lõi giữa hai mô hình nằm ở **vị trí của quyền quyết định**. 

Trong môi trường **DAC**, một cá nhân tạo ra tệp tin sẽ có toàn quyền đối với tệp tin đó, bao gồm quyền chia sẻ nó cho bất kỳ đồng nghiệp nào. Sự linh hoạt này giúp quá trình làm việc nhóm trơn tru, nhưng lại tước đi quyền kiểm soát luồng dữ liệu của bộ phận bảo mật. Nếu một tài khoản bị thỏa hiệp, mã độc có thể tận dụng quyền sở hữu để nhân bản thông tin.

Ngược lại, hệ thống **MAC** không quan tâm đến người tạo ra tài liệu. Nó chỉ đánh giá dựa trên nhãn bảo mật (Security Labels). Ngay cả khi một nhân sự cấp cao tạo ra một tài liệu nội bộ, họ cũng không thể chủ động gửi nó cho một người ở cấp độ truy cập thấp hơn nếu quy tắc hệ thống không cho phép. MAC thiết lập một rào cản luồng thông tin không thể phá vỡ bởi ý chí cá nhân.

## Kết Luận

DAC là lựa chọn thực tiễn cho các hệ thống máy tính cá nhân, doanh nghiệp nhỏ và các môi trường đề cao tính phối hợp linh hoạt. Trong khi đó, MAC được xem là giải pháp bắt buộc tại các cơ sở quân sự, chính phủ hoặc các hệ thống lưu trữ dữ liệu y tế, nơi việc rò rỉ một phần thông tin nhỏ cũng có thể dẫn đến rủi ro quy mô lớn. Trong thực tế, nhiều hệ điều hành hiện đại áp dụng thiết kế lai (hybrid), sử dụng MAC để bảo vệ hệ thống lõi và cấp quyền DAC cho không gian dữ liệu người dùng.

## Nguồn Tham Khảo
- `raw/articles/ModelsAndPolicies.md`
- `raw/articles/dac.md`
- `raw/articles/mac.md`
