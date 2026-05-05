---
title: "n8n (Workflow Automation)"
source: "compiled"
date_added: 2026-05-04
tags: [tool, workflow-automation, ai-orchestration]
aliases: [n8n, n-eight-n, nodemation]
status: draft
related:
  - "[[message-broker]]"
  - "[[publish-subscribe]]"
  - "[[docker]]"
summary: "Nền tảng workflow automation hybrid hỗ trợ Queue Mode với Redis và PostgreSQL để scale ở môi trường doanh nghiệp."
---

## Tổng Quan

n8n (đọc là "node-automation" hoặc "n-eight-n") là một nền tảng tự động hóa quy trình làm việc (workflow automation) mã nguồn mở (fair-code/source-available). Được thiết kế theo hướng node-based dựa trên Node.js, công cụ này cho phép người dùng kết nối nhiều ứng dụng và API khác nhau thông qua giao diện kéo-thả (Frontend) cùng một bộ thực thi (Execution Engine) để biến đổi dữ liệu dưới dạng JSON.

## Vai Trò Trong Kiến Trúc Hệ Thống

Trong môi trường doanh nghiệp và các dự án AI, n8n đóng vai trò là một điều phối viên (orchestrator) mạnh mẽ:
- **Hybrid Development:** Lấp đầy khoảng trống giữa no-code thuần túy và full-code bằng cách cho phép lập trình viên nhúng trực tiếp mã JavaScript hoặc Python vào các node xử lý logic phức tạp (rẽ nhánh, vòng lặp).
- **AI/LLM Readiness:** Thường được sử dụng để xây dựng RAG pipelines, tự động hóa tác vụ suy luận hàng loạt và điều phối LLM agents nhờ khả năng linh hoạt và kết nối API mạnh mẽ.
- **Queue Mode Scaling:** Để xử lý khối lượng dữ liệu lớn mà thiết lập đơn tiến trình không đáp ứng nổi, n8n hỗ trợ mô hình Queue Mode phân tách kiến trúc thành 3 lớp:
  1. **Main Instance:** Phục vụ UI/API và quản lý triggers, biến workflow thành job.
  2. **Message Broker:** Sử dụng Redis (qua BullMQ) để quản lý hàng đợi các job.
  3. **Workers:** Các tiến trình stateless liên tục kéo job từ Redis về xử lý và lưu kết quả vào PostgreSQL.

## Lợi Thế / Hạn Chế

**Lợi Thế:**
- **Self-Hosted:** Cho phép tổ chức tự lưu trữ (qua Docker/Node.js), đảm bảo kiểm soát hoàn toàn dữ liệu và tuân thủ các tiêu chuẩn bảo mật khắt khe như GDPR hay HIPAA.
- **Thư viện tích hợp:** Hỗ trợ sẵn hàng trăm node cho các dịch vụ phổ biến và tích hợp node HTTP Request đa năng.
- **Linh hoạt & Hiệu năng cao:** Kiến trúc Queue Mode giúp chia tách tải giữa quản lý API/UI và việc thực thi workflow nặng, đảm bảo hệ thống duy trì độ ổn định.

**Hạn Chế:**
- Việc thiết lập Queue Mode đòi hỏi hệ thống hạ tầng phức tạp hơn (bắt buộc dùng PostgreSQL và Redis, không thể dùng SQLite do không hỗ trợ xử lý đồng thời).

## Nguồn Tham Khảo

- Nguồn: `[[raw/articles/n8n-overview-architecture]]`
