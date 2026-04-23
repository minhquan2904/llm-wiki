---
title: "TypeScript Module 07: Hệ Gen Nhân Tạo (Generics)"
source: "raw/misc/ts/7.md"
date_added: 2026-04-23
tags: [typescript, generics, cyber-shogun]
aliases: []
status: draft
summary: "Khám phá bí ẩn tối thượng của cú pháp <T> - Hệ Gen Nhân Tạo giúp TypeScript linh hoạt tuyệt đối mà không cần dùng đến cái bẫy chết người 'any'."
---

# :material-dna: Module 07: Hệ Gen Nhân Tạo (Generics)

> *"Một thanh kiếm chỉ chém được thép thì sớm muộn cũng gãy trước một tấm khiên năng lượng. Kỹ sư thực thụ không đúc vũ khí một chiều, họ đúc ra một **Khuôn Mẫu Vi Sinh** có khả năng tự tiến hóa tương thích hoàn toàn theo loại năng lượng được nạp vào."* – **Kỷ Yếu Cyber-Shogun**

Giữa chiến trường Runtime khốc liệt, khát vọng lớn nhất của một lập trình viên là **Sự Tái Sử Dụng (Reusability)**. 
Nếu bạn chế tạo một khẩu súng chỉ bắn được Khối Lửa (`Fire`), khi cần bắn Băng (`Ice`), bạn phải viết lại một khẩu súng y hệt. Nếu bạn lấp liếm bằng cách dùng `any`, bạn vô tình mở ra chiếc hộp Pandora rỉ sét, biến khẩu súng thành một trạm rác tẩu hỏa (ai nhét một củ khoai tây vào súng cũng bắn được nhưng sẽ nổ tung khoang đạn).

TypeScript mang đến công nghệ tối thượng để giải quyết bài toán này: **Generics (Hệ Gen Nhân Tạo)**.

---

## 1. Khai Mở: Ký tự `<T>` là cái quái gì?

Bạn sẽ thấy hàng ngàn đoạn code TypeScript trên thế giới nhồi nhét hai dấu ngoặc nhọn `<T>`. Rất đáng sợ khi mới nhìn vào, nhưng bản chất lại cực kỳ dễ thấu hiểu.

=== "🎭 Cyber-Metaphor"

    Hãy tưởng tượng `<T>` là một **Khoang Quả Lọc Trống (Empty Variable Slot)**. 
    Lúc bạn thiết kế Bản Vẽ (Code Design), Khoang này CHƯA quy định sẽ chứa vật chất gì. Chỉ đến khoảnh khắc bạn vác Bản Vẽ đi đúc thật và kích hoạt (Function Call / Instantiation), bạn mới **bơm DNA** cụ thể vào cái Khoang đó. Từ giây phút đó, toàn bộ vũ khí sẽ "Hóa hình" đúng theo gen bạn bơm vào, an toàn 100%.

=== "💻 Tech Specs"

    Trong code, `T` là viết tắt thông dụng cho chữ **"Type"**. Nó hoạt động y hệt tham số biến cục bộ (variable parameters) trong hàm JavaScript, nhưng thay vì truyền Dữ Liệu Thực (Values như `10`, `"Hello"`), bạn truyền **Định Dạng (Types)** cho trình quản lý chặt của Compiler.

### 1.1 Khử Bẫy Ngầm chết người `any`

Nhìn vào chức năng sao chép vũ khí dưới đây:

```typescript title="bad_design.ts"
// Cách 1: Chỉ cho phép Clone Súng (Quá cứng nhắc, đút kiếm vô là lỗi)
function cloneGun(item: Gun): Gun { return item; }

// Cách 2: Dùng ANY (Quá nguy hiểm - Đánh mất Type An Toàn)
function cloneItem(item: any): any { return item; }

let katana = cloneItem({ name: "Cursed Blade", damage: 99 });
// LỖI NGẦM: Vì hàm trả về 'any', biến 'katana' giờ bị Đục Thủy Tinh Thể (Mù type). 
// Nếu bạn gõ nhầm katana.damege = undefined nó CŨNG KHÔNG BÁO LỖI, chết ngay lúc runtime!
```

Giờ hãy tiêm Hệ Gen vào quy trình:

