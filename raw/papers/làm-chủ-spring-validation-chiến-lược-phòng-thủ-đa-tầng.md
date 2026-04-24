---
title: "Làm Chủ Spring Validation: Chiến Lược Phòng Thủ Đa Tầng 🛡️"
source: "D:\9. Learn\12. llm wiki\raw\papers\validation.md"
date_added: 2026-04-24
tags: [papers]
status: draft
summary: ""
---

# Làm Chủ Spring Validation: Chiến Lược Phòng Thủ Đa Tầng 🛡️

Từ Jakarta Bean Validation cơ bản đến Kiến trúc Hệ thống Bền vững

## 1. Tư Duy Phòng Thủ Đa Tầng (Layered Defense)

"Một hệ thống mạnh mẽ bắt đầu từ việc định nghĩa dữ liệu đúng đắn." Đừng để dữ liệu bẩn (dirty data) lọt sâu vào hệ thống.
- **Tầng 1 (Client JSON ➡️ Controller Layer):** Đón lõng và lọc dữ liệu ngay tại cửa bằng `@Valid` / `@Validated`.
- **Tầng 2 (Filtered Data ➡️ Service Layer):** Chỉ xử lý Business Logic trên dữ liệu đã được làm sạch (Validated Data).
- **Tầng 3 (Persistence ➡️ Database):** Lưu trữ an toàn.

## 2. Hệ Sinh Thái & Các Thành Phần Cốt Lõi ⚙️

Validation trong Spring không phải là một khối liền khối mà là sự kết hợp của:
- **Specification (Bản tả kỹ thuật):** Jakarta Bean Validation 3.0 (JSR-380) - Chỉ định nghĩa API, Annotations.
- **Implementation (Triển khai):** Hibernate Validator - Bộ code thực thi (Reference Implementation) mà Spring sử dụng.
- **Integration (Tích hợp):** Spring Boot - Tự động cấu hình (Auto-configuration) thông qua `LocalValidatorFactoryBean`.

**Cài đặt:**
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

## 3. Các Annotation Cơ Bản: Sự Khác Biệt Quan Trọng 🔍

Bộ 3 hay gây nhầm lẫn nhất đối với String:

| Annotation | Checks for Null? | Checks for Empty String ""? | Checks for Whitespace " "? |
| --- | --- | --- | --- |
| `@NotNull` | ✅ Yes | ❌ No | ❌ No |
| `@NotEmpty` | ✅ Yes | ✅ Yes | ❌ No |
| `@NotBlank` | ✅ Yes | ✅ Yes | ✅ Yes |

**Các ràng buộc khác (Constraints):**
- **Numeric:** `@Min`, `@Max`, `@Positive`, `@Negative`
- **Time:** `@Past`, `@Future`, `@PastOrPresent`
- **Pattern:** `@Pattern(regexp="...")` (Regex)

💡 **Đặc tính:** Validation mang tính Declarative (Khai báo) - Bạn định nghĩa ràng buộc ngay trên Domain Model hoặc DTO, không cần viết code if/else dài dòng.

## 4. Trận Chiến Kinh Điển: @Valid vs @Validated ⚔️

| `@Valid` (Standard JSR-303) | `@Validated` (Spring Framework AOP) |
| --- | --- |
| Tiêu chuẩn của Java. | Hàng chính chủ của Spring. |
| Đánh dấu field trong DTO. | Dùng ở cấp độ Class (`@RestController`, `@Service`). |
| Dùng để validate object lồng nhau (Nested properties). | Dùng cho Method Parameters & Path Variables. |
| KHÔNG hỗ trợ Groups. | CÓ hỗ trợ Validation Groups. |

👉 **Quy tắc:** Dùng `@Valid` bên trong DTO. Dùng `@Validated` ở Controller khi cần dùng tính năng Groups hoặc validate trực tiếp tham số (params/path variables).

## 5. Validation Tại Tầng Controller 🚪

### 5.1. Request Body
Khi dùng `@Valid` kết hợp `@RequestBody`, nếu data sai, Spring sẽ ném ra lỗi `MethodArgumentNotValidException` (HTTP 400) trước khi chạy vào code của method.

```java
@PostMapping("/users")
public ResponseEntity<User> create(@Valid @RequestBody UserDto user) {
    // Code này MẶC ĐỊNH AN TOÀN, không chạy nếu validation thất bại
    return service.save(user);
}
```

