---
title: "TypeScript Module 02: Khung Giáp Exosuit (OOP)"
source: "raw/misc/ts/2.md"
date_added: 2026-04-23
tags: [typescript, oop, access-modifiers, cyber-shogun]
aliases: []
status: draft
summary: "Thiết kế Lập Trình Hướng Đối Tượng (OOP) và cơ chế phòng thủ Access Modifiers của Exosuit trong TypeScript."
---

# :material-shield-link-variant: Module 02: Khung Giáp Exosuit (OOP)

> "*Chúng ta không viết mã chỉ để chạy; chúng ta viết mã để tồn tại.*" – **Cyber-Shogun**

Trong chiến trường Runtime Wasteland đầy rủi ro, một hàm (function) hay một cục dữ liệu rời rạc là quá yếu ớt. **Class** (Lớp) không đơn thuần là bản thiết kế đối tượng OOP; nó là cấu trúc cho **Exosuit** (Bộ giáp cơ khí) – đơn vị chiến đấu cơ bản nhất. 

Bài viết này phân tích sâu về Tính Đóng Gói (Encapsulation) bằng cách sử dụng các Bổ từ Truy Cập (Access Modifiers). Đây không chỉ là "từ khóa code", mà là các cấp độ an ninh quân sự sinh tử.

---

## 1. Class: Bản Vẽ Kỹ Thuật & Khung Xương

Constructor đóng vai trò là "Giao Thức Lắp Ráp" (Assembly Protocol) – chuỗi khởi động đưa bộ giáp từ tĩnh sang trạng thái sẵn sàng chiến đấu. 

=== "🎭 Cyber-Metaphor"

    Khi lệnh `new CyberSamurai()` kích hoạt, nhà máy (Memory) sản xuất một bản thể duy nhất với hệ thống nội tạng độc quyền. Nếu thiếu giáp che chở, một đồng minh kém năng lực hoặc mã độc (malware) có thể thò tay thẳng vào tim phi công để đổi nhịp độ đập. Chúng ta cần phải hàn chặt các Tấm Giáp phân quyền quanh bộ khung xương này.

=== "💻 Tech Specs"

    ```typescript
    class CyberSamurai {
        // Thuộc tính
        designation: string;
        modelType: string;

        // Constructor: Giao Thức Lắp Ráp
        constructor(name: string, model: string) {
            this.designation = name;
            this.modelType = model;
            this.bootSequence();
        }

        bootSequence(): void {
            console.log("Hệ thống giáp khởi động...");
        }
    }

    // Tạo bản thể (Instance) mới
    const ronin = new CyberSamurai("Ghost_01", "Assault");
    ```

---

## 2. Public: Điểm Cứng & Giao Diện Ngoại Vi

=== "🎭 Cyber-Metaphor"

    !!! info "Lớp Giáp Ngoại Vi (External Hardpoints)"
        Mọi `public` modifier tương đương với Điểm Gắn Vũ Khí (Muzzle), ăng-ten liên lạc, cờ hiệu sau lưng Ronin. 
        Mọi người đều thấy nó. Kẻ thù có thể chém vào nó. Đồng minh có thể giao tiếp qua nó. Sự minh bạch là cần thiết, nhưng phơi bày quá nhiều là tử huyệt.

=== "💻 Tech Specs"

    Cấu hình mặc định của TypeScript (như JS) là `public`. 
    **Tầm nhìn:** Có thể truy cập mọi nơi (Tạo instance xong xài được ngay).

    ```typescript
    class Exosuit {
        // Radar ngoài, ai cũng có thể ping
        public callSign: string; 

        constructor(sign: string) {
            this.callSign = sign;
        }

        // Tương tác ngoại vi: Bóp cò súng
        public engageTarget(): void {
            console.log(`[${this.callSign}] Khai hỏa!`);
        }
    }

    const mech = new Exosuit("Alpha-1");
    mech.engageTarget(); // Hợp lệ, public mà!
    ```

---

## 3. Private: Mạch Thần Kinh Nội Bộ

=== "🎭 Cyber-Metaphor"

    !!! warning "Hệ Thống Nội Tại Dễ Bay Hơi"
        Nhịp tim phi công, Nhiệt độ Lò phản ứng nhiệt hạch. Bộ giáp CẦN biết để vận hành. Nhưng thằng bạn đứng cạnh **tuyệt đối không được quyền** chạm chĩa vào để điều chỉnh thanh làm mát của bạn.

        **Ảo ảnh của `private`**: Đây là tấm biển dán trên vỏ giáp ghi chữ "CẤM SỜ". Giới quý tộc (Trình biên dịch TSC) tuân thủ luật lệ này. Nhưng lũ Scavengers (Hacker dùng JS tại Runtime) hoàn toàn có thể bóc biển bạo lực thò tay vào.

=== "💻 Tech Specs"

    `private` chỉ **KIỂM TRA TẠI THỜI ĐIỂM BIÊN DỊCH** (Compile-time).
    **Tầm nhìn:** Chết đứng trong Class, cấm ngặt truy cập từ ngoài hay Subclass.

    ```typescript
    class Exosuit {
        // Tấm biển "Cấm sờ"
        private _fusionCoreTemp: number = 2000;

        private ventPlasma(): void {
            console.log("Xả nhiệt khẩn cấp!");
        }

        public regulateSystem(): void {
            if (this._fusionCoreTemp > 5000) this.ventPlasma();
        }
    }

    const suit = new Exosuit();
    // suit._fusionCoreTemp = 6000; // LỖI COMPILER: Thuộc tính private!
    
    // NHƯNG khi dịch ra JS thông thường, nó lại hợp lệ: 
    // suit._fusionCoreTemp = 6000; (JS runtime chằng quan tâm biển cấm).
    ```

