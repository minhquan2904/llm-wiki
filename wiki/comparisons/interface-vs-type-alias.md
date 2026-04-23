---
title: "So Sánh Interface và Type Alias Trong TypeScript"
source: "compiled"
date_added: 2026-04-23
tags: [typescript, interface, type-alias, comparison]
aliases: [Interface vs Type Alias, Declaration Merging, Intersection Types]
status: canonical
related:
  - "[[typescript]]"
  - "[[typescript-type-narrowing]]"
  - "[[typescript-oop]]"
summary: "Phân tích sự khác biệt về mặt kiến trúc, cơ chế kế thừa, và trải nghiệm lập trình (DX) giữa hai trường phái định kiểu cấu trúc dữ liệu cốt lõi trong TypeScript."
---

# So Sánh Interface và Type Alias Trong TypeScript

## Bối Cảnh
Trong hệ sinh thái [[typescript]], tồn tại hai công cụ cốt lõi để định nghĩa hình dáng (shape) của dữ liệu: `interface` (Giao diện) và `type` (Định danh kiểu - Type Alias). Dù trong nhiều trường hợp chúng có thể hoán đổi cho nhau, sự khác biệt về mặt triết lý thiết kế và cơ chế hoạt động bên dưới đòi hỏi kỹ sư phải đưa ra chiến lược lựa chọn phù hợp dựa trên bài toán kiến trúc.

## Bảng So Sánh

| Tiêu Chí | `interface` | `type` (Type Alias) |
| :--- | :--- | :--- |
| **Triết lý thiết kế** | Bản vẽ kỹ thuật (Blueprint) có tính cấu trúc và phân cấp. | Bí danh (Alias) đại diện cho công thức kết hợp của các kiểu. |
| **Cơ chế kế thừa** | Kế thừa phân cấp rõ ràng thông qua từ khóa `extends`. | Dung hợp cấu trúc thông qua toán tử Intersection (`&`). |
| **Đa Hình (Union Types)** | Không hỗ trợ toán tử `\|`. | Hỗ trợ tối đa toán tử `\|` (Ví dụ: `type A = B \| C`). |
| **Khả năng mở rộng (Declaration Merging)** | Cho phép gộp các khai báo trùng tên (Open Forge). | Báo lỗi ngay lập tức nếu khai báo trùng tên (Closed). |
| **Bản chất dữ liệu** | Phù hợp với Object và Class. | Định danh được mọi thứ: Primitive, Tuple, Mapped Types. |
| **Performance (Biên dịch)** | Caching nhanh, hiệu suất tốt hơn với các cấu trúc phân cấp sâu. | Cần tính toán lại khi có dung hợp phức tạp (`&`, `\|`). |
| **Trải nghiệm gỡ lỗi (DX)** | Lỗi hiển thị đích danh tên Interface ngắn gọn. | Lỗi có thể hiển thị toàn bộ cấu trúc phân tử (Wall of Red Text). |

## Phân Tích Chi Tiết

### 1. Cơ Chế Kế Thừa: Phân Cấp (`extends`) vs Dung Hợp (`&`)
- **Interface** sử dụng `extends` để xây dựng một phả hệ tĩnh. Trình biên dịch hiểu rõ mối quan hệ Cha-Con, do đó nó có thể Cache kết quả kiểm tra, giúp tăng tốc hiệu suất biên dịch. Nếu có xung đột thuộc tính (Ví dụ: Cha có `id: string`, Con đòi `id: number`), TypeScript sẽ báo lỗi ngay lập tức.
- **Type Alias** sử dụng toán tử Giao (`&` - Intersection) để đúc hai hoặc nhiều kiểu lại với nhau. Type không có khái niệm phả hệ. Khi xảy ra xung đột thuộc tính giữa hai Type, trình biên dịch không báo lỗi ngay, mà âm thầm biến thuộc tính đó thành kiểu `never`, gây ra lỗi ẩn (Runtime logic error) khi sử dụng.

### 2. Khả Năng Mở Rộng: Declaration Merging
Đây là đặc quyền Dị Biệt nhất của `interface`. Nếu bạn khai báo hai `interface` cùng tên trong cùng một Scope, TypeScript sẽ **tự động gộp** chúng thành một khối thống nhất.
```typescript
interface User { id: string; }
interface User { email: string; }
// Kết quả: User có cả id và email
```
**Phân tích:** 
- Tính năng này rất lý tưởng để viết type definitions (hồ sơ kiểu) nhằm mở rộng các thư viện của bên thứ ba (Ví dụ: cấy thêm phương thức vào `Window` object). 
- Tuy nhiên, trong dự án nội bộ, việc này tiềm ẩn rủi ro "ô nhiễm bản vẽ" nếu các kỹ sư vô tình đặt trùng tên interface. `type` an toàn hơn trong trường hợp này vì nó sẽ báo lỗi trùng lặp (Duplicate identifier).

### 3. Đa Hình Và Cấu Trúc Nguyên Thủy
Chỉ có `type` mới có khả năng sử dụng Union Types (`|`) để thiết lập cơ chế đa hình (Ví dụ: `type Response = Success | Error`). Ngoài ra, `type` có thể được sử dụng để định danh cho các kiểu nguyên thủy (`type ID = string`), giúp code mang tính miền (Domain-driven) rõ nét hơn. `interface` hoàn toàn bất lực trong các tác vụ này.

### 4. Trải Nghiệm Gỡ Lỗi (DX - Developer Experience)
Khi có lỗi gán sai kiểu:
- TypeScript sẽ báo lỗi với **tên cụ thể** của `interface` (VD: `Type '{...}' is not assignable to type 'HeavyArmor'`).
- Đối với `type` alias phức tạp (chứa nhiều Intersection và Union), TypeScript thường in ra toàn bộ cấu trúc bên trong (gọi là "The Wall of Red Text"), khiến việc đọc và dò lỗi tốn nhiều nỗ lực hơn.

## Kết Luận

Dựa trên các phân tích trên, chiến lược áp dụng thực tiễn trong các dự án doanh nghiệp như sau:

1. Dùng **`interface`** làm lựa chọn mặc định để:
   - Định nghĩa hình dáng của Object, Class cơ bản.
   - Định nghĩa Dữ liệu API (Contract) nhằm bảo vệ tính toàn vẹn và dễ đọc khi Debug.
   - Khi cần tận dụng hiệu suất biên dịch nhanh nhờ Caching của `extends`.
2. Dùng **`type`** khi:
   - Làm việc với Đa Hình (Union Types `|`).
   - Gán bí danh cho kiểu nguyên thủy (Primitive Data: `string`, `number`).
   - Xử lý các logic biến đổi kiểu phức tạp (Mapped Types, Conditional Types, Utility Types).

## Nguồn Tham Khảo
- [[raw/articles/ts-module-06.md]]
