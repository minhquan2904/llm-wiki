---
title: "Tích hợp và Gọi Ollama thông qua REST API"
source: "Web Search (compiled)"
date_added: 2026-05-05
tags: [autoresearch, ollama, api, local-llm]
aliases: [Ollama REST API]
status: draft
summary: "Hướng dẫn gọi mô hình Ollama thông qua endpoint REST API `/api/chat`, giải thích cơ chế stateless và streaming."
confidence: high
---

Ollama cung cấp REST API nội bộ, mặc định chạy ở cổng `11434`. Để tạo phản hồi dạng chat, endpoint chính được sử dụng là `POST /api/chat`.

### Cách sử dụng cơ bản
Ví dụ với cURL:
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "Tại sao bầu trời màu xanh?"
    }
  ]
}'
```

### Các khái niệm kỹ thuật cốt lõi

1. **Phi trạng thái (Statelessness):** 
   Endpoint `/api/chat` là stateless. Nó không tự ghi nhớ các lượt chat trước đó. Để duy trì một cuộc trò chuyện, ứng dụng của bạn phải gửi lại toàn bộ lịch sử chat (tất cả các tin nhắn `user` và `assistant`) trong mảng `messages` của mỗi request.
   
2. **Streaming mặc định:**
   Mặc định, API sẽ trả về dữ liệu dưới dạng luồng (streaming) gồm nhiều object JSON nhỏ. Điều này giúp UI hiển thị chữ chạy (typing effect) theo thời gian thực.
   Nếu bạn muốn tắt streaming và nhận toàn bộ câu trả lời trong một lần gọi, hãy thêm thuộc tính `"stream": false` vào body của request.

3. **Vai trò (Roles):**
   - `system`: Xác định hành vi hoặc tính cách của AI (thường nằm ở đầu mảng messages).
   - `user`: Tin nhắn đầu vào từ người dùng.
   - `assistant`: Phản hồi trước đó của mô hình (dùng để giữ ngữ cảnh).

### Các tham số quan trọng
- `model` (bắt buộc): Tên mô hình (vd: "llama3.2"). Mô hình phải được tải về sẵn.
- `messages` (bắt buộc): Mảng chứa các đối tượng hội thoại.
- `stream` (tùy chọn): Boolean, set là `false` nếu muốn tắt streaming.
- `format` (tùy chọn): Định dạng kết quả đầu ra (vd: `"json"`).
- `options` (tùy chọn): Chứa các tham số chạy runtime như `temperature` (sáng tạo), `num_ctx` (độ lớn context window).

### Cấu trúc Response
Một phản hồi thành công (khi `stream: false`) có dạng:
```json
{
  "model": "llama3.2",
  "created_at": "2026-05-05T04:00:00Z",
  "message": {
    "role": "assistant",
    "content": "Bầu trời màu xanh là do hiện tượng tán xạ..."
  },
  "done": true
}
```
Khả năng tương tác qua API giúp Ollama trở thành "trái tim" cho các ứng dụng tùy chỉnh hoặc chatbot nội bộ mà không bị phụ thuộc vào cloud.
