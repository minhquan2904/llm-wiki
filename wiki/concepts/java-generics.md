---
title: "Java Generics và Hệ Thống Kiểu"
source: "compiled"
date_added: 2026-04-24
tags: [concept, java, generics, types]
aliases: [java-generics, type-erasure, pecs, wildcards]
status: draft
related:
  - "[[typescript-generics]]"
  - "[[jackson-databind]]"
summary: "Phân tích cơ chế Generics trong ngôn ngữ Java, nguyên lý Type Erasure, và quy tắc sử dụng Wildcards (PECS) để đảm bảo tính an toàn bộ nhớ tại Compile-time."
---

# Java Generics và Hệ Thống Kiểu

Hệ thống Generics trong Java được ra mắt từ phiên bản Java 5 như một giải pháp nhằm chuyển dịch rủi ro kiểm tra kiểu dữ liệu (Type-checking) từ thời điểm chạy (Runtime) về thời điểm biên dịch (Compile-time). Thiết kế này nhằm triệt tiêu các lỗi `ClassCastException` tiềm ẩn do việc ép kiểu thủ công từ cấu trúc Raw Types cổ điển.

## Nguyên Lý Bất Biến (Invariance)

Khác với khái niệm mảng (Arrays) vốn có bản chất hiệp biến (Covariant), Generics trong Java tuân theo quy tắc Bất biến (Invariant). Điều này có nghĩa là mặc dù `Integer` là lớp con của `Number`, một danh sách `List<Integer>` hoàn toàn không phải là con của `List<Number>`. Nguyên lý thiết kế này được áp dụng nghiêm ngặt để đảm bảo an toàn bộ nhớ (Memory Safety), ngăn chặn việc chèn sai kiểu dữ liệu vào một tập hợp thông qua tham chiếu đa hình.

## Sự Xóa Kiểu (Type Erasure)

Một trong những hạn chế lớn nhất mang tính kiến trúc của Java Generics là Type Erasure (Xóa kiểu). Để duy trì khả năng tương thích ngược (Backward Compatibility) với các phiên bản Java tiền nhiệm, trình biên dịch (Compiler) sẽ tự động xóa mọi tham số Generic (ví dụ: `<T>`) thành `Object` hoặc giới hạn cận trên (Upper Bounds) trong Bytecode.

Bởi vì thông tin kiểu dữ liệu bị mất hoàn toàn tại thời điểm chạy, các hệ thống phân tích dữ liệu động (như việc Deserialize JSON thông qua [[jackson-databind]]) thường đối mặt với khó khăn khi nhận diện cấu trúc. Trình biên dịch Java tự động sinh ra các "Bridge Methods" nhằm xử lý và ép kiểu ngầm định để bù đắp sự mất mát thông tin này.

## Quy Tắc Wildcards và PECS

Để vượt qua giới hạn cứng nhắc của sự Bất biến, hệ thống kiểu Java cung cấp khái niệm Wildcards (`?`) nhằm tăng tính linh hoạt:

- **Unbounded Wildcard (`<?>`):** Chấp nhận mọi kiểu, nhưng hạn chế quyền ghi (không thể thêm dữ liệu mới ngoại trừ `null`).
- **Upper Bound (`<? extends T>`):** Chỉ thị tập hợp có chứa kiểu `T` hoặc con của `T`. An toàn để đọc (Read-only).
- **Lower Bound (`<? super T>`):** Chỉ thị tập hợp chứa kiểu `T` hoặc cha của `T`. An toàn để ghi (Write-only).

Quy tắc nền tảng của việc sử dụng Wildcards được giới kỹ sư tóm tắt thành **PECS** (Producer Extends, Consumer Super):
- Sử dụng `extends` khi tham số đóng vai trò là nhà cung cấp dữ liệu (Producer) - cần lấy giá trị ra ngoài.
- Sử dụng `super` khi tham số đóng vai trò là nhà tiêu thụ dữ liệu (Consumer) - cần nạp dữ liệu vào trong.

## Nguồn Tham Khảo
- `raw/papers/java-generics-bi-kip-tran-phai.md`
- `raw/papers/jackson.md`
