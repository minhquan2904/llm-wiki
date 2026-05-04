---
title: "Luồng Phê Duyệt Động (Dynamic Approval Workflow) Trong NGAC"
source: "raw/ngac/ngac_system/approval-flow.md"
date_added: 2026-05-04
tags: [concept, ngac, workflow, system-design]
aliases: [NGAC Approval Flow]
status: reviewed
related:
  - "[[ngac-permission-graph]]"
  - "[[ngac-microservices-architecture]]"
summary: "Phân tích hệ thống phê duyệt đa bước sử dụng đồ thị NGAC để linh hoạt phân công và xác thực quyền hạn theo thời gian thực."
---

## Định Nghĩa

Luồng phê duyệt (Approval Workflow) là một quy trình nghiệp vụ yêu cầu các đề xuất (mua sắm, nghỉ phép, thanh toán) phải vượt qua sự kiểm duyệt của một hoặc nhiều cấp quản lý. Trong kiến trúc NGAC, luồng phê duyệt không dùng mã cứng (hardcode) các cá nhân cố định, mà tận dụng đồ thị quyền để tìm kiếm động (dynamic assignment) những người có thẩm quyền tại thời điểm phát sinh yêu cầu.

## Cấu Trúc Của Một Yêu Cầu Phê Duyệt

Một luồng phê duyệt cấu thành từ 3 phần chính:
1. **Mẫu phê duyệt (Template):** Định nghĩa "luật" của quy trình (điều kiện kích hoạt, số bước duyệt, yêu cầu bao nhiêu người đồng thuận).
2. **Yêu cầu (Request):** Thể hiện của mẫu chứa dữ liệu thực tế do nhân viên nhập. Ngay khi tạo, mẫu phê duyệt sẽ được "đông lạnh" (cloned) vào yêu cầu để đảm bảo nếu Template thay đổi trong tương lai, yêu cầu hiện tại vẫn chạy đúng luật cũ.
3. **Phân công (Assignment):** Đại diện cho tác vụ được giao cho một người duyệt cụ thể tại một bước cụ thể, chứa trạng thái (`pending`, `approved`, `rejected`, `skipped`).

## Cơ Chế Duyệt Và Kiểm Tra Quyền

### Phân Công Dựa Trên Đồ Thị NGAC
Hệ thống tận dụng cơ chế tìm kiếm phạm vi (Scope Finding) của NGAC để phân công. Khi tạo yêu cầu:
- Nếu mẫu quy định người duyệt là "Trưởng phòng", hệ thống không truy vấn database nhân sự. Thay vào đó, nó hỏi NGAC: "Ai có quyền `approve` trên phòng ban hiện tại?".
- NGAC duyệt đồ thị và trả về tập hợp các `User IDs` khớp điều kiện, hệ thống dùng danh sách này để tạo các Assignment.

### Kiểm Tra Quyền Tại Thời Điểm Hành Động (Time-of-Action Re-check)
Đây là tính năng bảo mật then chốt của luồng phê duyệt.
- Khi người duyệt nhấn "Đồng ý", hệ thống **không chỉ** kiểm tra xem họ có Assignment hay không, mà còn **kiểm tra lại quyền NGAC ngay tại giây phút đó**.
- Lý do: Khoảng thời gian từ lúc tạo Assignment đến lúc người đó duyệt có thể kéo dài nhiều ngày. Trong thời gian đó, nhân viên có thể đã bị giáng chức hoặc chuyển sang phòng ban khác. NGAC Time-of-Action Re-check ngăn chặn lỗ hổng "bóng ma quyền hạn" này.

## Vòng Đời Của Luồng Duyệt

1. **Khởi tạo:** Yêu cầu sinh ra, hệ thống tự động tìm Template có độ ưu tiên cao nhất khớp điều kiện, đông lạnh Template, và phân công bước 1.
2. **Đồng thuận (Approval):** Mỗi khi một Assignment được chuyển trạng thái `approved`, hệ thống đếm số lượng phiếu thuận. Nếu đủ hạn mức của bước, nó chuyển sang bước tiếp theo.
3. **Phủ quyết (Rejection):** Theo quy tắc chặt chẽ, chỉ cần một người duyệt chọn `Từ chối` (Reject) tại **bất kỳ bước nào**, toàn bộ luồng phê duyệt sẽ bị chấm dứt ngay lập tức. Các Assignment còn lại ở mọi bước đều chuyển sang trạng thái `skipped`.
4. **Audit Log:** Mọi hành động duyệt, từ chối, kèm theo bình luận (comment) đều được đẩy vào bảng Audit (Nhật ký kiểm toán) dưới định dạng bất biến (Immutable) nhằm đảm bảo tính pháp lý.

## Nguồn Tham Khảo
- `raw/ngac/ngac_system/approval-flow.md`
