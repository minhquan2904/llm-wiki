---
title: "Command Pattern"
source: "compiled"
date_added: 2026-04-24
tags: [concept, design-patterns, oop, command-pattern]
aliases: ["Mẫu thiết kế Command", "Quản lý giao dịch", "Command Object"]
status: draft
related:
  - "[[state-pattern]]"
summary: "Mẫu thiết kế hành vi giúp biến đổi một yêu cầu thành một đối tượng độc lập, hỗ trợ thực thi bất đồng bộ, lưu vết kiểm toán và hoàn tác (Undo)."
---

# Command Pattern

## Định Nghĩa

**Command Pattern** là một mẫu thiết kế thuộc nhóm hành vi (Behavioral Design Pattern). Mẫu thiết kế này "vật thể hóa" (reifying) một yêu cầu, tức là chuyển đổi một yêu cầu thực thi từ dạng phương thức thông thường thành một đối tượng độc lập (Command Object) chứa đầy đủ thông tin về yêu cầu đó (Payload).

Thành phần cơ bản của Command Pattern bao gồm:
1. **Sender / Invoker**: Thành phần phát lệnh (ví dụ: Giao diện người dùng, App).
2. **Command Object**: Đối tượng đóng gói yêu cầu, chứa các phương thức như `execute()`, `undo()`.
3. **Receiver**: Thành phần tiếp nhận và thực thi logic nghiệp vụ lõi (ví dụ: Hệ thống Core Banking).

## Sức Mạnh Cốt Lõi: Hàng Đợi, Kiểm Toán và Hoàn Tác

Việc cô lập yêu cầu thành một đối tượng độc lập mang lại hàng loạt các cơ chế bảo mật và quản lý luồng dữ liệu mạnh mẽ, đặc biệt quan trọng trong các hệ thống tài chính:

* **Hàng đợi (Queue)**: Lệnh có thể được xếp hàng để xử lý bất đồng bộ, trì hoãn thực thi hoặc gửi qua mạng.
* **Kiểm toán & Bảo mật (Audit Trails)**: Bằng cách lưu trữ mọi đối tượng Command, hệ thống có thể truy vết mọi hành động (Timestamp, User, Action, State Before/After, Payload). Điều này là bắt buộc đối với các tiêu chuẩn quốc tế như ISO 27001.
* **Hoàn tác (Undo) và Giao dịch bù trừ (Compensating Transaction)**: Trong các hệ thống kế toán hoặc sổ cái (Ledger), dữ liệu thường có tính bất biến (Immutable), không tồn tại lệnh `DELETE`. Do đó, hành động Undo thực chất là việc thực thi một giao dịch bù trừ. Ví dụ: Nếu lệnh chuyển +100$ bị lỗi, hệ thống sẽ tự động phát sinh một Command bù trừ -100$ (Reversal of Tx) để cân bằng sổ sách.

## Kết Hợp Kiến Trúc Nâng Cao

Command Pattern đóng vai trò là "nguyên liệu" cơ bản cho các mô hình kiến trúc tiên tiến:

* **CQRS (Command Query Responsibility Segregation) & Event Sourcing**:
  * **Command Model (Write)**: Nhận các Command và ghi lại dưới dạng chuỗi các sự kiện (Event Store).
  * **Query Model (Read)**: Tái tạo trạng thái hệ thống từ chuỗi sự kiện lịch sử (Rehydrated State) để phục vụ cho các câu truy vấn hiển thị.
* **State Pattern**: Sự kết hợp giữa State và Command tạo ra **Mô hình Thực thi Có Bảo vệ**. Lệnh Command chỉ được phép thực thi nếu đối tượng State hiện tại cấp phép, đảm bảo an toàn tuyệt đối trước khi hệ thống lõi bị thay đổi.

## Nguồn Tham Khảo
- [[raw/articles/state-and-command-pattern-fintech.md]]
