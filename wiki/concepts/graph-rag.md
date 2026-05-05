---
title: "GraphRAG"
source: "compiled"
date_added: 2026-05-05
tags: [concept, ai, rag]
aliases: [Graph RAG, Knowledge Graph RAG]
status: draft
related:
  - "[[retrieval-augmented-generation]]"
summary: "Phương pháp RAG cải tiến kết hợp tìm kiếm vector với đồ thị tri thức để khai thác cấu trúc và mối quan hệ phức tạp giữa các tài liệu."
---

## Định Nghĩa

GraphRAG là một phương pháp cải tiến của kiến trúc [[retrieval-augmented-generation]] truyền thống. Thay vì chỉ dựa vào tìm kiếm ngữ nghĩa thông qua các vector độc lập, GraphRAG sử dụng Đồ thị Tri thức (Knowledge Graph) để ánh xạ các thực thể (entities) và mối quan hệ (relationships) giữa chúng từ kho tài liệu. Kỹ thuật này giúp mô hình AI không chỉ tìm ra đoạn văn bản chứa thông tin tương đồng mà còn hiểu được bối cảnh rộng hơn và các kết nối tiềm ẩn.

## Cơ Chế Nổi Bật

Trong các hệ thống quản lý tri thức cá nhân như Obsidian, GraphRAG khai thác mạnh mẽ hệ thống liên kết nội bộ (`[[wikilinks]]`). 

- **Vượt qua giới hạn của Vector Search:** Khi một khái niệm ở Note A liên quan đến hệ quả ở Note B, tìm kiếm vector thông thường (Vector RAG) có thể thất bại trong việc kết nối chúng nếu từ vựng không trùng khớp trực tiếp. GraphRAG giải quyết điểm mù này bằng cách rà soát theo các nút (nodes) và cạnh (edges) trong biểu đồ.
- **Tích hợp Hybrid:** Thường được triển khai kết hợp với Vector Search và BM25 (Hybrid Search) để đảm bảo độ bao phủ thông tin từ tra cứu từ khóa chính xác đến suy diễn khái niệm.

## Liên Hệ / Ứng Dụng

Trong hệ sinh thái LLM cục bộ, kỹ thuật GraphRAG đang được hiện thực hóa thông qua các công cụ như LightRAG, và được tích hợp vào các plugin của Obsidian như Neural Composer hoặc ObsidianRAG. Nhờ đó, trí tuệ nhân tạo có thể hiểu được tư duy kết nối của con người bên trong một vault, cung cấp các câu trả lời mang tính tổng hợp cao dựa trên mạng lưới ghi chú chằng chịt.

## Nguồn Tham Khảo
- [[raw/articles/obsidian-ollama-plugins.md]]
