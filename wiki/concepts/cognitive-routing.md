---
title: "Định Tuyến Nhận Thức Đa Chiều"
source: "compiled"
date_added: 2026-04-23
tags: [concept, ai, agent-routing]
aliases: [Cognitive Routing]
status: draft
related:
  - "[[antigravity-kit]]"
  - "[[sequential-multi-domain-execution]]"
summary: "Cơ chế phân tích ngữ nghĩa ngầm và tự động ánh xạ tác vụ tới chuyên gia AI phù hợp."
---

# Định Tuyến Nhận Thức Đa Chiều

## Định Nghĩa

Định tuyến Nhận thức Đa chiều (Cognitive Routing) là một cơ chế phân tích ngữ nghĩa ngầm (silent analysis) được nhúng trong nền tảng [[antigravity-kit]]. Chức năng cốt lõi của nó là giải phóng người dùng khỏi việc thiết kế câu lệnh thủ công (prompt engineering) để lựa chọn chuyên gia. Hệ thống sẽ tự động nhận diện ý định từ các mô tả tự nhiên để ánh xạ công việc tới các AI chuyên biệt, các mô-đun kỹ năng tương ứng, và định hướng luồng làm việc.

## Ma Trận Định Tuyến Tác Tử

Ma trận Định tuyến (Agent Selection Matrix) vận hành như một hệ thống tính toán phân loại độ phức tạp chứ không phải bảng tra cứu tĩnh. Khi tiếp nhận yêu cầu, cơ chế bóc tách các từ khóa (keywords) ẩn trong câu, đo lường bối cảnh từ tệp đang mở, và phân loại tác vụ (Đơn giản, Vừa, Phức tạp). Dựa trên tập luật này, hệ thống xác nhận nhu cầu và kích hoạt nhân dạng tác tử (`@agent`) kết hợp việc tiêm ngay lập tức tệp cấu hình chuyên ngành vào bộ nhớ tạm.

Ví dụ, nếu người dùng đề cập đến từ khóa "login" hay "auth", hệ thống không chọn tác tử máy chủ (backend) ngay mà ưu tiên định tuyến thêm tác tử bảo mật (`@security-auditor`) cùng với kỹ năng `vulnerability-scanner`.

## Tương Quan Chuyên Môn Chéo (Cross-Domain Symbiosis)

Sự phức tạp của định tuyến nhận thức không dừng lại ở việc chọn đơn lẻ một chuyên gia, mà còn kích hoạt sự tương quan chuyên môn chéo. Với các yêu cầu bao hàm đa thuộc tính, cơ chế sẽ từ chối việc chỉ định một lập trình viên đa năng. Thay vào đó, nó triệu hồi song song các chuyên gia cốt lõi để cùng xây dựng kiến trúc từ nhiều chiều không gian.

Trong yêu cầu xây dựng hệ thống đăng nhập, hệ thống định tuyến tác tử bảo mật để đánh giá chính sách và mã hóa mật khẩu, đồng thời định tuyến kiến trúc sư cơ sở dữ liệu (`@database-architect`) để thiết kế lược đồ bảng và tối ưu chỉ mục. Sự cộng sinh chéo này đảm bảo mọi yêu cầu đều được thiết lập theo góc nhìn đa chiều của doanh nghiệp thay vì tầm nhìn hẹp của một người phát triển đơn lẻ.

## Liên Hệ / Ứng Dụng

Định tuyến nhận thức đóng vai trò chuyển trạm cực kỳ quan trọng trong tiến trình [[sequential-multi-domain-execution]]. Đối với các yêu cầu đột phá cần hàm lượng chất xám cao, cơ chế nhận diện từ khóa sẽ triệu hồi hệ thống Tác tử điều phối (`@orchestrator` hoặc `@project-planner`) để chuyển sang pha Khám phá (Deep Research). Điều này thiết lập nền móng cho các hệ thống phần mềm dựa trên ý định, giúp loại bỏ hoàn toàn các cấu trúc tổ chức (silos) trong việc đánh giá mã nguồn.
