---
title: "DOM Performance Optimization"
source: "compiled"
date_added: 2026-04-23
tags: [concept, javascript, performance, dom]
aliases: [Reflow, Repaint, Event Delegation, DocumentFragment, Layout Thrashing]
status: draft
related:
  - "[[javascript-memory-management]]"
summary: "Phân tích nguyên lý hoạt động của DOM, tác động của Reflow/Repaint đến hiệu suất giao diện, và các chiến thuật tối ưu hóa mã JavaScript để giảm tải trình duyệt."
---

# DOM Performance Optimization

DOM (Document Object Model) là giao diện phản ánh cấu trúc HTML lên trình duyệt. Trong phát triển web, JavaScript xử lý logic cực kỳ nhanh gọn trong vùng nhớ, nhưng thao tác can thiệp trực tiếp vào DOM lại là một quy trình tốn kém tài nguyên khủng khiếp. Nắm vững cơ chế hoạt động của DOM và các chiến thuật tối ưu là yêu cầu bắt buộc để xây dựng các ứng dụng web mượt mà.

## 1. Cơ Chế Render: Reflow và Repaint

Bất kỳ lúc nào DOM bị thay đổi bởi JavaScript, trình duyệt đều phải thực hiện tiến trình Critical Rendering Path (Luồng Render Cắt Lớp):

- **Reflow (Layout):** Trình duyệt phải tính toán lại kích thước (width/height) và tọa độ hiển thị của toàn bộ các thẻ HTML. Đây là quá trình đắt đỏ nhất. Thậm chí, việc thay đổi kích thước của một phần tử con có thể kích hoạt chuỗi hiệu ứng domino, buộc tất cả phần tử cha và hàng xóm xung quanh phải tính toán lại (Reflow lan truyền).
- **Repaint (Paint):** Sau khi tính xong kích thước, trình duyệt bắt đầu tô màu (background, color, shadow) từng pixel lên màn hình. Repaint tốn thời gian nhưng ít "phá hoại" hiệu năng bằng Reflow.

> [!WARNING] Quy Tắc Tối Thượng
> Mọi chiến thuật tối ưu DOM đều xoay quanh một mục tiêu duy nhất: **Giảm thiểu tối đa số lần kích hoạt Reflow.**

## 2. Các Chiến Thuật Tối Ưu Hóa Trọng Tâm

### Batching (Gom Nhóm Thao Tác)
Thay vì chọc vào DOM liên tục trong một vòng lặp (ví dụ: gán `innerHTML` 100 lần), lập trình viên phải thực hiện thao tác tạo dữ liệu hoàn toàn bằng JavaScript nội bộ (ghép chuỗi trong biến). Chỉ sau khi chuỗi HTML đã hoàn thiện, mới thực hiện gán vào DOM đúng một lần duy nhất để chỉ kích hoạt 1 lần Reflow.

### Sử Dụng DocumentFragment
Khi cấu trúc HTML phức tạp và không thể dùng chuỗi để gán (`innerHTML`), lập trình viên phải dùng hàm `document.createElement`. Thay vì chèn từng thẻ con trực tiếp vào DOM thật (gây n-lần Reflow), hãy sử dụng `DocumentFragment`. 
Đây là một "DOM ảo" vô hình tồn tại trong vùng nhớ (RAM). Toàn bộ thao tác lắp ghép thẻ con được diễn ra trên Fragment này mà trình duyệt không hề hay biết. Sau khi hoàn tất, ta chèn toàn bộ Fragment vào DOM thật chỉ với một thao tác.

### Né Tránh Layout Thrashing (Máy Ép Dồn Layout)
Trình duyệt hiện đại có cơ chế tự tối ưu: nó sẽ gom nhiều thay đổi DOM lại và thực thi Reflow một lần ở cuối chu kỳ. Tuy nhiên, nếu bạn cố gắng đọc các thuộc tính kích thước hình học (như `offsetWidth`, `offsetHeight`) bằng JavaScript ngay lập tức, trình duyệt bị ép buộc phải tạm dừng tất cả và tính toán kích thước thực tế ngay thời điểm đó để trả dữ liệu cho bạn.

Việc vừa ghi thuộc tính CSS mới, vừa đọc lại kích thước liên tục trong một vòng lặp được gọi là **Layout Thrashing**, khiến trình duyệt vắt kiệt hiệu suất. 
**Cách giải quyết:** Tách biệt rõ ràng vòng lặp Đọc (Read) dữ liệu ra khỏi vòng lặp Ghi (Write) dữ liệu, hoặc sử dụng cơ chế lưu trữ (cache) các thông số đã đọc.

### Event Delegation (Ủy Quyền Sự Kiện)
Khi làm việc với các danh sách dài (ví dụ bảng 1000 dòng học sinh cần đính kèm nút "Xóa"), việc gán 1000 bộ lắng nghe (`addEventListener`) sẽ lập tức làm phình bộ nhớ [[javascript-memory-management#heap-memory-bộ-nhớ-động|Heap Memory]].
Lợi dụng cơ chế **Event Bubbling (Nổi bọt sự kiện)** - nơi các hành động click từ thẻ con lan truyền dần lên thẻ cha - ta chỉ cần gắn duy nhất một bộ lắng nghe ở thẻ cha bao trọn danh sách. Bộ lắng nghe này sẽ đón đầu và kiểm tra (`event.target.matches`) xem thẻ con cụ thể nào thực sự bị bấm, từ đó giảm thiểu tài nguyên mạng lưới Event Listener xuống mức thấp nhất.

## 3. Liên Hệ: Nền Tảng Của Virtual DOM

Chính sự nặng nề của việc tương tác trực tiếp với DOM (Vanilla DOM Manipulation) đã thúc đẩy sự ra đời của **Virtual DOM** trong hệ sinh thái ReactJS. 
Thay vì yêu cầu lập trình viên phải tự áp dụng các kỹ thuật thủ công như `DocumentFragment` hay Batching, Framework sẽ nhận trách nhiệm đối chiếu sự thay đổi trên một cấu trúc bộ nhớ DOM ảo. Sau đó, nó tự động áp dụng thuật toán tìm điểm khác biệt (Diffing), gom nhóm tất cả các cập nhật, và chủ động tương tác với DOM thật theo một cách tối ưu nhất (ít sinh ra Reflow nhất có thể).
