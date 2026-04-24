---
title: "Composition vs Inheritance"
source: "compiled"
date_added: 2026-04-24
tags: [comparison, oop, software-design]
aliases: [Composition over Inheritance, Kế thừa vs Composition]
status: canonical
related:
  - "[[spring-ioc-di]]"
summary: "Phân tích sự khác biệt giữa thiết kế theo mô hình Kế thừa (Inheritance) cứng nhắc và Lắp ráp (Composition) linh hoạt trong Lập trình Hướng Đối Tượng."
---

# Composition vs Inheritance

> "Thay vì nói A LÀ một loại của B (is-a), chúng ta sẽ nói A CÓ một B (has-a)."

## Bối Cảnh

Trong thiết kế phần mềm Hướng đối tượng (OOP), Kế thừa (Inheritance) từng được xem là công cụ vàng để tái sử dụng mã. Tuy nhiên, việc lạm dụng các cây phân cấp kế thừa sâu thường dẫn đến vấn đề "Chuối, Khỉ và Rừng rậm" (chỉ muốn một quả chuối nhưng nhận được cả con khỉ và khu rừng). Hệ thống trở nên "giòn" (brittle) và liên kết chặt chẽ (tightly coupled). 

Ngày nay, nguyên tắc **Composition over Inheritance** (Ưu tiên Lắp ráp hơn Kế thừa) kết hợp với Tiêm Phụ thuộc (Dependency Injection) được ưu tiên để xây dựng các hệ thống linh hoạt, dễ bảo trì và mở rộng.

## Bảng So Sánh

| Tiêu chí | Inheritance (Kế thừa) | Composition (Lắp ráp) |
| :--- | :--- | :--- |
| **Bản chất** | Mối quan hệ **"is-a"** (LÀ một). | Mối quan hệ **"has-a"** (CÓ một). |
| **Kiến trúc** | Phân cấp từ trên xuống (top-down), giống như những con búp bê Nga lồng vào nhau. | Phẳng và độc lập, giống như lắp ráp các khối LEGO. |
| **Độ kết dính** | Liên kết chặt chẽ (Tightly coupled) với lớp cha. Thay đổi ở lớp cha ảnh hưởng đến toàn bộ lớp con. | Liên kết lỏng lẻo (Loosely coupled). Các thành phần độc lập, dễ dàng thay thế. |
| **Khả năng mở rộng**| Khó khăn và rủi ro. Thường dẫn đến việc phải triển khai các phương thức không cần thiết (forced implementation) hoặc phá vỡ tính đa hình khi dùng từ khóa `new`. | Dễ dàng bằng cách tạo ra các thành phần mới và "cắm" (inject) chúng vào mà không phá vỡ cấu trúc hiện tại. |
| **Khả năng kiểm thử**| Khó cô lập logic để Unit Test do phụ thuộc ngầm định vào lớp cơ sở. | Khả năng kiểm thử cao. Dễ dàng sử dụng Mock/Fake cho các Interface được inject. |

## Phân Tích

### Cạm bẫy của Inheritance
Một ví dụ kinh điển là khi thiết kế hệ thống nhân sự. Nếu `FullTimeEmployee`, `PartTimeEmployee`, và `Contractor` đều kế thừa từ lớp `Employee`, rắc rối nảy sinh khi lớp cha có phương thức `CalculateBonus()`. Một `Contractor` (nhân viên hợp đồng) có thể không nhận thưởng, dẫn đến việc phải ghi đè (override) một phương thức vô nghĩa, vi phạm nguyên tắc thiết kế. Tệ hơn, nếu một người vừa là nhân viên toàn thời gian vừa là nhà thầu, cấu trúc phân cấp sẽ hoàn toàn sụp đổ. 

### Sức mạnh của Composition và Dependency Injection
Thay vì ép các lớp vào một cấu trúc phân cấp tĩnh, Composition chia nhỏ chức năng thành các "chiến lược" (Strategies) hoặc thành phần độc lập (Ví dụ: `ICompensationCalculator`, `IBenefitsPackage`, `IWorkSchedule`). Đối tượng chính chỉ chứa (has-a) các thành phần này. 

Khi kết hợp với cơ chế [[spring-ioc-di|Dependency Injection (DI)]], các phụ thuộc (dependencies) được "tiêm" vào đối tượng qua Constructor (thường thông qua Interface thay vì Implementation cụ thể). Điều này giúp đối tượng không cần biết chi tiết cách các thành phần hoạt động, đảm bảo tính liên kết lỏng lẻo và dễ dàng hoán đổi logic tại runtime hoặc trong quá trình Unit Testing.

## Kết Luận

Ưu tiên Composition không đồng nghĩa với việc loại bỏ hoàn toàn Inheritance. Nguyên tắc vàng để ra quyết định:
- **Sử dụng Inheritance khi:** Có một mối quan hệ "is-a" thực sự rõ ràng, thuần túy, và bạn muốn chia sẻ một cơ sở mã nguồn chung vững chắc hoặc khi mở rộng một lớp của framework.
- **Sử dụng Composition khi:** Có mối quan hệ "has-a", và hệ thống đòi hỏi sự linh hoạt tối đa để kết hợp các hành vi từ nhiều nguồn độc lập.
