---
title: "Thực tế về Graph Traversal trong kiến trúc Hybrid NGAC"
source: "compiled"
date_added: 2026-05-04
tags: [summary, ngac, architecture, graph]
aliases: [NGAC Graph Traversal Reality, Thực tế duyệt đồ thị NGAC]
status: reviewed
related:
  - "[[ngac-practical-implementation]]"
  - "[[ngac-permission-graph]]"
  - "[[next-generation-access-control]]"
summary: "Phân tích sự khác biệt giữa lý thuyết duyệt toàn bộ đồ thị (BFS/DFS) trong NGAC chuẩn và thực tế triển khai Hybrid NGAC với Denormalized SQL."
---

## Context

Câu hỏi đặt ra là: *"Theo tài liệu NGAC, khi check quyền hệ thống có load toàn bộ Graph lên để duyệt thuật toán BFS và DFS xem user có quyền không?"*

Đây là một hiểu lầm phổ biến khi áp dụng trực tiếp lý thuyết chuẩn (INCITS 565-2020) vào thực tế phần mềm. Trong triển khai thực tế (đặc biệt qua case study KyLan), hệ thống áp dụng kiến trúc Hybrid NGAC và không hề load toàn bộ tài nguyên hay duyệt đồ thị liên tục.

## Phân Tích

### 1. Không load "toàn bộ" Graph (Lược bỏ Object Nodes)
Theo lý thuyết NGAC chuẩn, mỗi tài nguyên cụ thể (file, tin nhắn) là một nút Object (O). Nếu có 1 triệu file, đồ thị sẽ phình to thành hàng triệu nút. Việc load toàn bộ lên bộ nhớ RAM (In-memory graph) để duyệt (Graph Traversal) sẽ đánh sập hệ thống hoặc gây độ trễ cực lớn. 

Trong kiến trúc lai (Hybrid NGAC), hệ thống **lược bỏ hoàn toàn các nút Object (O)**. Hệ thống chỉ tải các nút mức cấu trúc và ngữ nghĩa:
- Người dùng (U) và Nhóm người (UA)
- Nhóm tài nguyên (OA - như thư mục, dự án, phòng ban)
- Chính sách (PC)

Tài nguyên thực tế (file) chỉ tồn tại ở Database SQL và kế thừa quyền từ nút OA chứa nó. Nhờ vậy, đồ thị trong bộ nhớ co lại cực kỳ nhỏ (chỉ vài trăm nút, chưa tới 1MB) và chỉ scale theo số lượng nhân sự/cấu trúc tổ chức.

### 2. Không dùng BFS/DFS cho mọi thao tác check quyền
Hệ thống không liên tục duyệt đồ thị mỗi khi cần lấy danh sách quyền. Các nghiệp vụ được phân tách rạch ròi:
- **Truy vấn danh sách & Phân trang (Denormalized SQL):** Đối với các tác vụ hiển thị danh sách (như *"Danh sách phiếu cần duyệt"*), quyền hạn đã được giải mã (resolve) một lần từ trước và lưu dưới dạng phi chuẩn hóa (denormalized) vào bảng SQL (ví dụ: `approval_assignments`). Hệ thống query SQL thông thường, không đụng tới đồ thị, giải quyết hoàn toàn bài toán Pagination.
- **Câu hỏi xác định (NGAC Guard):** Hệ thống chỉ dùng đồ thị khi cần trả lời câu hỏi ủy quyền xác định (VD: *"User X có quyền Y trên tài liệu Z không?"*).

### 3. Bản chất của thuật toán duyệt (Graph Traversal)
Khi NGAC Guard hoạt động, hệ thống sử dụng thuật toán dò đường để tìm **Giao điểm (Intersection)** đi từ User và Resource hướng lên Policy Class (PC) chung. Mặc dù không gọi tên cụ thể là thuật toán BFS (Breadth-First Search) hay DFS (Depth-First Search), bản chất của quá trình này — ví dụ như khi duyệt ngược từ `Scope OA` tìm ra `U` có quyền `[approve]` trong Cấp độ Phê duyệt — chính là quá trình truy vết trên đồ thị.

## Kết Luận / Hành Động

- **Lý thuyết vs Thực tế:** NGAC nguyên bản dựa vào Graph Traversal toàn diện, nhưng Hybrid NGAC giới hạn đồ thị ở mức cấu trúc (bỏ Object nodes) và ủy thác việc hiển thị danh sách cho RDBMS.
- Nếu bạn thiết kế hệ thống cấp phép dựa trên NGAC, **tuyệt đối không dùng Graph để list/paginate**; hãy dùng Graph để giải quyết rule logic và đồng bộ hóa kết quả xuống CSDL quan hệ.

## Nguồn
- [[ngac-practical-implementation]]
- [[ngac-permission-graph]]
