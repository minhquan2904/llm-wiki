---
title: "Từ Nguyên tắc đến Kiến trúc: Dependency Injection là Trụ cột Chính"
source: "d:\\9. Learn\\12. llm wiki\\temp\\di_oop.md"
date_added: 2026-04-24
tags: [article, software-design, oop, dependency-injection, solid, dotnet]
aliases: [Dependency Injection trong OOP]
status: draft
summary: "Trình bày về nguyên tắc SOLID, vai trò của Dependency Injection (DI) trong việc giải quyết phụ thuộc cứng, và ứng dụng của DI trong các kiến trúc hiện đại như Clean Architecture và Vertical Slices."
---

# Từ Nguyên tắc đến Kiến trúc: Dependency Injection là Trụ cột Chính

Làm chủ nghệ thuật xây dựng phần mềm linh hoạt, dễ bảo trì và có khả năng mở rộng.

## 1. Khởi đầu: Khát vọng về Code Tốt hơn
Mọi nhà phát triển đều hướng tới việc xây dựng phần mềm có các đặc tính:
- Dễ bảo trì (Maintainable): Dễ dàng sửa lỗi và nâng cấp.
- Linh hoạt (Flexible): Thích ứng với các yêu cầu thay đổi.

**Các Nguyên tắc Nền tảng Chỉ đường:**
- **DRY (Don't Repeat Yourself):** Tránh trùng lặp code trong ứng dụng. Nguyên tắc này nhấn mạnh việc thay đổi code ở một nơi sẽ tự động cập nhật mọi nơi khác.
- **Dễ đọc (Readable):** Logic rõ ràng, dễ hiểu.
- **Có thể kiểm thử (Testable):** Các thành phần có thể được xác minh một cách độc lập.
- **KISS (Keep It Simple, Stupid):** Ưu tiên các giải pháp đơn giản hơn các giải pháp phức tạp vì chúng dễ hiểu, sử dụng và bảo trì hơn.
- **YAGNI (You Ain't Gonna Need It):** Chỉ nên triển khai chức năng sau khi bạn thực sự cần đến nó, tránh sự phức tạp không cần thiết và 'gold plating'.

Đây là những lý tưởng, nhưng làm thế nào để thực hiện chúng một cách có hệ thống?

## 2. Nền móng Lý thuyết: Các Nguyên tắc SOLID
SOLID là bộ 5 nguyên tắc thiết kế hướng đối tượng giúp chúng ta đạt được khát vọng về code tốt.

**S - Single Responsibility Principle (SRP)**
"Một lớp chỉ nên có một lý do duy nhất để thay đổi."
- Hệ quả: Thúc đẩy việc tạo ra các lớp nhỏ, chuyên biệt. (Khi chúng ta chia nhỏ các trách nhiệm, làm thế nào để kết nối chúng lại một cách linh hoạt?)

**O - Open/Closed Principle (OCP)**
"Các thực thể phần mềm nên mở cho việc mở rộng, nhưng đóng cho việc sửa đổi."
- Hệ quả: Khuyến khích sử dụng abstraction (interface, lớp trừu tượng) để thêm chức năng mới mà không cần sửa code cũ.

**L - Liskov Substitution Principle (LSP)**
"Các đối tượng của lớp con có thể thay thế cho các đối tượng của lớp cha mà không làm thay đổi tính đúng đắn của chương trình."
- Hệ quả: Đảm bảo tính nhất quán trong hệ thống phân cấp kế thừa.

**I - Interface Segregation Principle (ISP)**
"Client không nên bị buộc phải phụ thuộc vào các interface mà chúng không sử dụng."
- Hệ quả: Dẫn đến các interface nhỏ, tập trung và chuyên biệt hơn thay vì một interface quá phức tạp.

**D - Dependency Inversion Principle (DIP)**
"Các module cấp cao không nên phụ thuộc vào các module cấp thấp. Cả hai nên phụ thuộc vào abstraction."
- Hệ quả: Đây chính là nguyên tắc cốt lõi dẫn thẳng đến nhu cầu về Dependency Injection. Nó đảo ngược luồng phụ thuộc truyền thống.

💡 **Tóm lại:** SOLID chỉ ra con đường, nhưng chúng ta cần một công cụ để hiện thực hóa nó. DIP là nguyên tắc, DI là cơ chế.

## 3. Thách thức Cốt lõi: Sự Phụ thuộc Cứng (Tight Coupling)
Đây là "kẻ thù" của phần mềm linh hoạt.

**Vấn đề:**
- Các lớp tự tạo ra các dependency của chính chúng.
- Thay đổi một dependency (ví dụ: MessageWriter) đòi hỏi phải sửa đổi lớp sử dụng nó (Worker).
- Khó khăn trong việc kiểm thử (unit test) vì không thể thay thế (mock) các dependency.

**Ví dụ "Trước kia" (Phụ thuộc cứng):**
```csharp
public class Worker : BackgroundService
{
    // Phụ thuộc cứng! Lớp này tạo và phụ thuộc trực tiếp vào MessageWriter.
    private readonly MessageWriter _messageWriter = new();

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        _messageWriter.Write($"Worker running at: {DateTimeOffset.Now}");
        // ...
    }
}
```

## 4. Giải pháp: Inversion of Control & Dependency Injection
Chúng ta "đảo ngược quyền kiểm soát" việc tạo ra các dependency.

**Inversion of Control (IoC)**
Là một nguyên tắc thiết kế. Thay vì một đối tượng tự tạo dependency, quyền kiểm soát này được chuyển cho một thực thể bên ngoài (framework, container).

**Dependency Injection (DI)**
Là một mẫu thiết kế và là cách phổ biến nhất để hiện thực hóa IoC. Các dependency được "tiêm" vào đối tượng từ bên ngoài.

**Cơ chế:**
- `[DI Container] -> tiêm vào -> [Worker Class]`
- `[DI Container] -> tạo ra -> [MessageWriter Class]`
(DI là cơ chế cho phép chúng ta tuân thủ Nguyên tắc Đảo ngược Phụ thuộc - DIP)

## 5. DI hoạt động trong .NET như thế nào?
Một quy trình 3 bước đơn giản được tích hợp sẵn trong framework:

**Bước 1: Định nghĩa Abstraction (Interface)**
```csharp
public interface IMessageWriter
{
    void Write(string message);
}
```

**Bước 2: Đăng ký Dịch vụ (Service) trong Container**
Trong Program.cs. Ánh xạ interface tới một lớp cụ thể.
```csharp
builder.Services.AddSingleton<IMessageWriter, MessageWriter>();
```

**Bước 3: Tiêm (Inject) Dịch vụ vào Constructor**
Framework sẽ tự động cung cấp một instance khi Worker được tạo.
```csharp
public sealed class Worker(IMessageWriter messageWriter) : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        messageWriter.Write($"Worker running at: {DateTimeOffset.Now}");
        // ...
    }
}
```

## 6. Vòng đời Dịch vụ (Service Lifetimes)
Kiểm soát cách các dependency được tạo và chia sẻ. Lựa chọn đúng vòng đời là rất quan trọng:

- **Singleton (AddSingleton)**: Một instance duy nhất cho toàn bộ vòng đời ứng dụng.
  - Sử dụng cho: Các dịch vụ stateless, cấu hình, logging.
- **Scoped (AddScoped)**: Một instance duy nhất cho mỗi scope (ví dụ: một HTTP request trong ASP.NET Core).
  - Sử dụng cho: DbContext của EF Core, các dịch vụ cần duy trì trạng thái trong một request.
- **Transient (AddTransient)**: Một instance mới được tạo mỗi khi được yêu cầu.
  - Sử dụng cho: Các dịch vụ lightweight, stateless.

## 7. Sức mạnh của DI: Linh hoạt và Dễ kiểm thử
Nhìn lại ví dụ "sau khi" áp dụng DI:

- **Linh hoạt:** Dễ dàng thay đổi implementation mà không cần sửa Worker. Chỉ cần thay đổi một dòng trong Program.cs:
  ```csharp
  builder.Services.AddSingleton<IMessageWriter, LoggingMessageWriter>();
  ```
- **Dễ kiểm thử:** Có thể "tiêm" một MockMessageWriter trong unit test để kiểm tra logic của Worker một cách độc lập mà không cần đến console thật.

## 8. Xây dựng trên Nền tảng DI: Repository Pattern
DI là yếu tố cho phép các mẫu thiết kế mạnh mẽ hoạt động.

**Repository Pattern là gì?**
Một lớp trừu tượng (abstraction) hoạt động như một trung gian giữa tầng logic nghiệp vụ (business logic) và tầng truy cập dữ liệu (data access).
- Mục đích: Tách biệt logic nghiệp vụ khỏi chi tiết triển khai của cơ sở dữ liệu (EF Core, Dapper, SQL, v.v.), tuân thủ nguyên tắc SRP và DIP.

**DI đóng vai trò gì?**
Lớp Controller không tạo ra ProductRepository. Thay vào đó, nó phụ thuộc vào interface IProductRepository và DI Container sẽ "tiêm" vào một instance cụ thể.
```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private readonly IProductRepository _repo;

    // IProductRepository được tiêm vào đây!
    public ProductsController(IProductRepository repo)
    {
        _repo = repo;
    }
    // ...
}
```

## 9. Sự tiến hóa Kiến trúc: Từ Layers đến Slices
Các kiến trúc hiện đại đều phụ thuộc vào DI để quản lý sự phức tạp.

**N-Layered Architecture (Kinh điển)**
- Tổ chức: Theo các lớp kỹ thuật (Presentation -> Business Logic -> Data Access).
- Vấn đề: Các tính năng thường bị phân mảnh qua nhiều lớp, khó theo dõi.

**Clean Architecture (Hiện đại)**
- Tổ chức: Xoay quanh Domain và Use Cases.
- Quy tắc phụ thuộc: Mọi thứ hướng vào trong. Infrastructure phụ thuộc vào Application, Application phụ thuộc vào Domain.
- Vai trò của DI: Là cơ chế bắt buộc để thực thi quy tắc phụ thuộc này.

**Vertical Slice Architecture (Tiên tiến)**
- Tổ chức: Theo tính năng (feature) hoặc use case. Mỗi 'lát cắt' chứa mọi thứ cần thiết cho một tính năng (UI -> Logic -> Data).
- Vai trò của DI: Cung cấp các dependency chung (như DbContext) cho mỗi slice, giúp giảm sự couple giữa các tính năng.

## 10. Clean/Vertical Slice + DI = Công thức Chiến thắng
Sự kết hợp này tạo ra các hệ thống có tính module cao, dễ bảo trì và mở rộng.

- **Trong Clean Architecture:** DI Container quản lý việc cung cấp các implementation từ lớp Infrastructure (ví dụ: ProductRepository dùng EF Core) cho lớp Application (ví dụ: CreateProductCommandHandler) mà Application không cần biết về chi tiết của EF Core.
- **Trong Vertical Slices:** Mỗi slice là một đơn vị độc lập. DI tiêm các dependency cần thiết (ví dụ: DbContext, ILogger) vào từng slice, giúp chúng hoạt động mà không cần phụ thuộc lẫn nhau.

(DI là chất keo kết dính các lớp/slice một cách lỏng lẻo - loosely coupled).

## 11. Vòng lặp Tích cực của Thiết kế Tốt
DI không phải là điểm cuối, mà là trung tâm của một vòng lặp cải tiến liên tục:
1. Các Nguyên tắc (SOLID): Chỉ ra sự cần thiết của việc tách biệt và trừu tượng hóa.
2. Dẫn đến Decoupling: Các thành phần đã tách biệt giao tiếp với nhau như thế nào?
3. Dependency Injection: Cung cấp cơ chế để kết nối các thành phần một cách lỏng lẻo.
4. Cho phép Kiến trúc & Patterns Hiện đại: Repository, Clean Architecture, Vertical Slices trở nên khả thi.
5. Củng cố Nguyên tắc: Một kiến trúc tốt giúp việc áp dụng SOLID trở nên tự nhiên hơn.
(... và vòng lặp tiếp tục)

## 12. Các Điểm chính cần Ghi nhớ
- DI là một tư duy thiết kế, không chỉ là một kỹ thuật. Nó là cách thực thi Nguyên tắc Đảo ngược Phụ thuộc (DIP).
- DI là nền tảng để áp dụng hiệu quả các nguyên tắc SOLID. Nó giúp kết nối các thành phần có trách nhiệm duy nhất (SRP) và cho phép mở rộng mà không cần sửa đổi (OCP).
- Các kiến trúc hiện đại (Clean, Vertical Slice) không thể tồn tại nếu thiếu DI. DI là công cụ thiết yếu để quản lý sự phụ thuộc và duy trì sự tách biệt.
- Hãy tận dụng DI Container có sẵn trong .NET. Nó mạnh mẽ, dễ sử dụng và được tích hợp sâu vào hệ sinh thái.

---
**Liên hệ & Hỏi Đáp**
- Email: email@example.com
- LinkedIn: linkedin.com/in/yourprofile
- GitHub: github.com/yourusername
*(Quét mã QR trong slide gốc để truy cập kho code ví dụ và tài liệu tham khảo).*
