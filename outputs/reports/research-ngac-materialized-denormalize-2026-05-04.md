---
title: "Research: Materialized và Denormalization trong NGAC"
source: "autoresearch"
date_added: 2026-05-04
tags: [research, autoresearch, ngac]
status: draft
related: 
  - "[[ngac-practical-implementation]]"
  - "[[ngac-database-design]]"
summary: "Báo cáo nghiên cứu tự động về chiến lược tối ưu hóa đồ thị NGAC thông qua vật chất hóa (materialization) bao đóng bắc cầu và phi chuẩn hóa (denormalization)."
---

## Bối Cảnh
Mục tiêu nghiên cứu là khám phá cơ chế làm thế nào để tối ưu hóa bài toán truy vấn quyền (Authorization Checks) trong mô hình Next-Generation Access Control (NGAC). Do NGAC hoạt động dựa trên đồ thị (DAG), việc kiểm tra quyền đồng nghĩa với việc duyệt đồ thị để tính toán bao đóng bắc cầu (transitive closure). Khi kích thước đồ thị lớn, việc duyệt này có thể gây ra nút thắt cổ chai về hiệu năng, dẫn đến sự cần thiết của các kiến trúc tối ưu thông qua Materialization và Denormalization.

## Phát Hiện Chính
- **Đánh đổi hiệu năng Duyệt Đồ Thị vs. Tính Toán Trước (Pre-calculation):** Tính toán bao đóng bắc cầu trên đồ thị là tác vụ $O(V^3)$. Để khắc phục, các kiến trúc thực tế lưu trữ trước (cache) các đường đi hợp lệ dưới dạng một đồ thị phi chuẩn hóa (denormalized). Việc này giúp giảm thời gian truy vấn quyền xuống hằng số $O(1)$, nhưng bù lại gia tăng chi phí duy trì tính nhất quán khi đồ thị thay đổi (Write overhead). (Nguồn: [[ngac-materialized-denormalize]])
- **Materialization của Transitive Closure:** Việc vật chất hóa (Materializing) các đường dẫn (paths) và khả năng tiếp cận (reachability) trong đồ thị chính là một dạng view phi chuẩn hóa (denormalized view) chuyên dụng của hệ thống phân quyền NGAC. Policy Decision Point (PDP) có thể "tra cứu" thay vì "duyệt". (Nguồn: [[ngac-materialized-denormalize]])
- **Kiến trúc Hybrid / Denormalized SQL:** Trong thực tế dự án, thay vì duy trì vật chất hóa trên Graph Database tốn kém, hệ thống tách bạch vai trò: NGAC làm cổng (Guard) trả lời `YES/NO`, còn SQL phi chuẩn hóa lưu trữ danh sách các phiếu/tài nguyên đã được "giải mã" trước quyền để hỗ trợ truy vấn danh sách (List) và phân trang (Pagination). (Nguồn: [[ngac-practical-implementation]])

## Thực Thể & Khái Niệm Mới
- **Concept: Transitive Closure (Bao đóng bắc cầu):** Trong NGAC, nó mô tả tất cả các thực thể (Users/Objects) có thể "chạm" tới nhau thông qua các cạnh trung gian (như Assignment hay Association).
- **Concept: Incremental Updates (Cập nhật tăng dần):** Một thuật toán tối ưu hóa mà thay vì tính toán lại toàn bộ đồ thị khi có một sự kiện gán/hủy gán (Assign/Deassign), hệ thống chỉ cập nhật các mảnh đồ thị bị ảnh hưởng, làm giảm độ trễ ghi dữ liệu.

## Mâu Thuẫn (nếu có)
- Không có mâu thuẫn lớn. Tuy nhiên, sự cân bằng (trade-off) là một thách thức kỹ thuật: Hệ thống càng đọc nhiều (Read-heavy) thì Materialization càng mang lại lợi ích. Nếu hệ thống ghi quá nhiều (Write-heavy), Materialized Views trở thành gánh nặng.

## Câu Hỏi Mở
- Làm thế nào để áp dụng Incremental Updates hiệu quả nhất nếu đồ thị NGAC được lưu trong cơ sở dữ liệu quan hệ (ví dụ dùng thuật toán Recursive CTE)?
- Cơ chế giải quyết độ trễ giữa Graph PDP và Denormalized SQL (Eventual Consistency) diễn ra như thế nào trong môi trường Enterprise?

## Nguồn Đã Nạp
- [[ngac-materialized-denormalize]]
