---
title: "Cơ Chế Nâng Cao JavaScript"
source: "compiled"
date_added: 2026-04-23
tags: [concept, javascript, advanced, coercion, prototype, this]
aliases: [Type Coercion, Prototypal Inheritance, call, apply, bind, Ép kiểu ngầm, Chuỗi nguyên mẫu]
status: draft
related:
  - "[[javascript-variables-and-scope]]"
  - "[[javascript-under-the-hood]]"
summary: "Khám phá các cơ chế cấp cao và dễ gây nhầm lẫn nhất của JavaScript: Ép kiểu ngầm (Type Coercion), Kế thừa chuỗi nguyên mẫu (Prototypal Inheritance) và cách kiểm soát ngữ cảnh `this` với Call, Apply, Bind."
---

# Cơ Chế Nâng Cao JavaScript

JavaScript được tạo ra trong một thời gian cực kỳ ngắn (10 ngày vào năm 1995), vì vậy ngôn ngữ này mang theo một số "di sản" thiết kế độc đáo. Việc không hiểu rõ các cơ chế ngầm (under the hood) này thường dẫn đến những lỗi logic (bugs) cực kỳ khó phát hiện, hay còn được gọi vui là những khoảnh khắc *"JS Wat"*.

Dưới đây là 3 cơ chế cấp cao định hình nên bản chất thực sự của ngôn ngữ JavaScript.

## 1. Ép Kiểu Ngầm (Type Coercion)

JavaScript là một ngôn ngữ linh hoạt (loosely typed). Khi nó thực hiện phép toán giữa hai kiểu dữ liệu không tương thích, thay vì báo lỗi, JS engine sẽ tự động **ép kiểu (coercion)** một trong hai giá trị cho khớp với giá trị kia trước khi tính toán.

### Ví dụ Về Sự Nhầm Lẫn
```javascript
console.log("11" + 1); // "111"
console.log("11" - 1); // 10
console.log([] == ![]); // true
```
- Phép cộng `+`: JS ưu tiên **nối chuỗi**. Số `1` bị ép thành chuỗi `"1"` và ghép vào.
- Phép trừ `-`: Không tồn tại khái niệm "trừ chuỗi", nên JS ép chuỗi `"11"` thành số `11` rồi thực hiện tính toán toán học.

> [!WARNING] Giải Pháp Khắc Phục
> Sự ép kiểu ngầm khi sử dụng toán tử so sánh lỏng lẻo `==` tạo ra những kết quả vô lý. Quy tắc vàng trong Clean Code JavaScript là **luôn luôn sử dụng so sánh chặt chẽ `===` và `!==`**. Toán tử này kiểm tra cả giá trị lẫn kiểu dữ liệu (Type), ngăn chặn triệt để hành vi ép kiểu ngầm.

## 2. Kế Thừa Chuỗi Nguyên Mẫu (Prototypal Inheritance)

Trái ngược với các ngôn ngữ hướng đối tượng truyền thống (như Java hay C#) sử dụng Class-based inheritance, JavaScript sử dụng **Prototype-based Inheritance (Kế thừa dựa trên nguyên mẫu)**.

Bản chất của cơ chế này là sự **ủy quyền (delegation)**. Mỗi object trong JS có một liên kết nội bộ ngầm trỏ đến một object khác, được gọi là `prototype` (tổ tiên) của nó.
Khi bạn cố gắng truy cập một thuộc tính hoặc gọi một phương thức trên một object:
1. JS sẽ tìm trực tiếp bên trong object đó.
2. Nếu không có, nó sẽ "leo lên" chuỗi nguyên mẫu để tìm ở `prototype` của object đó.
3. Quá trình này tiếp diễn cho đến khi tìm thấy, hoặc chạm đỉnh chuỗi (thường là `null`) và trả về `undefined`.

```javascript
const HieuTruongPrototype = {
  sayGreeting: function() {
    console.log("Chào mừng tới trường! Tôi là: " + this.name);
  }
};

// Tạo object mới kế thừa từ HieuTruongPrototype
const hocSinh = Object.create(HieuTruongPrototype); 
hocSinh.name = "Nobita";

// hocSinh không có hàm sayGreeting, nhưng nó ủy quyền lên prototype để gọi
hocSinh.sayGreeting(); 
```

> Sự thật: Từ khóa `class` xuất hiện trong ES6 thực chất chỉ là "cú lừa cú pháp" (Syntactic Sugar). Bên dưới tầng mã máy, nó vẫn được biên dịch ngược về cơ chế liên kết Prototype.

## 3. Thao Túng Ngữ Cảnh (`this`) Với Call, Apply, Bind

Biến `this` trong JS không được xác định tại thời điểm hàm được định nghĩa, mà được quyết định tại thời điểm hàm **được gọi** (Execution Context). Để ép hàm nhận diện một object cụ thể làm `this`, JS cung cấp 3 phương thức có sẵn trên mọi function: `call`, `apply` và `bind`.

### `.call()` và `.apply()`: Mượn Hàm Và Thực Thi Ngay
Hai lệnh này có tác dụng: Mượn một hàm, trói `this` vào một object được chỉ định, và **thực thi hàm đó ngay lập tức**.
Điểm khác biệt duy nhất nằm ở cách truyền tham số (arguments):
- **`call(thisArg, arg1, arg2)`**: Truyền các tham số rời rạc, phân tách bằng dấu phẩy.
- **`apply(thisArg, [argsArray])`**: Truyền toàn bộ tham số dưới dạng một mảng (array).

```javascript
const person1 = { firstName: "Saitama" };
const person2 = { firstName: "Goku" };

function getFullName(title, group) {
  return `${title} ${this.firstName} - ${group}`;
}

// Dùng Call: Tham số truyền lẻ
getFullName.call(person1, "Anh Hói", "Hội Anh Hùng"); // "Anh Hói Saitama - Hội Anh Hùng"

// Dùng Apply: Tham số gói trong mảng
getFullName.apply(person2, ["Anh Khỉ", "Phi Đội Saiyan"]); // "Anh Khỉ Goku - Phi Đội Saiyan"
```

### `.bind()`: Đóng Băng Ngữ Cảnh Chờ Tương Lai
Khác với `call` và `apply`, phương thức `.bind(thisArg)` **không thực thi hàm ngay lập tức**. Thay vào đó, nó trả về một **bản sao hoàn toàn mới** của hàm, trong đó `this` đã được chốt chặt (hard-bound) vĩnh viễn vào object chỉ định. 

`bind` cực kỳ hữu ích trong lập trình bất đồng bộ (Async) như truyền hàm callback vào `setTimeout`, hoặc gán EventListener cho giao diện, để đảm bảo `this` không bị thất lạc (trỏ ra biến toàn cục `window` hoặc `undefined`).

```javascript
const user = { name: "Batman" };
function sayHello() { console.log("Hey, I'm " + this.name); }

const lockedHello = sayHello.bind(user); // Tạo bản sao đã trói 'this'

setTimeout(lockedHello, 5000); // 5 giây sau chạy, 'this' vẫn an toàn trỏ vào user
```