### 5.2. Path Variables & Query Parameters
Để validate các tham số rời rạc, bạn BẮT BUỘC phải đặt `@Validated` ở trên đầu class.

```java
@RestController
@Validated // <-- 1. Kích hoạt AOP Proxy cho Class
public class UserController {

    @GetMapping("/{id}")
    public User get(@PathVariable @Min(1) Long id) { // <-- 2. Constraint trực tiếp
        // ...
    }

}
```
**Lưu ý:** Trường hợp này sẽ ném ra `ConstraintViolationException` (Khác với lỗi ở Request Body).

## 6. Các Pattern Validation Nâng Cao 🔥

### Pattern 1: Nested Validation (Graph Traversal)
Khi DTO của bạn chứa một Object khác, bạn phải thêm `@Valid` vào thuộc tính đó để báo Spring duyệt sâu xuống dưới.

```java
public class UserDto {
    @NotBlank private String name;

    @Valid // <-- CHÌA KHÓA kích hoạt duyệt cây (Graph Traversal)
    @NotNull
    private AddressDto address;
}
```

### Pattern 2: Validation Groups (Xử Lý Ngữ Cảnh)
Ví dụ: Khi Tạo mới (Create), id phải NULL. Khi Cập nhật (Update), id bắt buộc phải CÓ.

```java
// 1. Gán Group vào DTO
public class UserDto {
    @Null(groups = OnCreate.class)
    @NotNull(groups = OnUpdate.class)
    private Long id;
}

// 2. Kích hoạt đúng Group tại Controller
@PostMapping
public void create(@Validated(OnCreate.class) @RequestBody UserDto dto) { ... }

@PutMapping
public void update(@Validated(OnUpdate.class) @RequestBody UserDto dto) { ... }
```

### Pattern 3: Cross-Parameter Validation (Validation Chéo)
Dùng khi cần so sánh 2 field với nhau (VD: startDate phải nhỏ hơn endDate).
- **Cách 1:** Viết Custom Class Validator.
- **Cách 2:** Dùng `@ScriptAssert(lang="javascript", script="_this.startDate < _this.endDate")` đặt trên đầu class DTO.

### Pattern 4: Tạo Custom Validator (Gắn nghiệp vụ đặc thù)
Tạo annotation riêng (VD: `@StrongPassword`) và class implement `ConstraintValidator`.

## 7. Xử Lý Lỗi Toàn Cục (Global Exception Handling) 🚑

Đừng trả về stack trace cho client. Hãy dùng `@ControllerAdvice` để gom lỗi `MethodArgumentNotValidException` và `ConstraintViolationException` lại, sau đó format thành một cục JSON chuẩn chỉ:

```json
{
    "status": 400,
    "error": "Validation Error",
    "details": {
        "email": "Invalid format",
        "age": "Must be 18+"
    }
}
```

## 8. 📐 Engineering Editorial: Patterns & Anti-Patterns

### Chiến Lược DTO: Tách Biệt hay Tái Sử Dụng?
- **Tái sử dụng (Dùng Groups):** DRY (Don't Repeat Yourself) nhưng rườm rà, dễ sai sót, vi phạm SRP (Single Responsibility Principle).
- **Tách biệt (VD: CreateUserRequest, UpdateUserRequest):** Contract API cực kỳ rõ ràng, bảo mật cao. Đánh đổi lại là phải map dữ liệu nhiều hơn.
**Khuyến nghị của Architect:** Ưu tiên Tách biệt DTO. Sự rõ ràng (Clarity) quan trọng hơn số lượng file.

### Dùng Java Records cho DTO 🚀
Records sinh ra là để làm Data Transfer Object. Nó minh bạch, bất biến (Immutable), thread-safe và validation ngay tại Constructor.

```java
public record UserRequest(
    @NotBlank String name,
    @Email String email
) {}
```

### Check-list Thực Tiễn:
- ✅ **NÊN Fail Fast:** Báo lỗi ngay lập tức ở rìa hệ thống.
- ✅ **NÊN Edge Validation:** Validate ngay tại Controller (Biên).
- ❌ **TRÁNH Validation Everywhere:** Không rải validation thừa thãi lặp lại ở cả Controller, Service, Repository.
- ❌ **TRÁNH Business Logic in Validator:** Không gọi Database trong Custom Validator (Tránh Coupling, giữ Validator thuần túy và nhanh).