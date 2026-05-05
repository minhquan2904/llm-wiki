---
title: "Research: n8n là gì"
source: "autoresearch"
date_added: 2026-05-04
tags: [research, autoresearch, workflow-automation]
status: draft
related: []
summary: "Báo cáo nghiên cứu tự động về n8n, công cụ tự động hóa quy trình làm việc (workflow automation) kết hợp sức mạnh của no-code và full-code."
---

## Bối Cảnh
Mục tiêu nghiên cứu tìm hiểu định nghĩa, cấu trúc, tính năng và cách thức hoạt động của nền tảng tự động hóa quy trình **n8n**, nhằm lấp đầy khoảng trống kiến thức về công cụ này trong Second Brain.

## Phát Hiện Chính
- **Định vị cốt lõi:** n8n là công cụ workflow automation lai (hybrid) mã nguồn mở (fair-code/source-available), giúp thu hẹp khoảng cách giữa no-code (dễ dùng, kéo thả) và code thuần (custom JS/Python). (Nguồn: [[n8n-overview-architecture]])
- **Self-Hosted & Privacy:** Lợi thế lớn nhất của n8n là khả năng tự lưu trữ trên máy chủ riêng (Self-Hosted), đảm bảo tuân thủ nghiêm ngặt các quy định bảo mật dữ liệu (GDPR, HIPAA). (Nguồn: [[n8n-overview-architecture]])
- **Khả năng AI/LLM:** n8n đang là một công cụ mạnh mẽ hỗ trợ tích hợp AI, orchestrate các mô hình ngôn ngữ lớn (LLM), RAG, và AI agents thông qua các node tích hợp hoặc custom code. (Nguồn: [[n8n-overview-architecture]])

## Thực Thể & Khái Niệm Mới
- **Concept: Queue Mode Architecture** Kiến trúc mở rộng để xử lý khối lượng dữ liệu lớn của n8n. Nó tách biệt Main Instance (chạy UI/API) khỏi các Worker Processes (thực thi tác vụ), và dùng Redis cùng PostgreSQL làm trung gian lưu trữ/điều phối hàng đợi công việc.
- **Concept: Node-based Design** Quy trình làm việc được cấu thành từ các "Nút". Dữ liệu truyền qua lại giữa các nút ở định dạng JSON để xử lý từng bước.

## Câu Hỏi Mở
- Mặc dù n8n rất thân thiện với lập trình viên nhờ custom code, tài liệu chưa đi sâu so sánh chi tiết hiệu suất của n8n so với các nền tảng tự động hóa cấp doanh nghiệp khác như Apache Airflow trong các tình huống Data Engineering cực nặng.
- Bản quyền Fair-code / Sustainable Use License của n8n ảnh hưởng như thế nào đến việc kinh doanh nhúng (embedding) của các startup phần mềm?

## Nguồn Đã Nạp
- [[n8n-overview-architecture]]
