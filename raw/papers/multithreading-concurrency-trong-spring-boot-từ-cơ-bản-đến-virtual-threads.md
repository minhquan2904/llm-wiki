---
title: "Multithreading & Concurrency trong Spring Boot: Từ Cơ Bản đến Virtual Threads"

date_added: 2026-04-24
tags: [papers]
status: draft
summary: ""
---

# Multithreading & Concurrency trong Spring Boot: Từ Cơ Bản đến Virtual Threads

Tối đa hóa Thông lượng (Throughput) và Khả năng phản hồi (Responsiveness).

## Thread vs. Process: Hiệu quả đi kèm rủi ro

- **Process (Tiến trình):** Chương trình độc lập, bộ nhớ (Memory Space) riêng biệt. Giao tiếp giữa các tiến trình (IPC) thường chậm.
- **Thread (Luồng):** Đơn vị thực thi nhẹ (Lightweight). Nhiều thread cùng chia sẻ chung một Heap Memory.
- **Rủi ro:** Chia sẻ Heap Memory đồng nghĩa với việc dễ gặp Race Conditions.

## Cơ chế Spring Proxy & @Async

- **Cơ chế:** Khi Client gọi một hàm có gắn `@Async` (External Call), Spring Proxy (Interceptor) sẽ chặn lời gọi này để đẩy task vào TaskExecutor, sau đó giao cho Worker Thread xử lý bất đồng bộ. Main Thread sẽ không bị blocking.
- **Cạm bẫy (Self-Invocation):** Việc gọi method nội bộ trong cùng một class (ví dụ: `this.method()`) sẽ bỏ qua lớp Proxy và chạy đồng bộ (Blocking Main Thread).

## Cấu hình ThreadPoolTaskExecutor: Hiểu đúng về Queue

- **Quy trình xử lý thread pool:** Core Pool ➔ Queue Capacity ➔ Max Pool ➔ Rejection Policy.
- **Sai lầm phổ biến:** Lập trình viên thường nghĩ rằng Spring sẽ tăng số lượng thread lên mức Max trước khi đưa task vào Queue.
- **Thực tế:** Thứ tự hoạt động chuẩn là: Lấp đầy Core Threads ➔ Lấp đầy Queue ➔ Tạo New Threads (cho tới khi chạm mức Max) ➔ Reject task.
- **Lời khuyên:** Hãy luôn định nghĩa Bean riêng biệt, đừng sử dụng cấu hình mặc định.

## Nguy hiểm từ Mặc định: SimpleAsyncTaskExecutor

- **Cơ chế mặc định:** Tạo mới một Thread cho MỖI request được gửi đến.
- **Vấn đề:** Không có cơ chế tái sử dụng luồng (No Pooling).
- **Hậu quả:** Gây cạn kiệt tài nguyên hệ thống (Out of Memory / Memory Leak) khi hệ thống chịu tải cao.

## Race Conditions: Khi song song hóa gây lỗi dữ liệu

- **Race Condition:** Xảy ra khi nhiều thread cùng đọc/ghi vào một tài nguyên chung tại cùng một thời điểm mà không có cơ chế đồng bộ. (Ví dụ: Thread A và Thread B cùng đọc giá trị 0, cùng cộng 1 và cùng ghi đè giá trị 1 thay vì giá trị kỳ vọng là 2).
- **Nguyên tắc:** Thao tác "Check-then-act" hoàn toàn không an toàn nếu thiếu cơ chế Lock.

## Công cụ Đồng bộ hóa (Synchronization Tools)

- **Cơ bản (synchronized):** Dễ sử dụng, chặn (lock) toàn bộ block/method. Tuy nhiên, dễ gây ra nút thắt cổ chai về mặt hiệu năng.
- **Linh hoạt (ReentrantLock):** Cho phép kiểm soát cao hơn (hỗ trợ try-lock, timeout). Yêu cầu phải quản lý giải phóng lock trong khối try/finally.
- **Hiệu năng cao (Atomic Variables):** Cơ chế Non-blocking thông qua CAS (Compare-And-Swap). Rất tối ưu cho các tác vụ như đếm số (ví dụ: `AtomicInteger`).

