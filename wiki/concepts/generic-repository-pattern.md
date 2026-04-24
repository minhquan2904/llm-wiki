---
title: "Generic Repository Pattern"
source: "compiled"
date_added: 2026-04-24
tags: [concept, oop, design-pattern, csharp]
aliases: [Mẫu thiết kế Generic Repository, Hướng tiếp cận Hybrid Repository, Leaky Abstraction]
status: draft
related:
  - "[[composition-vs-inheritance]]"
  - "[[spring-ioc-di]]"
summary: "Mẫu thiết kế cung cấp lớp giao tiếp dữ liệu chung nhằm giảm thiểu mã lặp lại, đồng thời đi kèm các đánh đổi về rò rỉ trừu tượng và hiệu năng."
---

# Generic Repository Pattern

## Định Nghĩa
**Generic Repository Pattern** là một mẫu thiết kế (design pattern) trong kỹ thuật phần mềm, đặc biệt phổ biến trong hệ sinh thái C# và .NET. Mẫu thiết kế này trừu tượng hóa các thao tác cơ sở dữ liệu cơ bản (CRUD: Create, Read, Update, Delete) vào một lớp duy nhất, có thể tái sử dụng cho bất kỳ thực thể (entity) nào bằng cách sử dụng kiểu tham số hóa (Generics - `<T>`). Mục tiêu cốt lõi của Generic Repository là tuân thủ nguyên tắc DRY (Don't Repeat Yourself), loại bỏ mã lặp lại (boilerplate code) khi thao tác với cơ sở dữ liệu.

Mẫu thiết kế này cấu thành từ hai phần chính:
1. **Hợp đồng (Contract):** Một interface (ví dụ: `IRepository<T>`) định nghĩa các thao tác CRUD tiêu chuẩn.
2. **Triển khai (Implementation):** Một lớp cụ thể (ví dụ: `GenericRepository<T>`) cung cấp logic thực thi cho hợp đồng trên.

## Lợi Ích Kiến Trúc
Việc sử dụng Generic Repository mang lại những ưu điểm rõ rệt trong việc thiết kế phần mềm linh hoạt:
- **Giảm mã lặp lại:** Loại bỏ nhu cầu tạo ra hàng chục lớp repository chuyên biệt chỉ để thực hiện các thao tác CRUD cơ bản cho từng bảng trong cơ sở dữ liệu.
- **Dependency Injection (DI):** Hoạt động hoàn hảo với cơ chế Tiêm Phụ thuộc (DI). Tầng nghiệp vụ (Service Layer) chỉ phụ thuộc vào interface `IRepository<T>`, qua đó phá vỡ sự kết nối cứng (tight-coupling) với tầng cơ sở dữ liệu.
- **Tối ưu Unit Testing:** Cho phép lập trình viên dễ dàng giả lập (mock) repository để kiểm thử logic nghiệp vụ một cách cô lập, hoàn toàn không cần kết nối tới cơ sở dữ liệu thật.

## Những Sự Đánh Đổi (Trade-offs)
Mặc dù Generic Repository rất thanh lịch, nhưng việc áp dụng một cách cứng nhắc cho mọi tình huống có thể tạo ra các vấn đề nghiêm trọng về kiến trúc.

### Cạm bẫy "Trừu tượng bị rò rỉ" (Leaky Abstractions)
Lớp trừu tượng của Generic Repository hoạt động tốt cho CRUD cơ bản, nhưng khi miền nghiệp vụ đòi hỏi các truy vấn phức tạp (ví dụ: join nhiều bảng, lọc theo điều kiện nghiệp vụ đa tầng), sự trừu tượng bắt đầu "rò rỉ". Các lập trình viên thường phải đối mặt với ngõ cụt: hoặc là nhồi nhét các truy vấn rườm rà (như `Expression<Func<T, bool>>`) vào interface chung làm "ô nhiễm" nó, hoặc xuyên thủng Repository bằng cách gọi trực tiếp đối tượng Context cơ sở dữ liệu ở Tầng Service.

### Vấn Đề Hiệu Năng (Performance Overhead)
Triết lý Hướng đối tượng (OOP) đề cao sự trừu tượng hóa, trong khi Lập trình Hướng dữ liệu (Data-Oriented Design) ưu tiên cách thức CPU xử lý dữ liệu vật lý trên RAM. Trong các ứng dụng đòi hỏi hiệu năng khắt khe, việc bọc các thao tác dữ liệu qua nhiều lớp trừu tượng (như Repository) thay vì truy vấn trực tiếp có thể gây ra hiện tượng nghẽn cổ chai (overhead).

## Hướng Tiếp Cận Hybrid (Lai)
Để khắc phục những hạn chế trên, hướng tiếp cận **Hybrid (Lai ghép)** được đề xuất như một mô hình tiến hóa, cân bằng giữa khả năng tái sử dụng và tính chuyên biệt hóa:

1. **Sử dụng Generic Repository:** Áp dụng cho các thực thể chỉ có thao tác CRUD đơn giản, chẳng hạn như dữ liệu từ điển, master data (Tags, Settings, Categories). Ở đây, tính tiện lợi và tiết kiệm mã được ưu tiên.
2. **Sử dụng Specialized Repository:** Áp dụng cho các thực thể cốt lõi (Core Domain Entities) chứa logic nghiệp vụ phức tạp. Các repository chuyên biệt này (ví dụ: `ProductRepository`) sẽ không triển khai `IRepository<T>` chung mà sở hữu một interface riêng biệt. Chúng "tiêm" trực tiếp Context của cơ sở dữ liệu để toàn quyền tối ưu hóa các câu lệnh truy vấn nội bộ, giữ cho logic nghiệp vụ không bị rò rỉ ra bên ngoài.

Mô hình Hybrid tái khẳng định triết lý: thiết kế phần mềm là nghệ thuật sử dụng đúng công cụ cho đúng bài toán, ưu tiên Lắp ráp linh hoạt (Composition) hơn là Kế thừa cứng nhắc.

## Nguồn Tham Khảo
- [[raw/articles/generic-repository-pattern.md|Generic Repository: Những Sự Đánh Đổi và Hướng Tiếp Cận Hybrid]]
