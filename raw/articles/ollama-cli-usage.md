---
title: "Hướng dẫn sử dụng Ollama qua CLI"
source: "Web Search (compiled)"
date_added: 2026-05-05
tags: [autoresearch, ollama, cli, local-llm]
aliases: [Ollama CLI Usage]
status: draft
summary: "Tổng hợp các cách sử dụng lệnh `ollama run` để tương tác, chạy kịch bản tự động hóa và quản lý mô hình."
confidence: high
---

Lệnh `ollama run` là phương thức chính để tương tác với các mô hình thông qua giao diện dòng lệnh (CLI). Nó cung cấp sự linh hoạt từ trò chuyện tương tác đến tự động hóa script.

### 1. Trò chuyện tương tác (Interactive Chat - REPL)
Để khởi động phiên chat tương tác, chỉ cần truyền tên mô hình:
```bash
ollama run llama3.2
```
Điều này sẽ mở ra một dấu nhắc (prompt) để bạn trò chuyện trực tiếp.
- Để thoát: Nhập `/bye` hoặc nhấn `Ctrl+D`.
- Để xóa ngữ cảnh chat hiện tại: Nhập `/clear`.
- Để xem các lệnh hỗ trợ trong phiên chat: Nhập `/?`.

### 2. Thực thi một lần (Single-Prompt Execution)
Nếu bạn chỉ muốn hỏi một câu và nhận câu trả lời ngay lập tức (phù hợp cho script), hãy truyền câu hỏi trực tiếp:
```bash
ollama run llama3.2 "Thủ đô của Pháp là gì?"
```

### 3. Piping và Redirection
Ollama cực kỳ mạnh mẽ khi kết hợp với các công cụ shell khác bằng toán tử pipe (`|`) và redirect (`<`, `>`):
- **Xử lý/Tóm tắt một file:**
  ```bash
  ollama run llama3.2 "Hãy tóm tắt văn bản sau:" < document.txt
  ```
- **Lưu câu trả lời ra file:**
  ```bash
  ollama run llama3.2 "Viết một bài thơ về vũ trụ" > poem.txt
  ```
- **Kết hợp lệnh khác:**
  ```bash
  cat data.json | ollama run llama3.2 "Giải thích cấu trúc JSON này"
  ```

### 4. Truyền câu hỏi nhiều dòng
Để truyền một prompt nhiều dòng trong bash, bạn có thể bọc bằng dấu ba nháy kép:
```bash
ollama run llama3.2 """
Đây là prompt nhiều dòng:
1. Ý thứ nhất
2. Ý thứ hai
Hãy giải thích chi tiết.
"""
```

### 5. Quản lý mô hình
- **Tải mô hình (pull):** `ollama pull <model-name>`
- **Danh sách mô hình đã tải:** `ollama ls`
- **Các mô hình đang chạy:** `ollama ps`
- **Dừng mô hình đang chạy:** `ollama stop <model-name>`
- **Xóa mô hình:** `ollama rm <model-name>`

**Lưu ý:** Nếu bạn chạy `ollama run <model>` mà mô hình chưa có trong máy, Ollama sẽ tự động tải nó về (tương tự như `docker run`).
