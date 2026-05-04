---
title: "NGAC Permission Graph: Đồ Thị Quyền Thực Tế"
source: "raw/ngac/ngac_in_real_project/permission-graph.md"
date_added: 2026-05-04
tags: [concept, ngac, architecture, graph]
aliases: [Đồ thị quyền NGAC, NGAC Graph, Permission Graph]
status: canonical
related:
  - "[[ngac-database-design]]"
  - "[[ngac-security-model]]"
  - "[[ngac-practical-implementation]]"
summary: "Phân tích cấu trúc đồ thị quyền NGAC (Permission Graph) qua các cấp độ tổ chức như Workspace, Department, Channel, Drive và Approval."
---

# NGAC Permission Graph: Đồ Thị Quyền Thực Tế

## Định Nghĩa

Đồ thị quyền NGAC (Permission Graph) là một cấu trúc biểu diễn trực quan toàn bộ các thực thể và mối quan hệ phân quyền trong hệ thống Next-Generation Access Control. Nó xác định "ai được phép làm gì trên tài nguyên nào" thông qua việc dò tìm các đường dẫn giao nhau (Intersection) đi từ phía người dùng và phía tài nguyên hướng lên chung một Policy Class (PC). Mọi thay đổi quyền hạn đều phản ánh dưới dạng thêm hoặc xóa các nút (Node) và cạnh (Assignment, Association) trên đồ thị này.

## Nguyên Tắc Hoạt Động Của Đồ Thị

Đồ thị NGAC vận hành dựa trên cơ chế đối xứng và nguyên tắc giao điểm (Intersection Principle):
1. **Phía người dùng (User Side):** Nút người dùng (U) gán vào các nhóm vai trò/nhóm người (UA), và UA gán vào Policy Class (PC).
2. **Phía tài nguyên (Resource Side):** Tài nguyên (O) gán vào các nhóm tài nguyên (OA), và OA cũng gán vào PC.
3. **Quyết định cấp quyền (Authorization Decision):** Hệ thống sẽ trả về **ALLOW** chỉ khi tồn tại chung một PC cho cả U và O, đồng thời trên hành trình di chuyển tồn tại một cạnh Association nối UA với OA chứa hành động (`operation`) tương ứng.

## Cấu Trúc Graph Theo Các Cấp Độ (Levels)

Trong các ứng dụng quy mô thực tế (như nền tảng làm việc đa Workspace), đồ thị được phân rã thành nhiều cấp độ phân mảnh:

### Cấp Độ Workspace (Workspace Level)
Là Policy Class (PC) cao nhất đại diện cho ranh giới công ty/tổ chức.
- **Owners (UA)** có Association `[full]` tới tất cả OA trong Workspace (Channels, Documents, Mgmt).
- **Members (UA)** chỉ có Association cấp quyền thao tác cơ bản `[read, write, create, upload]` tới các OA tương ứng.

### Cấp Độ Phòng Ban (Department Level)
Mỗi phòng ban tạo ra một tập hợp UA và OA lồng bên trong Workspace.
- **Thành viên phòng ban (Department Members - UA)** được gán vào Workspace PC.
- **Trưởng phòng (Department Chief - UA)** được thiết kế lồng bên trong (Containment) nút Department Members. Điều này giúp Trưởng phòng tự động kế thừa mọi quyền của thành viên, đồng thời có Association riêng với cấp độ `[toàn quyền]` trên tài nguyên phòng ban (Department Mgmt - OA).

### Cấp Độ Tài Liệu (Drive Level)
Tuân theo nguyên tắc kế thừa cấu trúc thư mục.
- Tệp tin (File - O) gán vào Thư mục chứa nó (Folder - OA). 
- Thư mục gán vào Thư mục cha, đệ quy liên tục cho đến khi chạm tới nút `Workspace Documents (OA)` ở gốc. Do đó, quyền áp dụng lên thư mục sẽ tự động bao trùm toàn bộ các tệp tin bên trong.

