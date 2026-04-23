---
title: "TypeScript Module 01: Lò Phản Ứng & Phân Hệ Cốt Lõi"
source: "raw/misc/ts/1.md"
date_added: 2026-04-23
tags: [typescript, basic-types, compiler, cyber-shogun]
aliases: []
status: draft
summary: "Hướng dẫn khởi động tsc (Nanoforge) và làm chủ các kiểu dữ liệu cơ bản (Basic Types) trong TypeScript."
---

# :material-tools: Module 01: Lò Phản Ứng & Phân Hệ Cốt Lõi

Khái niệm "Type Annotations" (Chú thích kiểu) hay "Static Typing" (Định kiểu tĩnh) không chỉ là những dòng code thêm vào cho có. Đó là các giao thức bảo vệ để bạn sinh tồn trong Runtime Wasteland (JavaScript nguyên bản).

Chúng ta sẽ tìm hiểu cách máy biên dịch `tsc` đúc ra code JS an toàn, và cách phân tích 5 hệ thống phòng thủ cơ bản nhất: **String, Number, Boolean, Any, Void**.

---

## 1. Kiến Tạo Lò Phản Ứng Nano (`tsc`)

JavaScript là vật liệu thô – linh hoạt nhưng mềm yếu. TypeScript là bản thiết kế hợp kim siêu cứng. Trình biên dịch `tsc` (TypeScript Compiler) chính là cỗ máy rèn đúc (Nanoforge) biến bản thiết kế đó thành thực tại thông qua quá trình **Type Erasure** (Loại bỏ kiểu).

=== "🎭 Cyber-Metaphor"

    > **Thiết lập Nanoforge**
    >
    > 1. **Kích hoạt Lò phản ứng:** Node.js (Core Reactor) cung cấp năng lượng.
    > 2. **Triệu hồi Nano-bot:** `npm install -g typescript`
    > 3. **Hiệu chỉnh Phác đồ:** `tsc --init` tạo ra `tsconfig.json` - quy định độ cứng của giáp.
    > 4. **Rèn đúc:** Chạy `tsc main.ts`. Lớp vỏ định kiểu (Type) sẽ sáng lên rồi tan biến (Type Erasure), chắt lọc ra thanh hợp kim JavaScript sắc bén nhất.

=== "💻 Tech Specs"

    **Vấn đề Kỹ thuật:** TypeScript *không* chạy trên trình duyệt hay Node.js. Nó là ngôn ngữ Transpiled.

    ```bash
    # 1. Cài đặt TypeScript global
    npm install -g typescript

    # 2. Khởi tạo cấu hình TS (tạo tsconfig.json)
    tsc --init

    # 3. Biên dịch file TS sang JS thủ công
    tsc main.ts
    ```

    !!! danger "Lưu ý quan trọng: Type Erasure"
        Các Type, Interface trong TypeScript **sẽ bị xóa sạch** sau khi build. Chúng không tồn tại lúc runtime. Đừng nhầm lẫn việc kiểm tra type với việc chạy code!

---

## 2. String: Dòng Dữ Liệu Hologram

