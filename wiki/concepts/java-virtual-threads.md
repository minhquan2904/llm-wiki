---
title: "Java Virtual Threads và Structured Concurrency"
source: "compiled"
date_added: 2026-04-24
tags: [concept, java, concurrency, virtual-threads]
aliases: [virtual-threads, loom, structured-concurrency]
status: draft
related:
  - "[[java-concurrency-fundamentals]]"
  - "[[spring-async-execution]]"
summary: "Cách mạng kiến trúc đa luồng từ Project Loom, tách rời luồng Java khỏi luồng Hệ điều hành thông qua Virtual Threads và định hình lại mô hình xử lý đa luồng hiện đại."
---

# Java Virtual Threads và Structured Concurrency

Ra mắt chính thức trên nền tảng Java 21 từ Project Loom, Luồng Ảo (Virtual Threads) đánh dấu một sự dịch chuyển hệ hình (Paradigm Shift) lớn lao trong lịch sử hệ sinh thái JVM. Nó thay đổi hoàn toàn cách thức máy ảo Java tương tác với hệ điều hành, mang đến năng lực vận hành hàng triệu luồng song song với chi phí tài nguyên cực thấp.

## Vấn Đề Luồng Nền Tảng (Platform Threads)

Trong kiến trúc truyền thống, mỗi đối tượng `Thread` của Java (Platform Thread) được ánh xạ trực tiếp tỷ lệ 1:1 với một luồng của Hệ điều hành (OS Thread). Luồng OS là một nguồn tài nguyên xa xỉ: nó đòi hỏi tới 1MB bộ nhớ ảo cấp phát trước, cần đến 1-2 mili-giây để khởi tạo, và hao tốn chi phí khi luân chuyển ngữ cảnh (Context Switching). Hạn chế tài nguyên phần cứng khiến mô hình này nhanh chóng chạm trần, tạo ra áp lực đè nặng lên kiến trúc xử lý của các hệ thống I/O bound.

## Cơ Chế Hoạt Động của Luồng Ảo

Luồng Ảo phá vỡ sự ràng buộc 1:1 bằng cách giới thiệu cấu trúc phân lớp M:N. Hàng triệu Luồng Ảo của Java (M) được máy ảo JVM tự động quản lý và ánh xạ động lên một nhóm nhỏ các Carrier Threads của hệ điều hành (N) chạy dưới tầng đáy.

Thuật toán ma thuật của cơ chế này là "Chuyển giao Quyền lực" (Unmounting). Khi một Luồng Ảo thực hiện lời gọi ngắt nghẽn I/O (I/O Blocking) như đọc file, gọi database, luồng ảo đó lập tức lưu trạng thái call stack vào bộ nhớ Heap và nhường Carrier Thread cho luồng ảo khác hoạt động. Khi dữ liệu I/O đã sẵn sàng, JVM khôi phục stack (Mounting) và tiếp tục thực thi.

## Sự Diệt Vong Của Thread Pools 

Lịch sử kỹ thuật sinh ra Thread Pool để tái sử dụng nguồn tài nguyên Luồng OS đắt đỏ. Khi Virtual Threads xuất hiện với chi phí khởi tạo tiệm cận con số không, khái niệm Bể luồng mất đi ý nghĩa thiết kế. Thay vì chia sẻ luồng từ một Pool tĩnh giới hạn, mỗi tác vụ giờ đây được tự do sở hữu một Luồng Ảo dùng một lần (Fire-and-forget). Trên Spring Boot 3.2+, việc kích hoạt tính năng này chỉ cần cờ cấu hình `spring.threads.virtual.enabled=true`.

Tuy vậy, kiến trúc Luồng Ảo bộc lộ hạn chế chí mạng (Thread Pinning) khi thao tác với Native Code hoặc đi qua khối lệnh độc quyền `synchronized` của Java cổ điển, buộc JVM phải trói chặt Luồng Ảo lên Carrier Thread và làm mất khả năng giải phóng. Lời giải kiến trúc đòi hỏi dịch chuyển toàn bộ mã `synchronized` sang `ReentrantLock`.

## Structured Concurrency

Bổ trợ cho sức mạnh của Luồng Ảo là nguyên lý Structured Concurrency (Đồng thời Có cấu trúc). Nhằm chống lại rủi ro sinh ra các luồng con mồ côi (Orphan Threads) thất lạc trong không gian hệ thống, kiến trúc này gói gọn vòng đời phân nhánh đa luồng vào trong các khối cấu trúc rõ ràng. Các tác vụ con sinh ra từ tác vụ cha sẽ bị buộc phải kết thúc vòng đời hoặc hủy bỏ (Cancel) khi khối lệnh cha sụp đổ, cung cấp khả năng kiểm soát chặt chẽ luồng nghiệp vụ.

## Nguồn Tham Khảo
- `raw/papers/multithreading-concurrency-trong-spring-boot-từ-cơ-bản-đến-virtual-threads.md`
