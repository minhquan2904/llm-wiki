---
title: "Generic Thần Công - Bí Kíp Trấn Phái Java"
source: "temp/Generics_Bí_Kíp_Trấn_Phái_Java.pdf"
date_added: 2026-04-24
tags: [concept, java, generics]
aliases: [java-generics, generic-thần-công, type-erasure, pecs]
status: draft
related:
  - "[[java]]"
summary: "Tài liệu giải thích Java Generics theo phong cách võ hiệp, bao gồm Type Erasure, Bridge Methods, Wildcards (PECS) và tương lai Project Valhalla."
---

# Generic Thần Công - Bí Kíp Trấn Phái Java

Tài liệu hướng dẫn về Java Generics được trình bày theo phong cách bí kíp võ công, giúp lập trình viên hiểu rõ từ cơ bản đến nâng cao về hệ thống kiểu (Type System) trong Java.

## 1. Giang Hồ Hỗn Loạn (Pre-Java 5) - Thực trạng Raw Types

Trước kỷ nguyên Java 5, mọi vật phẩm đều là `Object`. Các cao thủ phải tự mình ép kiểu (Explicit Casting), dẫn đến nguy cơ "Tẩu hỏa nhập ma" - lỗi `ClassCastException`.

```java
List danhSach = new ArrayList(); // Raw Type
danhSach.add("Kiếm");
danhSach.add(100); // Kẻ địch trà trộn (Integer)

String vuKhi = (String) danhSach.get(1);
// BÙM! ClassCastException tại Runtime ("Tẩu hỏa nhập ma!")
```

## 2. Hộ Thế Chân Khí - An toàn tuyệt đối tại Compile-time

**Khẩu quyết:** Chuyển dịch rủi ro từ Runtime về Compile-time. Sư phụ (Compiler) sẽ chặn đứng mọi chiêu thức sai kiểu trước khi chúng được tung ra.

```java
List<String> khoVuKhi = new ArrayList<String>();
khoVuKhi.add("Đồ Long Đao");

// khoVuKhi.add(100); // LỖI: Sư phụ (Compiler) chặn ngay lập tức!

String vuKhi = khoVuKhi.get(0); // ✔️ Không cần ép kiểu
```

## 3. Phản Phác Quy Chân - Toán tử Diamond `<>` & Cạm bẫy Raw Types

- **Chiêu thức mới (Java 7+)**: Toán tử Diamond `<>` giúp mã nguồn gọn gàng nhờ khả năng tự suy diễn kiểu (Type Inference).
  ```java
  Map<String, List<String>> map = new HashMap<>();
  ```
- **Cảnh báo Tà Công**: Tránh dùng Raw Types. Nó gây ra **"Ô nhiễm vùng nhớ" (Heap Pollution)** — một loại nội thương ngầm chỉ phát tác khi chạy.
  ```java
  List list = new ArrayList<String>(); // ❌ Đừng làm thế này!
  ```

## 4. Bất Biến Thần Công (Invariance)

**Định luật:** Trong Java Generics, `List<Con>` **KHÔNG PHẢI** là con của `List<Cha>`.
Tức là: `List<Integer> != List<Number>`

**Lý do:** Bảo vệ vùng nhớ. Nếu chấp nhận tính kế thừa này, ta có thể vô tình bỏ "Chuối" (`Double` - ví dụ 3.14) vào giỏ đang đựng "Táo" (`Integer`) thông qua tham chiếu "Hoa Quả" (`Number`). Điều này đảm bảo an toàn bộ nhớ (Memory Safety).

## 5. Chính Tà Bất Lưỡng Lập (Mảng vs Generics)

| Tính chất | Mảng (Arrays) | Generics |
| :--- | :--- | :--- |
| **Bản chất** | **Hiệp biến (Covariant)**: `Integer[]` là con của `Number[]`. | **Bất biến (Invariant)**: `List<Integer>` khác `List<Number>`. |
| **Kiểm tra tại** | Runtime | Compile-time |
| **Hậu quả sai kiểu**| Lỗi `ArrayStoreException` | Lỗi biên dịch (An toàn) |
| **Trạng thái** | **Reified**: Biết rõ kiểu khi chạy | **Erased**: Mù mờ về kiểu khi chạy (Type Erasure) |

**Cấm kỵ:** Không khởi tạo mảng Generic: `new List<String>[10];`

## 6. Vô Tướng Công (Type Erasure) - Sắc tức thị không, Hình tướng là hư ảo

Tại Runtime (JVM), Generic không tồn tại. Mọi tham số `<T>` bị xóa thành `Object` (hoặc Bounds) để duy trì hòa bình với các bậc tiền bối (Backward Compatibility - Tương thích ngược).

- **Trần thế (Code của bạn):**
  ```java
  List<String> list;
  list.get(0);
  ```
- **Cõi hư vô (Sau Compiler Process):**
  ```java
  List list;
  ((String)) list.get(0); // Ép kiểu ngầm định được thêm vào
  ```

