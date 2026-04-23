---
title: "Giao Thức Cổng Socrates"
source: "compiled"
date_added: 2026-04-23
tags: [concept, ai, socratic-gate, hallucination]
aliases: [Socratic Gate Protocol]
status: draft
related:
  - "[[antigravity-kit]]"
  - "[[cognitive-routing]]"
summary: "Cơ chế kiểm duyệt ý định tiền thực thi nhằm triệt tiêu ảo giác kiến trúc trong hệ thống AI."
---

# Giao Thức Cổng Socrates

## Định Nghĩa

Giao thức Cổng Socrates (Socratic Gate Protocol) là một cơ chế kiểm duyệt ý định tiền thực thi được tích hợp trong bộ khuôn khổ [[antigravity-kit]]. Lấy cảm hứng từ triết lý biện chứng của Socrates, giao thức này vô hiệu hóa xu hướng "nịnh bợ" (sycophancy) và tự suy diễn vô căn cứ của các mô hình ngôn ngữ lớn (LLM). Thay vì tự động sinh mã ngay khi nhận yêu cầu, hệ thống AI bị ép buộc phải tạm dừng tiến trình điện toán và chủ động đặt ra các câu hỏi chất vấn ngược lại người dùng.

## Ảo Giác Kiến Trúc (Architectural Hallucination)

Ảo giác kiến trúc là một rủi ro mang tính hệ thống xảy ra khi các tác tử AI tự ý đưa ra quyết định sai lệch về yêu cầu nghiệp vụ hoặc mẫu thiết kế (architecture patterns) dựa trên những câu lệnh mơ hồ. Trong môi trường điều phối đa tác tử khổng lồ, một chỉ thị thiếu rõ ràng có thể kích hoạt sai các chuyên gia, dẫn đến hệ lụy dây chuyền làm hỏng cấu trúc mã nguồn. Giao thức Cổng Socrates hoạt động như một lớp giáp phòng ngự ở cửa ngõ, triệt tiêu ảo giác này trước khi bất kỳ token mã hóa nào được sinh ra.

## Kịch Bản Kiểm Duyệt Tiền Thực Thi

Giao thức phân chia tín hiệu đầu vào thành ba kịch bản dựa trên mức độ rủi ro hệ thống, mỗi kịch bản có một quy tắc ép buộc riêng:

### Yêu Cầu Tính Năng Mới
Khi yêu cầu phát triển một tính năng mới làm gia tăng độ hỗn loạn kiến trúc (entropy), hệ thống buộc phải đặt ra **3 câu hỏi chiến lược**. Các câu hỏi này mang tầm vóc vĩ mô nhằm khoanh vùng các luồng xử lý hoặc thiết kế mô hình dữ liệu, tuyệt đối không được hỏi về các tiểu tiết giao diện.

### Sửa Lỗi Hệ Thống (Bug Fix)
Đối phó với nguy cơ tạo ra lỗi hồi quy (regression bugs) khi can thiệp vào mã nguồn, hệ thống áp dụng nhịp xác thực kép. Đầu tiên, AI phải tự tóm tắt lại bản chất gốc rễ của lỗi để con người kiểm duyệt tư duy chẩn đoán. Tiếp theo, hệ thống cùng người dùng định lượng phạm vi tác động dây chuyền (blast radius) trước khi bắt tay vào sửa mã.

### Yêu Cầu Mơ Hồ
Đối với các câu lệnh chung chung (ví dụ: "Tối ưu hóa cơ sở dữ liệu"), hệ thống sẽ đình chỉ toàn bộ hoạt động. Tác tử sẽ yêu cầu người dùng định lượng rõ ba biến số: Mục đích (giá trị kinh doanh đạt được), Người dùng mục tiêu (đối tượng phục vụ cuối), và Phạm vi ranh giới (vùng mã được phép và không được phép can thiệp).

## Liên Hệ / Ứng Dụng

Việc áp dụng Giao thức Cổng Socrates đã tạo ra một sự dịch chuyển mang tính nguyên lý gọi là "Shift-Left Cực đoan". Các rủi ro kiến trúc được phát hiện từ lúc mới chỉ định hình ở ngôn ngữ tự nhiên. Phương pháp này đóng vai trò quyết định trong việc tối ưu hóa ngân sách tài nguyên bằng cách buộc con người phải đảm nhận vị thế Kiến trúc sư trưởng, quy định rõ yêu cầu để hệ thống kéo về các bộ công cụ tương ứng từ Ma trận [[cognitive-routing]].
