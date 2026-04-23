---
title: "TypeScript Module 06: Cuộc Nội Chiến Kiến Trúc (Interface vs Type Alias)"
source: "raw/misc/ts/6.md"
date_added: 2026-04-23
tags: [typescript, interface, type-alias, cyber-shogun]
aliases: []
status: draft
summary: "Giải phẫu cuộc nội chiến muôn thuở trong TypeScript giữa Phái Bản Vẽ (Interface) và Thuật Giả Kim Lượng Tử (Type Alias)."
---

# :material-matrix: Module 06: Cuộc Nội Chiến Kiến Trúc (Interface vs Type Alias)

> *"Có kẻ chế tạo vũ khí bằng cách hàn đẽo các Bản Vẽ Kỹ Thuật cứng nhắc lại với nhau. Lại có kẻ biến đổi Cấu Trúc Phân Tử của vật liệu để rèn thành kim loại lỏng. Trong kỷ nguyên Neo-Edo, bạn phải là chúa tể của cả hai."* – **Kỷ Yếu Cyber-Shogun**

Trong hệ sinh thái TypeScript, tồn tại một cuộc chiến tư tưởng dai dẳng giữa hai trường phái thiết kế Cấu trúc Dữ liệu: **Interface** (Giao diện) và **Type Alias** (Định danh kiểu). 

Nhiều tân binh thường ném bừa một chữ `interface` hoặc `type` vào code mà không hiểu sức nặng vật lý của chúng. Đây không chỉ là câu chuyện của cú pháp (syntax). Đây là sự lựa chọn về **Chiến lược Kiến trúc**.

---

## 1. Phái Chỉnh Hình: Bản Vẽ Kỹ Thuật (Interface)

**Interface** đứng về phe của kỹ thuật cơ khí truyền thống. Nó hoạt động như một **Bản Vẽ Kỹ Thuật (Blueprint)**. Nó không tạo ra kim loại, nó quy định *hình dáng, khớp nối và thông số* của bộ giáp bạn sắp mặc vào. Tính chất tối hệ trọng của nó là khả năng **tái sử dụng, kế thừa phân cấp** và **Lò Rèn Mở**.

### 1.1 Khớp Nối Kế Thừa Phân Cấp (`extends`)

Với Interface, bạn không bao giờ đập đi xây lại. Kỹ sư lấy bản vẽ của *BasicArmor*, ráp thêm động cơ Jetpack và đặt tên là *HeavyArmor*.

```typescript
// Bản vẽ gốc
interface BasicArmor {
    id: string;
    defend(): void;
}

// Chế tạo Cấp 2, kế thừa Cấp 1
interface HeavyArmor extends BasicArmor {
    jetpackPower: number;
}
```

Trình biên dịch hiểu rằng `HeavyArmor` mang dòng máu của `BasicArmor`. Mối quan hệ phả hệ này được Cache lại rất nhanh, giúp công cụ check lỗi không tốn lực xử lý lại từ đầu.

### 1.2 "Lò Rèn Mở" (Declaration Merging)

Đây là tính năng Dị Biệt nhất, quyến rũ cực độ nhưng đi kèm sát thương cao của Interface.

Trong thế giới Cyber, nếu hai kỹ sư ở hai tòa tháp khác nhau cùng đưa ra một Bản Vẽ mang tên `interface Ronin`, compiler của TS sẽ không báo lỗi. **Nó tự động GỘP 2 bản vẽ thành một Bản Vẽ Tối Thượng.**

```typescript
// Thư viện A quy định
interface Ronin { id: string; }

// Thư viện B gắn thêm phụ kiện
interface Ronin { weapon: string; }

// KẾT QUẢ RUNTIME: Bộ giáp có cả 2 đồ
let myShogun: Ronin = { id: "001", weapon: "Katana" };
```

=== "🎭 Cyber-Metaphor"

    !!! warning "Cảnh Báo: Ô Nhiễm Bản Vẽ (Blueprint Pollution)"
        Cơ chế này hoàn hảo để bạn Mod (độ chế) các Thư viện bên thứ 3 (ví dụ: cấy thêm method vào `Window` object của trình duyệt). Nhưng trong dự án nội bộ, việc mở toang cửa lò rèn thế này là **Tự bắn vào trán (Footgun)**. Một dev cấp dưới vô tình đặt trùng tên `interface user`, lập tức Object bị gắn thêm hàng tá rác rưới mà bạn truy vết rất hộc máu.

---

## 2. Thuật Giả Kim: Cấu Trúc Phân Tử (Type Alias)

Nếu Interface là Bản vẽ vĩ mô, thì **Type Alias** đại diện cho **Công thức Hóa Học** can thiệp thẳng vào Hạt Cốt Lõi. Type không tạo ra Cấu trúc mới, nó đưa cho Chuỗi Phân Tử một cái *Bí Danh* (Alias).

