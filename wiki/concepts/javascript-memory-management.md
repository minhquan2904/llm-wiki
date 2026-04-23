---
title: "JavaScript Memory Management: Stack, Heap & Garbage Collection"
source: "compiled"
date_added: 2026-04-23
tags: [concept, javascript, core, performance]
aliases: [Stack, Heap, Garbage Collection, Memory Leak]
status: draft
related:
  - "[[javascript-variables-and-scope]]"
  - "[[javascript-under-the-hood]]"
summary: "Cơ chế cấp phát và giải phóng bộ nhớ trong JavaScript, sự khác biệt giữa Stack và Heap, nguyên lý dọn rác Mark-and-Sweep, và các nguyên nhân gây Memory Leak."
---

# JavaScript Memory Management: Stack, Heap & Garbage Collection

JavaScript là ngôn ngữ tự động thu gom rác (Garbage-collected language), nghĩa là trình biên dịch (Engine) tự động đảm nhận việc cấp phát khi dữ liệu được tạo ra và giải phóng bộ nhớ khi chúng không còn được sử dụng. Tuy nhiên, việc thiếu hiểu biết về cơ chế lưu trữ có thể dẫn đến các vấn đề nghiêm trọng về hiệu suất như rò rỉ bộ nhớ (Memory Leak) hoặc những hành vi tham chiếu không mong muốn.

Bộ nhớ trong JavaScript Engine (như V8) được chia thành hai khu vực chuyên trách: **Stack** và **Heap**.

## 1. Stack Memory (Bộ Nhớ Ngăn Xếp)

Stack là cấu trúc dữ liệu tuyến tính hoạt động theo nguyên tắc LIFO (Last-In-First-Out). Nó được thiết kế để xử lý dữ liệu có kích thước tĩnh, phân bổ nhanh chóng và giải phóng ngay khi ngữ cảnh thực thi (Execution Context) kết thúc.

### Đặc Điểm Lưu Trữ
- **Dữ Liệu Nguyên Thủy (Primitive Values):** Mọi kiểu dữ liệu nguyên thủy như `String`, `Number`, `Boolean`, `Undefined`, `Null`, `Symbol`, và `BigInt` đều được cấp phát dung lượng cứng và lưu trữ trực tiếp trên Stack.
- **Biến Tham Chiếu (Reference Pointers):** Khi khởi tạo Object hoặc Array, Stack không lưu trữ bản thân cấu trúc dữ liệu đó mà chỉ lưu một địa chỉ bộ nhớ (pointer) trỏ xuống vùng Heap chứa dữ liệu thực.
- **Trạng Thái Thực Thi:** Stack cũng là nơi ghi nhận lịch sử gọi hàm thông qua cơ chế Call Stack.

### Hành Vi Sao Chép
Khi gán một biến nguyên thủy sang một biến khác, JavaScript nhân bản một giá trị độc lập hoàn toàn trên một ô nhớ Stack mới. Sự thay đổi ở biến này không ảnh hưởng đến biến kia.

## 2. Heap Memory (Bộ Nhớ Động)

Heap là không gian lưu trữ phi cấu trúc, rộng lớn hơn, dùng để chứa dữ liệu phức tạp có khả năng thay đổi cấu trúc hoặc phình to trong quá trình thực thi (Dynamic data).

### Đặc Điểm Lưu Trữ
- **Kiểu Tham Chiếu (Reference Types):** Các cấu trúc dữ liệu phức tạp như `Object`, `Array`, và `Function` được đặt trọn vẹn trong Heap.
- **Tốc Độ Xử Lý:** Truy xuất dữ liệu từ Heap chậm hơn Stack do Engine phải thực hiện bước trung gian: tra cứu địa chỉ pointer lưu ở Stack, sau đó mới tìm đến đúng phân vùng dữ liệu dưới Heap.

### Hành Vi Tham Chiếu & Cạm Bẫy Đột Biến (Mutation)
Khác với Stack, khi gán một biến Object sang một biến mới, JavaScript không tạo ra một Object mới trong Heap. Nó chỉ sao chép địa chỉ pointer ở Stack. Hậu quả là cả hai biến cùng trỏ vào một bộ nhớ duy nhất. Bất kỳ sự thay đổi (mutation) nào thực hiện trên một biến cũng sẽ làm thay đổi trực tiếp biến còn lại. 

Đây cũng là lý do từ khóa `const` không thể bảo vệ Object khỏi việc bị sửa đổi thuộc tính; `const` chỉ khóa địa chỉ pointer trên Stack, không can thiệp vào tính chất "có thể đột biến" của dữ liệu dưới Heap. Hãy xem [[javascript-variables-and-scope|Bản chất tính bất biến của const]].

## 3. Garbage Collection (Cơ Chế Thu Gom Rác)

Garbage Collector (GC) là tiến trình chạy ngầm giúp thu hồi lại vùng nhớ từ những dữ liệu không còn giá trị sử dụng.

### Thuật Toán Mark-and-Sweep (Đánh Dấu & Quét)
Thay vì đếm số lần tham chiếu, Engine hiện đại áp dụng nguyên lý **Reachability** (Tính có thể tiếp cận).
1. **Roots (Gốc):** Quá trình bắt đầu từ các đối tượng gốc mặc định luôn tồn tại, ví dụ như `window` trong trình duyệt hoặc `global` trong Node.js.
2. **Mark (Đánh Dấu):** GC duyệt từ rễ, lần theo toàn bộ mạng lưới các pointer đang trỏ tới dữ liệu. Bất kỳ đối tượng Heap nào nằm trong mạng lưới này được đánh dấu là "Reachable" (đang sống).
3. **Sweep (Quét rác):** Các phân vùng Heap không được đánh dấu sẽ bị xem là rác mồ côi (không còn biến Stack nào trỏ tới) và bị hệ thống xóa sổ, trả lại dung lượng RAM trống.

## 4. Rò Rỉ Bộ Nhớ (Memory Leaks)

Memory Leak xảy ra khi một lượng lớn bộ nhớ đã hoàn thành nhiệm vụ thực tế nhưng vẫn vô tình giữ kết nối tham chiếu đến Roots, khiến thuật toán Mark-and-Sweep không thể dọn dẹp. Các nguyên nhân phổ biến nhất bao gồm:

- **Global Variables:** Quên sử dụng `let`/`const` khiến biến bị đẩy thẳng vào Root scope (`window`), buộc Engine phải duy trì biến đó suốt vòng đời của ứng dụng.
- **Event Listeners & Timers Vô Chủ:** Các hàm callback gắn vào `addEventListener` hay `setInterval` là các tham chiếu sống. Khi một DOM element bị hủy khỏi giao diện nhưng không gọi `removeEventListener` hoặc `clearInterval`, khối lượng công việc và dữ liệu trong callback vẫn treo vĩnh viễn trên bộ nhớ.
- **Closure Ngâm Quá Lâu:** Một [[javascript-variables-and-scope#lexical-scope-và-closure|hàm Closure]] liên tục hoạt động sẽ duy trì môi trường scope cha của nó. Nếu dữ liệu trong scope cha rất lớn nhưng hàm Closure sống mãi, Engine sẽ không bao giờ dám thu gom dữ liệu đó.