=== "🎭 Cyber-Metaphor"

    !!! info "Giao Thức Liên Lạc (Data Streams)"
        Trong mũ giáp, `String` không chỉ là văn bản. Nó là mã lệnh giao tiếp hiện lên mặt kính HUD chữ xanh `Neon Cyan`.

        Template Literals (dấu backtick `` ` ``) chính là các **Khe cắm Module**. Khi báo tọa độ cho đồng đội, biến số bay vào vị trí `${}` và khớp lại với tiếng "click" cơ khí thỏa mãn. Ráp sai module sẽ bị hệ thống báo lỗi ngay lập tức.

=== "💻 Tech Specs"

    Trong JS, chuỗi rất dễ gây lỗi nếu đem cộng với số (vd: `"Sector " + 7`). Trong TypeScript, `string` ép kiểu chặt chẽ từ dòng code đầu tiên.

    ```typescript
    // Khai báo rõ ràng đây là dữ liệu văn bản
    let sector: string = "7";

    // Sử dụng Template Literal an toàn tuyệt đối
    let message: string = `Approaching Sector ${sector}`;

    // Báo lỗi ngay lập tức ở lúc viết code (Compile time)
    // message = 100; // Error: Type 'number' is not assignable to type 'string'
    ```

---

## 3. Number: Hệ Thống Đo Đạc (Telemetry)

=== "🎭 Cyber-Metaphor"

    !!! warning "Chỉ Số Năng Lượng (Energy/Ballistics)"
        Sự chính xác của `Number` quyết định sống còn. Việc tính toán sai lệch quỹ đạo đạn sẽ làm vũ khí kẹt hoặc nổ tung.
        Nếu bạn cố tình nạp đạn bằng "chữ" (Text) vào súng, màn hình HUD sẽ nhấp nháy đỏ rực kèm cảnh báo:
        *TYPE MISMATCH: CANNOT LOAD TEXT INTO BALLISTICS CALCULATOR.*

=== "💻 Tech Specs"

    JS quy mọi số về IEEE 754 floating point. TypeScript bảo vệ tính toàn vẹn toán học bằng việc khóa kiểu biến ở dạng `number` (hỗ trợ cả int, float, hex, binary).

    ```typescript
    let ammoCount: number = 250;
    let shieldIntegrity: number = 98.5;
    let hexKey: number = 0xf00d; // Hỗ trợ hệ thập lục phân

    // Tự tin làm toán mà không sợ Type Coercion kỳ quặc của JS
    let currentPower: number = ammoCount + shieldIntegrity;

    // ammoCount = "Empty"; // Báo lỗi: không thể truyền string vào number
    ```

---

## 4. Boolean: Tính Năng Nhận Diện (IFF Toggles)

=== "🎭 Cyber-Metaphor"

    !!! success "Hệ Thống An Toàn (Safety Switches)"
        Công tắc gạt ảo trên HUD.
        Màu **Xanh lá (true)**: Hệ thống vũ khí Online.
        Màu **Đỏ (false)**: Khóa an toàn / Tàng hình.
        Nếu công tắc lỏng lẻo, bạn nhấn nhầm nút "0" hoặc "" (falsy trong JS gốc), khiên năng lượng có thể tắt phụt ngay giữa trận.

=== "💻 Tech Specs"

    Boolean trong TS chỉ thuần túy nhận `true` hoặc `false`, diệt trừ tận gốc các lỗi so sánh lỏng lẻo do Truthy/Falsy của JavaScript tạo ra.

    ```typescript
    let isShieldsUp: boolean = true;
    let isEngaged: boolean = false;

    if (isShieldsUp) {
        console.log("An toàn.");
    }

    // JS cho phép, nhưng TS sẽ cấm:
    // isShieldsUp = 1; // Error: Type 'number' is not assignable to type 'boolean'.
    ```

---

## 5. Any: Giao Thức Cuồng Nộ (The Berserk Protocol)

=== "🎭 Cyber-Metaphor"

    !!! danger "CHẾ ĐỘ CUỒNG NỘ: KÍCH HOẠT"
        Dùng `Any` nghĩa là bạn vứt bỏ bộ giáp bảo vệ. Màn hình HUD bị nhiễu (Glitch), chuyển đỏ báo động. Thông báo chớp tắt: **SAFETY PROTOCOLS DISABLED**.
        Bạn có thể code cực nhanh, nhưng hệ thống radar cảnh báo rủi ro xung quanh đã tắt ngúm. Một đòn chí mạng Runtime Error có thể kết liễu bạn lúc nào không hay.

=== "💻 Tech Specs"

    `any` là con dao hai lưỡi. Nó tắt hoàn toàn quá trình Type Checking của TS, đưa code trở về JS thông thường. Đừng bao giờ lạm dụng cấu trúc này trừ khi bạn thực sự phải làm việc với các hệ thống legacy hoặc dữ liệu thô chưa rõ hình thù.

    ```typescript
    let unknownEntity: any = "Biến hình";

    unknownEntity = 42; // Vượt rào thành công
    unknownEntity = true; // Vượt rào thành công

    // Dù không tồn tại, trình biên dịch vẫn nhắm mắt cho qua!
    // Nhưng TẠI RUNTIME SẼ CRASH!
    // unknownEntity.flyToTheMoon();
    ```

---

## 6. Void: Giao Thức Xả Nhiệt (Venting Protocols)

=== "🎭 Cyber-Metaphor"

    !!! quote "Lệnh Xả Nhiệt"
        Khi Ronin ra lệnh "Khởi động bộ đẩy" (`activateThrusters()`), năng lượng cháy bừng, phản lực đẩy vọt lên. Hàm này chỉ thực thi thao tác, không trả lại bất cứ vật thể nào.
        Giống như bắn một viên đạn: Đạn bay đi, chứ đạn không găm ngược trở lại tay người bắn. Lệnh báo **EXECUTION COMPLETE**.

=== "💻 Tech Specs"

    `void` thường dùng để định nghĩa giá trị trả về của hàm không có dữ liệu trả về (thường chứa thao tác bên lề `side-effects` như ghi log, đổi DOM...).

    ```typescript
    // Hàm này chỉ thực hiện công việc, không có lệnh return giá trị dữ liệu
    function logCombatData(enemyName: string): void {
        console.log(`Đã lưu dữ liệu chiến đấu của ${enemyName} vào hộp đen.`);
        // return 123; // Error: Type 'number' is not assignable to type 'void'.
    }

    logCombatData("Scavenger_01");
    ```

---

> **Nhiệm vụ tiếp theo:** Bạn đã học cách tạo Lò phản ứng `tsc` và gắn 5 mô-đun sinh tồn. Trạm tiếp theo: [Module 02: Khung Giáp Exosuit (OOP)](./2.md) để đúc lớp vỏ bảo vệ.