```typescript title="generic_design.ts"
// Cách 3: Hệ Gen Nhân Tạo (Hòa Nhập Khẩn Cấp)
function cloneItem<T>(item: T): T {
    return item; // Trả về đúng chất liệu gì đưa vào
}

// Lúc gọi lệnh, bạn "tiêm" Gen của MeleeWeapon vào khoang <T>
let katana = cloneItem<MeleeWeapon>({ name: "Cursed Blade", damage: 99 });

// 💥 ĐỈNH CAO: Bật "Type Inference"
// Compiler TS thông minh đến mức tự phân tích dữ liệu rồi Tự Nội Suy Gen mà KHÔNG CẦN CHỈ ĐỊNH RÕ <...>.
let laserGun = cloneItem({ name: "Plasma Cannon", range: 1000 }); 
// TS TỰ HIỂU: <T> lúc này chính là cấu trúc { name: string, range: number }! Quá uy lực!
```

---

## 2. Tiêm Gen Tầng Kiến Trúc (Generic Interfaces & Classes)

Không chỉ dùng cho Function rèn đồ xài một lần, Lõi `<T>` đóng vai trò chủ chốt bậc nhất để sinh ra những **Bản Vẽ Đột Biến (Generic Interfaces)**.

Chúng ta đến với metaphor thực dụng nhất ngoài chiến trường thực: **Lõi Vali Lượng Tử (Quantum Storage)**. Đây là hộp chứa vật phẩm thần bí – thứ mà bất kỳ Frontend Developer nào cũng đối mặt 100% trong đời thực dưới dạng **API Response**. Cứ gọi một API thì hệ thống Back-end ném trả về cho bạn 1 cái vali:

```typescript title="api_response.ts"
// Kỹ sư tạo ra một Cái Vali Giao Thức chung chung. Bên trong chứa 1 chất <T> bất kỳ 
interface QuantumBox<T> {
    statusCode: number;
    message: string;
    payload: T; // Hạt nhân T nằm ở đây
}

interface UserData { id: string; role: "Shogun" | "Ronin"; }
interface WeaponData { model: string; ammo: number; }

// Khi Sever gửi tín hiệu chứa Người dùng
const userSignal: QuantumBox<UserData> = {
    statusCode: 200,
    message: "Transmitted",
    payload: { id: "USR-99", role: "Shogun" } // TS check rất căng: Role mà gõ Sai chữ "Shogun" là ăn phạt Đỏ!
};

// Khi Server gửi tín hiệu đạn dược Vũ khí
const weaponSignal: QuantumBox<WeaponData> = {
    statusCode: 200,
    message: "Arming...",
    payload: { model: "Railgun", ammo: 50 }
};
```

