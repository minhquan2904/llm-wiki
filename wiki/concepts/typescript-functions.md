---
title: "Giải Phẫu Cấu Trúc Hàm Trong TypeScript (Functions)"
source: "compiled"
date_added: 2026-04-23
tags: [typescript, functions, concept]
aliases: [TypeScript Functions, Optional Parameters, Void vs Never]
status: canonical
related:
  - "[[typescript]]"
  - "[[typescript-type-narrowing]]"
summary: "Phân tích cấu trúc định kiểu của hàm, quản lý tham số và sự phân biệt sâu sắc giữa hai kiểu trả về đặc thù: void và never."
---

# Giải Phẫu Cấu Trúc Hàm Trong TypeScript

## Định Nghĩa
Trong hệ sinh thái TypeScript, hàm (function) được quản lý dưới dạng một hợp đồng chặt chẽ với dung sai bằng 0. Khác với sự lỏng lẻo của JavaScript thuần túy, mọi tham số đầu vào (Input) và kết quả trả về (Output) của một hàm trong [[typescript]] đều bị ràng buộc bởi các chú thích kiểu (Type Annotations), qua đó chặn đứng các luồng dữ liệu lỗi ngay tại thời điểm biên dịch (Compile-time).

## 1. Định Kiểu Hàm (Typed Functions)
Việc định kiểu cho hàm là kỷ luật bắt buộc để đảm bảo tính toàn vẹn của chuỗi xử lý logic. Trình biên dịch sẽ báo lỗi ngay lập tức nếu dữ liệu truyền vào không khớp với thiết kế.

```typescript
// Tham số vatLieu bắt buộc phải là string.
// Hàm cam kết sẽ trả lại một giá trị kiểu string.
function cheTaoVuKhi(vatLieu: string): string {
    return `Tiến trình: Đang rèn vũ khí từ ${vatLieu}`;
}

let sword = cheTaoVuKhi("Titanium"); // Hợp lệ
// let gun = cheTaoVuKhi(999); // LỖI COMPILER: 'number' không gán được cho 'string'
```

## 2. Quản Lý Tham Số (Parameters)

### Tham Số Tùy Chọn (Optional Parameters)
Được biểu thị bằng dấu hỏi chấm `?`. Khi một tham số được đánh dấu tùy chọn, TypeScript sẽ tự động ngầm định kiểu của nó thành một dạng lai (Union Type) kết hợp với `undefined` (ví dụ: `string | undefined`). Điều này buộc lập trình viên phải thiết lập luồng kiểm tra (If Guard) trước khi sử dụng.

```typescript
function cuongHoaVuKhi(id: number, buaChu?: string): void {
    if (buaChu) { // Bắt buộc kiểm tra undefined
        console.log(`Vũ khí ${id} được cường hóa bởi [${buaChu.toUpperCase()}]`);
    } else {
        console.log(`Vũ khí ${id} hoạt động ở trạng thái cơ sở.`);
    }
}
```

### Tham Số Mặc Định (Default Values)
Cung cấp một giá trị dự phòng nếu hàm được gọi mà không truyền dữ liệu cho tham số tương ứng. Cách tiếp cận này an toàn và tường minh hơn so với việc sử dụng `undefined`.

```typescript
function hieuChinhOngNgam(doPhongDai: number = 1.5): number {
    return doPhongDai * 100;
}
let aim1 = hieuChinhOngNgam(); // Áp dụng giá trị mặc định: 1.5
```

## 3. Cổng Xả Và Vực Sâu: `void` vs `never`
Nhiều kỹ sư nhầm lẫn giữa một hành động "thực thi xong không báo cáo" (`void`) và một hành động "bóp nghẹt hệ thống" (`never`).

### Kiểu trả về `void`
Sử dụng khi hàm thực thi xong một Tác vụ có hệ lụy phụ (Side-effect: Đổi giao diện, in log) nhưng không trả về bất cứ dữ liệu nào để tái sử dụng (`return`). Quá trình xử lý chạy trọn vẹn và tự kết thúc.

```typescript
function ghiNhatKy(trangThai: string): void {
    console.log(`[LOG]: ${trangThai}`);
    // Tuyệt đối không có lệnh return giá trị
}
```

### Kiểu trả về `never`
Là một trạng thái tuyệt đối — đại diện cho **những giá trị không bao giờ có thể xảy ra**. Một hàm định kiểu `never` là một "cửa ngõ không thể quay lại". Nó chứa một vòng lặp bất tận (`while (true)`) hoặc trực tiếp ném ra một lỗi (Throw Error), qua đó làm gián đoạn hoặc kết liễu hoàn toàn luồng thực thi Runtime của ứng dụng ngay tại điểm đó. Trình biên dịch hiểu rằng mọi dòng mã đặt sau lời gọi hàm `never` đều là mã chết (Unreachable Code).

```typescript
function loiHeThongNghiemTrong(lyDo: string): never {
    throw new Error(`CẢNH BÁO FATAL ERROR: ${lyDo}`);
    // Luồng Runtime kết thúc tại đây, không bao giờ return hay chạy xuống dưới.
}
```

## Nguồn Tham Khảo
- [[raw/articles/ts-module-04.md]]
