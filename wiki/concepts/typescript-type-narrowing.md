---
title: "Đa Hình Và Cơ Chế Thu Hẹp Kiểu Trong TypeScript"
source: "compiled"
date_added: 2026-04-23
tags: [typescript, type-narrowing, union-types, concept]
aliases: [Union Types, Type Narrowing, Discriminated Unions, Exhaustiveness Checking]
status: canonical
related:
  - "[[typescript]]"
  - "[[typescript-functions]]"
  - "[[interface-vs-type-alias]]"
summary: "Phân tích cơ chế quản lý đa hình thông qua Union Types và các kỹ thuật thu hẹp kiểu dữ liệu (Type Narrowing) nhằm đảm bảo an toàn tại Compile-time."
---

# Đa Hình Và Cơ Chế Thu Hẹp Kiểu Trong TypeScript

## Định Nghĩa
Xung đột cốt lõi của lập trình ngôn ngữ định kiểu tĩnh (Statically Typed) là việc xử lý sự uyển chuyển của dữ liệu mà không làm suy giảm tính an toàn. Trong [[typescript]], bài toán này được giải quyết thông qua cơ chế **Đa Hình (Polymorphism)** bằng `Union Types` và các luồng kiểm soát logic để **Thu Hẹp Kiểu (Type Narrowing)**.

## 1. Cơ Chế Đa Hình: Union Types (`|`)
Bằng cách sử dụng toán tử đường ống dọc (`|`), biến có thể khai báo để chấp nhận nhiều cấu trúc kiểu dữ liệu khác nhau. Tuy nhiên, tính năng này đi kèm một luật bảo vệ nghiêm ngặt: Trình biên dịch chỉ cho phép truy cập vào các **thuộc tính dùng chung (Common Properties)** trên tất cả các kiểu hình thành nên Union.

```typescript
function kiemTra(thietBi: string | number) {
    // thietBi.length; // LỖI: Thuộc tính 'length' chỉ có ở string, number không có.
    console.log(thietBi.toString()); // HỢP LỆ: Cả string và number đều chia sẻ hàm này.
}
```

Để truy cập vào các thuộc tính hoặc phương thức đặc thù của từng kiểu, lập trình viên buộc phải sử dụng các cơ chế nhận diện để bóc tách luồng kiểm tra (Type Narrowing).

## 2. Type Narrowing: Các Kỹ Thuật Quét Mục Tiêu
Type Narrowing là quá trình thu hẹp một không gian biến đổi (`string | number`) thành một "Vùng an toàn" (v.d. chắc chắn là `string`), giúp IntelliSense hiển thị chính xác các phương thức khả dụng.

### Cảm Biến Nguyên Thủy (`typeof`)
Sử dụng toán tử `typeof` kết hợp với khối lệnh điều kiện (`if/else`) là kỹ thuật phổ biến nhất để phân tách các kiểu nguyên thủy (Primitive Types).

```typescript
function kichHoat(dauVao: string | number) {
    if (typeof dauVao === "string") {
        // Bên trong khối lệnh này, TS hiểu 100% dauVao là String
        console.log(dauVao.toUpperCase());
    } else {
        // Luồng còn lại tự động được suy luận là Number
        console.log(dauVao.toFixed(2));
    }
}
```

### Quét Phụ Kiện Đặc Trưng (`in`)
Khi làm việc với các đối tượng phức tạp (Object/Interface), `typeof` trở nên vô dụng vì mọi đối tượng đều trả về kết quả là `"object"`. Để bóc tách, ta dùng toán tử `in` nhằm truy vấn một thuộc tính (property) hoặc phương thức (method) có tính nhận diện.

```typescript
interface Kiem { maiSac(): void; doBaoMon: number }
interface Sung { napDan(): void; soLuongDan: number }

function baoTri(thietBi: Kiem | Sung) {
    if ("napDan" in thietBi) {
        thietBi.napDan(); // Thu hẹp kiểu thành đối tượng Sung
    } else {
        thietBi.maiSac(); // Thu hẹp kiểu thành đối tượng Kiem
    }
}
```

## 3. Bản Vẽ Tối Thượng: Discriminated Unions
Khi Union Type bao gồm nhiều hơn 2 hình dáng (ví dụ 5-10 giao diện khác nhau), việc dùng `in` trở thành "thảm họa if-else". Mô hình thiết kế chuẩn cho trường hợp này là **Discriminated Unions (Tagged Unions)**. 

Phương pháp này tạo ra một trường dữ liệu (field) cố định (thường đặt tên là `kind` hoặc `type`) với giá trị chuỗi (Literal String) được "khắc laze chết" vào mỗi Object Interface.

```typescript
interface CheDoKiem { kind: "can_chien"; doSac: number; }
interface CheDoSung { kind: "tam_xa"; soDan: number; }
type VuKhiLai = CheDoKiem | CheDoSung;

function vanHanh(vuKhi: VuKhiLai) {
    switch (vuKhi.kind) { // Điều hướng bằng trường Literal cố định
        case "can_chien":
            console.log(vuKhi.doSac); // Ép kiểu 100% thành CheDoKiem
            break;
        case "tam_xa":
            console.log(vuKhi.soDan); // Ép kiểu 100% thành CheDoSung
            break;
    }
}
```

## 4. Kiểm Tra Tận Tuyệt (Exhaustiveness Checking)
Đây là chiến thuật nâng cao bảo vệ vòng đời bảo trì ứng dụng. Nếu tương lai có một kỹ sư thêm một biến thể mới vào `type VuKhiLai` nhưng quên không cập nhật luồng `switch-case`, TS sẽ không phát sinh lỗi ngay lập tức, dẫn đến Runtime Crash tại môi trường production.

Bằng cách nhét biến sót lại vào khối `default` và gán cưỡng chế nó thành kiểu `never`, hệ thống sẽ ném ra lỗi đỏ rực tại Compile-time ngay thời khắc đoạn mã bị bỏ quên.

```typescript
function vanHanhAnToan(vuKhi: VuKhiLai) {
    switch (vuKhi.kind) {
        case "can_chien": break;
        case "tam_xa": break;
        default:
            // NẾU LUỒNG QUÊN XỬ LÝ MỘT BIẾN THỂ NÀO ĐÓ:
            // vuKhi sẽ gán đè lên Kiểu "never" -> PHÁT LỖI COMPILER LẬP TỨC.
            const _kiemTraToanDien: never = vuKhi;
            return _kiemTraToanDien;
    }
}
```

## Nguồn Tham Khảo
- [[raw/articles/ts-module-05.md]]
