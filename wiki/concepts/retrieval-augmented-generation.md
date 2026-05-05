---
title: "Retrieval-Augmented Generation"
source: "compiled"
date_added: 2026-05-05
tags: [concept, ai, rag]
aliases: [RAG, Local RAG Wiki]
status: draft
related:
  - "[[graph-rag]]"
  - "[[ollama]]"
  - "[[anythingllm]]"
  - "[[smart-connections]]"
summary: "Kiến trúc sinh văn bản tăng cường truy xuất, kết nối mô hình ngôn ngữ với cơ sở dữ liệu riêng để cung cấp ngữ cảnh chính xác."
---

## Định Nghĩa

Retrieval-Augmented Generation (RAG) là một kiến trúc trí tuệ nhân tạo kết hợp sức mạnh sinh ngôn ngữ của LLM với khả năng tìm kiếm thông tin từ một cơ sở dữ liệu bên ngoài. Thay vì phụ thuộc hoàn toàn vào kiến thức đã được huấn luyện sẵn của mô hình, RAG cho phép hệ thống truy xuất các tài liệu liên quan đến câu hỏi của người dùng, sau đó cung cấp chúng cho LLM như một ngữ cảnh (context) bổ sung để tạo ra câu trả lời chính xác, cập nhật và có thể kiểm chứng.

## Cơ Chế Hoạt Động (Pipeline)

Một luồng công việc (pipeline) RAG tiêu chuẩn bao gồm năm giai đoạn cốt lõi:

1. **Ingestion (Nạp dữ liệu):** Thu thập tài liệu thô từ nhiều nguồn khác nhau (như Wiki files, Markdown, PDFs).
2. **Chunking (Phân mảnh):** Hệ thống cắt các tài liệu lớn thành các phần nhỏ (chunks) để dễ quản lý và tìm kiếm.
3. **Embedding (Nhúng):** Sử dụng một mô hình Embedding (ví dụ: `nomic-embed-text`) để chuyển đổi các đoạn văn bản (chunks) thành các vector số học đại diện cho ý nghĩa của chúng.
4. **Storage (Lưu trữ):** Các vector này được lưu trữ trong một Vector Database chuyên dụng (như ChromaDB, Qdrant, hoặc Weaviate).
5. **Retrieval & Generation (Truy xuất và Sinh văn bản):** 
   - Khi có truy vấn từ người dùng, hệ thống sẽ thực hiện quá trình embedding lên chính câu hỏi đó.
   - Tìm kiếm trong Vector Database để lấy ra các chunks có độ tương đồng cao nhất (Semantic Search).
   - Gửi các chunks đã tìm được kèm theo câu hỏi gốc tới LLM (ví dụ: Llama 3) để tổng hợp thành câu trả lời cuối cùng.

## Liên Hệ / Ứng Dụng

RAG đặc biệt hữu ích trong việc xây dựng các "Local Knowledge Base" (Kho tàng tri thức cục bộ) hoặc "Second Brain" bảo mật tuyệt đối. Người dùng có thể triển khai hệ thống RAG cục bộ bằng cách kết hợp framework [[ollama]] (chạy LLM) với các giải pháp giao diện All-in-One như [[anythingllm]], hoặc tích hợp thẳng vào phần mềm ghi chú thông qua các plugin như [[smart-connections]] của Obsidian. Sự kết hợp này mang lại khả năng trò chuyện trực tiếp với tài liệu cá nhân mà không cần gửi dữ liệu nhạy cảm lên đám mây.

## Nguồn Tham Khảo
- [[raw/articles/ollama-rag-wiki-integration.md]]
- [[raw/articles/obsidian-ollama-plugins.md]]
