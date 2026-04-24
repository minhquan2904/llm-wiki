---
title: "Bất Đồng Bộ Trong Spring Boot"
source: "compiled"
date_added: 2026-04-24
tags: [concept, java, spring, async, multithreading]
aliases: [spring-async, enableasync, threadpooltaskexecutor]
status: draft
related:
  - "[[java-concurrency-fundamentals]]"
  - "[[spring-annotations]]"
summary: "Phân tích kiến trúc thực thi bất đồng bộ của Spring Framework dựa trên Annotation @Async và vai trò của ThreadPoolTaskExecutor."
---

# Bất Đồng Bộ Trong Spring Boot

Thực thi bất đồng bộ (Asynchronous Execution) là một mô hình thiết kế nhằm tăng cường thông lượng (throughput) của hệ thống bằng cách đẩy các tác vụ nặng (như gửi email, gọi API bên thứ ba) ra khỏi luồng xử lý yêu cầu chính (Request Thread). Trong Spring Boot, kiến trúc này được đơn giản hóa một cách triệt để thông qua các siêu dữ liệu (Metadata).

## Cấu Trúc Thực Thi Cơ Bản

Mô hình bất đồng bộ của Spring được thiết lập dựa trên hai yếu tố nền tảng:
- **`@EnableAsync`:** Đặt tại lớp cấu hình (Configuration) để ra lệnh cho IoC Container kích hoạt một Bean Post Processor (BPP) chuyên biệt. BPP này có nhiệm vụ rà soát toàn bộ các bean và sinh ra lớp Proxy AOP cho những đối tượng có chứa hàm được đánh dấu bất đồng bộ.
- **`@Async`:** Đặt tại các phương thức cụ thể. Khi có lệnh gọi đến phương thức này, lớp Proxy của Spring sẽ đánh chặn lời gọi, đóng gói thành một tác vụ `Runnable` hoặc `Callable` và ném vào một bể luồng (Thread Pool) để thực thi ngầm.

Sự phụ thuộc vào cơ chế Proxy sinh ra một cạm bẫy thiết kế nghiêm trọng (Proxy Pitfall): Việc gọi một hàm `@Async` từ một hàm khác bên trong cùng một lớp đối tượng (Self-invocation) sẽ làm cơ chế bất đồng bộ thất bại, do luồng điều khiển đi tắt qua mã thực tế mà không đi xuyên qua lớp vỏ Proxy. 

## ThreadPoolTaskExecutor: Trái Tim Xử Lý

Mặc định, nếu không được cấu hình, Spring sử dụng `SimpleAsyncTaskExecutor`. Tuy nhiên, đây là một điểm yếu hệ thống chết người vì trình thực thi này sẽ tạo ra một luồng hệ điều hành hoàn toàn mới cho mỗi tác vụ, gây nguy cơ cạn kiệt tài nguyên bộ nhớ (Out of Memory).

Trong kiến trúc ứng dụng cấp doanh nghiệp (Enterprise Architecture), giới kỹ sư luôn phải tự định nghĩa một `ThreadPoolTaskExecutor` (một cấu trúc bao bọc lớp `ThreadPoolExecutor` lõi của Java). Thiết kế bể luồng đòi hỏi thiết lập ba tham số dung lượng sinh tử:
- **Core Pool Size:** Lực lượng thường trực, sẵn sàng nghênh chiến.
- **Queue Capacity:** Phòng chờ đệm. Chỉ khi phòng chờ này đầy, Spring mới gọi chi viện.
- **Max Pool Size:** Kích thước chi viện tối đa. Nếu vượt quá ngưỡng này, chính sách từ chối (Rejection Policy) sẽ được kích hoạt.

## Giám Sát Cấu Trúc Bất Đồng Bộ

Để nhận về kết quả từ hàm bất đồng bộ, Spring yêu cầu kiểu trả về phải bọc trong các đối tượng tương lai (Future Objects) như `CompletableFuture`. Việc kết hợp `CompletableFuture` với `@Async` cung cấp năng lực kết nối đa chuỗi (Chaining) mượt mà, cho phép khai báo các hành vi "chờ hoàn thành" hoặc "hợp nhất kết quả" mà không làm đóng băng tiến trình chính.

## Nguồn Tham Khảo
- `raw/papers/multithreading-concurrency-trong-spring-boot-từ-cơ-bản-đến-virtual-threads.md`
- `raw/papers/spring-framework-làm-chủ-custom-annotation-metaprogramming.md`
