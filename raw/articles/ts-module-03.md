---
title: "TypeScript Module 03: Hệ Điều Hành Trung Tâm (tsconfig)"
source: "raw/misc/ts/3.md"
date_added: 2026-04-23
tags: [typescript, tsconfig, strict-mode, cyber-shogun]
aliases: []
status: draft
summary: "Báo cáo kỹ thuật về Hệ Điều Hành Trung Tâm (tsconfig.json) và các giao thức kiểm soát môi trường (Rules) của TypeScript."
---

# :material-cogs: Module 03: Hệ Điều Hành Trung Tâm (tsconfig)

> *"Không một lớp Giáp nào cản được đạn nếu định luật bảo toàn khối lượng của vũ trụ bị bẻ cong."*

Nếu `Class` là khung xương của Exosuit (Bộ giáp), thì `tsconfig.json` chính là **Hệ Điều Hành (OS)** của không gian kỹ thuật số bạn hoạt động. Nó định nghĩa các chuẩn vật lý, sự nghiêm ngặt của luật An ninh mạng, và cấu trúc DNA cuối cùng của mã JavaScript sinh ra từ Nanoforge (`tsc`).

Sự tồn vong của một dự án lớn không phụ thuộc vào code đẹp hay xấu, mà vào cấu trúc OS được cấu hình chặt tới mức nào.

---

## 1. Compiler Options: Cấu Hình Nhân (Kernel Setting)

Trường `compilerOptions` là trái tim cấu hình. Phân hệ quan trọng đầu tiên: Cấu hình Khung Giao Tiếp Máy (Hardware compatibility & Mesh Network)

### Target: Tương Thích Thế Hệ Cổ Điển hay Tương Lai?
Tùy chọn `target` dán nhãn phiên bản JS (ECMAScript) mà mã nguồn TypeScript của bạn chắt vắt ra.

🛠 **Tech Specs:**
- `ES5`: Biên dịch ra công nghệ đồ đá cổ đại. Polyfills cồng kềnh đầy rẫy mã phụ (Bloatware) để bắt ép đám browser cổ lỗ sĩ hiểu.
- `ES2020` / `ES2022`: Phổ thông mạnh mẽ, hàm mũi tên (arrow func) mượt mà gọn nhẹ.
- **TypeScript 5.7+ (`ES2024`)**: Chế độ vũ khí tương lai. Hỗ trợ thẳng hàm `Object.groupBy` siêu tốc và `Promise.withResolvers`. Hãnh hãnh tiến lên phiên bản cao nhất có thể nhé môi trường Runtime của bạn!

### Module: Cấu Pháp Mạng Lưới
Cài đặt lưới Giao Thức đóng gói các file tách rời lại với nhau.
- `CommonJS`: Kết nối vật lý kiểu truyền thống của Node.js (cũ rích, đồng bộ).
- `ESNext` / `NodeNext`: **Tuyệt Sắc.** Mạng không dây hiện đại, hỗ trợ chuẩn xác cơ chế chắt lọc mã thừa "Tree-shaking". `NodeNext` tại TS 5.7 thậm chí còn check Security nghiêm ngặt import JSON.

---

## 2. Strict Mode: Bộ Luật Samurai (Bushido)

Flag `strict: true` là nhát chém thanh tẩy sự lỏng lẻo. Bật cờ này, bộ cảnh báo Cố Vấn Tốt Bụng biến hành một Vị Tướng Quân Thiết Quân Luật đi gõ đầu từng kẽ hở hớ hênh của Codebase.

=== "🤺 noImplicitAny (Trục Xuất Hư Vô)"

    - **Mối đe dọa:** Biến báo không định dạng? TypeScript sẽ nhắm mắt tặc lưỡi `any`! Nó tạo lỗ hổng toang hoác vào thẳng Giáp Chống Đạn.
    - **Bushido:** `noImplicitAny` Hét Thẳng: *Sương Mù Chiến Tranh phải tan biến! Khai báo rõ Địch Ta hoặc tước quyền thực thi!* Cứ ko gõ type là báo Đỏ rực Compile.

=== "🕳 strictNullChecks (An Toàn Khoảng Trống)"

    - **Mối đe dọa:** Lắm JS dev khoái gán giá trị String cũng được mà lúc khởi tạo lại cứ `null`. Lâu dần vấp thảm họa Runtime *"Cannot read property ABC of undefined"*.
    - **Bushido:** Cờ này ly khai tách bạch 1 biến đã String là phải là String chứ không lấy null nhét càn được. Nếu có rủi ro trống rỗng, bắt buộc đeo bảo hiểm bằng Union (v.d: `string | null`). Mọi thao tác đều ép gõ check If Tồn Tại.

