---
title: "Từ Rừng Rậm đến LEGO: Nghệ thuật thiết kế phần mềm"
source: "d:\\9. Learn\\12. llm wiki\\temp\\oop_lego.md"
date_added: 2026-04-24
tags: [article, software-design, oop, composition, inheritance, di]
aliases: [Composition over Inheritance, oop-lego]
status: draft
summary: "Phân tích vấn đề của kế thừa (Inheritance) trong OOP và đề xuất sử dụng Composition kết hợp với Dependency Injection để thiết kế hệ thống phần mềm linh hoạt, dễ bảo trì."
---

# Từ Rừng Rậm đến LEGO: Nghệ thuật thiết kế phần mềm

## Vấn đề "Chuối, Khỉ và Rừng rậm"

> “Vấn đề với các ngôn ngữ hướng đối tượng là chúng luôn mang theo một môi trường ngầm định. Bạn chỉ muốn một quả chuối, nhưng thứ bạn nhận được lại là một con khỉ đột cầm quả chuối và cả khu rừng rậm.”

Câu nói nổi tiếng này gói gọn một thách thức kinh điển trong thiết kế phần mềm: sự phụ thuộc ngoài ý muốn và độ phức tạp leo thang.

## Từ ẩn dụ đến thực tế: Khi hệ thống trở nên cứng nhắc và khó bảo trì

### Vấn đề
Các hệ thống phần mềm thường trở nên "giòn” (brittle) và liên kết chặt chẽ (tightly coupled). Một thay đổi nhỏ ở một nơi có thể gây ra lỗi ở những nơi không ngờ tới.

### Nguyên nhân gốc rễ
Lạm dụng Kế thừa (Inheritance). Chúng ta thường bị cuốn hút bởi sự thanh lịch của các cây phân cấp kế thừa sâu, nhưng chúng lại là nguồn gốc của sự phức tạp.

## Giới thiệu phép ẩn dụ so sánh

*   🪆 **Kế thừa (Inheritance)**: Giống như những con búp bê Nga lồng vào nhau. Cứng nhắc, phân cấp và khó thay đổi một lớp bên trong mà không ảnh hưởng đến các lớp bên ngoài.
*   🧱 **Composition**: Giống như những khối LEGO. Các thành phần độc lập, có thể tái sử dụng và kết hợp linh hoạt để tạo ra bất cứ thứ gì bạn cần.

## Phân tích Case Study: Hệ thống quản lý nhân viên

Hãy xem xét một cách tiếp cận phổ biến khi xây dựng hệ thống quản lý nhân viên. Ban đầu, việc sử dụng kế thừa có vẻ rất tự nhiên và hợp lý.

```csharp
// Base class
public class Employee
{
    public string Name { get; set; }
    public decimal Salary { get; set; }

    public virtual decimal CalculateBonus()
    {
        return Salary * 0.10m;
    }
}

// Lớp con 1
public class FullTimeEmployee : Employee { /* ... */ }

// Lớp con 2
public class PartTimeEmployee : Employee { /* ... */ }

// Lớp con 3
public class Contractor : Employee
{
    // VẤN ĐỀ 1: Một Contractor có thực sự LÀ một Employee không?
    // Họ kế thừa thuộc tính Salary dù có thể được trả lương theo giờ.

    // VẤN ĐỀ 2: Việc triển khai bắt buộc (forced implementation) ngay cả khi không có ý nghĩa.
    public override decimal CalculateBonus()
    {
        // Contractors don't get bonuses, but we're forced to override
        return 0;
    }
}
```

Câu hỏi đặt ra: Nếu có một nhân viên vừa là FullTime vừa là Contractor thì sao? Cấu trúc phân cấp này sẽ sụp đổ.

## Phá vỡ tính đa hình: Cạm bẫy của override và new

Sự khác biệt giữa `override` và `new` không chỉ là về cú pháp. Nó ảnh hưởng trực tiếp đến tính đa hình - một trong những trụ cột của OOP. Từ khóa `new` chỉ đơn thuần che giấu (hides) phương thức của lớp cơ sở, không thực sự ghi đè nó.

**Sử dụng override (Hành vi đúng)**
```csharp
public class Base
{
    public virtual void Foo() { Console.WriteLine("Base => Foo"); }
}

public class Overrider : Base
{
    public override void Foo() { Console.WriteLine("Overrider => Foo"); }
}

// Cách sử dụng
Base base1 = new Overrider();
base1.Foo();
// Kết quả (Output): 'Overrider => Foo'
// (Đúng như mong đợi, phương thức của lớp con được gọi)
```

