# 🧠 Second Brain của Tôi

> Hệ thống quản lý kiến thức cá nhân được vận hành bởi AI, dựa trên **Phương pháp Karpathy LLM Wiki**. Tại đây, các AI agent sẽ tự động viết, cấu trúc và bảo trì một wiki trên Obsidian từ các dữ liệu thô mà tôi thu thập.

## 🌟 Tổng Quan

Đây là kho lưu trữ kiến thức cá nhân của tôi. Thay vì tự tay ghi chép và sắp xếp mọi thứ, tôi đóng vai trò là "người thu thập" (curator), còn AI sẽ làm những việc nặng nhọc như đọc hiểu, tổng hợp và liên kết thông tin.

Vòng lặp cốt lõi:

1. **Tôi nạp nguồn** (bài viết, paper, tweet, video) vào thư mục `raw/`.
2. **AI biên dịch** chúng thành các bài wiki có cấu trúc, liên kết chặt chẽ trong thư mục `wiki/`.
3. **Tôi hỏi đáp** với kho kiến thức này, và AI sẽ trả lời dựa trên chính những gì tôi đã lưu trữ.
4. **Kiến thức tích lũy** — mỗi chu kỳ giúp hệ thống ngày càng thông minh và phong phú hơn.

## 📂 Kiến Trúc Thư Mục

```text
Second-brain/
├── raw/                 ← Tài liệu gốc. AI KHÔNG BAO GIỜ chỉnh sửa thư mục này.
├── wiki/                ← Kiến thức đã biên dịch. AI duy trì 100%.
├── outputs/             ← Các báo cáo, tóm tắt và nội dung do AI tạo ra.
├── sessions/            ← Nhật ký hội thoại (chat sessions) từ các dự án.
└── AGENTS.md            ← Sổ tay vận hành và bộ quy tắc cốt lõi cho các AI Agent.
```

## 🔄 Các Workflow Chính

Hệ thống của tôi được trang bị các workflow tự động sau:

| Lệnh            | Chức Năng                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| `/ingest`       | Nạp tài liệu gốc (URL, file) vào `raw/` với frontmatter chuẩn.                                       |
| `/compile`      | Đọc tài liệu gốc và biên dịch thành bài wiki. Có hệ thống **phát hiện mâu thuẫn**.                   |
| `/ask`          | Hỏi đáp dựa trên kiến thức trong wiki.                                                               |
| `/save`         | **Chat-to-Wiki**: Trích xuất những insight hay từ cuộc trò chuyện và lưu thẳng vào wiki.             |
| `/cleanup`      | Kiểm tra sức khỏe wiki (giọng văn, cấu trúc, liên kết) và quét các mâu thuẫn tồn đọng.               |
| `/breakdown`    | Quét wiki tìm các khái niệm còn thiếu và đề xuất tạo bài mới.                                        |
| `/autoresearch` | **Nghiên cứu tự động**: Tự động tìm kiếm web, đánh giá nguồn, nạp và tổng hợp báo cáo về một chủ đề. |

## 🛡️ Tiêu Chuẩn Chất Lượng

Để wiki không biến thành một "bãi rác" thông tin, AI phải tuân thủ các quy tắc nghiêm ngặt trong `AGENTS.md`:

- **Phát hiện mâu thuẫn:** AI không bao giờ âm thầm ghi đè thông tin xung đột. Nó sẽ giữ lại cả hai luồng thông tin và đặt cảnh báo `[!warning]` để tôi duyệt.
- **Đọc lại trước khi cập nhật:** AI bắt buộc phải đọc toàn bộ bài viết trước khi chỉnh sửa.
- **Giới hạn kích thước:** Các bài viết được giữ ở độ dài 15-120 dòng. Chủ đề nào quá lớn sẽ được tách ra bài riêng.
- **Giọng văn Bách khoa toàn thư:** Viết khách quan, trung lập, luôn có dẫn chứng nguồn, không dùng ngôn ngữ "blog" hay bình luận cá nhân.

## 🛠️ Công Nghệ Sử Dụng

- **[Obsidian](https://obsidian.md/)**: Giao diện chính để tôi xem, tìm kiếm và điều hướng qua các file Markdown.
- **LLM Agents**: Gemini / Claude / Cursor đóng vai trò như bộ não để xử lý, viết và duy trì nội dung.

---

_Đây là một bộ não thứ hai "sống" — nó đang học hỏi và phát triển mỗi ngày cùng với tôi._
