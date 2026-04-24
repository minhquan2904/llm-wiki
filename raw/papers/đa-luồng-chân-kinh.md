---
title: "ĐA LUỒNG CHÂN KINH 📜"
source: "D:\9. Learn\12. llm wiki\raw\papers\concurrency.md"
date_added: 2026-04-24
tags: [papers]
status: draft
summary: ""
---

# ĐA LUỒNG CHÂN KINH 📜
Bí Pháp Quản Lý Tài Nguyên & Định Tâm - Nhập môn Java Concurrency cho tân thủ

## 1. Giang Hồ Hiểm Ác: Quần Hùng Tranh Bá ⚔️

**Bối Cảnh:** Java Heap chính là chốn giang hồ, nơi các Threads (băng đảng) tranh giành tài nguyên (Shared Objects).

**Nguy Cơ (The Danger):**
- **Tẩu hỏa nhập ma (Race Condition):** Dữ liệu bị sai lệch, ghi đè lẫn nhau khi không có cơ chế đồng bộ (Synchronization).
- **Bất định (Non-deterministic):** Lỗi "tâm linh", lúc bị lúc không, thay đổi theo thời điểm chạy, cực kỳ khó debug và tái hiện.

> "Trong thế giới đa luồng, kẻ nào kiểm soát được trạng thái (State), kẻ đó xưng bá."

## 2. Vũ Khí Khí Giới: Từ Phế Tích đến Thần Binh 🛡️

### Phế Tích Thời Xưa
- **HashMap (Nhanh nhưng mỏng manh):** Tốc độ cao nhưng phòng thủ kém (Not Thread-Safe). Bị nhiều luồng tấn công cùng lúc sẽ dẫn đến hỏng dữ liệu.
- **Hashtable (Chậm chạp):** Phòng thủ tuyệt đối (Synchronized) nhưng sử dụng Khóa Toàn Bộ Cổng Thành (Global Lock). Một Thread đang đọc/ghi là tất cả các Thread khác phải đứng ngoài chờ.

### Thần Binh Xuất Thế: ConcurrentHashMap 🗡️
**Tuyệt Kỹ: Phân Thân Chi Thuật (Bucket Locking / CAS)**
**Cơ chế:**
- Không khóa toàn bộ Map. Chỉ khóa phân vùng nhỏ (bucket) đang bị thay đổi.
- Tối ưu bằng CAS (Compare-And-Swap) trên Java 8+.

**Kết quả:** High Concurrency - Đọc không bị chặn, Ghi chỉ chặn cục bộ.

## 3. Tuyệt Kỹ Thao Tác Map (Chiêu Thức) 🥋

### Chiêu Thức 1: Tiên Hạ Thủ Vi Cường (`putIfAbsent`) - Cương Công
```java
map.putIfAbsent(key, new HeavyObject());
```
- **Hành động:** Chế tạo vũ khí (`new HeavyObject()`) TRƯỚC khi kiểm tra xem key đã có chưa.
- **Điểm yếu:** Lãng phí nội công (CPU/Memory). Nếu key đã có, cái object nặng nề kia sẽ bị vứt đi. Chỉ nên dùng cho value siêu nhẹ (như String, Integer).

### Chiêu Thức 2: Dĩ Nhu Chế Cương (`computeIfAbsent`) - Thái Cực
```java
map.computeIfAbsent(key, k -> new HeavyObject());
```
- **Hành động:** Sử dụng Lambda Function. Chỉ thực sự khởi tạo đối tượng KHI VÀ CHỈ KHI key chưa tồn tại.
- **Hiệu quả:** Tiết kiệm nội công tối đa, bảo đảm tính nguyên tử (Atomicity).

## 4. Cấm Kỵ Giang Hồ: Tuyệt Đối Không Null ☠️

**Quy Tắc Bang Hội ConcurrentHashMap:** Key KHÔNG được Null, Value KHÔNG được Null!

**Lý do:** Trong môi trường đa luồng, Null gây ra sự mơ hồ (Ambiguity). Nếu `map.get(key)` trả về `null`, ta không thể biết là Key không tồn tại hay Value thực sự là Null. Sự mơ hồ này tạo ra `NullPointerException` đoạt mạng.

**Khắc phục:** Sử dụng giá trị mặc định, thẻ trống, hoặc `Optional`.

## 5. Kim Cang Bất Hoại: Tâm Bất Biến (Immutable Objects) 🧘‍♂️