**Sử dụng new (Phá vỡ đa hình)**
```csharp
public class Hider : Base
{
    public new void Foo() { Console.WriteLine("Hider => Foo"); }
}

// Cách sử dụng
Base base2 = new Hider();
base2.Foo();
// Kết quả (Output): 'Base => Foo'
// (Không như mong đợi, phương thức của lớp cơ sở được gọi)
```

Khi sử dụng `new`, polymorphism sẽ không hoạt động. Trình biên dịch sẽ không tra cứu phương thức được kế thừa. Điều này có thể che giấu lỗi và gây ra các bug khó tìm.

## Sự thay đổi chiến lược: Ưu tiên Composition hơn Inheritance

“Thay vì nói A LÀ một loại của B (is-a), chúng ta sẽ nói A CÓ một B (has-a)."

*   **Linh hoạt (Flexibility)**: Kết hợp các thành phần độc lập để tạo ra các đối tượng phức tạp.
*   **Dễ bảo trì (Maintainability)**: Thay đổi logic trong một thành phần không ảnh hưởng đến các thành phần khác.
*   **Dễ mở rộng (Extensibility)**: Thêm chức năng mới bằng cách tạo ra các thành phần mới, không cần thay đổi cấu trúc kế thừa hiện có.

### Thiết kế lại hệ thống nhân viên bằng Composition

Chúng ta chia nhỏ các chức năng thành các "chiến lược" (strategies) độc lập và đóng gói chúng sau các interface.

```csharp
// Các "chiến lược" có thể hoán đổi (Interfaces)
public interface ICompensationCalculator { /* ... */ }
public interface IBenefitsPackage { /* ... */ }
public interface IWorkSchedule { /* ... */ }

// Lớp Employee mới sử dụng composition (has-a)
public class Employee
{
    public string Name { get; set; }
    public decimal BasePay { get; set; }

    private readonly ICompensationCalculator _compensation;
    private readonly IBenefitsPackage _benefits;
    private readonly IWorkSchedule _schedule;

    // Dependency Injection qua constructor
    public Employee(
        ICompensationCalculator compensation,
        IBenefitsPackage benefits,
        IWorkSchedule schedule)
    {
        _compensation = compensation;
        _benefits = benefits;
        _schedule = schedule;
    }

    public decimal CalculateBonus() => _compensation.CalculateBonus(BasePay);
}
```

### Lắp ráp các "khối LEGO": Sức mạnh của sự linh hoạt

Với thiết kế mới, việc tạo ra bất kỳ loại nhân viên nào chỉ đơn giản là việc “cắm” các thành phần phù hợp vào. Không cần tạo lớp mới, không cần thay đổi cây kế thừa.

```csharp
// Nhân viên toàn thời gian
var fullTime = new Employee(
    "Alice", 75000m,
    new SalariedCompensation(0.15m), // 15% bonus
    new StandardBenefits(),
    new FullTimeSchedule()
);

// Nhân viên hợp đồng
var contractor = new Employee(
    "Carol", 50000m,
    new NoBonus(), // No bonus
    new NoBenefits(),
    new ContractSchedule()
);

// Một trường hợp đặc biệt: Toàn thời gian nhưng lương theo giờ
var hybrid = new Employee(
    "David", 60000m,
    new HourlyCompensation(), // Fixed bonus
    new StandardBenefits(),
    new FullTimeSchedule()
);
```

## Nền tảng của Composition: Encapsulation và Properties

Để các thành phần (components) hoạt động tốt, chúng cần phải đóng gói (encapsulate) trạng thái và logic bên trong của chúng một cách hiệu quả. Trong C#, Properties là cách chuẩn mực để thực hiện encapsulation, thay thế cho các phương thức getter/setter.

| Public Field (Nên tránh) ❌ | Auto-Property (Nên dùng) ✅ |
| :--- | :--- |
| `public string Title;` | `public string Title { get; set; }` |
| **Nhược điểm**: Việc thay đổi từ field sang property là một 'breaking change', đòi hỏi phải biên dịch lại toàn bộ code phụ thuộc. Bạn không thể databind, và reflection hoạt động khác đi. | **Ưu điểm**: Trông gọn gàng, nhưng quan trọng hơn, nó cho phép bạn thêm logic (validation, logging, lazy-loading) vào `get` hoặc `set` sau này mà không phá vỡ API. Đây là nền tảng cho việc xây dựng các thành phần có thể bảo trì. |

