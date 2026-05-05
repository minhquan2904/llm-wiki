---
title: "Research: Cách sử dụng và tích hợp Ollama (CLI, API, IDE)"
source: "autoresearch"
date_added: 2026-05-05
tags: [research, autoresearch, ollama]
status: draft
related: ["[[ollama]]"]
summary: "Báo cáo nghiên cứu tự động về các phương thức sử dụng Ollama thông qua dòng lệnh, REST API và tích hợp IDE."
---

## Bối Cảnh
Sau khi tìm hiểu về kiến trúc của Ollama, mục tiêu nghiên cứu tiếp theo là làm rõ **cách thức vận hành** thực tế của hệ thống này: Cách người dùng điều khiển qua dòng lệnh (CLI), cách phần mềm bên thứ 3 tương tác qua API, và cách các lập trình viên sử dụng nó trong IDE.

## Phát Hiện Chính

- **Sức mạnh của CLI (`ollama run`):** CLI không chỉ dành để chat trực tiếp (REPL) mà còn cho phép tự động hóa mạnh mẽ thông qua cơ chế piping của bash (`<`, `>`). Ollama tự động tải mô hình (pull) nếu chưa có sẵn. (Nguồn: [[raw/articles/ollama-cli-usage.md]])
- **Kiến trúc API phi trạng thái (Stateless):** Ollama cung cấp REST API tại `POST /api/chat`. API này mặc định là stream data và **không lưu trữ lịch sử chat**. Lập trình viên phải tự quản lý và gửi lại toàn bộ ngữ cảnh `messages` trong mỗi request. (Nguồn: [[raw/articles/ollama-api-usage.md]])
- **Hỗ trợ IDE liền mạch (Continue.dev):** Có thể biến VS Code thành công cụ AI mạnh mẽ (giống GitHub Copilot) hoàn toàn cục bộ bằng Continue. Cấu hình phân định rõ 2 luồng: Mô hình dùng cho Chat (vd: Llama 3) và Mô hình dùng cho Autocomplete (tiên đoán code, vd: Qwen Coder). (Nguồn: [[raw/articles/ollama-ide-integration.md]])

## Thực Thể & Khái Niệm Mới
- **Concept: Stateless API Chat:** Cơ chế API không lưu lịch sử, bắt buộc client phải gửi kèm mảng lịch sử hội thoại trong payload.
- **Concept: Tab Autocomplete Model:** Mô hình AI (thường nhỏ và siêu nhanh như qwen-coder:1.5b) chuyên biệt chỉ để gợi ý code khi người dùng gõ phím, phân biệt với mô hình Chat (như llama3) dùng để hỏi đáp.
- **Tool: Continue.dev:** Một extension mã nguồn mở cho IDE (VS Code, JetBrains) đóng vai trò là client giao tiếp với các local LLM (qua Ollama).

## Nguồn Đã Nạp
- [[raw/articles/ollama-cli-usage.md]]
- [[raw/articles/ollama-api-usage.md]]
- [[raw/articles/ollama-ide-integration.md]]
