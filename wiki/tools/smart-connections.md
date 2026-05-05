---
title: "Smart Connections"
source: "compiled"
date_added: 2026-05-05
tags: [tool, obsidian, plugin, ai]
aliases: [Smart Connections Obsidian]
status: draft
related:
  - "[[retrieval-augmented-generation]]"
  - "[[ollama]]"
summary: "Plugin của Obsidian hỗ trợ tìm kiếm ngữ nghĩa và tính năng chat AI dựa trên kiến trúc Vector RAG thông qua Ollama."
---

## Tổng Quan

Smart Connections là một trong những plugin cộng đồng ổn định và được sử dụng rộng rãi nhất dành cho phần mềm ghi chú Obsidian. Nó được tạo ra để biến vault cá nhân thành một trợ lý AI thông minh bằng cách tích hợp trực tiếp khả năng xử lý ngôn ngữ tự nhiên vào môi trường ghi chú. 

## Vai Trò Trong Môi Trường Ghi Chú

Plugin này đóng vai trò thực thi kiến trúc [[retrieval-augmented-generation]] (RAG) ngay bên trong Obsidian:
- **Lập chỉ mục (Indexing):** Smart Connections quét qua toàn bộ các ghi chú (notes) trong vault, sử dụng mô hình nhúng (như `nomic-embed-text`) để tạo vector embeddings và lưu trữ chúng trực tiếp trên máy cục bộ.
- **Tìm kiếm Ngữ nghĩa (Semantic Search):** Cho phép người dùng tìm kiếm các đoạn ghi chú dựa trên ý nghĩa (ngữ cảnh) thay vì chỉ khớp chính xác từ khóa.
- **Trợ lý Chat (Vault Chat):** Cung cấp giao diện trò chuyện bên thanh lề (sidebar), cho phép người dùng đặt câu hỏi với LLM (thường chạy qua [[ollama]]). LLM sẽ trả lời bằng cách tổng hợp thông tin từ các đoạn ghi chú đã được truy xuất.

## Lợi Thế / Hạn Chế

**Lợi thế:**
- **Tích hợp Sâu:** Hoạt động trơn tru ngay bên trong giao diện quen thuộc của Obsidian mà không cần phải chuyển đổi sang phần mềm khác.
- **Bảo mật Tối đa:** Khi được cấu hình kết nối tới địa chỉ `http://localhost:11434` của Ollama, toàn bộ quá trình lập chỉ mục và truy vấn dữ liệu diễn ra hoàn toàn offline (ngoại tuyến). Không có bất kỳ dòng dữ liệu nhạy cảm nào bị gửi ra đám mây.

**Hạn chế:**
- **Tiêu thụ Tài nguyên:** Quá trình lập chỉ mục ban đầu (indexing phase) cho một vault lớn, cũng như việc chạy mô hình nhúng và LLM đồng thời trên máy cá nhân, đòi hỏi lượng RAM và VRAM đáng kể.
- **Giới hạn của Vector RAG:** Bản chất dựa trên Vector RAG khiến nó đôi khi gặp khó khăn trong việc suy luận các mối quan hệ đa tầng giữa nhiều ghi chú, một điểm yếu mà các plugin sử dụng [[graph-rag]] như Neural Composer hay ObsidianRAG có thể khắc phục tốt hơn.

## Nguồn Tham Khảo
- [[raw/articles/obsidian-ollama-plugins.md]]
