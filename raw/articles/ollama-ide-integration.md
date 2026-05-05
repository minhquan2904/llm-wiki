---
title: "Tích hợp Ollama với IDE (Ví dụ: Continue.dev)"
source: "Web Search (compiled)"
date_added: 2026-05-05
tags: [autoresearch, ollama, ide, continue.dev, coding]
aliases: [Ollama IDE Integration]
status: draft
summary: "Hướng dẫn kết nối Ollama với IDE (VS Code) thông qua extension Continue.dev để hỗ trợ lập trình hoàn toàn offline."
confidence: high
---

Việc kết hợp Ollama với các phần mềm soạn thảo mã (IDE) như VS Code là một trong những use-case phổ biến nhất. Tiêu biểu là việc sử dụng extension **Continue.dev** để tạo ra một môi trường lập trình có AI hỗ trợ hoàn toàn cục bộ, riêng tư và miễn phí.

### Các bước tích hợp Continue.dev với Ollama

**1. Chuẩn bị mô hình**
Trước tiên, bạn cần tải về các mô hình phù hợp từ terminal:
- Mô hình để trò chuyện/hỏi đáp code (Chat): `ollama pull llama3.1` (hoặc `deepseek-coder`).
- Mô hình để tự động hoàn thiện code (Autocomplete): `ollama pull qwen2.5-coder:1.5b`.

**2. Cài đặt Continue.dev**
Mở VS Code, vào mục Extensions, tìm kiếm "Continue" và cài đặt.

**3. Cấu hình kết nối**
Sau khi cài đặt, Continue thường tự động nhận diện các mô hình Ollama đang chạy cục bộ (Autodetect). Bạn có thể chọn mô hình từ danh sách thả xuống ở thanh bên (sidebar) của Continue.
Nếu việc tự động nhận diện thất bại, bạn có thể chỉnh sửa file `config.json` của Continue thủ công bằng cách thêm cấu hình:

```json
{
  "models": [
    {
      "title": "Ollama Llama 3.1",
      "provider": "ollama",
      "model": "llama3.1"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Ollama Qwen Coder",
    "provider": "ollama",
    "model": "qwen2.5-coder:1.5b"
  }
}
```

### Xử lý sự cố (Troubleshooting)
- **Đảm bảo Ollama đang chạy:** Mở terminal và gõ `curl http://localhost:11434/version`. Nếu có phản hồi, Ollama đang hoạt động.
- **Tên mô hình chính xác:** Tên cấu hình trong `config.json` phải khớp tuyệt đối với tên trả về khi gõ lệnh `ollama ls`.
- **Tải lại Continue:** Nếu sửa file cấu hình mà chưa thấy tác dụng, hãy dùng Command Palette của VS Code (`Ctrl+Shift+P`) và gọi lệnh **"Continue: Reload"**.
