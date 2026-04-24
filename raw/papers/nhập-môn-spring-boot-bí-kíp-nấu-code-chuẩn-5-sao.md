---
title: "Nhập môn Spring Boot: Bí kíp 'Nấu Code' Chuẩn 5 Sao 👨‍🍳"
date_added: 2026-04-24
tags: [papers, java, spring-boot, basics, architecture]
status: draft
summary: ""
---

# Nhập môn Spring Boot: Bí kíp 'Nấu Code' Chuẩn 5 Sao 👨‍🍳

Học 20% kiến thức cốt lõi để giải quyết 80% công việc (Phong cách lười biếng nhưng hiệu quả). Dành cho người mới bắt đầu - The 'Omakase' Edition.

## 1. Bạn muốn nấu ăn hay muốn đi rèn chảo? 🔨

- **Vấn đề:** Code thuần (Plain Java) bắt bạn phải tự khởi tạo và quản lý từng 'nguyên liệu' (object) bằng từ khóa `new`.

```java
// The Nightmare (Cơn ác mộng)
Connection conn = new Connection("url", "user", "pass");
UserDao dao = new UserDao(conn);
EmailService email = new EmailService();

UserService service = new UserService(dao, email); // Aaaaaaah!
```

- **Hậu quả:** Code rối như mì Spaghetti, khó bảo trì, và bạn kiệt sức trước khi kịp nấu món chính.
- **Giải pháp:** Cần một người quản lý để lo việc vặt này.

## 2. Gặp gỡ Quản lý Bếp: IoC Container (ApplicationContext) 📋

- **Inversion of Control (IoC):** Thay vì bạn gọi nhân viên, nhân viên (Container) sẽ gọi bạn. Bạn không tự tạo object, Container sẽ tạo và đưa cho bạn.
- **Bean:** Tên gọi sang chảnh của các object (nguyên liệu/dụng cụ) được Spring quản lý.
- **Quy tắc 80/20:** Quên `BeanFactory` đi. Hãy nhớ `ApplicationContext` là sếp tổng ở đây.

**Công thức:**
Nguyên liệu (POJOs) + Công thức (Metadata) = Hệ thống đã chuẩn bị (Ready for Use)

## 3. Dependency Injection (DI): “Đừng đi chợ, hãy order!” 🍔

### Cách 1: Constructor Injection (Khuyên dùng 🌟)

```java
public Chef(Knife knife) {
    this.knife = knife;
}
```

**Tại sao:** Bắt buộc có nguyên liệu mới được nấu (No Null), dễ test, bất biến (Immutable). (The Spring team generally advocates constructor injection).

### Cách 2: Field Injection (@Autowired)

```java
@Autowired
private Knife knife;
```

**Tại sao tránh:** Nhanh nhưng 'dầu mỡ'. Khó test, dễ bị `NullPointerException`.

## 4. Dán nhãn cho nguyên liệu (Stereotypes) 🏷️

Để Spring biết class của bạn làm nhiệm vụ gì, hãy dán nhãn cho nó:

- `@Component`: Nhãn chung chung. “Đây là một Bean”.
- `@Service`: Business Logic (Khu vực chế biến).
- `@Repository`: Database (Kho hàng) - Hỗ trợ tự động xử lý lỗi SQL.
- `@Controller` / `@RestController`: Web (Phục vụ bàn).

**Pro Tip:** Đừng dùng `@Component` cho mọi thứ giống như gọi tất cả nguyên liệu là “Đồ ăn”. Hãy cụ thể hơn!

## 5. Khi không thể "dán nhãn" (@Configuration & @Bean) 📖

- **Vấn đề:** Bạn không thể viết `@Component` lên code của thư viện bên thứ 3 (ví dụ: Gson, DataSource).
- **Giải pháp:** Tạo một class `@Configuration` (Sách công thức) và dùng method `@Bean`.

```java
@Configuration
public class KitchenConfig {

    @Bean
    public Sauce specialSauce() {
        return new ThirdPartySauce(); // Spring sẽ quản lý cái này
    }

}
```

## 6. Spring Boot: Đầu bếp biết đọc suy nghĩ (Auto-configuration) 🎩

- **Vấn đề:** Cấu hình thủ công rất mệt mỏi.
- **Giải pháp:** Spring Boot nhìn vào những gì bạn có trong bếp (classpath) và tự động thiết lập.
  - Thấy bạn mua H2 Database? -> Boot tự tạo DataSource.
  - Thấy bạn có Spring Web? -> Boot tự bật Tomcat server.