## Gắn kết các thành phần: Vai trò của Dependency Injection (DI)

Dependency Injection (DI) là một kỹ thuật để đạt được Inversion of Control (IoC). Thay vì một đối tượng tự tạo ra các dependency của nó, các dependency này được “tiêm” (inject) vào từ bên ngoài. Nó là cơ chế giúp "cắm" các khối LEGO lại với nhau.

**Trước (Không có DI - Liên kết chặt chẽ):**
```csharp
public class Worker : BackgroundService
{
    // Dependency được hard-code
    private readonly MessageWriter _writer = new MessageWriter();
    // ...
}
```
*Vấn đề: Để thay thế MessageWriter, bạn phải sửa đổi lớp Worker. Rất khó để unit test.*

**Sau (Có DI - Liên kết lỏng lẻo):**
```csharp
// Phụ thuộc vào interface, không phải implementation cụ thể
public sealed class Worker : BackgroundService
{
    private readonly IMessageWriter _messageWriter;

    // Dependency được "tiêm" vào qua constructor
    public Worker(IMessageWriter messageWriter)
    {
        _messageWriter = messageWriter;
    }
}
```
*Lợi ích: Worker không biết về MessageWriter, chỉ biết về IMessageWriter. Dễ dàng thay đổi implementation và dễ dàng unit test.*

## Interfaces: Hợp đồng cho sự linh hoạt và khả năng kiểm thử

Interfaces là chất keo kết dính thiết kế dựa trên composition. Chúng định nghĩa "cái gì" một thành phần có thể làm, chứ không phải "làm như thế nào".

**Lợi ích cho Unit Testing:**
Khi một lớp phụ thuộc vào interface, chúng ta có thể dễ dàng tạo ra một "mock" hoặc "fake" implementation của interface đó để cô lập lớp đang được kiểm thử khỏi các dependency thực (như database, network).

```csharp
// Lớp cần được test phụ thuộc vào IUserDataService
public class BonusCalculator
{
    private readonly IUserDataService _dataService;
    public BonusCalculator(IUserDataService dataService)
    {
        _dataService = dataService;
    }
    // ... logic tính toán bonus
}

// Trong Unit Test, chúng ta tạo một "fake" service
public class FakeUserDataService : IUserDataService
{
    public User GetById(int id) => new User { IsDeserved = true };
}

// Giờ đây, chúng ta có thể test BonusCalculator mà không cần kết nối database
[TestMethod]
public void TestBonusCalculation()
{
    // Arrange
    var fakeService = new FakeUserDataService();
    var calculator = new BonusCalculator(fakeService);

    // Act & Assert...
}
```

## Kết quả: Từ "Rừng rậm" đến một hệ thống có cấu trúc, dễ bảo trì

| Cách tiếp cận cũ (Kế thừa) | Cách tiếp cận mới (Composition + DI) |
| :--- | :--- |
| ❌ Liên kết chặt chẽ, cấu trúc cứng nhắc. | ✅ Liên kết lỏng lẻo, các thành phần độc lập. |
| ❌ Thay đổi khó khăn và rủi ro. | ✅ Dễ dàng mở rộng và thay đổi. |
| ❌ Khó kiểm thử (unit test). | ✅ Khả năng kiểm thử cao. |
| ❌ Bạn muốn quả chuối, nhưng nhận cả khu rừng. | ✅ Bạn chỉ cần yêu cầu quả chuối, và DI container sẽ đưa nó cho bạn. |

## Lựa chọn công cụ phù hợp cho từng công việc

Ưu tiên Composition không có nghĩa là loại bỏ hoàn toàn Inheritance. Kế thừa vẫn có giá trị khi tồn tại một mối quan hệ ‘is-a' thực sự và rõ ràng (ví dụ, `Dog` là một `Animal`) hoặc khi mở rộng các lớp framework.

**Quy tắc vàng (Rule of Thumb)**
*   **Sử dụng Inheritance khi**: Mối quan hệ là "is-a". Bạn muốn tái sử dụng mã nguồn và có một cơ sở chung vững chắc.
*   **Sử dụng Composition khi**: Mối quan hệ là "has-a". Bạn cần sự linh hoạt, muốn kết hợp các hành vi từ nhiều nguồn khác nhau.

*Hãy ngừng xây dựng những con búp bê Nga. Thay vào đó, hãy bắt đầu tư duy bằng những khối LEGO.*
