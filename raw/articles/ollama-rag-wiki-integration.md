---
title: "Xây dựng Local RAG Wiki với Ollama"
source: "autoresearch"
date_added: 2026-05-05
tags: [autoresearch, ollama, rag, wiki]
aliases: []
status: draft
summary: "Cách thiết lập một hệ thống RAG (Retrieval-Augmented Generation) cục bộ cho Wiki bằng Ollama và các công cụ mã nguồn mở."
confidence: high
---

# Xây dựng Local RAG Wiki với Ollama

Để xây dựng một RAG wiki cục bộ với Ollama, bạn cần thiết lập một pipeline có thể nạp (ingest) tài liệu của bạn, lưu trữ chúng vào vector database, và truy xuất chúng để cung cấp ngữ cảnh cho một LLM.

Vì việc xây dựng từ đầu đòi hỏi nhiều công sức lập trình, phần lớn người dùng lựa chọn các nền tảng RAG mã nguồn mở đã được xây dựng sẵn để xử lý các độ phức tạp này.

## 1. Nền tảng được đề xuất (Cách dễ nhất)

Các công cụ này cung cấp giao diện người dùng (UI) thân thiện để quản lý "wiki" (tài liệu) của bạn và trò chuyện với chúng, sử dụng Ollama làm backend.

- **AnythingLLM:** Một ứng dụng desktop All-in-One rất được khuyến nghị. Nó tự động quản lý việc chia nhỏ tài liệu (chunking), lưu trữ vector, và kết nối với Ollama. Bạn chỉ cần trỏ nó tới một thư mục chứa các file markdown/PDF trên máy tính, và nó sẽ coi thư mục đó như một wiki.
- **LeetTools:** Một công cụ thân thiện với developer, cho phép xây dựng local knowledge base qua giao tiếp dòng lệnh (CLI), có khả năng xử lý PDF và file cục bộ với mức tiêu thụ bộ nhớ tối thiểu.

## 2. Các thành phần kỹ thuật cốt lõi (Nếu tự xây dựng)

Nếu bạn muốn tự xây dựng hệ thống bằng Python hay ngôn ngữ khác, bạn sẽ cần stack sau:

- **Runtime:** **Ollama** (để chạy LLM và mô hình Embedding).
- **Embedding Model:** Một mô hình để biến văn bản thành vector số (ví dụ: `nomic-embed-text` rất được khuyến nghị vì độ hiệu quả và chất lượng).
- **Vector Database:** Nơi lưu trữ tài liệu wiki đã được vector hóa để tìm kiếm tương đồng siêu tốc (ví dụ: **ChromaDB**, **Qdrant**, hoặc **Weaviate**).
- **Framework:** Sử dụng **LangChain** hoặc **LlamaIndex**. Các thư viện này đóng vai trò kết nối document loader, vector store, và Ollama API.

## 3. Luồng công việc cơ bản của Local RAG Wiki

Dù dùng tool có sẵn hay tự code, quy trình đều gồm 5 bước:

1. **Ingestion:** Thu thập tài liệu (Wiki files, Markdown, PDFs).
2. **Chunking:** Hệ thống cắt các file lớn thành các phần nhỏ dễ quản lý (chunks).
3. **Embedding:** Mô hình embedding (chạy trong Ollama) chuyển đổi các chunks này thành số (vectors).
4. **Storage:** Các vectors được lưu vào Local Vector Database.
5. **Retrieval & Generation:**
   - Khi bạn đặt câu hỏi, hệ thống sẽ embed câu hỏi đó.
   - Tìm kiếm trong database các chunks liên quan nhất.
   - Gửi các chunks đó kèm câu hỏi của bạn tới LLM (vd: Llama 3) để tạo ra câu trả lời.

## Checklist tóm tắt để bắt đầu

1. **Cài đặt Ollama:** Tải từ ollama.com.
2. **Kéo mô hình (Pull Models):**
   - `ollama pull llama3.1` (hoặc mô hình chat yêu thích)
   - `ollama pull nomic-embed-text` (bắt buộc để chạy tính năng tìm kiếm embedding).
3. **Chọn Frontend:**
   - Dùng GUI: Tải AnythingLLM.
   - Tự code: Tạo project với LlamaIndex hoặc LangChain và trỏ vào API mặc định của Ollama `http://localhost:11434`.
