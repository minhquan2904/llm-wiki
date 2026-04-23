---
title: "TypeScript Module 05: Vũ Khí Lai & Nhãn Quan Chiến Thuật"
source: "raw/misc/ts/5.md"
date_added: 2026-04-23
tags: [typescript, union-types, type-narrowing, cyber-shogun]
aliases: []
status: draft
summary: "Tổng thuật về Đa Hình học (Union Types) và Nhãn Quan Chiến Thuật (Type Narrowing) trong TypeScript."
---

# :material-sword-cross: Module 05: Vũ Khí Lai & Nhãn Quan Chiến Thuật

> *"Một thanh kiếm chỉ biết chém gọi là vũ khí. Một thanh kiếm vừa có thể chém gần, vừa gập lại thành nòng súng ngắm laze, đó là một Hệ Thống Tác Chiến Lai. Nhưng để dùng Hệ Thống đó không tự bắn vào chân, kỹ năng của phi công phải chuyển hóa dựa theo cơ học lượng tử."* – **Cẩm nang Cyber-Shogun**

Xung đột lớn nhất của lập trình viên cấu trúc (Statically typed) là xử lý sự uyển chuyển của dữ liệu. Nếu biến chỉ là `string` thì quá cứng nhắc. Nếu biến là `any` thì thành rác rưởi mất kiểm soát rủi ro.

Cầu nối Hoàn Hảo cho điều này là **Sự Đa Hình** (Polymorphism) bằng con đường `Union Types` (Kiểu Hợp) và **Nhãn Quan Thu Hẹp** (Type Narrowing).

---

## 1. Cơ Chế Đa Hình: Union Types (`|`)

Nhờ cơ chế Lý thuyết Tập hợp, chúng ta có thể tạo ra một Khe Cắm Vũ Khí Đa Năng. Cắm súng cũng được, cắm gươm cũng xong. Dùng ký tự **thanh dọc kép (`|`)**.

=== "🎭 Cyber-Metaphor"

    !!! info "Khe Cắm Vũ Khí Lai (Hybrid Weapon)"
        Khai báo `string | number` giống như bạn dặn dò CPU của bộ giáp: *"Cứ nhận hàng. Nếu anh ta cắm Kiếm (chuỗi Text) vào cũng cho qua. Nếu thọc Băng Đạn Pháo (con số) thì cũng chốt khóa."*. Nhưng tuyệt nhiên, thọc cái khác ví dụ như Gói Máu (Boolean) là chặn ngay ngoài cổng.

=== "💻 Tech Specs"

    ```typescript
    // Biến này chấp nhận 2 hình dạng
    let dauVaoVuKhi: string | number; 
    
    dauVaoVuKhi = "Kiếm Laze"; // OK
    dauVaoVuKhi = 50.5; // OK (Cỡ nòng)
    // dauVaoVuKhi = true; // LỖI COMPILER: Lệch cấu hình
    ```

### Bất Cập: Luật Giới Hạn Của Tập Giao

Khi đã xài Union Type, TS sẽ đứng ra bảo vệ bạn một cách hơi... cục súc. Nó phân tích: *Khẩu súng thì không có Lưỡi Dao. Cây Kiếm thì không có Băng Đạn. Vậy tao chỉ cho phép bấm những nút CÓ CHUNG TRÊN CẢ 2 VŨ KHÍ.* (Chỉ được phép sử dụng Common Properties).

```typescript
function kiemTraVuKhi(vuKhi: string | number) {
    // vuKhi.length; // LỖI: Thuộc tính 'length' kiếm độ dài Text (string), 'number' làm gì có!
    // vuKhi.toFixed(2); // LỖI: Text thì làm gì hiểu lệnh thu gọn số thập phân (number)!
    
    console.log(vuKhi.toString()); // ĐƯỢC PHÉP: Cả súng cả kiếm đều có hàm dịch chữ.
}
```

Để phá vỡ luật thô thiển này và xả láng skill đặc thù. Bạn phải trang bị **Nhãn Quan Chiến Thuật** (Type Narrowing) nhằm bật chế độ Mắt Đại Bàng quét hình láng xem cái gì đang nắm trong tay.

---

## 2. Type Narrowing: Các Giao Thức Quét Mục Tiêu

Hành động **Thu Hẹp Type** (Narrowing) là quá trình bóp nhỏ không gian mù mờ (`string | number`) chạy vào một khối Lệnh Vùng Xanh Tinh Khiết chỉ còn duy nhất 1 type.

### 2.1 Cảm Biến Cổ Điển: Gọi Hàm `typeof`

Hữu dụng khi cần quét dò vật liệu nguyên thủy Cơ bản (Primitive: string, number, boolean).

```typescript
function kichHoatVuKhi(dauVao: string | number) {
    // 👁 Quét Laze dò Cấu trúc
    if (typeof dauVao === "string") {
        // [Vùng Xanh Kiếm Khí]: Bên trong ngàm IF này, TS hiểu 100% dauVao = String
        // IntelliSense xô ra toàn bộ lịnh dành riêng cho Text.
        console.log(`Tấn công Kiếm khí: ${dauVao.toUpperCase()}`);
    } else {
        // [Vùng Xanh Súng Đạn]: Trừ điểm String, phần còn lại của Else dĩ nhiên là Number
        console.log(`Bắn Pháo Ray: ${dauVao.toFixed(2)} MJ`);
    }
}
```

### 2.2 Quét Phụ Tùng Đặc Trưng: Phép Thử `in`

