---
title: ":material-file-tree: Virtual DOM vs Real DOM: Bí mật đằng sau hiệu năng gốc của React"
source: "D:\9. Learn\12. llm wiki\raw\articles\react\3.md"
date_added: 2026-04-24
tags: [articles]
status: draft
summary: ""
---

# :material-file-tree: Virtual DOM vs Real DOM: Bí mật đằng sau hiệu năng gốc của React

!!! abstract "Thông tin bài học"
    - **Series**: React Core · **Bài số**: 3
    - **Độ khó**: Beginner :material-arrow-right: Intermediate
    - **Thời gian**: ~15 phút
    - **Stack**: React 18, JavaScript, DOM API

---

Khi học React, một trong những thuật ngữ đầu tiên bạn sẽ nghe đến là **Virtual DOM** (DOM Ảo). Nhưng tại sao nó lại tồn tại? Nó giải quyết vấn đề gì mà khiến React trở thành công cụ kiến tạo UI phổ biến hàng đầu thế giới?

Hãy cùng đi tìm câu trả lời từ gốc rễ vấn đề.

## 1. Nỗi đau của Real DOM: Vấn đề nằm ở đâu?

Cần phải làm rõ một hiểu lầm phổ biến: **Bản thân thao tác truy xuất phần tử DOM (như `document.getElementById`) không hề chậm**. Nó xử lý nhanh tương đương với việc bạn chọc vào một Object thông thường trong JavaScript.

Vậy cái gì làm web chậm đi? **Đó là những gì xảy ra sau khi cấu trúc DOM bị sửa đổi.**

Mỗi một lần cấu trúc DOM thay đổi (thêm, bớt thẻ HTML, thay đổi kích thước, vị trí từ CSS), trình duyệt sẽ phải trải qua một quy trình vô cùng phức tạp và tốn kém gọi là quá trình hiển thị vòng đời trình duyệt (**Browser Rendering Pipeline**):

1. **DOM Tree**: Cập nhật lại những thay đổi lên cấu trúc cây HTML.
2. **Render Tree**: Nhào nặn lại qua bộ quy tắc CSS.
3. **Layout (Reflow)**: Tính toán lại kích thước và vị trí hình học của **TẤT CẢ** các thành phần trên màn hình để sắp đặt nó đúng chỗ mới. Chỉ cần một phần tử thay đổi kích thước, các phần tử xung quanh đều có rủi ro bị dịch chuyển theo.
4. **Paint (Repaint)**: Vẽ lại từng pixel lên màn hình để hiển thị thay đổi mới đó.

> 🛠️ **Ẩn dụ:** Hãy tưởng tượng **Real DOM** giống như việc xếp những hạt cườm nhỏ bằng tay tạo thành một bức tranh to trên sàn nhà. Giờ bạn muốn chèn thêm một hạt cườm vào giữa. Nếu làm đúng cách (tối ưu manual), bạn nhấc rất nhẹ 1 hạt ra rồi đặt 1 hạt vào. Nhưng cách xử lý thông thường của hệ thống Real DOM lại là "vứt toàn bộ mảng tranh quanh chỗ đó đi, xếp hạt cườm vòng quanh đó lại từ đầu cho khớp lại với nhau" (Reflow/Repaint). Cực kỳ tốn kém công sức và thời gian nếu bạn bắt hệ thống làm vậy liên tục với hàng chục, hàng trăm thao tác nối tiếp nhau!

**Ví dụ tệ nếu code Vanilla JS không được tối ưu theo khối:**

```javascript
const list = document.getElementById('my-list');

// Bạn muốn cập nhật thêm 3,000 thẻ item vào danh sách.
// Mỗi lần thực thi vòng lặp add 1 item tạo ra 1 thao tác rời rạc => Browser bắt buộc phải render đi render lại (reflow) hàng ngàn lần.
for (let i = 0; i < 3000; i++) {
  const li = document.createElement('li');
  li.innerText = `Item ${i}`;
  list.appendChild(li); 
}
```

---

## 2. Giải pháp: Virtual DOM - Tầng đệm chiến lược

### Virtual DOM là gì?

**Virtual DOM** (DOM ảo) không chạy bằng năng lượng phép thuật cao siêu nào cả. Cốt lõi nó thực chất chỉ là **một bản sao nháp (Blueprint)** của cây Real DOM. Cây bản nháp này được biểu diễn chuẩn hóa dưới dạng các **JavaScript Object** vô cùng nhẹ nhàng, mỏng dính và được đặt sẵn trong bộ nhớ trong (In-memory - ví dụ RAM của máy vi tính / điện thoại).

Ví dụ, một cấu trúc thẻ `<div>` trên Real DOM sẽ được React biểu diễn lại thành một Virtual DOM Object trông như thế này:

```javascript
// Virtual DOM đơn giản chỉ là khối dữ liệu cấu trúc
const virtualDiv = {
  type: 'div',
  props: {
    className: 'container'
  },
  children: ['Hello React!']
}
```

