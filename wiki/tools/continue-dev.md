---
title: "Continue.dev"
source: "compiled"
date_added: 2026-05-05
tags: [tool, ide, ai, coding]
aliases: [Continue]
status: canonical
related:
  - "[[ollama]]"
summary: "Tiện ích mở rộng mã nguồn mở dành cho IDE, mang lại trải nghiệm hỗ trợ lập trình AI (như GitHub Copilot) hoàn toàn cục bộ."
---

## Tổng Quan

Continue.dev là một tiện ích mở rộng (extension) mã nguồn mở dành cho các phần mềm soạn thảo mã nguồn (IDE) phổ biến như VS Code và JetBrains. Nó cho phép các nhà phát triển dễ dàng kết nối IDE của họ với các Mô hình Ngôn ngữ Lớn (LLMs), bất kể là mô hình đám mây hay chạy cục bộ trên máy cá nhân.

## Vai Trò Trong Môi Trường Phát Triển

Khi kết hợp với các trình quản lý mô hình cục bộ như Ollama, Continue đóng vai trò là "cầu nối giao diện" (client), mang lại trải nghiệm hỗ trợ lập trình tương tự GitHub Copilot nhưng hoàn toàn offline và bảo mật:

- **Tách Biệt Luồng Mô Hình:** Continue phân chia rõ ràng hai luồng công việc chính:
  - **Mô hình Trò Chuyện (Chat):** Xử lý các câu hỏi logic, giải thích mã nguồn hoặc tái cấu trúc (thường dùng các mô hình lớn như `llama3`).
  - **Mô hình Tự Động Hoàn Thiện (Autocomplete):** Chuyên trách dự đoán và gợi ý mã nguồn ngay khi người dùng đang gõ phím (sử dụng các mô hình nhỏ, siêu nhanh như `qwen2.5-coder:1.5b`).
- **Quản lý Cấu Hình Tùy Chỉnh:** Quá trình kết nối được định nghĩa minh bạch thông qua file `config.json`, cho phép lập trình viên tự do chuyển đổi giữa các nhà cung cấp (provider) và các mô hình khác nhau.

## Lợi Thế / Hạn Chế

**Lợi thế:**
- **Hoàn Toàn Bảo Mật:** Khi kết nối với local LLM, toàn bộ mã nguồn của doanh nghiệp không bao giờ rời khỏi máy trạm.
- **Linh Hoạt và Miễn Phí:** Khả năng cắm và chạy (plug-and-play) đa dạng các mô hình mã nguồn mở tiên tiến nhất mà không tốn phí đăng ký (subscription).

**Hạn chế:**
- **Phụ Thuộc Phần Cứng:** Chất lượng của trải nghiệm hoàn thiện mã thời gian thực phụ thuộc rất lớn vào sức mạnh tính toán (đặc biệt là GPU) của máy cá nhân.

## Nguồn Tham Khảo
- [[raw/articles/ollama-ide-integration.md]]
