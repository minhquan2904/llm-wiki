---
title: "So Sánh Small LLMs: Llama 3.2 vs Phi-3.5 vs Gemma 2"
source: "compiled"
date_added: 2026-05-05
tags: [comparison, ai, slm, llm]
aliases: [Llama 3.2 vs Phi 3.5 vs Gemma 2]
status: draft
related:
  - "[[llama-3.2-3b-instruct]]"
  - "[[ollama-vs-vllm-vs-lmstudio]]"
summary: "Phân tích và đối chiếu hiệu năng của ba mô hình ngôn ngữ nhỏ gọn hàng đầu: Llama 3.2 3B, Phi-3.5 Mini và Gemma 2 2B."
---

## Bối Cảnh

Xu hướng phát triển trí tuệ nhân tạo đang chứng kiến sự trỗi dậy của các Mô hình Ngôn ngữ Nhỏ gọn (Small Language Models - SLMs). Những mô hình này được thiết kế để chạy trực tiếp trên thiết bị cá nhân (on-device) nhằm tiết kiệm chi phí, đảm bảo quyền riêng tư và hoạt động ngoại tuyến. Ba đại diện tiêu biểu nhất trong phân khúc từ 2 đến dưới 4 tỷ tham số hiện nay là Llama 3.2 3B Instruct (Meta), Phi-3.5 Mini (Microsoft) và Gemma 2 2B (Google).

## Bảng So Sánh

| Tiêu chí | Llama 3.2 3B Instruct | Phi-3.5 Mini | Gemma 2 2B |
| :--- | :--- | :--- | :--- |
| **Nhà phát triển** | Meta | Microsoft | Google |
| **Cửa sổ ngữ cảnh** | 128,000 tokens | 128,000 tokens | 8,192 tokens |
| **Định hướng tối ưu** | Tuân thủ chỉ dẫn, tóm tắt, sử dụng công cụ (Tool use) | Suy luận logic, toán học, lập trình | Hiệu suất siêu gọn nhẹ, cân bằng kích thước/khả năng |
| **Thế mạnh lõi** | Agentic tasks, xử lý tài liệu cực dài | Tư duy logic hàn lâm (Logic/Math benchmarks) | Triển khai trên các thiết bị cực kỳ hạn chế phần cứng |

## Phân Tích Chuyên Sâu

### Sức mạnh Suy luận và Toán học
**Phi-3.5 Mini** là mô hình dẫn đầu khi xét đến các bài kiểm tra học thuật đòi hỏi tư duy phân tích sâu. Nhờ phương pháp huấn luyện đặc biệt tập trung vào dữ liệu chất lượng cao (thường là dữ liệu tổng hợp như "textbook-like data"), mô hình của Microsoft thường ghi điểm nhỉnh hơn các đối thủ trong các bài kiểm tra như GSM8K, ARC-Challenge, và MMLU. Đây là lựa chọn lý tưởng cho các ứng dụng mang tính giáo dục hoặc giải quyết vấn đề logic.

### Ứng dụng Thực dụng và Ngữ cảnh Dài
**Llama 3.2 3B Instruct** tỏa sáng trong các ứng dụng thực tế. Meta đã định vị mô hình này cho các tác vụ mang tính trợ lý ảo (assistant-like) và đặc biệt là khả năng kết nối công cụ (agentic workflows). Điểm cộng lớn nhất là khả năng xử lý khối lượng ngữ cảnh khổng lồ (128k tokens) ngang bằng với Phi-3.5, biến nó thành lựa chọn hàng đầu cho các bài toán tóm tắt tài liệu dài hay trích xuất thông tin (RAG).

### Tính Gọn Nhẹ Cực Đoan
**Gemma 2 2B** chọn một lối đi khác khi giới hạn cửa sổ ngữ cảnh ở mức 8K tokens để đổi lấy sự nhẹ bén và khả năng tối ưu hóa kiến trúc xuất sắc của Google. Nó đạt được tỷ lệ hiệu năng trên kích thước (performance-to-size ratio) cực kỳ ấn tượng, thường đánh bại nhiều mô hình lớn thế hệ cũ trên các benchmarks. Đây là sự lựa chọn tối ưu khi phần cứng triển khai có bộ nhớ RAM/VRAM thực sự eo hẹp.

## Kết Luận

Việc lựa chọn mô hình phụ thuộc hoàn toàn vào bài toán thực tế:
- Chọn **Phi-3.5 Mini** nếu ứng dụng đòi hỏi khả năng lập luận, toán học và lập trình mạnh mẽ.
- Chọn **Llama 3.2 3B Instruct** cho các tác vụ cần phân tích tài liệu dài, xây dựng hệ thống Agentic phức tạp hoặc tuân thủ các luồng hướng dẫn chặt chẽ.
- Chọn **Gemma 2 2B** khi đối mặt với những ràng buộc khắt khe nhất về bộ nhớ và tài nguyên thiết bị mà vẫn cần một AI có năng lực tổng quát ổn định.

## Nguồn Tham Khảo
- [[raw/articles/small-llm-comparison-llama-phi-gemma.md]]