Khi cầm trong tay những Cỗ Máy Khổng Lồ (Object) chứ không phải cục đá mẻ nguyên thủy (String). Hàm `typeof` sẽ rác rưởi vì nó quét Cỗ Máy nào cũng kêu tên chung là "Object". Lúc này, ta quét "Hình Dập Nổi Phụ Kiện".

```typescript
interface LuoiKiem { maiSac(): void; doBaoMon: number }
interface SungPhao { napDan(): void; soLuongDan: number }

function baoTri(thietBi: LuoiKiem | SungPhao) {
    // 👁 Mắt đại bàng lia tìm lỗ lẫy cắm đạn
    if ("napDan" in thietBi) {
        // TS hiểu: Chỉ có SungPhao mới có nạp đạn. 
        // Lập tức thu hẹp Type thành SungPhao.
        thietBi.napDan(); 
    } else {
        // Bóp chặt lại còn LuoiKiem
        thietBi.maiSac();
    }
}
```

---

## 3. Bản Vẽ Tối Thượng: Discriminated Unions

Nếu Vũ Khí Lai của bạn không rẽ 2 nhánh mà Mở 5-10 Chế Độ khác nhau? Dùng `in` hay `typeof` check từng cái sẽ khiến màng hình mù mịt rác rưởi của đống `if else` dây rợ lê thê.

Đây là lúc giăng bẫy **Mẫu Tagged Union (Discriminated Unions)**. Ở mỗi interface, ta đắp cho nó 1 bảng hiệu Huỳnh Quang Cố Định rực ánh sáng (chuỗi Literal cụ thể tên là `kind` hoặc `type`).

=== "🎭 Cyber-Metaphor"

    Thay vì hý hoáy ngắm xem đồ vật đó có gờ lồi hay gờ lõm, tại Xưởng sản xuất, ta đúc lên trán mỗi vũ khí một Chữ Nổi Dạ Quang: `CẬN_CHIẾN` hoặc `TẦM_XA`. Phi công chỉ việc lướt Switch bảng chữ, Hệ Điều Hành sẽ tự sang số. Gọn và Sang Trọng Tuyệt Đối.

=== "💻 Tech Specs"

    ```typescript
    interface CheDoKiem {
        kind: "can_chien"; // Biển báo Huỳnh Quang chết cứng
        doSac: number;
    }

    interface CheDoSung {
        kind: "tam_xa"; // Biển báo Huỳnh Quang chết cứng
        soDan: number;
    }

    type VuKhiLai = CheDoKiem | CheDoSung;

    function vanHanh(vuKhi: VuKhiLai) {
        // Switch/Case lia vào trúng tâm của "kind"
        switch (vuKhi.kind) {
            case "can_chien":
                // 100% Trở thành Sword
                console.log(`Vung kiếm. Độ sắc bén: ${vuKhi.doSac}`);
                break;
            case "tam_xa":
                // 100% Trở thành Gun
                console.log(`Khai hỏa. Đạn còn: ${vuKhi.soDan}`);
                break;
        }
    }
    ```

---

## 4. Kiểm Tra Tận Tuyệt (Exhaustiveness Checking)

Sẽ thế nào nếu 1 tháng sau, kỹ sư cập nhật thêm bản vẽ Vũ Khí Lai: `interface CheDoKhien { kind: "phong_thu" }` nhét vào `type VuKhiLai`. Lúc rúc đầu vào hầm ngầm gõ code, bạn Quên Khuấy cập nhật Hầm Chứa switch-case bắt loại vũ khí thứ 3. 

Một kẻ hở chết trôi. Lúc rút Khiên ra, bạn không có Hàm điều khiển nó -> Runtime Crash nhảm nhí. 

**Vá Lỗ Bằng Vực Sâu `never`**: Mặc định, nếu TS lướt hết các Case được chỉ đích. Nó sẽ vứt cái xác của Object còn tàn tích chạy tụt tuốt luốt vào ngăn `default`. Ngay tại Default, ta nhét hàm kiểm định bắt trói kiểu bằng Dây Thừng Khóa Tử Ngữ `never`.

```typescript
function vanHanhAnToan(vuKhi: VuKhiLai) {
    switch (vuKhi.kind) {
        case "can_chien": /* Xử Lý Kiếm */ break;
        case "tam_xa":    /* Xử Lý Súng */ break;
        default:
            // 🚨 NẾU BỎ QUÊN "phong_thu", vụKhi ở đây còn Sống Mạng mang Type CheDoKhien
            // Ném CheDoKhien gán đè lên Kiểu "never" (Kiểu rỗng ko bắt chứa) -> TS Rằng HÉ LÊN LỖI COMPILE!
            const _kiemTraToanDien: never = vuKhi;
            return _kiemTraToanDien;
    }
}
```

Thắng Lợi Toàn Diện! Cái chết tại Compile-Time (Màu Đỏ Khét) cứu cái mạng Phi Công giữa chiến trường chớp nhoáng (Vụ Nổ Runtime-Time). 

> **Điều cốt lõi:** Đây là đẳng cấp phân chia ranh giới giữa một Tân binh và một Cyber-Shogun lọc lõi. Đã dùng Union - Buộc dùng Narrow Switch quét cạn bã rác với Bẫy Never Dưới Đáy Phễu!
> 
> **Nhiệm vụ tiếp theo:** Bạn đã nắm trong tay hệ thống vũ khí đa hình. Nhưng cuộc nội chiến về lõi thiết kế vũ khí vẫn đang diễn ra. Hãy tiến vào [Module 06: Nội Chiến Kiến Trúc](./6.md) để chọn phe phái cho riêng minh.
