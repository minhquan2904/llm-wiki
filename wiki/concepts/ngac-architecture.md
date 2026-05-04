---
title: "Kiến trúc NGAC (Next-Generation Access Control)"
source: "compiled"
date_added: 2026-05-04
tags: [concept, ngac, architecture, access-control]
aliases: [NGAC Architecture]
status: reviewed
related:
  - "[[next-generation-access-control]]"
  - "[[ngac-security-model]]"
  - "[[abac-architecture]]"
summary: "Phân tích cấu trúc thực thi của NGAC bao gồm Information Flows và Functional Entities (PEP, PDP, EPP...)."
---

## Định Nghĩa Kiến Trúc

Kiến trúc NGAC (Next-Generation Access Control) mở rộng mô hình kiểm soát truy cập truyền thống bằng cách định hình một quy trình phối hợp mạnh mẽ giữa các thành phần thực thi. Mục đích chính của kiến trúc này là cung cấp cơ chế phân quyền dựa trên thuộc tính động, đáp ứng nhanh chóng với các sự kiện thay đổi trạng thái (context events) trong thời gian thực, đồng thời tách biệt hoàn toàn phần xử lý chính sách (PDP) và phần thực thi chính sách (PEP).

## Các Luồng Thông Tin (Information Flows)

Theo tiêu chuẩn INCITS 565-2020, hệ thống NGAC phân chia luồng thông tin thành ba quá trình chính:

1. **Resource Access (Truy cập tài nguyên):** Luồng yêu cầu của người dùng muốn tiếp cận một dữ liệu/tài nguyên cụ thể. PEP bắt giữ yêu cầu này và chuyển cho PDP quyết định.
2. **Administration Access (Truy cập quản trị):** Luồng điều chỉnh các quy tắc bảo mật. Quản trị viên tương tác qua PAP để sửa đổi chính sách kiểm soát.
3. **Event Context (Bối cảnh sự kiện):** Luồng các trạng thái động, ví dụ: người dùng đổi phòng ban, mối đe dọa xâm nhập. PIP và EPP xử lý luồng này để liên tục làm mới ngữ cảnh đưa ra quyết định.

## Functional Entities (Thực thể chức năng)

Kiến trúc NGAC bao gồm các thực thể cốt lõi sau:

- **PEP (Policy Enforcement Point - Điểm thực thi chính sách):** Cổng chặn mọi luồng yêu cầu truy cập từ người dùng và buộc thực hiện quyết định từ PDP.
- **PDP (Policy Decision Point - Điểm quyết định chính sách):** Bộ não trung tâm, đối chiếu yêu cầu của PEP với dữ liệu hiện trạng để cấp hoặc từ chối quyền.
- **PAP (Policy Administration Point - Điểm quản trị chính sách):** Giao diện để thiết lập, định dạng và bảo trì các bộ quy tắc, thuộc tính người dùng và tài nguyên.
- **PIP (Policy Information Point - Điểm thông tin chính sách):** Kho chứa thông tin ngữ cảnh, nơi cung cấp dữ liệu thuộc tính động cho PDP.
- **EPP (Event Processing Point - Điểm xử lý sự kiện):** Nút thắt thông minh quan trọng nhất của NGAC. EPP giám sát môi trường để bắt các thay đổi và lập tức kích hoạt phản ứng thay đổi cấu trúc thuộc tính.
- **RAP (Resource Access Point - Điểm truy cập tài nguyên):** Cửa ngõ vật lý/logic gắn liền với tài nguyên. Phối hợp với PEP để bảo vệ tài nguyên thật sự.

## Liên Hệ / Ứng Dụng

Sự kết hợp giữa PEP, PDP và đặc biệt là EPP giúp NGAC có khả năng xây dựng các hệ thống bảo mật tự phục hồi (self-healing), chủ động điều hướng truy cập khi phát hiện bất thường mà không cần sự can thiệp thủ công từ quản trị viên.

## Nguồn Tham Khảo
- `raw/ngac/ngac.md` (INCITS 565-2020 standard)