Cùng 1 cấu trúc Bản Vẽ chung là `QuantumBox`, nhưng nhờ Bơm gen `<T>`, chúng ta bảo vệ nguyên vẹn cấu trúc tĩnh của hàng nghìn chuẩn Signal API khác nhau, không một ai được chừa chỗ viết lại `status` hay `message` cả trăm lần. DRY (Don't Repeat Yourself) một cách thần thánh.

---

## 3. Xiềng Xích Gen: Khống Chế Thiết Quân Luật (`extends`)

Sức mạnh sinh cơ càng lớn, hậu quả càng phi mã. Nếu bạn để Khoang `<T>` lỏng lẻo trôi nổi, đám lính đánh thuê nghiệp dư có thể cẩu thả nạp Dịch Trầm Tính vào Súng Chứa Cốt Lõi Lửa, tàn đời cục cưng của bạn.

```typescript title="loi_do.ts"
function printCyberID<T>(item: T) {
    console.log(item.id); 
    // ^ LÕI ĐỎ LÒM: TS tát vỡ mặt vì Compiler bảo nó không chắc chắn "100% các loại Gen T" đều ngầm chứa một Property tên là 'id'! Lỡ người ta truyền `number` vào thì sao?
}
```

Chúng ta cần phải thiết ban **Thiết Quân Luật (Constraints)**: *"Tụi bây có thể truyền gen đạn dược gì vào T cũng được, NHƯNG nó BẮT BUỘC phải quy tụ dòng máu 'Có Chứa Đặc Điểm Này'"*. Lúc này, vũ khí `extends` sẽ giáp gai vào ngoặc nhọn `< >`.

```typescript title="constraints.ts"
// Định nghĩa quy tắc Vạch Đỏ Môi Trường
interface Identifiable {
    id: string; // Điều kiện tối thượng
}

// KHÓA LÕI BẮT RỄ Gen: <T extends Identifiable>
function printCyberID<T extends Identifiable>(item: T) {
    console.log(`Tiến hành rã đông ID: ${item.id}`); // HỢP LỆ! TS đã hoàn toàn tin tưởng! 
}

printCyberID({ id: "NINJA-01", stealth: true }); // Chạy tốt (vì Object này có chứa id: string)

printCyberID({ name: "Cyborg" }); 
// 🚨 CẢNH BÁO TỬ HÌNH KHÔNG CHO COMPILE: Argument of type '{ name: string; }' is not assignable to parameter of type 'Identifiable'.
```

---

## 4. Cấy Nhiều Gen và Gen Mặc Định (Multiple & Defaults)

Một sinh vật siêu việt sinh ra từ nhiều Lõi Gen khác nhau hoàn toàn có thể được ráp mạch lại với nhau. TS Compiler hỗ trợ tiêm đa luồng Cấp bậc.

```typescript title="multi_gen.ts"
// Sinh vật Mech lai tạo giữa <T> (hệ vũ khí lõi) và <U> (hệ năng lượng)
class CyberMech<T, U> {
    constructor(public weaponCore: T, public energyCore: U) {}
}

const gundam = new CyberMech<Sword, NuclearReactor>(mySword, myReactor);
```

**Kháng Thể Mặc Định (Default Generics):**
Đều đặn đề phòng kỹ sư bận rộn quên nạp Gen vào, Bộ quản lý được phép đặt **Cấu Trúc Gen Mặc Định** thông qua `=`.

```typescript title="default_gen.ts"
interface HologramConfig<T = string> {
    displayValue: T;
}

// Bác sĩ bỏ qua không bơm Gen -> T ngầm xác định chắc chắn là kiểu hệ `string`
const defaultSign: HologramConfig = { displayValue: "Cảnh Báo Đột Ngột" };

// Bác sĩ CỐ TÌNH ép Gen T sang hệ `number`
const countSign: HologramConfig<number> = { displayValue: 404 };
```

---

## 5. Nhật Ký Tối Hậu: Bác Sĩ Gen Căn Phân

| Kỹ thuật Gen | Ứng Dụng Khốc Liệt Trong Thực Chiến Frontend/Backend | Mức Độ Ranh Giới |
|--------------|-------------------------------------------------------|:----------------:|
| Phễu `<T>` ở hàm `function foo<T>` | Sử dụng nhiều vô đối khi viết Array Helper/Utils dùng chung, Hook React (`useState<T>`). Ép kiểu đầu ra tự ôm trọn kiểu đầu vào. | Băng Tân Binh |
| Tiêm `<T>` vào `interface` | Lặp cực kỳ nhiều để tạo cấu trúc Vỏ Vali Thần Bí: API Response (`AxiosResponse<T>`), Data Table, Pagination Struct. | Sống Còn |
| Cùm Xích `<T extends X>` | Giới hạn Phễu Gen. Biến TS thành tay Độc Tài tát sưng mặt các Developer khác nếu nhét dữ liệu cẩu thả không đáp ứng khuôn mẫu con. | Nâng Cao Lọc Lõi |

> **Nhiệm vụ tiếp theo:** Bạn đã sở hữu vũ khí cơ khí Interface, hóa chất Lượng tử Type Alias, và đỉnh cao nhất là Lõi Kỹ Thuật Sinh Học **Generics**. Giờ đây, khi bạn lê bước ra khỏi những tàn dư của miền đất hỏng hóc Runtime JavaScript, bạn đã một tay điều khiển được sức mạnh tối cao của Typescript Exosuit, sẵn sàng giải quyết bất kỳ kiến trúc khổng lồ nào trong thực tế. Series cốt lõi kết thúc, chặng đường ứng dụng của Shogun chính thức thức giấc!