---

## 4. #Private: Chế Độ Tàng Hình Tuyệt Đối

=== "🎭 Cyber-Metaphor"

    !!! danger "Đóng Gói Hộp Đen Bọc Chì (Stealth Mode)"
        Đây mới là sự bảo vệ hàng thật. Một khối dữ liệu tàng hình, hoàn toàn bất khả xâm phạm tại Runtime. Dành riêng cho Mã khóa An ninh, Token điều lệnh. Ngay cả khi Radar đối phương (Inspect) lướt qua, nó cũng vô hình.

=== "💻 Tech Specs"

    Dùng cú pháp `#` (Chuẩn ECMAScript) thay vì chữ `private` của TS. Dữ liệu này **THỰC SỰ KHÓA KÍN TẠI RUNTIME** trên engine JS V8. Lỗi syntax sẽ quăng thẳng mặt kẻ truy lậu.

    ```typescript
    class StealthSuit {
        // Cú pháp ECMAScript Hard-Private
        #encryptionKey: string; 

        constructor(key: string) {
            this.#encryptionKey = key;
        }

        public decrypt(msg: string) {
            return `Decrypted with ${this.#encryptionKey}`;
        }
    }

    const ninja = new StealthSuit("XYZ999");
    // console.log(ninja.#encryptionKey); // SyntaxError Lập Tức! Không ai đọc được!
    ```

---

## 5. Protected: Công Nghệ Gia Tộc

=== "🎭 Cyber-Metaphor"

    !!! success "Bí Kíp Võ Đường (Clan Tech)"
        Một bản vẽ thiết kế Thủy lực chung (BaseArmor) có bí quyết nén dầu riêng. Cha (Base Class) chia sẻ nó cho Con (HeavyArmor, LightArmor) để Con sáng tạo tiếp trên nền tảng đó. 
        NHƯNG, bí kíp tuyệt đối KHÔNG lọt ra tay kẻ ngoại đạo (Cấm truy cập từ instance bên ngoài).

=== "💻 Tech Specs"

    **Tầm nhìn:** Vừa truy cập được trong Class cha, VỪA kế thừa dùng được trong Class con (Extends).

    ```typescript
    class BaseArmor {
        // Secret của dòng họ Armor
        protected armorIntegrity: number = 100; 
    }

    class HeavyArmor extends BaseArmor {
        public reinforce(): void {
            // Con nối nghiệp dùng đồ nghề của Cha
            this.armorIntegrity += 50; 
            console.log(`Độ bền tăng lên: ${this.armorIntegrity}`);
        }
    }

    const unit = new HeavyArmor();
    unit.reinforce(); // Hợp lệ, gọi hàm public
    // unit.armorIntegrity = 0; // LỖI! Kẻ ngoại đạo không được chạm vào.
    ```

---

## 6. Readonly: Niêm Phong Nhà Máy

=== "🎭 Cyber-Metaphor"

    !!! quote "Con Dấu Niêm Phong (Factory Sealed)"
        Số Serial Nhà Sản Xuất, Tải Trọng MAX. Những thông số được khắc Laze thủ công vào thẳng ROM (Read-Only Memory). Không một thế lực nào trên chiến trường làm mờ đi những vết khắc danh tính này.

=== "💻 Tech Specs"

    Thuộc tính TĨNH. Sau vòng đời Constructor xong xuôi, cấm chỉ định ghi đè lại suốt phần đời còn lại.

    ```typescript
    class Exosuit {
        // Khắc laze không cho đổi
        public readonly serialNumber: string;

        constructor(id: string) {
            this.serialNumber = id; // Hợp lệ: Lúc đúc trong lò được gán 1 lần
        }

        public updateFirmware() {
            // this.serialNumber = "Hacked-ID"; // LỖI HIỂN NHIÊN! Bị niêm phong rồi!
        }
    }
    ```

---

## :material-shield-star: Bảng Tổng Hợp An Ninh & Tôn Chỉ

Tóm tắt quyền hạn bảo vệ của bộ giáp của bạn:

| Cấp Độ Bảo Vệ | Ẩn Dụ Cyber | Được Dùng Trong Class | Được Dùng SubClass | Gọi Từ Ngoài Instance | Bảo Vệ Lúc Chạy (JS) |
|---|---|:---:|:---:|:---:|:---:|
| `public` | Điểm Cứng Ngoại Vi | :material-check: | :material-check: | :material-check: | :material-close: |
| `protected` | Công Nghệ Gia Tộc | :material-check: | :material-check: | :material-close: | :material-close: |
| `private` (TS) | Tấm Biển "Cấm Sờ" | :material-check: | :material-close: | :material-close: | :material-close: |
| `#private` (JS) | Hộp Đen Tàng Hình | :material-check: | :material-close: | :material-close: | :material-check: (An toàn JS)|
| `readonly` | Niêm Phong Máy | :material-check: | :material-check:* (chỉ đọc) | :material-check:* (chỉ đọc) | :material-close: |

**Bộ Luật Ranh Giới (Principle of Least Privilege)**
Luôn thiết kế mặc định mọi thuộc tính là `#private` hoặc `private`. Chỉ nới lỏng ra `protected` khi BẠN MUỐN có hệ gen Subclass kế thừa. Chỉ nhả ra lưới ngoài `public` khi thật sự cần cái Cổng tương tác.

> **Nhiệm vụ tiếp theo:** Bộ giáp đã vững chãi. Đã đến lúc chúng ta cài đặt [Hệ Điều Hành Trung Tâm (tsconfig)](./3.md) để quy định luật tiến hóa vật lý chung cho toàn bộ môi trường.
