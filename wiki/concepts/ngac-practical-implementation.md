---
title: "NGAC In Practice: Triển Khai Thực Tế"
source: "raw/ngac/ngac_in_real_project/ngac-practical-guide.md"
date_added: 2026-05-04
tags: [concept, ngac, implementation, architecture, kylan]
aliases: [Hybrid NGAC, NGAC Practical Implementation, NGAC trong thực tế]
status: canonical
related:
  - "[[next-generation-access-control]]"
  - "[[ngac-architecture]]"
  - "[[ngac-database-design]]"
  - "[[ngac-permission-graph]]"
  - "[[ngac-transitive-closure]]"
summary: "Phân tích kiến trúc triển khai NGAC thực tế (Case study: KyLan), giải quyết bài toán hiệu năng thông qua lược bỏ Object nodes và kết hợp NGAC Guard với Denormalized SQL."
---

# NGAC In Practice: Triển Khai Thực Tế

## Định Nghĩa

Triển khai NGAC thực tế (NGAC In Practice) là quá trình áp dụng lý thuyết Next-Generation Access Control (INCITS 565-2020) vào môi trường phần mềm quy mô lớn. Trong thực tế, việc bê nguyên xi lý thuyết đồ thị NGAC vào mã nguồn thường vấp phải giới hạn về dung lượng bộ nhớ (Memory) và hiệu năng truy vấn phân trang (Pagination). Do đó, kiến trúc triển khai thực tế thường áp dụng mô hình lai (Hybrid Pattern), biến đổi một số nguyên lý NGAC chuẩn để tối ưu hóa, ví dụ như lược bỏ các nút đối tượng (Object Nodes) và sử dụng cơ sở dữ liệu quan hệ (RDBMS) làm vùng đệm danh sách.

## Bài Toán Hiệu Năng và Kích Thước Đồ Thị

Trong NGAC chuẩn, mỗi tài nguyên cụ thể (như một tệp tin, tin nhắn, hay phiếu phê duyệt) được coi là một nút Object (O) trong đồ thị. Khi hệ thống có hàng triệu tài nguyên, đồ thị NGAC sẽ phình to dẫn đến chi phí duyệt đồ thị (Graph Traversal) cực kỳ tốn kém.

Ví dụ tại dự án KyLan với 200 nhân viên, 20 phòng ban và 1 triệu tập tin:
- Nếu áp dụng lý thuyết: Đồ thị chứa ~1.000.200 nút, chiếm hàng trăm MB bộ nhớ và khiến `CheckAccess` rất chậm.
- Quyết định kiến trúc: **Lược bỏ hoàn toàn Object (O) nodes khỏi đồ thị**. Hệ thống chỉ tải các nút mức ngữ nghĩa và container: Người dùng (U), Nhóm người (UA), Nhóm tài nguyên (OA), và Chính sách (PC). File hay tin nhắn chỉ tồn tại trong cơ sở dữ liệu và kế thừa quyền từ nút OA chứa nó.
- Tác động: Kích thước đồ thị giảm xuống chỉ còn ~500 nút, giữ bộ nhớ ở mức dưới 1 MB, trong khi tốc độ truy vấn tăng vọt. Kích thước đồ thị lúc này chỉ tỉ lệ thuận (scale) theo số lượng nhân sự và phòng ban thay vì lượng dữ liệu tải lên.

## Kiến Trúc Hybrid: NGAC Guard + Denormalized SQL

Để giải quyết bài toán truy vấn và hiển thị danh sách (như tính năng xem "Danh sách các phiếu cần duyệt" cùng lúc áp dụng phân trang), việc sử dụng đơn thuần đồ thị NGAC là không khả thi. Giải pháp được áp dụng là sự kết hợp giữa NGAC và CSDL quan hệ:

1. **NGAC đóng vai trò Cổng Bảo Vệ (Guard):** Chỉ dùng để trả lời câu hỏi ủy quyền xác định ("Người dùng X có quyền làm Y trên đối tượng Z không?"). Không bao giờ dùng NGAC để tìm kiếm danh sách (list).
2. **Denormalized SQL đóng vai trò Lưu Trữ (Store/List):** Danh sách quyền và người cần phê duyệt được giải mã (resolve) một lần thông qua NGAC tại thời điểm tạo dữ liệu, sau đó ghi chú lại dưới dạng phi chuẩn hóa (denormalized) vào bảng SQL (ví dụ: `approval_assignments`). Mọi tác vụ hiển thị và phân trang (paging, sorting) sẽ chỉ thao tác trên SQL.

## Cơ Chế Phân Quyền Vận Hành (Sharing)

Chia sẻ (Sharing) trong hệ thống triển khai không đồng nghĩa với việc sao chép (clone) dữ liệu vật lý. Cơ chế Sharing được thực hiện bằng cách mở "lối đi" mới trên đồ thị quyền:

- Khi một tệp tin đơn lẻ cần được chia sẻ, hệ thống sẽ tạo một nút vỏ bọc `Share_OA` (Object Attribute) đặc biệt trên đồ thị NGAC. Tệp tin (chỉ nằm ở SQL) sẽ kế thừa từ `Share_OA`. Nút này liên kết quyền với người dùng được mời.
- Việc chia sẻ ra ngoài hoặc thu hồi (Revoke) đơn giản chỉ là thao tác thêm hoặc xóa nút vỏ bọc và cạnh liên kết (Assignment/Association), đảm bảo tính toàn vẹn và duy nhất của dữ liệu gốc.
- Đối với chia sẻ nội bộ phòng ban, tệp tin không cần tạo node NGAC riêng, quyền vẫn được quy định bởi Object Attribute của thư mục cha.

## Thay Đổi Nhân Sự và Reconciliation

Trong môi trường doanh nghiệp, sự thay đổi nhân sự (Nghỉ việc, thay quản lý) diễn ra thường xuyên. Khi thay đổi người trong cùng một chức danh (User Attribute):
- **Phía NGAC Graph:** Cập nhật có hiệu lực tức thì chỉ bằng việc xóa cạnh gán (Assignment) của người cũ và thêm cạnh mới cho người mới.
- **Phía Denormalized SQL:** Dữ liệu có thể rơi vào tình trạng bất đồng bộ (stale data). Cơ chế Đồng bộ lại (Reconciliation) sẽ được kích hoạt để dò tìm và thay thế người thực thi cũ bằng người thực thi mới trong các bảng SQL phi chuẩn hóa (ví dụ: gán lại phiếu chờ duyệt). Các lịch sử đã duyệt vẫn được giữ nguyên.

## Liên Hệ / Ứng Dụng

- Triển khai NGAC quy mô lớn (Enterprise NGAC Implementation).
- Thiết kế hệ thống Access Control kết hợp với Database.
- Tối ưu hóa truy vấn quyền trong kiến trúc Microservices và gRPC.

## Nguồn Tham Khảo

- Ghi chú quá trình triển khai dự án NGAC KyLan: `raw/ngac/ngac_in_real_project/ngac-practical-guide.md`
