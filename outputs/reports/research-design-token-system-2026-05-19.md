---
title: "Research: Design Token System"
source: "autoresearch"
date_added: 2026-05-19
tags: [research, autoresearch, design-tokens, design-system, frontend, figma]
status: draft
related: []
summary: "Báo cáo nghiên cứu tự động về hệ thống design token: kiến trúc 3 tầng, chuẩn W3C DTCG 2025, toolchain thực tế."
---

## Bối Cảnh

Nghiên cứu về Design Token System — nền tảng kỹ thuật cho mọi design system hiện đại. Wiki hiện chưa có bất kỳ bài nào về chủ đề này. Mục tiêu: nắm rõ khái niệm, kiến trúc phân tầng, chuẩn hóa W3C, và workflow thực tế.

**Knowledge Gaps ban đầu:**
- Design token là gì và tại sao cần thiết?
- Kiến trúc phân tầng hoạt động thế nào?
- Chuẩn DTCG có định nghĩa format JSON ra sao?
- Làm thế nào để từ Figma → production code?

---

## Phát Hiện Chính

### 1. Ba Tầng Kiến Trúc Là Cốt Lõi

(Nguồn: [[design-token-system-contentful]])

Design tokens được tổ chức theo 3 tầng:

| Tầng | Tên khác | Vai trò |
|------|----------|---------|
| Tầng 1 | Primitive / Global | Giá trị thô (hex color, px size) |
| Tầng 2 | Semantic / Alias | Ngữ nghĩa sử dụng (`text-default`, `bg-primary`) |
| Tầng 3 | Component | Override cho từng component (`button-radius`) |

**Ý nghĩa thực tế:** Thay vì designer phải chọn từ 5 màu chấp nhận được, họ chỉ cần gọi `text-default`. Design rules được nhúng vào system.

**Multi-brand theming:** Hai brand chỉ cần override tầng Component — cùng component structure, khác giá trị. Brand A: `button-radius: 4px`, Brand B: `button-radius: 50px`.

### 2. W3C DTCG Spec 2025.10 — Chuẩn JSON Chính Thức

(Nguồn: [[design-token-dtcg-spec-2025]])

Tháng 10/2025, W3C Community Group công bố phiên bản ổn định đầu tiên. Đây là cột mốc quan trọng: lần đầu tiên có chuẩn vendor-neutral để exchange tokens giữa các tool.

**Format cốt lõi:**
```json
{
  "color": {
    "$type": "color",
    "brand": {
      "primary": { "$value": "#0066cc" }
    }
  },
  "text-primary": { "$value": "{color.brand.primary}" }
}
```

**Aliasing bằng curly brace** `{path.to.token}` là cú pháp chuẩn để tham chiếu chéo giữa tầng Primitive → Semantic → Component.

**Tầm ảnh hưởng:** Figma, Adobe, Google, Amazon, Disney, Shopify, v.v. đều đã/đang triển khai.

### 3. Toolchain Thực Tế: Figma → Code

(Nguồn: [[design-token-toolchain-figma-2025]])

Không có tool nào làm tất cả — cần pipeline:

```
Figma Variables → Tokens Studio → JSON → Style Dictionary → CSS/Swift/XML
```

- **Style Dictionary**: Transform engine phổ biến nhất, xử lý naming convention và platform-specific format.
- **Tokens Studio**: Plugin Figma đóng vai trò bridge — sync tokens, quản lý themes.
- **Figma Variables**: Native nhưng không tự sync ra code; cần pipeline.

**Theme generation best practice:** Tạo file riêng cho mỗi tổ hợp theme thay vì một file chứa tất cả:
```
light_casual.css | dark_casual.css | light_business.css | dark_business.css
```

---

## Thực Thể & Khái Niệm Mới

- **Primitive Token**: Token thô, giá trị tuyệt đối (không tham chiếu token khác)
- **Semantic Token**: Token có ngữ nghĩa, tham chiếu primitive → biểu đạt *mục đích*
- **Component Token**: Token cụ thể cho component, cho phép override per-brand
- **Mode**: Biến thể giá trị trong cùng collection (light/dark)
- **Theme**: Duplicate toàn bộ token set với brand khác
- **DTCG**: Design Tokens Community Group — nhóm W3C soạn thảo chuẩn
- **Style Dictionary**: Transform engine (Amazon, open source)
- **Tokens Studio**: Plugin Figma để quản lý và export tokens
- **Hub-and-spoke**: Kiến trúc phân phối token — token là hub, các platform là spoke
- **Token Guardian**: Role governance chuyên chặn token bloat

---

## Mâu Thuẫn (nếu có)

**"Variables vs Tokens"**: Một số nguồn coi Figma Variables = Design Tokens; các nguồn khác phân biệt rõ. Consensus hiện tại: Variables là implementation trong Figma, Tokens là vendor-neutral concept. Figma Variables *có thể export thành* design tokens nhưng không tương đương hoàn toàn.

**Độ confidence**: medium — phân biệt này vẫn đang được ngành thống nhất, đặc biệt sau khi DTCG spec 2025 ra đời.

---

## Câu Hỏi Mở

1. Cách tích hợp design tokens với một CSS framework cụ thể (Tailwind v4 dùng CSS variables native — liệu có thể bỏ Style Dictionary không)?
2. Chiến lược migrate design system cũ (hard-coded values) sang token-based system?
3. Token versioning và backward compatibility khi token bị rename/deprecated?

---

## Nguồn Đã Nạp

- [[design-token-system-contentful]] — Contentful blog, kiến trúc 3 tầng, best practices
- [[design-token-dtcg-spec-2025]] — W3C DTCG spec 2025.10, JSON format chính thức
- [[design-token-toolchain-figma-2025]] — Figma Variables + Style Dictionary workflow
