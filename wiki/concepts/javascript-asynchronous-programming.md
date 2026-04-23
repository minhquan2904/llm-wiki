---
title: "JavaScript Asynchronous Programming"
source: "compiled"
date_added: 2026-04-23
tags: [concept, javascript, core, async]
aliases: [Bất đồng bộ, Promise, Async/Await, Callback Hell]
status: draft
related:
  - "[[javascript-under-the-hood]]"
  - "[[clean-code-javascript-patterns]]"
  - "[[rxjs-reactive-programming]]"
summary: "Tiến trình tiến hóa của xử lý bất đồng bộ trong JavaScript: từ hạn chế của Callbacks, đến sự ra đời của Promises và cú pháp Async/Await hiện đại, cùng chiến thuật gọi song song Promise.all."
---

# JavaScript Asynchronous Programming

Do bản chất đơn luồng (Single-Threaded) của [[javascript-under-the-hood|Event Loop và Call Stack]], JavaScript phải áp dụng mô hình xử lý bất đồng bộ (Asynchronous) để đảm đương các tác vụ mất thời gian (I/O, gọi API, đọc file) mà không làm đóng băng (block) luồng giao diện chính.

Hành trình chinh phục bất đồng bộ của JavaScript đã trải qua ba kỷ nguyên tiến hóa quan trọng.

## 1. Kỷ Nguyên Callbacks & Vấn Nạn Callback Hell

Ban đầu, JavaScript sử dụng **Callback** (hàm truyền vào dưới dạng tham số) để thông báo khi một tác vụ bất đồng bộ hoàn tất. Tuy nhiên, cách làm này lộ rõ nhược điểm chí mạng khi các tác vụ có tính phụ thuộc tuần tự. 

Việc gọi API B dựa trên kết quả của API A, và tiếp tục API C từ kết quả của B, sẽ sinh ra cấu trúc mã lồng nhau liên tục, đẩy lề phải của mã nguồn thụt sâu dần. Hiện tượng này được gọi là **Callback Hell** (hay Kim tự tháp diệt vong - Pyramid of Doom). Cấu trúc này không chỉ khó đọc mà còn gây cực kỳ nhiều khó khăn trong việc theo dõi và xử lý lỗi (error handling) ở các tầng khác nhau.

## 2. Kỷ Nguyên Promises (ES2015)

Để thoát khỏi Callback Hell, chuẩn ES6 giới thiệu **Promise** (Lời hứa). Promise là một đối tượng đại diện cho một tác vụ có thể hoàn tất (hoặc thất bại) trong tương lai. 

Một Promise luôn nằm ở một trong ba trạng thái:
- `Pending`: Đang xử lý, chưa có kết quả.
- `Fulfilled / Resolved`: Tác vụ thành công, trả dữ liệu vào hàm `.then()`.
- `Rejected`: Tác vụ thất bại, trả lỗi vào hàm `.catch()`.

**Ưu điểm cốt lõi:** Promise giải quyết bài toán lồng ghép bằng cách cho phép nối chuỗi (Flat Chaining) các `.then()`. Lợi thế lớn nhất là khả năng sử dụng duy nhất một khối `.catch()` ở cuối chuỗi để "tóm" toàn bộ lỗi phát sinh từ bất kỳ mắt xích nào phía trên, giúp luồng kiểm soát lỗi trở nên tập trung và an toàn.

## 3. Kỷ Nguyên Hiện Đại: Async / Await (ES2017)

Dù Promise đã là một bước tiến lớn, việc nối chuỗi `.then()` vẫn mang tư duy lập trình hàm, đôi khi khó làm quen với lập trình viên backend. `async` / `await` ra đời như một "Syntactic Sugar" (cú pháp hỗ trợ) xây dựng trên nền tảng Promise.

**Sức mạnh của Async/Await:**
- Giúp mã bất đồng bộ đọc phẳng phiu như mã đồng bộ tuyến tính (synchronous).
- Tạm dừng (block giả lập) không gian của hàm chứa từ khóa `await` cho đến khi tác vụ hoàn thành, nhưng hoàn toàn không chặn (non-blocking) luồng chính của trình duyệt.
- Cho phép sử dụng khối `try...catch` truyền thống để xử lý lỗi một cách tự nhiên.

*Lưu ý:* Từ khóa `await` chỉ được phép sử dụng bên trong một hàm đã được khai báo với tiền tố `async` (trừ trường hợp Top-Level Await trong ES Modules).

## 4. Bẫy Hiệu Suất: Gọi Tuần Tự (Serial) vs Song Song (Parallel)

Khi lạm dụng `async/await`, lập trình viên dễ rơi vào bẫy gọi tuần tự (Serial) không cần thiết. Nếu bạn viết nhiều lệnh `await` nằm kế tiếp nhau trên từng dòng để lấy dữ liệu từ 3 API hoàn toàn độc lập (không dựa vào data của nhau), mã sẽ phải chờ API 1 chạy xong mới kích hoạt API 2. Tổng thời gian xử lý bằng tổng thời gian của cả 3 API cộng lại, gây sụt giảm nghiêm trọng khả năng đáp ứng đồng thời (Concurrency).

**Giải Pháp `Promise.all`:**
Khi các tác vụ bất đồng bộ không có sự phụ thuộc lẫn nhau, hãy kích hoạt chúng cùng lúc và dùng `Promise.all([...])` để chờ đợi. Bằng cách này, tổng thời gian phản hồi chỉ bằng tác vụ chậm nhất trong nhóm, tối ưu hóa triệt để hiệu năng mạng. (Tương tự [[clean-code-javascript-patterns#xử-lý-bất-đồng-bộ-trong-vòng-lặp|xử lý vòng lặp bất đồng bộ]]).
