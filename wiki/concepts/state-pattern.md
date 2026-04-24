---
title: "State Pattern"
source: "compiled"
date_added: 2026-04-24
tags: [concept, design-patterns, oop, state-pattern]
aliases: ["Mẫu thiết kế State", "Quản lý trạng thái"]
status: draft
related:
  - "[[command-pattern]]"
summary: "Mẫu thiết kế hành vi cho phép một đối tượng thay đổi hành vi của nó khi trạng thái nội bộ thay đổi, giúp loại bỏ các câu lệnh điều kiện phức tạp."
---

# State Pattern

## Định Nghĩa

**State Pattern** là một mẫu thiết kế thuộc nhóm hành vi (Behavioral Design Pattern), cho phép một đối tượng (Context) thay đổi hành vi của nó khi trạng thái nội bộ bị thay đổi. Đối tượng đó dường như sẽ thay đổi luôn cả lớp (class) của nó. Cơ chế này đạt được bằng cách tách biệt mỗi trạng thái thành một lớp riêng biệt và ủy quyền các hành vi tương ứng cho đối tượng trạng thái hiện tại.

## Vai Trò Giải Quyết Vấn Đề

Trong các hệ thống phần mềm nghiệp vụ phức tạp (ví dụ: Core Banking trong FinTech), vòng đời của một thực thể thường đi qua rất nhiều trạng thái khác nhau (ví dụ: Tài khoản chuyển từ `New` -> `Active` -> `Suspended` -> `Closed`). 

Việc quản lý trạng thái truyền thống thường phụ thuộc vào các biến cờ (flags) phức tạp và một khối lượng lớn các câu lệnh điều kiện (if-else/switch-case) chồng chéo. Hệ quả là "Spaghetti code", rủi ro bảo trì cực cao và dễ dẫn đến lỗi khi một sửa đổi logic ở trạng thái này vô tình làm hỏng trạng thái khác.

State Pattern giải quyết dứt điểm vấn đề này thông qua nguyên tắc **Single Responsibility (SRP)**:
1. **Mỗi trạng thái là một Class riêng biệt.**
2. **Context (Bối cảnh)**: Giữ một tham chiếu đến đối tượng State hiện tại và ủy quyền (delegate) mọi công việc liên quan đến trạng thái cho đối tượng này.

## So Sánh Kỹ Thuật: State vs. Strategy Pattern

Mặc dù có sơ đồ UML (kiến trúc lớp) gần như tương đồng, mục tiêu và cách vận hành của hai mẫu thiết kế này lại hoàn toàn khác biệt:

| Tiêu chí | State Pattern | Strategy Pattern |
|----------|---------------|------------------|
| **Mục tiêu (Focus)** | Cái gì (What/Status) - Quản lý vòng đời thực thể. | Như thế nào (How/Algorithm) - Chọn thuật toán để thực thi. |
| **Tác nhân thay đổi** | Tự động, do quá trình nội tại (Internal Transitions) kích hoạt. | Do Client chủ động lựa chọn và cấu hình từ bên ngoài (External Choice). |
| **Nhận thức nội bộ** | Các lớp State thường biết về sự tồn tại của nhau để thực hiện chuyển đổi trạng thái (Transitions). | Các Strategy hoàn toàn độc lập, không biết về nhau. |

## Sự Hợp Nhất Chiến Lược (Kết Hợp Command Pattern)

Trong kiến trúc bền vững, State Pattern thường kết hợp với Command Pattern tạo thành **Mô hình Thực thi Có Bảo vệ (Guarded Execution Model)**:
1. Một lệnh thực thi (Command) được gửi đến hệ thống.
2. Context (ví dụ: Tài khoản) sẽ hỏi State hiện tại xem hành động này có được phép thực thi hay không.
3. Nếu không được phép (ví dụ: Tài khoản đang `Suspended`), yêu cầu sẽ bị từ chối ngay lập tức.
4. Ngược lại, nếu lệnh được thực thi thành công và dẫn đến sự thay đổi trạng thái (ví dụ: Rút tiền làm số dư nhỏ hơn 0), lệnh đó có thể tác động ngược lại để Context chuyển trạng thái (ví dụ: Chuyển sang `OverdrawnState`).

## Nguồn Tham Khảo
- [[raw/articles/state-and-command-pattern-fintech.md]]
