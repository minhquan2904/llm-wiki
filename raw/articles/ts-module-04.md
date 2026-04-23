---
title: "TypeScript Module 04: Lò Rèn Kỹ Thuật (Functions)"
source: "raw/misc/ts/4.md"
date_added: 2026-04-23
tags: [typescript, functions, void, never, cyber-shogun]
aliases: []
status: draft
summary: "Nghiên cứu giải phẫu cấu trúc Hàm (Functions), Optional Parameters và định nghĩa kiểu trả về void/never trong TypeScript."
---

# :material-anvil: Module 04: Lò Rèn Kỹ Thuật (Functions)

> *"Viết code không đơn thuần là gõ phím; đó là quá trình rèn đúc logic. Kỷ luật ở khâu đầu vào quyết định sự vĩ đại của thành phẩm."* – **Cyber-Shogun**

Trong hệ sinh thái TypeScript, hàm (function) là đơn vị dây chuyền sản xuất cơ bản nhất. Khác với JavaScript thuần túy — nơi các tham số (parameters) là thùng rỗng vô định lỏng lẻo chấp nhận mọi rác rưởi quăng vào — TypeScript thiết lập các **Lò Rèn Kỹ Thuật** với bản hợp đồng dung sai bằng 0. Khi dữ liệu đi vào, nó phải đúng chuẩn.

---

## 1. Giải Phẫu Học Hàm Định Kiểu (Typed Functions)

Nhiệm vụ đầu tiên của Cyber-Shogun là ràng buộc tuyệt đối Đầu Vào (Input) và Đầu Ra (Output). Tại sao ư? Bởi vì thả lỏng đầu vào cho một thợ rèn sẽ tạo ra thảm họa. 

=== "🎭 Cyber-Metaphor"

    !!! warning "Hệ Thống Phễu Lọc"
        Hãy tưởng tượng Lò phản ứng Nanoforge của bạn. Bạn muốn rèn một thanh Katana từ Titanium. Nếu hệ thống cho phép "Bất kỳ vật liệu nào" (Any), một tân binh có thể ném một cục móp nhựa dẻo vào. Lò vẫn rèn, nhưng thanh kiếm tạo ra sẽ đứt gãy ngay nhát chém đầu tiên giữa chiến trường (Runtime Error). TS khóa chết miệng Lò: Gọi sai vật liệu? **Kích hoạt tự động khóa, Lỗi Compile.**

=== "💻 Tech Specs"

    Dưới đây là một hàm phân xưởng không định kiểu trong JS, cực kỳ vô trách nhiệm:
    
    ```javascript
    // (BẮT ĐẦU JS) Lỏng lẻo, vatLieu mang type 'any' ngầm định
    function cheTaoVuKhi(vatLieu) {
        return "Đang rèn vũ khí từ " + vatLieu; 
    }
    ```

    Trong TS, chúng ta phải Chú Thích Tường Minh (Explicit Annotations) cả tham số lẫn vật phẩm trả về:

    ```typescript
    // (BẮT ĐẦU TS) Kỷ luật quân đội
    // vatLieu phải là chuỗi ký tự :string
    // Hàm này cam kết sẽ trả lại một chuỗi ký tự :string
    function cheTaoVuKhi(vatLieu: string): string {
        return `Tiến trình: Đang rèn vũ khí từ ${vatLieu}`;
    }

    let sword = cheTaoVuKhi("Titanium"); // Khớp hoàn hảo.
    // let gun = cheTaoVuKhi(999); // LỖI COMPILER: 'number' không thọt được vào lỗ 'string'
    ```

---

## 2. Thiết Kế Tùy Biến: Optional & Default Parameters

Trong thực chiến, một khẩu súng có thể không cần thiết phải lắp kèm Ống ngắm quang học, hoặc áo giáp có một lớp khiên mặc định nếu phi công không yêu cầu gia cố.

### 2.1 Tham Số Tùy Chọn (Optional `?`)

=== "🎭 Cyber-Metaphor"

    !!! info "Khe cắm phụ kiện (Optional Slot)"
        Dấu `?` đánh dấu đây là một Khe Cắm Mở. Phi công có quyền cắm Bùa Chú cường hóa hoặc bỏ trống. Tuy nhiên, Lò rèn sẽ tự động hiểu rằng nếu bỏ trống, giá trị bên trong sẽ là Không Khí (undefined). Do đó, phi công bắt buộc phải móc máy quét ra IF kiếm tra: *“Khe này có đồ không?”* trước khi truyền năng lượng vào, nếu không sẽ chập điện.

