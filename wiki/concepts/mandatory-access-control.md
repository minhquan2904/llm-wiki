---
title: "Kiểm soát truy cập bắt buộc (Mandatory Access Control - MAC)"
source: "raw/articles/mac.md"
date_added: 2026-04-23
tags: [concept, abac, mac]
aliases: [MAC, Mandatory Access Control]
status: draft
related:
  - "[[discretionary-access-control]]"
  - "[[dac-vs-mac]]"
summary: "Mô hình kiểm soát truy cập nghiêm ngặt do cơ quan quản trị trung tâm thiết lập, không phụ thuộc vào ý muốn của người dùng."
---

## Định Nghĩa

Kiểm soát truy cập bắt buộc (Mandatory Access Control - MAC) là mô hình bảo mật mà trong đó quyền truy cập vào các đối tượng hệ thống được quyết định bởi một cơ quan quản trị trung tâm, dựa trên các quy tắc hệ thống cứng nhắc. Không giống như [[discretionary-access-control]], người dùng thông thường không có khả năng thay đổi quyền truy cập của tài nguyên, kể cả khi họ là người tạo ra tài nguyên đó.

## Các Mô Hình MAC Phổ Biến

MAC không phải là một cơ chế duy nhất mà là một khái niệm bao trùm nhiều mô hình kiểm soát chuyên biệt:

### 1. Bảo mật Đa mức (Multilevel Security - MLS)
MLS được thiết kế chủ yếu cho môi trường quân sự và chính phủ nhằm ngăn chặn luồng thông tin rò rỉ từ các cấp bảo mật cao xuống cấp thấp. Hệ thống gán các mức bảo mật theo thứ bậc (Ví dụ: Tuyệt mật, Bí mật, Không mật) và theo phân loại phòng ban (NATO, Hạt nhân) cho cả chủ thể và đối tượng.
- **Tính chất đơn giản (No read up):** Chủ thể chỉ được đọc đối tượng nếu mức bảo mật của chủ thể thống trị mức bảo mật của đối tượng.
- **Tính chất sao (No write down):** Chủ thể chỉ được ghi vào đối tượng nếu mức bảo mật của đối tượng thống trị mức bảo mật của chủ thể.
Mặc dù chặt chẽ, MLS vẫn đối mặt với rủi ro rò rỉ thông tin qua các "kênh ẩn" (covert channels).

### 2. Bức tường Trung Quốc (Chinese Wall Policy)
Mô hình này phổ biến trong môi trường tài chính, tư vấn nhằm ngăn chặn rủi ro xung đột lợi ích (Conflict of Interest - COI).
Chính sách quy định rằng một chủ thể không thể truy cập dữ liệu của một tổ chức nếu chủ thể đó đã từng tiếp cận dữ liệu của một tổ chức đối thủ thuộc cùng một lớp COI. Quyền đọc và ghi được điều chỉnh linh hoạt theo lịch sử truy cập của người dùng để đảm bảo thông tin nội bộ của các đối thủ cạnh tranh bị cô lập hoàn toàn.

### 3. Cấu hình RBAC theo hướng MAC
Kiểm soát truy cập dựa trên vai trò ([[abac-vs-rbac|RBAC]]) thường được dùng như một phương pháp để giả lập các quy tắc của MAC. Thông qua việc kiểm soát chặt chẽ quá trình cấp phát quyền hạn (Permission), thiết lập phân tách trách nhiệm (Separation of Duty - SoD) và nguyên tắc đặc quyền tối thiểu (Least Privilege), quản trị viên có thể đảm bảo luồng truy cập tuân thủ các chính sách bắt buộc mà không cần triển khai một hệ thống MLS phức tạp.

## Ứng Dụng

Mô hình MAC cung cấp mức độ bảo vệ toàn vẹn và bảo mật dữ liệu ở cấp độ cao nhất. Tuy nhiên, chi phí triển khai, thiết lập nhãn dán bảo mật và quản lý vận hành là những trở ngại lớn, khiến MAC thường chỉ phù hợp cho các cơ quan tình báo, quân sự, y tế hoặc hệ thống tài chính yêu cầu bảo mật nghiêm ngặt.

## Nguồn Tham Khảo
- `raw/articles/mac.md`
