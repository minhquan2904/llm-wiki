---
title: "Hệ Gen Nhân Tạo (Generics) Trong TypeScript"
source: "compiled"
date_added: 2026-04-23
tags: [typescript, generics, concept]
aliases: [TypeScript Generics, Generic Constraints, Generic Default]
status: canonical
related:
  - "[[typescript]]"
  - "[[typescript-functions]]"
  - "[[interface-vs-type-alias]]"
summary: "Phân tích sức mạnh của Generics, cách sử dụng tham số kiểu <T> để kiến tạo các cấu trúc dữ liệu và hàm linh hoạt, có thể tái sử dụng cao mà không đánh đổi tính an toàn tĩnh."
---

# Hệ Gen Nhân Tạo (Generics) Trong TypeScript

## Định Nghĩa
Trong kỹ thuật phần mềm, khả năng **Tái Sử Dụng (Reusability)** là một yêu cầu cốt lõi. Trong các ngôn ngữ định kiểu tĩnh như [[typescript]], việc định nghĩa cứng nhắc các kiểu (Types) thường cản trở việc viết mã có khả năng mở rộng. Nếu sử dụng `any` để lách luật, hệ thống sẽ mất đi toàn bộ rào chắn an toàn (Type Safety). 

**Generics** là giải pháp kiến trúc giải quyết triệt để bài toán này. Nó cho phép truyền *Định dạng Kiểu (Types)* như những tham số vào hàm, class, hoặc interface, giúp cấu trúc này tự động điều chỉnh phù hợp với dữ liệu tại thời điểm thực thi.

## 1. Giải Mã Ký Tự `<T>`
Ký tự `<T>` (viết tắt của Type) đóng vai trò như một **Khoang Quả Lọc Trống (Empty Variable Slot)** tại thời điểm thiết kế. Khi cấu trúc được khởi tạo hoặc gọi, một "Gen" (kiểu dữ liệu thực tế) sẽ được "tiêm" vào khoang này.

```typescript
// Định nghĩa một hàm Generic
function cloneItem<T>(item: T): T {
    return item;
}

// Khi gọi hàm, tiêm kiểu cụ thể (VD: <string>)
let myName = cloneItem<string>("Shogun"); 

// Sức mạnh của Type Inference: TypeScript tự nội suy T là cấu trúc Object
let weapon = cloneItem({ name: "Plasma", range: 1000 });
```
Sự thông minh của trình biên dịch (Compiler) nằm ở cơ chế **Type Inference**. Thường thì bạn không cần khai báo rõ `<...>`, TypeScript sẽ tự động phân tích dữ liệu đầu vào và suy luận chính xác cấu trúc để gán cho `T`.

## 2. Bản Vẽ Đa Hình (Generic Interfaces & Classes)
Generics là xương sống của việc thiết kế các cấu trúc dữ liệu lớn, đặc biệt là trong việc bao bọc các phản hồi từ API (API Responses). Bằng cách thiết lập một giao diện (Interface) với lõi `<T>`, hệ thống giữ được bộ khung cố định trong khi thay đổi linh hoạt phần "nhân" bên trong.

```typescript
// Giao diện chung bọc dữ liệu trả về từ Server
interface QuantumBox<T> {
    statusCode: number;
    message: string;
    payload: T; // Hạt nhân dữ liệu biến đổi
}

interface UserData { id: string; role: string; }
interface WeaponData { model: string; ammo: number; }

// Bọc UserData
const userSignal: QuantumBox<UserData> = {
    statusCode: 200,
    message: "OK",
    payload: { id: "U99", role: "Admin" }
};

// Bọc WeaponData bằng cùng một giao diện
const weaponSignal: QuantumBox<WeaponData> = {
    statusCode: 200,
    message: "Armed",
    payload: { model: "Railgun", ammo: 50 }
};
```
Cách tiếp cận này tuân thủ tuyệt đối nguyên tắc DRY (Don't Repeat Yourself), tránh việc phải viết lặp lại các trường `statusCode` hay `message` cho mỗi loại dữ liệu.

## 3. Thiết Quân Luật Khống Chế (`extends`)
Mở toang `<T>` có thể dẫn đến rủi ro khi người dùng truyền vào một kiểu dữ liệu không có các thuộc tính mà hàm yêu cầu thực thi. Để bảo vệ logic, TypeScript cung cấp cơ chế **Generic Constraints (Ràng buộc Kiểu)** thông qua từ khóa `extends` đặt trong ngoặc nhọn.

```typescript
interface Identifiable {
    id: string; // Yêu cầu bắt buộc
}

// T bị khóa lại: Chỉ chấp nhận các kiểu có chứa thuộc tính 'id'
function printID<T extends Identifiable>(item: T) {
    console.log(item.id); // Trình biên dịch hoàn toàn tin tưởng
}

printID({ id: "NINJA-01", stealth: true }); // Hợp lệ
// printID({ name: "Cyborg" }); // LỖI COMPILER: Không có thuộc tính 'id'
```

## 4. Đa Luồng & Gen Mặc Định (Multiple & Default)

### Đa tham số Kiểu (Multiple Generics)
Một cấu trúc có thể tiếp nhận nhiều tham số kiểu khác nhau (thường ký hiệu là `T`, `U`, `V`...).
```typescript
class CyberMech<T, U> {
    constructor(public core: T, public energy: U) {}
}
```

### Kiểu Mặc Định (Default Generics)
Giống như tham số hàm mặc định, Generics cho phép chỉ định một kiểu dự phòng (Fallback) nếu người gọi không cung cấp kiểu rõ ràng.
```typescript
interface Config<T = string> {
    value: T;
}

const defaultConfig: Config = { value: "Warning" }; // T ngầm định là string
const customConfig: Config<number> = { value: 404 }; // Ép T thành number
```

## 5. Tổng Kết Ứng Dụng Thực Tiễn
Generics đóng vai trò tối quan trọng ở các tầng hệ thống:
- Ở mức độ hàm: Xây dựng các thư viện Utils, Helpers có khả năng bao trọn và trả về đúng kiểu dữ liệu (Ví dụ: `useState<T>` trong React).
- Ở mức độ cấu trúc: Thiết kế Data Tables, Pagination Wrapper, HTTP Response Wrapper (`AxiosResponse<T>`).
- Sử dụng ràng buộc `extends` để lập thiết quân luật, từ chối dữ liệu rác ngay từ vòng phân tích cú pháp tĩnh.

## Nguồn Tham Khảo
- [[raw/articles/ts-module-07.md]]
