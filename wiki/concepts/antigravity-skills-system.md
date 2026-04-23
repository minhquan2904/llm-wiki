---
title: "Hệ Thống Kỹ Năng (Skills System)"
source: "compiled"
date_added: 2026-04-23
tags: [concept, ai, skills, context-optimization]
aliases: [Antigravity Skills System]
status: draft
related:
  - "[[antigravity-kit]]"
  - "[[cognitive-routing]]"
summary: "Cơ chế phân tán tri thức và tải động để chống suy giảm nhận thức cho tác tử AI."
---

# Hệ Thống Kỹ Năng (Skills System)

## Định Nghĩa

Hệ thống Kỹ năng (Skills System) là một lớp giao thức hạ tầng chuyên biệt trong [[antigravity-kit]] dùng để tổ chức và phân tán cơ sở tri thức cho các tác tử AI. Thay vì nạp toàn bộ cấu trúc dự án và quy tắc thiết kế vào một "Ngữ cảnh Nguyên khối" khổng lồ, hệ thống chia nhỏ tri thức thành các mô-đun độc lập và áp dụng cơ chế Tải Lũy tiến (Progressive Disclosure). Cơ chế này chỉ tiêm kiến thức vào tác tử khi phát sinh tác vụ tương tác cụ thể.

## Khủng Hoảng Nhận Thức Do Nhồi Nhét Ngữ Cảnh

Việc nạp quá tải dữ liệu gây ra sự lãng phí token (Token Waste) và kích hoạt "sự suy giảm nhận thức" do giới hạn toán học của cơ chế chú ý (attention mechanism) trong mô hình ngôn ngữ. Các bệnh lý điển hình bao gồm:
- **Lost-in-middle**: Sự rơi rụng thông tin ở giữa khối ngữ cảnh dài.
- **Nhiễm độc (Poisoning)**: Việc chèn các công cụ không liên quan làm phân tán trọng số và khiến mô hình chệch hướng.
- **Phân tâm (Distraction)**: AI tập trung vào các quy tắc định dạng hơn là giải quyết logic cốt lõi.
- **Bối rối (Confusion)** và **Xung đột (Clash)**: Hậu quả từ việc ép AI đóng vai quá nhiều ngành và tiếp nhận các chỉ thị mâu thuẫn.

## Cấu Trúc Hạt Nhân Của Kỹ Năng

Hệ thống quy hoạch tri thức thành 37 mô-đun độc lập (Kỹ năng). Cấu trúc vật lý của mỗi mô-đun kỹ năng bao gồm:
- Tệp chỉ thị cốt lõi `SKILL.md`: Chứa siêu dữ liệu (meta-data), danh sách công cụ và nguyên tắc cốt lõi được nạp đầu tiên.
- Thư mục tài liệu tham chiếu `references/`: Chứa các quy luật thiết kế phức tạp hoặc thông số API phục vụ nhu cầu nâng cao.
- Thư mục kịch bản tự động `scripts/`: Chứa các công cụ tiện ích bằng Python/Bash để tác tử tự khởi chạy audit.
- Thư mục tài nguyên hỗ trợ `assets/`.

Các kỹ năng được chia thành năm miền trọng yếu: Giao diện người dùng (Frontend & UI), Giao thức kết nối (Backend & API), An ninh mạng, Kiến trúc Máy chủ, và Đánh giá Nhận thức. Việc tải các kỹ năng rời rạc giúp chặn đứng hiện tượng phân tâm, bảo đảm một chuyên gia chỉ tư duy với khối tri thức thuần nhất.

## Cơ Chế Tải Động Lũy Tiến

Thuật toán tải động vận hành thông qua quy trình bốn bước: bộ định tuyến phân giải từ khóa người dùng, khớp nhu cầu với loại kỹ năng tương ứng, tải nội suy tệp `SKILL.md` vào bộ nhớ làm việc, và cuối cùng tiến hành thực thi.

Để bảo vệ trí nhớ vĩnh viễn, hệ thống áp đặt "Ngân sách ngữ cảnh" (Context Budget) khắt khe. Hệ thống thiết lập giới hạn cứng số lượng tác tử và kỹ năng tối đa được phép gọi cùng lúc. Khi vượt rào cản tài nguyên, hệ thống sẽ tự động cắt tỉa (pruning) các kỹ năng phụ để bảo toàn mức độ tập trung.

## Liên Hệ / Ứng Dụng

Khi được tích hợp cùng Máy chủ Ngữ cảnh (Model Context Protocol - MCP), Hệ thống kỹ năng giúp chuyển đổi kiến trúc nội bộ thành mạng lưới suy luận sâu. Các giao thức như Sequential Thinking hỗ trợ phân rã bài toán, và Memory MCP hỗ trợ lưu trữ siêu dữ liệu vĩnh viễn. Kiến trúc phân tán này đã hiện thực hóa được tầm nhìn **Phát triển Hướng Đặc tả (Spec-Driven Development)** trong quy trình sản xuất phần mềm.