### Cấp Độ Phê Duyệt (Approval Level)
Thay vì kiểm tra người dùng trước, hệ thống duyệt đồ thị theo chiều ngược để tìm "Ai có quyền".
- Cấu trúc: `Chief (UA) → Scope OA [approve]`.
- Khi có yêu cầu tạo ra tại một `Scope OA`, hệ thống tìm các Association có quyền `[approve]` hướng tới OA này, từ đó truy vết ngược ra các UA và U có thẩm quyền phê duyệt tương ứng.

## Thao Tác Chuyển Đổi Quyền Hạn (Graph Operations)

Toàn bộ nghiệp vụ cấp/thu hồi quyền được quy về các phép toán đồ thị (Graph Math):
- **Thêm thành viên vào nhóm:** Tạo một cạnh Assignment từ U tới UA.
- **Thu hồi quyền:** Xóa cạnh Assignment.
- **Tạo quyền mới cho nhóm:** Tạo một Association giữa UA và OA với danh sách `operations`.

## Các Mẫu Kiểm Tra Quyền (Authorization Patterns)

Hệ thống tận dụng đồ thị để giải quyết 4 bài toán phân quyền phổ biến:
1. **Kiểm tra trực tiếp (Direct Check):** "User A có quyền X trên đối tượng Y không?". Dùng cho các thao tác cụ thể (vd: gửi tin nhắn, xóa file). Kết quả là Có/Không (`DecisionAllow`/`DecisionDeny`).
2. **Lọc danh sách (Filter List):** "Trong 20 kênh chat, user A có quyền đọc những kênh nào?". Thay vì dùng SQL JOIN phức tạp, hệ thống chuyển sang hỏi NGAC từng ID một và lọc ra kết quả hợp lệ.
3. **Tìm phạm vi (Scope Finding):** "Những ai có quyền duyệt yêu cầu mua sắm tại phòng ban này?". Thay vì hỏi từ User tới Tài nguyên, hệ thống đi ngược từ Tài nguyên (Scope OA) tìm về tất cả các UA có chứa quyền `approve`. Dùng chủ yếu trong Luồng phê duyệt động.
4. **Kiểm tra tại thời điểm hành động (Time-of-Action Re-check):** "Lúc phân công duyệt, User A có quyền. Bây giờ lúc bấm duyệt, User A còn quyền không?". Hệ thống luôn gọi NGAC kiểm tra lại vào khoảnh khắc user thực thi hành động để chống lỗ hổng "bóng ma quyền hạn" (khi nhân sự chuyển phòng ban).

## Chiến Lược Quản Lý Bộ Nhớ (Memory Strategy)

Vì đồ thị quyền có thể rất lớn, Policy Service không tải toàn bộ vào RAM mà áp dụng chiến lược phân mảnh (Sharding):
- **Per-Workspace Shards:** Đồ thị được chia nhỏ và tải lên RAM theo từng Workspace. Khi có request liên quan đến Workspace nào, Shard của Workspace đó sẽ được truy cập.
- **LRU Eviction:** Trình quản lý `ShardManager` sử dụng cơ chế O(1) LRU (Least Recently Used) dựa trên doubly-linked list và index map. Khi số lượng Shards vượt quá `maxShards` (mặc định 1000), các Shard lâu không dùng sẽ bị loại bỏ khỏi bộ nhớ để giải phóng RAM.
- **Lazy Load & Fallback:** Các Shard được lazy-load khi có request đầu tiên. Trong trường hợp Shard bị lỗi hoặc chưa sẵn sàng, hệ thống có thể fallback về Global Graph (chứa đồ thị tổng) để đảm bảo không gián đoạn dịch vụ.

## Liên Hệ / Ứng Dụng

- Dùng đồ thị NGAC để kiểm soát quyền trong môi trường B2B / SaaS Multi-tenant.
- Thiết kế hệ thống phê duyệt động (Dynamic Approval Workflow).
- Giảm thiểu việc sao chép dữ liệu (Data Duplication) nhờ cơ chế thừa kế đồ thị thay vì Access Control List (ACL).

## Nguồn Tham Khảo

- Sơ đồ chi tiết đồ thị cấp phép: `raw/ngac/ngac_in_real_project/permission-graph.md`
