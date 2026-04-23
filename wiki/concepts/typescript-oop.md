---
title: "Lập Trình Hướng Đối Tượng Trong TypeScript (OOP)"
source: "compiled"
date_added: 2026-04-23
tags: [typescript, oop, access-modifiers, concept]
aliases: [TypeScript OOP, Access Modifiers, TypeScript Class]
status: canonical
related:
  - "[[typescript]]"
  - "[[tsconfig]]"
summary: "Kiến trúc Lập trình Hướng đối tượng (OOP) trong TypeScript và hệ thống bảo mật dữ liệu thông qua các Bổ từ Truy Cập (Access Modifiers)."
---

# Lập Trình Hướng Đối Tượng Trong TypeScript (OOP)

## Định Nghĩa
Trong [[typescript]], cấu trúc `Class` không chỉ đóng vai trò là một khuôn mẫu (bản thiết kế) hướng đối tượng thuần túy, mà còn thiết lập một cơ chế đóng gói (Encapsulation) mạnh mẽ để kiểm soát luồng dữ liệu. Tài liệu *"Sinh Tồn Trong Kỷ Nguyên Kỹ Thuật Số"* mô tả Class như "khung xương cho một Exosuit", và các Access Modifiers (Bổ từ truy cập) chính là "các lớp giáp bảo vệ phi công khỏi các can thiệp bên ngoài hoặc mã độc".

## Các Bổ Từ Truy Cập (Access Modifiers)

### 1. Cấp độ `public` (Mặc định)
Là cấp độ truy cập mở nhất. Mọi thuộc tính và phương thức đều có thể được đọc và ghi từ mọi nơi (cả bên trong lớp, lớp kế thừa và các thực thể khởi tạo bên ngoài). Nếu không định nghĩa rõ ràng, TypeScript mặc định coi mọi thành viên là `public`.

### 2. Sự khác biệt giữa `private` và `#private`
TypeScript và JavaScript cung cấp hai cơ chế bảo vệ riêng tư với sự khác biệt cốt lõi về thời điểm thực thi (Compile-time vs Runtime):

*   **`private` (Chuẩn TypeScript):**
    Ngăn chặn việc truy cập dữ liệu từ bên ngoài hoặc từ các lớp con (Subclasses) tại thời điểm **biên dịch (Compile-time)**. Tuy nhiên, sau khi mã được dịch sang JavaScript, lớp bảo vệ này hoàn toàn biến mất (do cơ chế Type Erasure), khiến dữ liệu có thể bị thay đổi tại Runtime nếu bị truy cập trực tiếp.
*   **`#private` (Chuẩn ECMAScript):**
    Sử dụng ký tự `#` trước tên biến. Đây là cơ chế bảo vệ chặt chẽ (Hard-Private) được hỗ trợ trực tiếp bởi Engine JavaScript (V8). Dữ liệu này thực sự bất khả xâm phạm tại **thời điểm chạy (Runtime)**. Việc cố tình truy cập sẽ gây ra lỗi Cú pháp (`SyntaxError`). Tài liệu so sánh cơ chế này như một "Hộp đen bọc chì tàng hình", tuyệt đối an toàn.

### 3. Cấp độ `protected`
Cung cấp khả năng bảo vệ chia sẻ trong chuỗi kế thừa (Inheritance). Thuộc tính `protected` có thể truy cập nội bộ và bên trong các lớp con (Subclasses) được mở rộng (extends) từ lớp cha, nhưng hoàn toàn bị cấm truy cập từ các thực thể khởi tạo bên ngoài (Instances).

### 4. Bổ từ tĩnh `readonly`
Đóng vai trò niêm phong dữ liệu (Factory Sealed). Các thuộc tính được gắn `readonly` chỉ có thể được gán giá trị tại thời điểm khai báo hoặc thông qua phương thức khởi tạo (`constructor`). Sau giai đoạn đó, giá trị không thể bị thay đổi (tương đương với bộ nhớ ROM).

## Bảng So Sánh Quyền Hạn Kiểm Soát

| Cấp Độ Bảo Vệ | Trong Class (Self) | Kế Thừa (Subclass) | Môi Trường Ngoài (Instance) | Bảo Vệ Thời Gian Thực (JS Runtime) |
| :--- | :---: | :---: | :---: | :---: |
| `public` | Có | Có | Có | Không |
| `protected` | Có | Có | Không | Không |
| `private` | Có | Không | Không | Không |
| `#private` | Có | Không | Không | **Có** |
| `readonly` | Có | Chỉ Đọc | Chỉ Đọc | Không |

**Nguyên Tắc Đặc Quyền Tối Thiểu (Principle of Least Privilege):**
Thiết kế hướng đối tượng tốt trong TypeScript đòi hỏi phải mặc định các thuộc tính là `#private` hoặc `private`. Quyền hạn chỉ nên được nới lỏng sang `protected` để phục vụ kế thừa, và chỉ công khai `public` khi bắt buộc cần cung cấp giao diện tương tác ra bên ngoài.

## Nguồn Tham Khảo
- [[raw/articles/ts-module-02.md]]
