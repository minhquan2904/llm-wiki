---
title: "Llama 3.2 3B Instruct"
source: "compiled"
date_added: 2026-05-05
tags: [tool, ai, llm, slm]
aliases: [Llama 3.2 3B, Llama 3.2]
status: draft
related:
  - "[[small-llms-llama-phi-gemma]]"
  - "[[ollama]]"
summary: "Mô hình ngôn ngữ nhỏ gọn (SLM) 3 tỷ tham số của Meta, hỗ trợ 128k ngữ cảnh và tối ưu cho thiết bị cá nhân."
---

## Tổng Quan

Llama 3.2 3B Instruct là một mô hình ngôn ngữ nhỏ gọn (Small Language Model - SLM) được phát triển bởi Meta, sở hữu khoảng 3 tỷ tham số. Được thiết kế đặc biệt để tối ưu hóa cho các thiết bị biên (edge devices) và thiết bị di động, mô hình này mang lại khả năng suy luận mạnh mẽ ngay trên phần cứng cục bộ mà không cần phụ thuộc vào tài nguyên điện toán đám mây khổng lồ. Việc triển khai Llama 3.2 3B thường được thực hiện dễ dàng thông qua các công cụ quản lý mô hình cục bộ như [[ollama]].

## Kiến Trúc và Cơ Chế Kỹ Thuật

Trái tim của Llama 3.2 3B Instruct là kiến trúc Transformer tự hồi quy (auto-regressive) đã được tối ưu hóa. Hai đặc điểm kỹ thuật nổi bật nhất của mô hình này bao gồm:

- **Grouped-Query Attention (GQA):** Một biến thể của cơ chế chú ý giúp tăng cường khả năng mở rộng (scalability) và hiệu năng suy luận (inference performance). GQA giảm đáng kể lượng bộ nhớ VRAM cần thiết so với Multi-Head Attention truyền thống, làm cho mô hình rất phù hợp với môi trường hạn chế tài nguyên.
- **Cửa sổ ngữ cảnh siêu lớn (Massive Context Window):** Hỗ trợ độ dài ngữ cảnh lên tới 128,000 tokens. Điều này cho phép mô hình tiếp nhận và xử lý khối lượng tài liệu khổng lồ (tương đương với hàng trăm trang sách) trong một lần truy vấn, vượt trội so với nhiều đối thủ trong cùng phân khúc.

## Quy Trình Huấn Luyện và Tinh Chỉnh

Để đạt được hiệu suất cao trên một kiến trúc nhỏ gọn, Meta đã áp dụng một quy trình huấn luyện tinh vi:

1. **Pre-training:** Mô hình được huấn luyện trước trên một tập dữ liệu khổng lồ lên tới 9 nghìn tỷ tokens. Đáng chú ý, Meta đã sử dụng phương pháp chưng cất tri thức (Knowledge Distillation) từ các "người đàn anh" lớn hơn là Llama 3.1 8B và 70B. Kỹ thuật này giúp mô hình 3B phục hồi hiệu năng và học được các biểu diễn phức tạp sau quá trình thu gọn kích thước (pruning).
2. **Alignment:** Mô hình được tinh chỉnh theo chỉ dẫn (Instruction-tuned) thông qua Supervised Fine-Tuning (SFT) và Reinforcement Learning with Human Feedback (RLHF) để đảm bảo đầu ra an toàn, hữu ích và bám sát ý định của người dùng.

## Lợi Thế / Hạn Chế

**Lợi thế:**
- Hiệu suất xuất sắc trong các tác vụ tuân thủ chỉ dẫn phức tạp (Instruction following), tóm tắt văn bản, và sử dụng công cụ (Tool use/Agentic applications).
- Hỗ trợ đa ngôn ngữ chính thức (Anh, Đức, Pháp, Ý, Bồ Đào Nha, Hindi, Tây Ban Nha, và Thái).
- Khả năng làm việc xuất sắc với tài liệu dài nhờ 128k context window.

**Hạn chế:**
- Tuy mạnh mẽ trong phân khúc 3B, mô hình vẫn sẽ gặp khó khăn với các tác vụ suy luận toán học và logic hàn lâm quá phức tạp khi so sánh với các mô hình chuyên biệt về logic như họ Phi-3 của Microsoft.

## Nguồn Tham Khảo
- [[raw/articles/llama-3-2-3b-instruct-specs.md]]
- [[raw/articles/small-llm-comparison-llama-phi-gemma.md]]