### 2.1 Đa Hình Mềm Dẻo (Unions)
Chỉ có Type mới thấu hiểu được Lý Thuyết Lượng Tử `HOẶC` (Đã nói rành rẽ ở **[Module 05](./5.md)**). Bạn không thể bắt một cái Bản vẽ Cơ khí (Interface) chứa 1/2 thanh kiếm HOẶC 1/2 nòng súng. Bản vẽ phải cố định. 
Nhưng Phân tử (Type) thì làm được.

```typescript
// 100% Độc quyền của Type Alias. Interface hoàn toàn bất lực.
type Ammo = ExplosiveRound | PiercingRound | EMPBlast;
```

### 2.2 Liên Kết Tinh Thể Khắc Nghiệt (Intersection `&`)

Type Alias không dùng khái niệm "Kế thừa mẹ - con" (`extends`). Nó bắt hai phân tử Đâm Xầm vào nhau để Đúc lại thành một Cục Vàng Tối Mật.

```typescript
type Human = { brains: boolean };
type Cyborg = { metalBones: boolean };

// Đúc thẳng ra CyberSamurai
type CyberSamurai = Human & Cyborg; 
```

=== "🎭 Bẫy Cấu Trúc: Sự cố Chập Mạch `never`"

    !!! danger "Ứng xử với Lỗi Xung Đột"
        Khi lấp rắp 2 món đồ:
        - Nếu ta dùng **Interface `extends`**: Thuộc tính của Cha và Con mà xung đột (Vd: Cha đòi `id: string`, con đòi `id: number`) => Compiler hiện Vạch Đỏ ngáp ngay tại chỗ: *"Hàn không dính, cút!"*
        - Nếu ta ép bằng **Type `&`**: Lò rèn vẫn chạy êm ru không Báo động. Nhưng ngay tại điểm đứt gãy, nó âm thầm chuyển Type thành Lỗ Đen `never`. Giao cỗ máy vào tay, chạy lên chiến trường súng tắc không bắn được đạn. Lỗi siêu ma!

---

## 3. Khác Biệt Sống Còn: "Bức Tường Máu" (DX vs Performance)

Ngoài khác biệt về cú pháp, thứ phân biệt hai Phe Phái này chói rọi nhất là Trải nghiệm của Kẻ Cầm Máy (DX - Developer Experience) lúc Debug rò rỉ.

**Phe Interface (Gọn Gàng & Định Danh):**
Khi lỗi bung lên, IDE sẽ báo lỗi bằng Đích Danh Tên Bản Vẽ. 
> *"Lỗi: Mày lắp sai đồ vào áo giáp `HeavyArmor`."*

**Phe Type Alias (Bức Tường Đỏ):**
Do Type chỉ là "Bí Danh" ghép từ 1 nùi công thức nguyên tử chắp vá. Khi hỏng ở một Type chằng chịt, TS sẽ xổ tung toàn bộ Hệ Phân Tử ra màn hình cho bạn xem. 
> *"Lỗi: Mày lắp sai đồ vào `{ A: string, B: bool, C: { D: abc } ... }`"*

Cái nùi Text khổng lồ trên terminal có thể dài hàng chục dòng, người trong giang hồ gọi nó là **"The Wall of Red Text"**. Cực vất vả khi Debug.

---

## 4. Tối Hậu Thư (Quy Luật Quân Đội)

Không có trường phái nào vô địch tuyệt đối. Hãy găm chặt Luật Bushido này vào Não Bộ để vận hành Exosuit mượt mà nhất trong dự án doanh nghiệp:

| Tình huống tham chiến | Khuyên dùng | Lý do bẻ khóa |
|-----------------------|-------------|---------------|
| **Định nghĩa Object, Class cơ bản** | `:material-check: Interface` | Caching siêu tốc, báo lỗi ngắn gọn, hỗ trợ Kế thừa minh bạch. |
| **Khai báo Dữ liệu API** | `:material-check: Interface` | Tên Contract được bảo vệ xuyên suốt hệ thống backend tới Frontend. |
| **Union Types (Cái này HOẶC Cái kia)** | `:material-check: Type Alias` | Bởi vì Interface làm mợ gì có chức năng này! |
| **Data Primitive (`string`, `number`)** | `:material-check: Type Alias` | Gắn tên biến `type ID = string` để tăng độ rõ nghĩa đọc hiểu (Domain-driven). |
| **Logic Toán Học Biến Đổi Kiểu** | `:material-check: Type Alias` | Xài cho Mapped & Conditional Types (Thuật Giả Kim Cấp Cao). |

> *Kết luận: Để thiết kế Kiến Trúc, dùng **Interface**. Để lắp ráp dữ liệu đa hình, dùng **Type Alias**.*
> 
> **Nhiệm vụ tiếp theo:** Thế giới Cyber-Shogun vẫn còn những lõi gen nhân tạo chưa được khai phá. Hãy chuẩn bị tinh thần bước vào **[Module 07: Hệ Gen Nhân Tạo (Generics)](./7.md)**.
