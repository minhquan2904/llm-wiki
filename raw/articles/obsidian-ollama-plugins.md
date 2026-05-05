---
title: "Tích hợp Ollama vào Obsidian Wiki thông qua RAG Plugins"
source: "autoresearch"
date_added: 2026-05-05
tags: [autoresearch, ollama, obsidian, rag]
aliases: []
status: draft
summary: "Đánh giá các plugin cộng đồng giúp kết nối Obsidian Wiki với Ollama để tạo ra một Local Knowledge Base."
confidence: high
---

# Tích hợp Ollama vào Obsidian Wiki thông qua RAG Plugins

Sử dụng Ollama cho quá trình Retrieval-Augmented Generation (RAG) bên trong Obsidian cho phép bạn trò chuyện trực tiếp với kho tàng tri thức (local knowledge base) hoàn toàn offline, đảm bảo quyền riêng tư dữ liệu 100%.

Để thiết lập, bạn cần một Local LLM runner (Ollama) và một Obsidian plugin quản lý RAG pipeline (index ghi chú thành định dạng có thể tìm kiếm và kết nối chúng tới LLM).

## Các Plugins Khuyên Dùng Cho Obsidian RAG

Có nhiều plugin cộng đồng hỗ trợ luồng công việc này. Tùy thuộc vào nhu cầu, bạn có thể chọn:

- **Smart Connections:** Một trong những plugin lâu đời và ổn định nhất cho tìm kiếm ngữ nghĩa (semantic search) và chat. Nó kết nối các ghi chú tới Local LLMs qua Ollama, cho phép đặt câu hỏi dựa trên toàn bộ vault.
- **ObsidianRAG:** Một RAG plugin chuyên dụng sử dụng LangGraph để truy vấn vault. Nó tập trung vào quyền riêng tư, hoạt động offline, và các tính năng nâng cao như Hybrid Search (Vector + BM25) và GraphRAG (sử dụng `[[wikilinks]]` để mở rộng ngữ cảnh).
- **Neural Composer:** Một lựa chọn phức tạp hơn nếu bạn muốn vượt ra khỏi tìm kiếm vector thông thường. Nó tích hợp **LightRAG** để xây dựng Knowledge Graph (thực thể và mối quan hệ) từ ghi chú, giúp AI hiểu *ngữ cảnh* và *sự kết nối* giữa các ý tưởng, thay vì chỉ khớp từ khóa.
- **Mini-RAG:** Một plugin nhẹ nhàng, tập trung cho phép trò chuyện với LLM trong ngữ cảnh của một số ghi chú hoặc thư mục cụ thể, thay vì index toàn bộ vault cùng lúc.

## Các Bước Thiết Lập Chung

Dù mỗi plugin có hướng dẫn riêng, luồng công việc thường tuân theo cấu trúc sau:

1. **Cài đặt & Chạy Ollama:** Chắc chắn Ollama đang chạy ngầm trên hệ thống.
2. **Kéo mô hình (Pull Models):**
   - *Chat model:* `ollama pull [model-name]` (vd: `llama3` hoặc `gemma3`).
   - *Embedding model:* `ollama pull nomic-embed-text` (rất khuyến nghị cho RAG vì độ hiệu quả tối ưu cho máy cá nhân).
3. **Cài đặt Obsidian Plugin:** Vào **Settings > Community Plugins**, tìm plugin đã chọn (vd: "Smart Connections") và bật nó lên.
4. **Cấu hình Plugin:**
   - Trỏ plugin về địa chỉ Ollama URL (mặc định: `http://localhost:11434`).
   - Chọn chat model và embedding model đã tải.
5. **Index Vault của bạn:** Hầu hết plugin sẽ yêu cầu một giai đoạn "indexing", lúc này nó sẽ quét qua ghi chú, tạo vector embeddings, và lưu cục bộ để AI có thể "đọc" knowledge base. Sau khi index xong, bạn có thể bắt đầu trò chuyện.

## Mẹo Để Thành Công

- **Phần cứng rất quan trọng:** Chạy RAG cục bộ rất tiêu tốn tài nguyên. Nếu hệ thống chậm chạp, hãy đảm bảo bạn đang dùng embedding models nhỏ và hiệu quả như `nomic-embed-text`.
- **GraphRAG vs Vector RAG:** Nếu standard RAG không "hiểu" được mối quan hệ giữa các ghi chú (ví dụ: không kết nối được methodology ở Note A với result ở Note B), hãy cân nhắc plugin như **Neural Composer** vì chúng dùng GraphRAG để khai thác wikilinks hiện có.
- **Quyền riêng tư:** Vì chạy cục bộ, luôn đảm bảo plugin cấu hình trỏ tới `localhost`, bảo đảm không có dữ liệu nào gửi lên đám mây.