=== "⚙ strictPropertyInitialization (Kiểm Tra Chuỗi Khởi Động)"

    - **Mối đe dọa:** Vẽ ra trên bản vẽ Mech có tên lửa, nhưng lúc `constructor` quên đấu điện. Chạy xịt.
    - **Bushido:** Class nào vẽ ra property mà Không set khởi tạo Giá Trị gốc và Không cấp phép null. BÁO LỖI ngay Lò phản ứng biên dịch (TSC). (Đặc biệt TS 5.7 nâng cấp luồn lách check lồng hàm cực chát).

=== "🎯 exactOptionalPropertyTypes (Cơ Khí Sắc Lẹm)"

    - **Sắc Thái Tinh Tế:** Báo giá trị thiếu dấu hỏi `color?: string` khác hoàn toàn với gán giá trị cụ thể `color: undefined`. Một cái là khe sắm vũ khí **Trống**, một cái là cố tình nhét một cục **Phế Liệu Undefined rỗng tuếch** vào cắm súng.
    - **Bushido:** Flag này ép Cố Tình Phân Định! Muốn trống rỗng hay muốn gỡ Phụ Tùng? Sai ý, chém!

---

## 3. Kho Khí Tài Mới: Tiến Hóa TypeScript 5.7 / 5.8 

Chiến Binh Cyber phải liên tục tải Patch Công nghệ mới nhất. Năng lực Engine Compiler gần đây đẻ ra các lệnh "Phá vỡ quy tắc cũ":

!!! tip "--rewriteRelativeImportExtensions (TS 5.7+)"
    Bạn đang đau não khi Deno/Bun chạy native, bắt ở Code TS viết đường truyền dán mác `.ts` trong khi Node lại cạch mặt?
    **Cờ này là phép thuật hậu cần**: Ta Tự Do gõ `.ts` trong file gốc của ta cho đã cái nết IDE lướt, lúc compile đúc Nanoforge nó TỰ TRANSLATE toàn bộ dán chữ cái thánh `.js`. Sướng điên người!

!!! abstract "--erasableSyntaxOnly (BETA TS 5.8)"
    **Chế Độ Tàng Hình Node.js**. Thay vì tải engine Tsc nặng ạch biên dịch từ từ sang JS. Có cờ này, TS buộc bạn tuân thủ luật viết cực siêu tốc: CHỈ Dùng Cú Pháp gỡ Type là chạy cái rẹt được Native Node. Tuyệt cấm dùng phím tắt `enum` hay `parameter props` chế loại lằng nhằng dính rễ hệ runtime. Code thanh tịnh - Trình chạy chớp mắt (`--experimental-strip-types`).

!!! warning "noUncheckedIndexedAccess (Đề xuất bật)"
    Dù list quái vật mới có 5 con. Bạn truy cập chém túi bụi `enemies[8]`. JS không sập ngay mà ói ra `undefined` rồi sau đó dây chuyền sập theo. TS xưa nay hiền nên cho qua.
    Gắn cờ này! TSC ép chê bai: *Khoan, mi làm gì chắc phần tử [8] có hình dạng? Phải móc giáp If Guard bọc lại ngay!*

---

## 4. Tóm Tắt Luật Hệ Thống Bất Di Bất Dịch

> *Chép ngay mớ Config rợn người này vào `tsconfig.json` khi boot 1 dự án mới toanh 2025. Hứa với Cyber-Shogun, nó sẽ cứu cái chân của bạn khỏi những phát tự chĩa bắn nhầm đầy đau đớn.*

| Config Flag | Mục Đích Tối Thượng Nôm Na | Nguy Cơ Nếu Vô Hiệu / Bỏ Qua |
|---|---|---|
| `strict: true` | Bật **Toàn Bộ Cảnh Sát Cấp Cao** đi tuần | Mã nguồn như thùng rác lộ thiên JS cũ. |
| `noImplicitAny` | Phải khai báo biến | Bị tập kích ngầm (Sương mù chiến thuật) |
| `strictNullChecks`| Rõ ràng giữa giá trị và Không gian trống rỗng | Mất áp suất nổ nát bét màn hình (undefined crash) |
| `noUncheckedIndexedAccess` | Phải xin phép chọc Array Object Index | Lụi đao vô không trung té xuống vực |
| `target: "ES2022/2024"` | Bắt lính dùng Đồ Chơi Máy Thời Đại Mới | Phình Code Rác tốn Băng thông lố bịch |

> **Nhiệm vụ đúc kết:** Giờ đây bạn đã đúc Giáp (Class OOP) trên một nền Hệ Điều Hành (tsconfig) đanh thép. Điểm đến tiếp theo là trạm trang bị: [Module 04: Lò Rèn Kỹ Thuật (Functions)](./4.md).
