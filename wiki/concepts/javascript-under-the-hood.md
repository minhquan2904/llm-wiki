---
title: "JavaScript Under The Hood: Call Stack, Event Loop & Execution Context"
source: "compiled"
date_added: 2026-04-23
tags: [concept, javascript, core, architecture]
aliases: [Event Loop, Call Stack, Microtask, Macrotask, Execution Context]
status: draft
related:
  - "[[javascript-memory-management]]"
  - "[[javascript-asynchronous-programming]]"
summary: "Phân tích kiến trúc cốt lõi của JavaScript: cơ chế Single-Threaded, Execution Context, quá trình xử lý bất đồng bộ thông qua Web APIs và nguyên lý hoạt động của Event Loop."
---

# JavaScript Under The Hood: Call Stack, Event Loop & Execution Context

Mặc dù JavaScript là một ngôn ngữ **Single-Threaded** (đơn luồng - chỉ thực thi một lệnh tại một thời điểm), nó vẫn có khả năng xử lý các tác vụ mạng, đếm giờ, và tương tác UI phức tạp mà không làm chặn (blocking) luồng chính. 

Khả năng này không bắt nguồn từ bản thân JavaScript Engine, mà đến từ sự phối hợp nhịp nhàng giữa Engine và môi trường lưu trữ (Browser hoặc Node.js). Toàn bộ hệ thống này hoạt động dựa trên 4 thành phần kiến trúc cốt lõi.

## 1. Execution Context & Call Stack

### Execution Context (Bối cảnh thực thi)
Mỗi khi một đoạn mã JavaScript được chạy, một môi trường cô lập được sinh ra gọi là Execution Context. Có hai loại bối cảnh chính:
- **Global Execution Context (GEC):** Khởi tạo đầu tiên khi chạy ứng dụng, sinh ra đối tượng cục bộ (`window` trong Browser) và cấp phát con trỏ `this` mặc định.
- **Function Execution Context (FEC):** Khởi tạo mỗi khi một hàm được gọi.

Mọi Execution Context đều trải qua 2 giai đoạn:
1. **Creation Phase (Pha Khởi Tạo):** JS Engine quét qua mã nguồn, cấp phát vùng nhớ Stack cho các biến và thiết lập cơ chế Hoisting (hoặc Temporal Dead Zone đối với `let/const`). (Xem thêm [[javascript-variables-and-scope|Bản chất quản lý biến]]).
2. **Execution Phase (Pha Thực Thi):** Mã được thực thi tuần tự từ trên xuống dưới, tính toán các biểu thức và gán lại giá trị vào bộ nhớ.

### Call Stack (Ngăn xếp lệnh)
Call Stack là nơi Engine theo dõi lịch sử thực thi mã, hoạt động theo nguyên tắc LIFO (Last-In-First-Out).
- Khi một hàm được gọi, bối cảnh thực thi (FEC) của nó được ném lên đỉnh Stack.
- Engine luôn bắt buộc phải xử lý hàm nằm trên đỉnh Stack trước tiên. 
- Khi hàm tính toán xong (`return`), nó tự động "pop" ra khỏi Stack, nhường quyền điều khiển lại cho hàm bên dưới.

Việc gọi đệ quy không điểm dừng sẽ liên tục nạp các hàm mới vào đây, làm tràn bộ nhớ và gây ra lỗi `Maximum call stack size exceeded`.

## 2. Web APIs (Môi trường cung cấp tính năng)

Bản thân V8 Engine không biết cách thao tác với DOM hay gửi `fetch` API. Khi Call Stack gặp một tác vụ bất đồng bộ (như `setTimeout` hoặc `fetch`), JavaScript lập tức bàn giao (offload) tác vụ này cho **Web APIs** (hoặc C++ APIs trong Node.js). 

Hành vi ủy quyền này giúp Call Stack rảnh tay ngay lập tức để tiếp tục biên dịch dòng code kế tiếp, hình thành nên bản chất Non-blocking I/O mạnh mẽ của ngôn ngữ.

## 3. Hàng Đợi Tác Vụ (Task Queues)

Sau khi Web APIs thực hiện xong tác vụ (hết thời gian timer, nhận được dữ liệu từ Server), nó không được phép đưa kết quả nhảy thẳng vào Call Stack (điều này sẽ gây loạn luồng thực thi). Thay vào đó, Web APIs đẩy các callback vào phòng chờ (Queue) để xếp hàng.

JavaScript có 2 hàng đợi với thứ tự ưu tiên khác biệt:

1. **Microtask Queue (Hàng Đợi V.I.P):** Xử lý ưu tiên tối đa. Phân vùng này chứa các callback được tạo ra từ `Promises` (chuỗi `.then`, `.catch`), từ khóa `async/await`, hoặc đối tượng `MutationObserver`.
2. **Macrotask Queue / Callback Queue (Hàng Đợi Phổ Thông):** Chứa các callback thông thường đến từ `setTimeout`, `setInterval` hay các Event Listener của DOM (ví dụ như click, scroll).

## 4. Kẻ Điều Phối - Event Loop

Event Loop là một vòng lặp đồng bộ vô hạn, giám sát song song Call Stack và Task Queues. Nhiệm vụ của nó là trả lời câu hỏi: *"Ai sẽ là hàm tiếp theo được đẩy lên Call Stack?"*. 

Thuật toán của Event Loop hoạt động cực kỳ chính xác theo các bước sau:
1. Nếu **Call Stack đang bận**, Event Loop đứng đợi.
2. Ngay khi **Call Stack rỗng hoàn toàn**, Event Loop chuyển ánh nhìn xuống các hàng đợi.
3. Đầu tiên, nó "xả" toàn bộ khối lượng công việc trong **Microtask Queue** lên Call Stack. Quá trình xả tiếp tục cho đến khi Microtask Queue trống trơn không còn phần tử nào.
4. Chỉ khi khối lượng công việc V.I.P đã được giải quyết trọn vẹn, Event Loop mới trích xuất **một tác vụ duy nhất** nằm đầu **Macrotask Queue** và đẩy lên Call Stack.
5. Vòng lặp tuần hoàn tiếp diễn lặp đi lặp lại.

Cấu trúc chặt chẽ này giải thích hiện tượng Promise luôn được thực thi trước setTimeout mặc dù cả hai cùng được đẩy ra khỏi Call Stack tại cùng một thời điểm.