```java
@SpringBootApplication
public class MyKitchenApp {
    public static void main(String[] args) {
        SpringApplication.run(MyKitchenApp.class, args);
    }
}
```

**Key Takeaway:** "Opinionated Defaults" - Boot đưa ra ý kiến chủ quan để bạn bắt đầu nhanh hơn.

## 7. Thuật toán của Bếp trưởng (@Conditional) 🧠

Auto-configuration hoạt động dựa trên các điều kiện (Conditions) nằm trong file `spring.factories`.

- `@ConditionalOnClass`: Tìm thấy class X không? (Nếu có -> Tạo Bean Y).
- `@ConditionalOnMissingBean`: Đầu bếp có tự làm sốt không? (Nếu không -> Dùng sốt đóng chai mặc định của Boot).

## 8. Combo Nguyên Liệu (Starters) 📦

Đừng quản lý từng file `.jar` riêng lẻ. Hãy dùng Starters.

- `spring-boot-starter-web`: Bao gồm mọi thứ để mở nhà hàng (Tomcat, Spring MVC, Jackson...).
- `spring-boot-starter-data-jpa`: Bao gồm Hibernate, JDBC, Transaction Manager.

**Lợi ích:** Tạm biệt 'Jar Hell' (Xung đột phiên bản).

## 9. Nêm nếm gia vị (Configuration Properties) 🧂

### Cách 1: @Value

```java
@Value("${app.name}")
private String appName;
```

Tốt cho gia vị đơn lẻ. Khó quản lý khi có quá nhiều.

### Cách 2: @ConfigurationProperties (Quy tắc 80/20)

Gom nhóm các config (vd: `database.url`, `database.user`) vào một Java Object (POJO).
**Lợi ích:** Type-safe, có autocomplete.

## 10. Chiêu cuối: Phục vụ khách khó tính (Strategy Pattern) 🥗🥩

- **Tình huống:** Bạn có `VeganService`, `MeatService`, `KetoService` cùng implement interface `DietService`.
- **Spring Magic:** Thay vì viết if/else, hãy inject một List hoặc Map.

```java
@Autowired
private List<DietService> allDiets;
// Spring tự động tìm tất cả các Bean implement DietService và bỏ vào List này!
```

**Kết quả:** Code mở rộng dễ dàng (Open/Closed Principle). Thêm chế độ ăn mới không cần sửa code cũ.

## 11. Phân loại thùng hàng (Generics Magic) 📦

Java thường bị "Type Erasure" (mất thông tin Generic lúc chạy), nhưng Spring thông minh hơn.
Nếu bạn có `Repository<User>` và `Repository<Product>`:

```java
@Autowired
Repository<User> userRepository;
```

Khi `@Autowired Repository<User>`, Spring sẽ không đưa nhầm `Repository<Product>`.
**Tại sao:** Spring check generic signature trong Bean Definition (Hỗ trợ từ Spring 3.2).

## 12. Sơ chế và Dọn dẹp (Lifecycle) 🧽

- `@PostConstruct`: Chạy sau khi Dependency Inject xong. Dùng để tẩm ướp (khởi tạo logic).
- `@PreDestroy`: Chạy trước khi ứng dụng tắt. Dùng để dọn dẹp tài nguyên.

**Quy tắc:** Đừng để Constructor làm việc quá sức. Hãy để `@PostConstruct` làm việc đó.

## 13. Kiểm định chất lượng (Testing) 🧪

Đừng phục vụ “gà sống” ra Production!

- `@SpringBootTest`: Khởi động toàn bộ “nhà bếp” (Full context). Tốt nhưng chạy chậm.
- `@MockBean`: Dùng đồ giả (Mock) cho những thứ bạn không muốn test (ví dụ: Database thật).
- `@WebMvcTest`: Chỉ test phần "Phục vụ bàn” (Controller), không đụng vào Bếp (Service/Repo). Nhanh gọn.

## 🚀 Thực đơn 80/20 (Tổng kết - Cheat Sheet)

- **IoC/DI:** Để Spring lo việc tạo object. Luôn ưu tiên dùng Constructor Injection.
- **Stereotypes:** Dùng `@Service`, `@Controller`, `@Repository` đúng chỗ để phân tầng (Layering) rõ ràng.
- **Config:** Dùng `@Configuration` + `@Bean` cho hàng ngoại nhập (3rd party libraries).
- **Auto-config:** Hiểu `@Conditional` để biết tại sao "phép màu" lại xảy ra.
- **Cool Trick:** Dùng `List<Interface>` để xử lý Strategy Pattern cực kỳ thanh lịch.

Code ít, hiệu quả nhiều. Go build something cool!
