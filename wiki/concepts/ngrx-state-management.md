---
title: "NgRx State Management"
source: "compiled"
date_added: 2026-04-23
tags: [concept, javascript, angular, ngrx, state-management]
aliases: [Redux, Prop Drilling, Store, Reducer, Action, Selector, Effect]
status: draft
related:
  - "[[rxjs-reactive-programming]]"
  - "[[javascript-variables-and-scope]]"
summary: "Kiến trúc quản trị trạng thái tập trung (State Management) thông qua NgRx trong Angular, giải quyết bài toán Prop Drilling và cơ chế luân chuyển dữ liệu một chiều."
---

# NgRx State Management

Khi một ứng dụng Frontend phát triển lớn, việc truyền dữ liệu giữa các Component thông qua cơ chế cha-con (`@Input()` và `@Output()`) tạo ra một mạng lưới liên kết chằng chịt. Cấu trúc này được gọi là **Prop Drilling**, gây ra khó khăn cực lớn trong việc theo dõi luồng dữ liệu, debug lỗi, và tái sử dụng mã nguồn.

Để giải quyết vấn đề này, kiến trúc **State Management (Quản trị trạng thái tập trung)** ra đời. Trong hệ sinh thái Angular, **NgRx** là thư viện triển khai mô hình Redux Pattern nổi tiếng nhất, được xây dựng hoàn toàn dựa trên sức mạnh của [[rxjs-reactive-programming|RxJS Observables]].

## 1. Nguyên Lý Kho Trữ Tập Trung (Store)

Thay vì để dữ liệu nằm rải rác ở từng Component, NgRx di chuyển toàn bộ dữ liệu (State) của ứng dụng vào một "Kho chứa trung ương" duy nhất gọi là **Store** (Single Source of Truth). 

Mọi Component (lúc này trở thành các "Dumb Components" - Component thụ động) chỉ đảm nhận hai nhiệm vụ:
- Lấy dữ liệu từ Store về để hiển thị (Render).
- Thông báo ra bên ngoài khi người dùng tương tác (nhấn nút, nhập form).

Sự luân chuyển dữ liệu tuân thủ nghiêm ngặt **Luồng dữ liệu một chiều (Unidirectional Data Flow)** thông qua 5 thành phần cốt lõi:

### 1. Actions (Lệnh Trạng)
Khi người dùng tương tác, Component không tự xử lý logic mà chỉ phát ra một Action (Ví dụ: `[Auth Page] Login User`). Action là các gói tin mô tả "điều gì vừa xảy ra", có thể đính kèm dữ liệu (payload).

### 2. Reducers (Người Cập Nhật Trạng Thái)
Reducer là thành phần duy nhất trong hệ thống có quyền quyết định thay đổi dữ liệu trong Store. Khi lắng nghe được một Action, nó phân tích dữ liệu và tạo ra State mới.
> [!CAUTION] Tính Bất Biến (Immutability)
> Reducer bắt buộc phải là một **Hàm thuần túy (Pure Function)**. Nó tuyệt đối không được sửa đổi (mutate) State hiện tại (đã phân tích kỹ trong bài [[javascript-variables-and-scope#bản-chất-tính-bất-biến-của-const|Tính bất biến]]). Thay vào đó, Reducer sử dụng cú pháp Spread Operator (`...`) để sao chép State cũ, ghi đè phần thay đổi, và trả về một State hoàn toàn mới.

### 3. Selectors (Bộ Trích Xuất Dữ Liệu)
Store có thể chứa hàng chục megabyte dữ liệu. Để các Component lấy đúng mảnh dữ liệu chúng cần mà không làm giật tải toàn hệ thống, NgRx sử dụng Selectors. Selectors giống như các camera giám sát, chỉ trích xuất đúng một vùng nhỏ dữ liệu (ví dụ: `selectAllUsers`) và có cơ chế ghi nhớ (Memoization) để tối ưu hiệu suất.

### 4. Effects (Bộ Xử Lý Bất Đồng Bộ)
Tuyệt đối cấm Reducers thực hiện các tác vụ tốn thời gian như gọi API. Khi ứng dụng cần gọi API, một Action (ví dụ: `[User] Fetch Users`) sẽ được phát ra. **Effects** đứng bên ngoài lắng nghe Action này, chặn nó lại, thực hiện gọi API (sử dụng các RxJS Operators như `switchMap`, `map`), và cuối cùng phát ra một Action mới mang theo kết quả (`[User API] Load Success`) để Reducer cập nhật vào Store.

## 2. Ưu Điểm Tuyệt Đối Của Kiến Trúc NgRx

Mặc dù NgRx yêu cầu thời gian khởi tạo (boilerplate) đáng kể, cấu trúc Lầu Năm Góc này mang lại những lợi ích vượt trội cho các dự án quy mô doanh nghiệp:

1. **Khử Tùy Tiện Luồng Logic:** Mọi thay đổi dữ liệu đều đi theo đúng một chiều `Action -> (Effect) -> Reducer -> Store -> Selector -> Component`. Lỗi xảy ra ở đâu, lập trình viên khoanh vùng chính xác ở đó.
2. **Khả Năng Kiểm Thử Độc Lập (Unit Testing):** Bằng cách tách bạch logic (Reducer/Effect) khỏi giao diện (Component), việc viết Unit Test cho từng chức năng trở nên dễ dàng và độ bao phủ cao.
3. **Time Traveling Debugging:** Vì mọi hành động thay đổi State đều tạo ra một đối tượng State mới (nhờ tính bất biến), lập trình viên có thể sử dụng Redux DevTools để "quay ngược thời gian", hoàn tác (undo) các hành động, và tái hiện chính xác tình trạng lỗi của UI ở bất kỳ thời điểm nào trong quá khứ.