### Cơ chế hoạt động: Bộ đôi Diffing và Batching

React đưa Virtual DOM làm tầng đệm để giải quyết "Nỗi đau Real DOM" thông qua quy trình 3 bước cốt lõi:

#### Bước 1: Khởi tạo/Render lại bản nháp
Mỗi khi dữ liệu cục bộ (`state`) hoặc dữ liệu truyền vào (`props`) của một Component bị đổi khác đi, thay vì lao thẳng ngay vào Real DOM để xử lý, React sẽ tạo mới ra một cây quy chiếu Virtual DOM từ sự thay đổi trên.
Công việc này diễn ra **chớp nhoáng** vì Javascript tạo Object lên RAM thì cực kỳ nhanh nhạy (hoàn toàn không dính líu hay kích hoạt tới Reflow hay Repaint bên ngoài).

#### Bước 2: Diffing (Thuật toán Tìm vết xước)
Ngay lúc này, React có 2 phiên bản bản nháp: Cây **DOM ảo Cũ** và Cây **DOM ảo Mới**. 
React áp dụng ngay thuật toán tìm điểm khác biệt **Diffing (độ phức tạp O(n))** để quét và so sánh hai cây. Cỗ máy nhẩm tính: *"Mọi thẻ xung quanh đều y nguyên, chỉ duy nhất cái hộp văn bản `Input` này bị gõ thêm ký tự 'A' mới vào, và màu viền nó đang chuyển sang đỏ"*. 

#### Bước 3: Reconciliation & Batching (Đóng gói thao tác)
Tiếp theo, React thu thập (Batching) tất cả các thay đổi siêu nhỏ dồn cục lại thành một "Gói cập nhật nhất thống" (Reconciliation). React cuối cùng sẽ cử duy nhất một gói mệnh lệnh tối ưu nhất gửi xuống hệ thống **Real DOM**.
Đến đây, trình duyệt chỉ nhận duy nhất 1 yêu cầu thao tác cuối cùng nên nó chỉ bắt buộc phải chịu trận gánh Reflow và Paint đi cùng **đúng chỉ một lần**. Tiết kiệm đáng kể hiệu năng tổng quan của ứng dụng.

---

## 3. Lầm tưởng định kiến về Virtual DOM

> [!WARNING] VIRTUAL DOM CÓ THẬT SỰ TỰ NHIÊN MÀ "NHANH HƠN" REAL DOM KHÔNG?
> Nhắc tới Virtual DOM, có rất nhiều bạn bị lầm tưởng định kiến và hiểu nhầm rằng: *"Ứng dụng React nhanh vì Virtual DOM truy xuất nhanh hơn Real DOM"*. Về khía cạnh kỹ thuật thuần kết luận như trên là **HOÀN TOÀN SAI**.

Sự thật mất lòng: Viết những thao tác gắp thẻ thông qua thao tác tay **trực tiếp thẳng lên Real DOM (Vanilla JS)** thì **LUÔN LUÔN NHANH HƠN MỌI MẶT** nếu so kè đi đường vòng trung gian qua bộ nhớ và framework. 
Bằng chứng là, khi một chuyên gia Frontend tự viết thuần bằng Javascript, tự biết thu gom kết dính DOM thông qua các lớp ẩn như `DocumentFragment` rồi hãy nhúng để né tránh triệt để Reflow... app của họ chạy không hề thua kém độ mượt, đôi lúc nhỉnh hơn so với React.

**Vậy tại sao React và Virtual DOM sinh ra làm gì? Chẳng nhẽ chỉ để thêm lớp cồng kềnh?**

Bởi vì nó ban tặng cho nhóm đội ngũ lập trình một kiến trúc tên là **Lập trình Khai báo (Declarative)**. 
Trở lại bằng với React, bạn sẽ không còn phải vất vả đau đầu quan tâm căn thời gian khi nào gọi `appendChild`, khi nào gỡ DOM, khi nào phải gói `DocumentFragment` vào để tránh lỗi chập Reflow màn hình ra sao nữa.
Trong React, bạn chỉ việc gõ lạch cạch "tuyên ngôn": *Giữa Trạng Thái Ghi Log và Trạng Thái Submit Thành công có giao diện chênh lệch thế nào*, thế là tất thảy quy trình tối ưu đắng cay giằng xé bên trong đó Virtual DOM và cấu trúc React sẽ tự động lo toan tối ưu thay bạn. 

---

> 💡 **Tóm kết luận lại:** 
> - **Virtual DOM nhanh** tuyệt đối không phải vì hành động tạo thẻ DOM giả trên bộ nhớ nó mang năng lượng diệu kỳ.
> - **Virtual DOM đưa React trở nên mượt mà** chính bởi vì nó đứng ra đóng vai làm "vị chiến lược gia trung gian", **hạn chế đi phần tối đa những hành vi thừa thãi rườm rà** phát tín hiệu sửa đổi trực tiếp lên đối tượng "xót xa và đắt đỏ" Real DOM.