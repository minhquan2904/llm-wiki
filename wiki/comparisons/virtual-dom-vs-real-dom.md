---
title: "So sánh Virtual DOM và Real DOM"
source: "compiled"
date_added: 2026-04-24
tags: [comparison, react, dom, performance]
aliases: [Virtual DOM vs Real DOM, Virtual DOM, Real DOM]
status: canonical
related:
  - "[[dom-performance-optimization]]"
  - "[[javascript-under-the-hood]]"
summary: "Phân tích sự khác biệt về bản chất và hiệu năng giữa kiến trúc Real DOM truyền thống và giải pháp trung gian Virtual DOM của React."
---

# So sánh Virtual DOM và Real DOM

## Bối Cảnh

Sự cạnh tranh giữa việc quản lý Real DOM trực tiếp bằng JavaScript thuần (Vanilla JS) và việc sử dụng tầng đệm Virtual DOM qua các Framework như React luôn là một chủ đề kỹ thuật then chốt. Nút thắt cổ chai không nằm ở thao tác truy xuất dữ liệu trên cấu trúc DOM mà nằm ở hệ quả sau khi sửa đổi: **Trình duyệt (Browser Rendering Pipeline)** buộc phải tính toán lại hình học (Reflow) và vẽ lại giao diện (Repaint). Cuộc chiến tối ưu hóa thực chất là cuộc đua hạn chế các chu trình tốn kém này.

## Bảng So Sánh

| Tiêu chí | Real DOM | Virtual DOM |
|:---|:---|:---|
| **Bản chất** | Là cấu trúc dữ liệu vật lý được trình duyệt sinh ra để biểu diễn cấu trúc của một tài liệu HTML. | Là một bản sao nháp ảo, lưu trữ dưới dạng các Object JavaScript thông thường trong bộ nhớ trong (RAM). |
| **Hành vi cập nhật** | Chỉnh sửa trực tiếp từng phần tử. Nếu không sử dụng các kỹ thuật thu gom (như `DocumentFragment`), mỗi thao tác nhỏ đều kích hoạt Reflow và Repaint riêng lẻ. | Ghi nhận thay đổi trên bản nháp, đối chiếu với bản nháp trước đó và gộp tất cả thay đổi thành một gói cập nhật duy nhất (Batching). |
| **Tốc độ tuyệt đối** | **Nhanh nhất** nếu lập trình viên kiểm soát thủ công một cách hoàn hảo và tối ưu. | Luôn luôn chậm hơn thao tác thủ công chuẩn mực vì phải trải qua tầng trung gian xử lý bộ nhớ và thuật toán của Framework. |
| **Mô hình lập trình** | Mệnh lệnh (Imperative) — Bắt buộc phải miêu tả chi tiết từng bước thao tác (gọi hàm `appendChild`, xóa DOM...). | Khai báo (Declarative) — Chỉ cần định nghĩa kết quả mong muốn, hệ thống sẽ tự động tìm phương án thay đổi cấu trúc với ít chi phí nhất. |

## Phân Tích

Sự ra đời của Virtual DOM không nhằm mục đích biến các thao tác web trở nên nhanh hơn giới hạn vật lý của JavaScript, mà là tạo ra một môi trường phát triển nhất quán để tự động hóa các thao tác tối ưu phức tạp.

Virtual DOM vận hành thông qua quy trình ba bước tinh giản:
1. **Khởi tạo bản nháp**: Biểu diễn toàn bộ sự kiện đổi mới của dữ liệu cục bộ (`state`) hoặc dữ liệu từ cha truyền vào (`props`) thành một hệ thống Object trên RAM thay vì chạm vào hệ thống đồ họa thực tế.
2. **Tìm kiếm sự khác biệt (Diffing)**: Triển khai thuật toán tuyến tính $O(n)$ để so khớp cây Virtual DOM mới với phiên bản tiền nhiệm của nó nhằm định vị chính xác vị trí và nội dung đã biến đổi.
3. **Đóng gói (Reconciliation & Batching)**: Thu thập toàn bộ các thay đổi riêng lẻ, đúc kết thành một luồng lệnh duy nhất và áp thẳng xuống Real DOM. 

Chính cơ chế Batching này đóng vai trò như một bức tường phòng ngự, bảo vệ Real DOM khỏi bị đánh phá liên tục bởi hàng trăm yêu cầu cập nhật, qua đó đảm bảo cho quá trình Reflow và Repaint của trình duyệt diễn ra ở tần suất thấp nhất có thể.

## Kết Luận

Virtual DOM không phải là một "cỗ máy phép thuật" biến ứng dụng trở nên nhanh nhẹn hơn Real DOM về mặt tốc độ truy xuất cơ bản. Lợi ích thực sự của nó nằm ở việc bảo vệ kiến trúc trình duyệt bằng cách triệt tiêu các hành vi cập nhật dư thừa, đồng thời mang đến một mô hình lập trình Khai báo (Declarative). Lập trình viên có thể tập trung mô tả dòng chảy logic của giao diện mà không phải bận tâm việc nhúng tay vào các khâu tối ưu cơ sở dữ liệu DOM rườm rà dễ dẫn đến sai sót.

## Nguồn Tham Khảo

- [[raw/articles/material-file-tree-virtual-dom-vs-real-dom-bí-mật-đằng-sau-hiệu-năng-gốc-của-rea.md]]