## Context Propagation: Vấn đề "Mất dấu" User

- **Vấn đề:** `ThreadLocal` (thường chứa SecurityContext/User) không tự động truyền từ Main Thread sang Async Thread, dẫn đến việc luồng mới nhận giá trị null context.
- **Giải pháp:** Sử dụng `DelegatingSecurityContextAsyncTaskExecutor` để bọc (wrap) task lại, đảm bảo context được lan truyền.

## Transaction & Async: Cặp đôi xung khắc

- **Đặc tính:** Transaction luôn gắn liền với Thread (Thread-bound). Mỗi luồng sẽ giữ một Database Connection riêng biệt.
- **Rủi ro 1:** Nếu Async Thread bị lỗi ➔ Main Thread KHÔNG rollback.
- **Rủi ro 2:** Nếu Main Thread rollback ➔ Async Thread vẫn thực hiện Commit bình thường.

## Scheduling: Đừng để tắc nghẽn

- **Mặc định:** Default Single-Thread Scheduler của Spring chỉ có duy nhất 1 luồng để chạy các task theo lịch.
- **Rủi ro:** Nếu một task bị treo (chạy quá lâu), nó sẽ chặn toàn bộ hệ thống schedule, làm các task sau đó bị trễ (Late!).
- **Fix:** Cấu hình `ThreadPoolTaskScheduler` với `poolSize > 1`.

## Tương lai: Virtual Threads (Java 21)

- **Platform Threads:** Nặng nề (Heavy), ánh xạ tỉ lệ 1:1 với OS Threads.
- **Virtual Threads:** Nhẹ (Lightweight), ánh xạ tỉ lệ M:N.
- **Lợi ích:** Cho phép scale lên hàng triệu luồng, cực kỳ lý tưởng cho các tác vụ I/O (Database, Network).
- **Config:** Để kích hoạt trong Spring Boot, dùng: `spring.threads.virtual.enabled = true`

## Structured Concurrency

- **Nguyên lý:** Coi nhiều thread chạy đồng thời như một đơn vị công việc (Scope) duy nhất.
- **Lợi ích:** Tự động hủy (Cancellation) các task liên quan và dọn dẹp khi có bất kỳ một lỗi nào xảy ra. Loại bỏ hoàn toàn tình trạng "luồng mồ côi".

## Scoped Values: Thay thế ThreadLocal

- **ThreadLocal:** Dễ thay đổi (Mutable) và tốn kém tài nguyên (Expensive), giống như một mớ dây chằng chịt.
- **ScopedValue:** Cung cấp luồng dữ liệu một chiều thẳng tắp, an toàn.
  - Chia sẻ dữ liệu an toàn (Immutable).
  - Mang lại hiệu năng cao khi kết hợp với hàng triệu Virtual Threads.

## Best Practices Checklist

- **Luôn định nghĩa Executor:** Tuyệt đối tránh sử dụng mặc định `SimpleAsyncTaskExecutor`.
- **Hiểu Queue Capacity:** Nhớ rõ luồng xử lý: Core ➔ Queue ➔ Max.
- **Xử lý Exception:** Luôn dùng `AsyncUncaughtExceptionHandler`.
- **Context:** Chú ý lan truyền Security & Transaction đúng cách giữa các luồng.
- **Return Values:** Sử dụng `CompletableFuture` để trả về kết quả.
- **Graceful Shutdown:** Cấu hình đợi các task hoàn thành trước khi tắt ứng dụng.

## Lời kết: "Magic" cần sự thấu hiểu

> "Spring che giấu sự phức tạp, nhưng đừng để nó che giấu sự hiểu biết của bạn."

Review lại cấu hình Thread Pool của bạn ngay hôm nay.
