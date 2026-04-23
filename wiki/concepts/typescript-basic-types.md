---
title: "Các Kiểu Dữ Liệu Cơ Sở Trong TypeScript (Basic Types)"
source: "compiled"
date_added: 2026-04-23
tags: [typescript, basic-types, type-system, concept]
aliases: [TypeScript Basic Types, Type Annotations, Static Typing]
status: canonical
related:
  - "[[typescript]]"
  - "[[typescript-functions]]"
summary: "Hệ thống các kiểu dữ liệu nền tảng trong TypeScript bao gồm string, number, boolean, any và void nhằm kiểm soát tính toàn vẹn dữ liệu."
---

# Các Kiểu Dữ Liệu Cơ Sở Trong TypeScript

## Định Nghĩa
Trong [[typescript]], Type Annotations (Chú thích kiểu) và Static Typing (Định kiểu tĩnh) là cơ chế bắt buộc nhằm bảo vệ tính toàn vẹn của dữ liệu trong quá trình phát triển. TypeScript cung cấp 5 hệ thống phòng thủ cơ bản nhất cho các giá trị nguyên thủy (primitives) và hành vi của hệ thống: **String, Number, Boolean, Any và Void**.

## Các Kiểu Dữ Liệu Cốt Lõi

### 1. String
Kiểu `string` ép buộc giá trị phải là văn bản, ngăn chặn các lỗi cộng chuỗi với số tiềm ẩn trong JavaScript. Tài liệu *"Sinh Tồn Trong Kỷ Nguyên Kỹ Thuật Số"* mô tả Template Literals (`` ` ``) như "các khe cắm module", nơi biến số (`${}`) phải khớp chính xác vào vị trí của nó để hoàn thiện dữ liệu giao tiếp một cách chặt chẽ.

```typescript
let sector: string = "7";
let message: string = `Approaching Sector ${sector}`; // Template Literal
// message = 100; // Báo lỗi Type 'number' is not assignable to type 'string'
```

### 2. Number
Không phân biệt số nguyên (int) hay số thực (float), mọi giá trị số học trong TypeScript được quản lý dưới kiểu `number` (hỗ trợ cả hệ thập lục phân - hex, nhị phân - binary). Cơ chế này khóa kiểu biến chặt chẽ để đảm bảo an toàn cho các thuật toán tính toán, loại bỏ các hiện tượng "Type Coercion" dị thường của JavaScript gốc.

```typescript
let ammoCount: number = 250;
let shieldIntegrity: number = 98.5;
let hexKey: number = 0xf00d;
let currentPower: number = ammoCount + shieldIntegrity;
```

### 3. Boolean
Kiểu `boolean` chỉ nhận duy nhất hai giá trị `true` hoặc `false`. Việc định kiểu tường minh giúp hệ thống loại trừ các rủi ro so sánh lỏng lẻo dựa trên tính chất Truthy/Falsy của JavaScript.

### 4. Any
Kiểu `any` là một cơ chế ngoại lệ, cho phép biến nhận mọi loại dữ liệu và vượt qua toàn bộ quá trình kiểm tra kiểu (Type Checking). 
Sử dụng `any` đồng nghĩa với việc vô hiệu hóa hệ thống bảo vệ của TypeScript và đưa đoạn mã trở về trạng thái thiếu an toàn của JavaScript. Khuyến nghị chỉ sử dụng `any` khi phải tương tác với hệ thống cũ (legacy) hoặc dữ liệu thô không rõ cấu trúc. Tài liệu hệ thống cảnh báo rằng việc lạm dụng `any` tương đương với việc "tắt hệ thống radar cảnh báo rủi ro" và kích hoạt giao thức cuồng nộ (The Berserk Protocol) không an toàn.

```typescript
let unknownEntity: any = "Biến hình";
unknownEntity = 42; 
unknownEntity = true; 
// Trình biên dịch bỏ qua lỗi, nhưng có thể gây crash tại runtime
```

### 5. Void
Trái ngược với `any`, `void` thường được sử dụng để định nghĩa kiểu trả về cho các [[typescript-functions|hàm]] không mang dữ liệu đầu ra. Hàm kiểu `void` chỉ thực thi các thao tác có hệ lụy phụ (side-effects) như ghi log, thao tác DOM hoặc kích hoạt sự kiện mà không có lệnh `return` trả giá trị.

```typescript
function logCombatData(enemyName: string): void {
    console.log(`Đã lưu dữ liệu chiến đấu của ${enemyName} vào hộp đen.`);
    // return 123; // Error
}
```

## Nguồn Tham Khảo
- [[raw/articles/ts-module-01.md]]
