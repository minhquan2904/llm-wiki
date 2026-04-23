---
title: "JavaScript Variables, Scope & Functions"
source: "compiled"
date_added: 2026-04-23
tags: [concept, javascript, core]
aliases: [Scope, Closure, Hoisting, Arrow Function]
status: draft
related:
  - "[[javascript-under-the-hood]]"
  - "[[clean-code-javascript-patterns]]"
summary: "Tổng hợp cơ chế khai báo biến (var/let/const), phạm vi hoạt động (Scope), Hoisting, Closure và cấu trúc hàm trong JavaScript."
---

# JavaScript Variables, Scope & Functions

Trong hệ sinh thái JavaScript, cách thức khai báo biến và định nghĩa hàm ảnh hưởng trực tiếp đến cấu trúc bộ nhớ và vòng đời dữ liệu. Bài viết này làm rõ các cơ chế quản trị trạng thái biến, phân tích sự rò rỉ bộ nhớ, và các nguyên lý đằng sau phạm vi hoạt động của mã nguồn.

## Các Từ Khóa Khai Báo Biến

JavaScript cung cấp ba từ khóa chính để cấp phát vùng nhớ: `var`, `let`, và `const`. Chúng khác biệt chủ yếu về phạm vi hoạt động (scope), khả năng khai báo lại, và quy luật kéo dãn (Hoisting).

### `var` và Function Scope
`var` là từ khóa khai báo nguyên thủy của JavaScript. Đặc điểm chí mạng của nó là chỉ hiểu được **Function Scope** (phạm vi hàm) hoặc **Global Scope** (phạm vi toàn cục), mà bỏ qua các giới hạn của khối lệnh block (`{...}`). Điều này dẫn đến hiện tượng "rò rỉ" (leak) biến ra bên ngoài vòng lặp hoặc lệnh điều kiện if-else. Ngoài ra, `var` cho phép khai báo lại nhiều lần trong cùng một scope mà không báo lỗi, làm tăng nguy cơ ghi đè dữ liệu.

### `let`, `const` và Block Scope (ES6)
Để giải quyết những nhược điểm của `var`, chuẩn ES6 (2015) giới thiệu `let` và `const`. Cả hai đều áp dụng **Block Scope**, nghĩa là chúng chỉ tồn tại an toàn bên trong cặp dấu ngoặc nhọn `{...}` khai báo chúng. 
- **`let`**: Được thiết kế cho các biến số có thể thay đổi giá trị theo thời gian.
- **`const`**: Tạo ra một ràng buộc tham chiếu bất biến (constant binding). 

### Bản Chất Tính Bất Biến Của `const`
Sử dụng `const` ngăn chặn hoàn toàn việc gán lại định danh biến (reassignment) vào một giá trị khác. Tuy nhiên, nó không đảm bảo tính bất biến nội hàm (immutability) của dữ liệu. Nếu `const` trỏ đến một kiểu dữ liệu tham chiếu (Reference Type) như Object hay Array, thuộc tính bên trong của cấu trúc đó hoàn toàn có thể bị thay đổi (mutated). Để đóng băng hoàn toàn một đối tượng ở mức bề mặt nông, lập trình viên sử dụng phương thức `Object.freeze()`.

## Hoisting và Temporal Dead Zone (TDZ)

Hoisting là cơ chế JavaScript đưa các khai báo lên đầu scope tại Giai đoạn Khởi tạo Bộ nhớ (Memory Creation) của [[javascript-under-the-hood|Execution Context]].

- **Hoisting với `var`**: Trình biên dịch đưa từ khóa lên đầu scope và cấp phát ngay giá trị mặc định là `undefined`. Điều này cho phép gọi biến trước cả khi luồng mã thực thi đến dòng khai báo.
- **Temporal Dead Zone (Vùng chết tạm thời)**: Trái với `var`, biến khai báo bằng `let` và `const` vẫn bị hoisted nhưng không được khởi tạo giá trị. Khoảng trống từ đầu scope cho đến dòng khai báo biến được gọi là TDZ. Mọi nỗ lực truy cập biến trong TDZ đều sẽ kích hoạt lỗi `ReferenceError`, giúp đảm bảo tính an toàn của thứ tự mã nguồn.

## Các Kiểu Khai Báo Hàm (Functions)

Hàm trong JavaScript là First-class citizens (Công dân hạng nhất), cho phép chúng được coi như biến, truyền làm tham số hoặc trả về giá trị.

1. **Function Declaration (Hàm Khai Báo):** Viết bằng từ khóa `function` ở đầu. Nó được hoisted toàn bộ cả cấu trúc lên đỉnh scope, cho phép gọi hàm trước khi khai báo.
2. **Function Expression (Biểu Thức Hàm):** Gán một hàm ẩn danh vào một biến. Cơ chế hoisting phụ thuộc vào từ khóa (`var` hay `let/const`) khai báo biến chứa hàm đó.
3. **Arrow Function (Hàm Mũi Tên):** Cú pháp tinh gọn từ ES6. Ngoài việc ngắn gọn, Arrow Function sở hữu một cơ chế xử lý tham chiếu `this` cực kỳ khác biệt so với Regular Function.

## Vấn Đề Về Ngữ Cảnh (`this`)

Ngữ cảnh tham chiếu của `this` là nguồn gốc sinh ra nhiều hành vi khó đoán.
- Trong **Regular Function**, `this` trỏ về đối tượng (Object) trực tiếp gọi hàm đó vào thời điểm thực thi.
- Trong **Arrow Function**, cơ chế này bị loại bỏ. Hàm mũi tên sử dụng Lexical `this`, nghĩa là nó sẽ "kế thừa" giá trị `this` từ phạm vi hàm cha (môi trường bao bọc nó) tại thời điểm nó được viết ra. Nhờ vậy, Arrow Function là cấu trúc hoàn hảo để viết các hàm callback (ví dụ `setTimeout`) mà không làm suy hao ngữ cảnh.

Để cưỡng chế tham chiếu `this` cho một hàm nhất định, ngôn ngữ cung cấp bộ ba chức năng [[javascript-advanced-mechanisms|call, apply và bind]].

## Lexical Scope và Closure

Lexical Scope quy định rằng phạm vi truy cập biến của một hàm phụ thuộc vào vị trí khối mã tĩnh của nó lúc được lập trình, không phụ thuộc vào nơi hàm được gọi.

Từ Lexical Scope, cơ chế **Closure (Bao đóng)** được sinh ra. Closure xảy ra khi một hàm nội bộ (inner function) duy trì kết nối bền vững với các biến trong scope của hàm cha bao bọc nó, ngay cả khi hàm cha đã kết thúc quá trình thực thi và bị xóa khỏi Call Stack. Closure là nguyên lý cốt lõi để khởi tạo các biến private, bảo vệ dữ liệu khỏi sự can thiệp từ bên ngoài và đóng gói module thay cho các mẫu thiết kế OOP truyền thống.