**Immutable Object:** Một đối tượng KHÔNG THỂ thay đổi trạng thái sau khi được sinh ra. (VD: String, Integer, Records).
- Trạng thái bất biến => Thread-Safe Tuyệt Đối.
- Không cần khóa đồng bộ (No Synchronization). Hàng vạn mũi tên (Read Threads) bắn vào cũng không hề hấn.

### Khẩu Quyết Luyện Công (4 Bước Tạo Immutable Object)
1. **Class final:** Ngăn chặn phản đồ (Không cho kế thừa / subclassing).
2. **Fields private final:** Phong bế huyệt đạo (Chỉ gán 1 lần, không bao giờ đổi).
3. **Không Setters:** Ngăn kẻ gian thao túng từ bên ngoài.
4. **Constructor Initialization:** Truyền toàn bộ công lực ngay lúc khai sinh.

### Ảnh Phân Thân Chi Thuật (Defensive Copies) 🥷
Nếu Object của bạn giữ một danh sách (List), kẻ địch lấy được List đó có thể lén thêm bớt phần tử (vì List mặc định là mutable).

Khắc phục bằng Sao chép phòng thủ:
```java
public class Ninja {
    private final List<Weapon> weapons;

    public Ninja(List<Weapon> inputWeapons) {
        // Constructor: Nhận vào bản sao
        this.weapons = List.copyOf(inputWeapons);
    }

    public List<Weapon> getWeapons() {
        // Getter: Trả về bản sao chỉ đọc
        return Collections.unmodifiableList(this.weapons);
    }
}
```

## 6. Tuyệt Kỹ Thất Truyền: Java Records 🏆

Thay vì phải tự viết hàng chục dòng code Boilerplate (như thời Java cũ) để có một Immutable Class, hãy dùng Java 14+ Records:
```java
public record User(String name, int age) {}
```
- Tự động sinh `private final` fields.
- Không sinh setters.
- Tích hợp sẵn `equals()`, `hashCode()`, `toString()`.
- Phòng thủ tối đa với công sức tối thiểu.

## 7. Spring Phái: Độc Cô Cầu Bại & Cạm Bẫy Stateful 🏯

**Quy Tắc Spring:** Mặc định các Beans là Singleton (Chỉ có 1 bản thể duy nhất).
**Thực tế:** 1 Instance này phải phục vụ hàng ngàn HTTP Requests đồng thời.

### ⚠️ Tẩu Hỏa Nhập Ma: Cạm Bẫy Stateful
Việc lưu trữ trạng thái người dùng vào biến toàn cục (Field) của Singleton Bean là tự sát.

```java
@Service
public class StatefulTrapService {
    // DANGER ZONE !!!
    private User currentUser;

    public void processUser(User user) {
        this.currentUser = user; // Thread B có thể ghi đè Thread A ngay tại đây!
        // ...
    }
}
```
**Giải Pháp:** Spring Bean phải hoàn toàn Stateless (Không mang vác hành lý). Hãy sử dụng Biến cục bộ (Local Variables) bên trong Method. Biến cục bộ nằm trên Stack Memory, hoàn toàn tách biệt cho từng Thread.

## 8. Trúc Cơ: Truyền Công (Injection) 🏛️

Xây dựng nền móng kiến trúc vững chắc.
- **Field Injection** (`@Autowired` trên biến): Xây nhà trên cát. Rất dễ dính `NullPointerException`, khó viết Unit Test, và biến không thể là `final`.
- **Constructor Injection:** Xây nhà trên đá. Đảm bảo Bean được khởi tạo với đầy đủ các Dependency, và cho phép set các field này là `final` (Immutable). Luôn ưu tiên cách này.

---

## 🚀 Hạ Sơn Hành Hiệp (Cheat Sheet Tổng Kết)
- **Vũ Khí:** Dùng `ConcurrentHashMap` và tuyệt chiêu `computeIfAbsent` để xử lý collection đa luồng.
- **Hộ Thể:** Luôn ưu tiên thiết kế các Object là Immutable (dùng `final` hoặc Java `Record`s).
- **Tâm Pháp:** Spring Bean mặc định là Singleton -> Bắt buộc phải **Stateless**. Không lưu data vào field của class.
- **Căn Cơ:** Bỏ `@Autowired` trên Field, hãy sử dụng **Constructor Injection**.

> Nắm vững những yếu quyết này, code an toàn - ngủ ngon giấc!