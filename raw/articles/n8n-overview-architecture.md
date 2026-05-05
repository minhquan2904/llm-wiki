---
title: "Tổng quan về n8n và Kiến trúc mở rộng"
source: "autoresearch"
date_added: 2026-05-04
tags: [autoresearch, n8n, workflow-automation]
aliases: [n8n, n-eight-n, nodemation]
status: draft
summary: "Tổng quan về công cụ tự động hóa n8n, kiến trúc thực thi và cách thức mở rộng theo mô hình Queue Mode."
confidence: high
---

# Tổng quan về n8n và Kiến trúc mở rộng

n8n (đọc là "node-automation" hoặc "n-eight-n") là một nền tảng tự động hóa quy trình làm việc (workflow automation platform) mạnh mẽ, cung cấp mã nguồn (source-available / fair-code). Nó cho phép người dùng kết nối các ứng dụng, dịch vụ và API khác nhau để tạo ra các luồng tự động hóa đa bước.

Được định vị là một công cụ lai (hybrid tool), n8n lấp đầy khoảng trống giữa các nền tảng tự động hóa no-code đơn giản và các giải pháp kỹ thuật viết code hoàn toàn.

## Core Architecture (Kiến trúc cốt lõi)
Kiến trúc của n8n được thiết kế để linh hoạt, có thể mở rộng và thân thiện với nhà phát triển. Nó được xây dựng chủ yếu bằng **Node.js**.

- **Node-Based Design:** Các workflow được cấu thành từ các "node" (nút) riêng biệt. Mỗi node đại diện cho một hành động cụ thể (ví dụ: lấy dữ liệu từ API, gửi email, hoặc biến đổi dữ liệu).
- **Workflow Editor (Frontend):** Giao diện web trực quan, kéo-thả để người dùng thiết kế, kết nối và quản lý các workflow. Nó tạo ra một định dạng JSON đại diện cho workflow.
- **Execution Engine (Backend/Worker):** Động cơ cốt lõi phân tích cú pháp workflow JSON và thực thi luồng công việc theo từng bước. Dữ liệu được truyền giữa các node dưới dạng JSON có cấu trúc.
- **Mô hình triển khai có thể mở rộng (Scalable Deployment Modes):**
  - **Self-Hosted:** Người dùng có thể tự lưu trữ n8n trên hạ tầng riêng (dùng Docker hoặc Node.js), mang lại quyền kiểm soát hoàn toàn về dữ liệu, bảo mật và tuân thủ (GDPR, HIPAA).
  - **Queue Mode:** Dành cho môi trường production, n8n có thể được triển khai với các tiến trình worker riêng biệt để xử lý khối lượng lớn các workflow chạy đồng thời.

## Key Features (Tính năng chính)
- **Hybrid Development (No-Code + Full-Code):** Giao diện kéo thả dễ dùng cho người không chuyên, nhưng cũng rất dễ mở rộng. Lập trình viên có thể viết JavaScript hoặc Python trực tiếp trong workflow để xử lý logic phức tạp.
- **Thư viện tích hợp đồ sộ:** Tích hợp sẵn hàng trăm node cho các dịch vụ phổ biến (Slack, Google Sheets, GitHub). Node HTTP Request đa năng cho phép kết nối với bất kỳ REST API nào chưa được hỗ trợ.
- **AI/LLM Readiness:** Rất phổ biến để xây dựng các luồng tự động hóa AI, điều phối LLM agents, tạo RAG pipelines, và tự động hóa các tác vụ suy luận hàng loạt (batch inference).
- **Logic phức tạp:** Hỗ trợ rẽ nhánh điều kiện (Conditional Branching), vòng lặp (Loops), và xử lý lỗi (Error Handling).
- **Bảo mật:** Quản lý an toàn các API keys, OAuth2. Hỗ trợ SSO và Role-Based Access Control (RBAC).

## Scaling: The "Queue Mode" Architecture
Trong mô hình đơn tiến trình (single-process setup) mặc định, Web UI, hệ thống xử lý trigger và việc thực thi workflow cạnh tranh cùng CPU và bộ nhớ. Khi hiệu suất bị thắt cổ chai, hệ thống cần chuyển sang **Queue Mode**. Kiến trúc này tách biệt n8n thành 3 lớp chính:

1. **Main Instance (The Dispatcher):** Phục vụ UI và API, quản lý triggers. Nó không thực thi workflow mà đóng gói workflow thành một Job và đẩy vào Redis.
2. **Redis (The Message Broker):** Sử dụng thư viện BullMQ để quản lý hàng đợi các job thực thi đang chờ xử lý. Điều phối việc giao job cho các worker.
3. **Worker Processes (The Executors):** Các tiến trình riêng biệt, stateless (không lưu trạng thái) liên tục kéo job từ Redis về để thực thi logic và ghi kết quả cuối cùng vào cơ sở dữ liệu.

### Yêu cầu để scale (Queue Mode Requirements):
- **Database:** Bắt buộc dùng **PostgreSQL** (khuyến nghị 13+). SQLite không hỗ trợ xử lý đồng thời từ nhiều tiến trình.
- **Message Broker:** **Redis** để giao tiếp giữa Main instance và Workers.
- **Binary Data Storage:** Cần hệ thống lưu trữ ngoài (như S3) nếu workflow xử lý dữ liệu nhị phân (ảnh, file).
- **Shared Encryption Key:** Mọi instances phải chia sẻ cùng một mã hóa để giải mã đúng credentials từ database.

## Khi nào cần Scale?
- Khi hiệu năng giảm sút, UI chậm hoặc webhook bị timeout do hệ thống bận thực thi workflow nặng.
- Khi cần xử lý song song khối lượng lớn request vượt quá khả năng của một CPU/Process.
- Đảm bảo độ tin cậy: Tách rời API/UI khỏi tải xử lý nền để tránh sập hệ thống quản trị.
