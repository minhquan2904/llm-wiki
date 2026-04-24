---
title: "Từ Nguyên tắc đến Kiến trúc: Dependency Injection là Trụ cột Chính"
source: "compiled"
date_added: 2026-04-24
tags: [concept, software-design, oop, dependency-injection, solid, dotnet]
status: draft
related:
  - "[[spring-ioc-di]]"
  - "[[composition-vs-inheritance]]"
  - "[[generic-repository-pattern]]"
summary: "Phân tích nguyên lý SOLID, cơ chế Đảo ngược Điều khiển (IoC) và Tiêm Phụ thuộc (DI) như những trụ cột kiến trúc giúp giảm thiểu phụ thuộc cứng trong phát triển phần mềm."
---

## Khát vọng Phần mềm và Nguyên tắc SOLID
Phát triển phần mềm linh hoạt (Flexible) và dễ bảo trì (Maintainable) luôn là mục tiêu cốt lõi của kỹ thuật phần mềm. Để đạt được điều này, hệ thống cần đáp ứng các tiêu chuẩn cơ bản như DRY (Không lặp lại code), Dễ đọc, Có thể kiểm thử độc lập, và KISS/YAGNI (Giữ hệ thống đơn giản và không phát triển những gì chưa cần thiết).

Bộ nguyên tắc thiết kế **SOLID** đóng vai trò là nền móng lý thuyết để hướng dẫn cách kiến trúc mã nguồn hướng đối tượng:
- **S - Single Responsibility Principle (SRP):** Khuyến khích chia nhỏ lớp, mỗi lớp chỉ có một lý do duy nhất để thay đổi.
- **O - Open/Closed Principle (OCP):** Ưu tiên mở rộng thông qua tính trừu tượng hóa thay vì sửa đổi trực tiếp mã nguồn.
- **L - Liskov Substitution Principle (LSP):** Đảm bảo sự toàn vẹn của mô hình kế thừa.
- **I - Interface Segregation Principle (ISP):** Chia nhỏ các interface thay vì một giao diện quá phức tạp.
- **D - Dependency Inversion Principle (DIP):** Nguyên tắc Đảo ngược Phụ thuộc quy định rằng các module cấp cao và cấp thấp đều nên phụ thuộc vào các lớp trừu tượng (abstraction), không nên phụ thuộc trực tiếp vào nhau. 

Nguyên tắc DIP chính là tiền đề lý thuyết dẫn đến nhu cầu về **Dependency Injection (DI)**. SOLID chỉ ra sự cần thiết, còn DI cung cấp cơ chế để kết nối.

## Sự Phụ thuộc Cứng (Tight Coupling)
Một hệ thống truyền thống thường đối mặt với vấn đề "Phụ thuộc cứng" khi các lớp tự khởi tạo các đối tượng phụ thuộc (dependency) của riêng chúng thông qua từ khóa `new`.

Hệ lụy của phụ thuộc cứng là việc thay đổi một dịch vụ sẽ kéo theo sự sửa đổi hàng loạt ở các lớp sử dụng dịch vụ đó. Hơn nữa, nó ngăn cản quá trình cô lập mã nguồn để thực hiện Unit Test vì lập trình viên không thể thay thế các dịch vụ này bằng các đối tượng giả lập (Mock).

## Inversion of Control (IoC) và Dependency Injection
Để phá vỡ sự phụ thuộc cứng, kiến trúc hiện đại áp dụng nguyên lý **Inversion of Control (IoC)** (Đảo ngược điều khiển). Quyền kiểm soát việc khởi tạo đối tượng được chuyển từ chính đối tượng đó sang một thực thể bên ngoài, thường được gọi là Container.

**Dependency Injection (DI)** là mẫu thiết kế (design pattern) hiện thực hóa nguyên lý IoC. Thay vì đối tượng tự khởi tạo phụ thuộc, Container sẽ "tiêm" (inject) những phụ thuộc đã được khởi tạo sẵn vào đối tượng, thường thông qua hàm tạo (Constructor Injection).

Cơ chế này mang lại khả năng linh hoạt cao, cho phép hoán đổi các phiên bản triển khai (implementation) mà không làm ảnh hưởng đến mã nguồn sử dụng dịch vụ, đồng thời cho phép tiêm các đối tượng Mock trong môi trường kiểm thử.

## Quản lý Vòng đời Dịch vụ (Service Lifetimes)
Trong hầu hết các DI Container hiện đại (như của .NET hoặc Spring), vòng đời của đối tượng được quản lý chặt chẽ theo ba mức độ phân bổ:
- **Singleton:** Một phiên bản duy nhất được khởi tạo và chia sẻ trong suốt vòng đời của ứng dụng. Phù hợp cho các dịch vụ không trạng thái (stateless) và cấu hình.
- **Scoped:** Khởi tạo một phiên bản duy nhất cho mỗi phạm vi cụ thể (thường là một HTTP Request). Rất quan trọng đối với các thành phần cần duy trì trạng thái giao dịch như kết nối cơ sở dữ liệu (ví dụ: `DbContext`).
- **Transient:** Một phiên bản hoàn toàn mới được tạo ra mỗi khi có yêu cầu tiêm phụ thuộc. Thường dùng cho các dịch vụ nhẹ và không lưu trạng thái.

## Ứng dụng trong Các Kiến trúc Hiện đại
DI không chỉ là một công cụ đơn lẻ mà là chất kết dính hạt nhân cho các mẫu kiến trúc cấp cao:
- **Repository Pattern:** DI tách biệt tầng logic nghiệp vụ khỏi tầng truy cập dữ liệu bằng cách tiêm các đối tượng thực thi `IRepository` vào logic, giữ cho miền (domain) hoàn toàn không biết về cơ sở dữ liệu.
- **Clean Architecture:** DI là cơ chế bắt buộc để thực thi quy tắc "Mọi thứ hướng vào trong". Lớp hạ tầng (Infrastructure) cung cấp thực thi, và DI Container sẽ cung cấp chúng cho lớp ứng dụng (Application) mà không phá vỡ quy tắc vòng tròn phụ thuộc.
- **Vertical Slice Architecture:** Phân tách hệ thống theo từng tính năng độc lập. DI tiêm các phụ thuộc cốt lõi như kết nối dữ liệu vào từng lát cắt (slice), cho phép mỗi lát cắt vận hành độc lập.

Sự tương hỗ giữa SOLID và DI tạo ra một vòng lặp tích cực: Áp dụng SOLID đòi hỏi sự trừu tượng hóa, trừu tượng hóa dẫn đến nhu cầu kết nối lỏng lẻo (Decoupling), và DI đáp ứng nhu cầu này. Ngược lại, việc có sẵn DI Container khuyến khích lập trình viên tuân thủ SOLID một cách tự nhiên hơn.