## 7. Đả Thông Kinh Mạch (Bridge Methods)

Khi xóa kiểu (Type Erasure), phương thức con (ví dụ `setData(Integer)`) không còn khớp với cha (`setData(Object)`). Trình biên dịch phải âm thầm tạo ra **'Cầu nối' (Synthetic Bridge)** để duy trì dòng chảy Đa hình (Polymorphism).

```java
class MyNode extends Node {
  // Phương thức ẩn do Compiler tạo ra (Bridge Method):
  public void setData(Object data) {
    this.setData((Integer) data); // Ép kiểu và chuyển tiếp
  }
  
  // Phương thức thực tế của bạn:
  public void setData(Integer data) { ... }
}
```

## 8. Lăng Ba Vi Bộ (Wildcards `?`) - Uyển chuyển như bước trên sóng

Khi luật Bất biến quá cứng nhắc, ta dùng Wildcard (`?`) để đạt sự linh hoạt.

**Chiêu thức: Unbounded Wildcard `List<?>`**
- **Chấp nhận**: Bất kỳ danh sách nào.
- **Cái giá**: Chỉ có thể ĐỌC `Object`. Cấm thêm phần tử (trừ `null`).

```java
void printList(List<?> list) {
  for (Object elem : list) {
      // OK
  }
  // list.add("Hi"); // ❌ Lỗi biên dịch!
}
```

## 9. Hấp Tinh Đại Pháp (Upper Bound: `? extends T`) - The Producer

- **Khẩu quyết**: `List<? extends Number>`
- **Ý nghĩa**: Danh sách chứa một loại con nào đó của `Number`.
- **ĐỌC (✅)**: An toàn. Luôn lấy ra được `Number`.
- **GHI (❌)**: Cấm kỵ. Không thể thêm phần tử vì không biết kiểu thực sự.
- **Sử dụng**: Dùng cho tham số cung cấp dữ liệu (Producer).

## 10. Dời Hoa Tiếp Mộc (Lower Bound: `? super T`) - The Consumer

- **Khẩu quyết**: `List<? super Integer>`
- **Ý nghĩa**: Danh sách chứa một loại cha nào đó của `Integer`.
- **GHI (✅)**: An toàn. Có thể thêm `Integer` (và các lớp con của nó).
- **ĐỌC (⚠️)**: Hạn chế. Chỉ lấy ra được kiểu `Object`.
- **Sử dụng**: Dùng cho tham số tiếp nhận/lưu trữ dữ liệu (Consumer).

## 11. Khẩu Quyết Tâm Pháp: PECS

**P E C S** = **P**roducer **E**xtends, **C**onsumer **S**uper

- Muốn lấy dữ liệu ra? ➔ Dùng `extends`
- Muốn nạp dữ liệu vào? ➔ Dùng `super`

**Công thức bí kíp (ví dụ trong Collections.copy):**
```java
// Sao chép từ 'src' (lấy ra) sang 'dest' (nạp vào)
Collections.copy(List<? super T> dest, List<? extends T> src)
```

## 12. Tử Huyệt (Restrictions) - Những vùng cấm của Generic Thần Công

1. **Kiểu Nguyên Thủy**: Không dùng `List<int>`. Phải dùng `List<Integer>` (tốn kém tài nguyên cho Boxing/Unboxing).
   ```java
   List<Integer> numbers = new ArrayList<>();
   ```
2. **Khởi tạo**: Không thể `new T()` hoặc khởi tạo mảng generic `new List<String>[10]`.
   ```java
   // ❌ ERROR: new T();
   ```
3. **Tĩnh (Static)**: Biến static `T` bị cấm (vì `T` không tồn tại khi class được load).
   ```java
   // ❌ ERROR: static T instance;
   ```
4. **Ngoại lệ**: Không thể bắt ngoại lệ generic.
   ```java
   // ❌ ERROR: catch (T e) { ... }
   ```

## 13. Phi Thăng Tiên Giới - Tương lai: Project Valhalla

Cộng đồng Java đang tu luyện tầng thứ tiếp theo mang tên **Project Valhalla** nhằm loại bỏ hoàn toàn gánh nặng của Boxing/Unboxing.

- **Specialized Generics**: Cho phép `List<int>` thực sự (Hiệu năng tương đương C++).
  ```java
  List<int> numbers = new ArrayList<>();
  ```
- **Reified Generics**: Khôi phục thông tin kiểu tại Runtime.

## 14. Đại Triệt Đại Ngộ - The Master's Wisdom

1. Generic là sự thỏa hiệp vĩ đại giữa **An toàn** và **Tương thích ngược**.
2. Hiểu rõ 'Vô Tướng Công' (**Erasure**) để tránh cạm bẫy.
3. Thành thục '**PECS**' để viết API linh hoạt.

> "Mã nguồn sạch là mã nguồn an toàn. Người luyện võ chân chính dùng Type System làm vũ khí bảo vệ sự ổn định của hệ thống."
> — _Codemia Resources - 2026_