=== "💻 Tech Specs"

    Khi gắn `?`, TypeScript **tự động** ép kiểu tham số đó thành một dạng lai `Type | undefined`. Nó ép dev bạn phải xử lý cả tình huống giá trị bị bỏ quên.

    ```typescript
    function cuongHoaVuKhi(id: number, buaChu?: string): void {
        // BAT BUỘC KIỂM TRA vì buaChu có thể là undefined
        if (buaChu) {
            console.log(`Vũ khí ${id} được cường hóa bởi [${buaChu.toUpperCase()}]`);
        } else {
            console.log(`Vũ khí ${id} hoạt động ở trạng thái cơ sở.`);
        }
    }

    cuongHoaVuKhi(12); // Không truyền buaChu -> Vẫn chạy tốt.
    cuongHoaVuKhi(45, "Lửa Địa Ngục"); 
    ```

### 2.2 Tham Số Mặc Định (Default Values)

Thay vì để trống `undefined`, chúng ta nhét sẵn một linh kiện dự phòng vào đó. Đây là cách thiết lập cấu hình Baseline hoàn hảo cho Người Dùng.

```typescript
// Nếu phi công không chọn độ thu phóng ngắm, hệ thống tự cấp kính ngắm 1.5x
function hieuChinhOngNgam(doPhongDai: number = 1.5): number {
    return doPhongDai * 100; // Trả về tỷ lệ tiêu cự ngắm
}

let aim1 = hieuChinhOngNgam(); // Sử dụng đồ Default: 1.5
let aim2 = hieuChinhOngNgam(4.0); // Override lên đồ Xịn: 4.0
```

---

## 3. Cổng Xả & Vực Sâu: Phân Tích Sự Trống Rỗng (`void` vs `never`)

Nhiều tân binh TS nhầm lẫn giữa một hành động "Cứ làm đi, khỏi báo cáo" và một hành động "Làm xong thì cả cái System đổ sập".

=== "💨 Void: Lệnh Xả Nhiệt"

    Sử dụng khi Hàm thực hiện xong một Tác Vụ (Side-effect: Đổi UI, Nhả log Console) nhưng không trả về bất cứ Giá Trị Tái Chế nào (return data) về cho chuỗi sản xuất tiếp theo.
    
    > **Ẩn Dụ:** Mở van áp suất để khói nhiệt đùn ra. Xả xong là xong.
    
    ```typescript
    function ghiNhatKyRen(trangThai: string): void {
        console.log(`[LOG LÒ RÈN]: ${trangThai}`);
        // Không có return giá trị ở đây
    }
    ```

=== "💥 Never: Nút Kích Nổ Fatal Error"

    Khái niệm này CỰC KỲ KHÓ, đại diện cho những giá trị **Tuyệt Đối Không Thể Nào Sinh Ra Được**. Hàm trả về `never` là một Cửa Ngõ Không Thể Quay Lại. Hàm chứa Vòng Lặp Bất Tận (While True) hoặc Hàm ném Báo Động Đỏ (Throw Error) đập chết toàn bộ tiến trình.
    
    > **Ẩn Dụ:** Tự Hủy Cuộn Lõi Hạt Nhân. Không ai biết chuyện gì xảy ra sau vụ nổ, vì Runtime ở đó đã kết liễu.
    
    ```typescript
    function loiHeThongNghiemTrong(lyDo: string): never {
        // App sẽ crash ngang tại đây, không có lệnh chạy nào phía dưới hàm này được thực thi.
        throw new Error(`CẢNH BÁO HƯ HỎNG: ${lyDo}`);
    }
    ```

> **Nhiệm vụ tiếp theo:** Lò Rèn đã luyện thành thục những vũ khí cấu trúc ổn định. Nhưng chiến trường khốc liệt cần nhiều hơn thế. Chúng ta tiến về [Bước 5: Chế Tạo Vũ Khí Lai Sinh Học](./5.md) với quyền năng Union Type!
