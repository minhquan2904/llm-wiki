---
title: "Design Tokens Format Module 2025.10 — W3C DTCG Specification"
source: "https://www.designtokens.org/tr/drafts/format/"
date_added: 2026-05-19
tags: [autoresearch, design-tokens, DTCG, W3C, specification, standard]
aliases: []
status: draft
summary: "Chuẩn JSON chính thức cho design tokens của W3C Community Group (DTCG), phiên bản ổn định đầu tiên 2025.10."
confidence: high
---

# Design Tokens Format Module 2025.10 — DTCG Spec

## Tổng Quan

W3C Design Tokens Community Group (DTCG) công bố phiên bản ổn định đầu tiên vào tháng 10/2025. Chuẩn này cung cấp định dạng vendor-neutral để chia sẻ design decisions giữa các tool và platform.

Đã được áp dụng bởi: Figma, Adobe, Sketch, Framer, Penpot, Tokens Studio, Knapsack, Supernova, zeroheight, và tổ chức từ Amazon, Google, Microsoft, Meta, Shopify, Disney, GM, v.v.

## File Format

- MIME type: `application/design-tokens+json`
- File extension: `.tokens` hoặc `.tokens.json`
- Format: JSON

## Cấu Trúc Token

```json
{
  "tokenName": {
    "$value": "<giá trị>",
    "$type": "<loại token>",
    "$description": "<mô tả tùy chọn>",
    "$extensions": {},
    "$deprecated": true
  }
}
```

- `$value`: Bắt buộc
- `$type`: Bắt buộc (trừ khi kế thừa từ group cha)

## Các Loại Token ($type)

| Type | Mô tả | Ví dụ value |
|------|--------|-------------|
| `color` | Màu sắc với colorSpace, components, hex | `"#0066cc"` |
| `dimension` | Đo lường khoảng cách | `"16px"`, `"1rem"` |
| `fontFamily` | Font name hoặc mảng tên | `["Inter", "sans-serif"]` |
| `fontWeight` | 1–1000 hoặc string | `700`, `"bold"` |
| `duration` | Thời gian animation | `"200ms"`, `"0.2s"` |
| `cubicBezier` | Đường cong animation | `[0.4, 0, 0.2, 1]` |
| `number` | Giá trị số không đơn vị | `1.5` |

## Composite Types (Token kết hợp)

| Type | Các thuộc tính |
|------|----------------|
| `border` | color + width + style |
| `shadow` | color + offsetX + offsetY + blur + spread |
| `transition` | duration + delay + timingFunction |
| `typography` | fontFamily + fontSize + fontWeight + lineHeight |
| `gradient` | mảng color stops với positions |
| `strokeStyle` | string preset hoặc dash pattern |

## Groups & Tổ Chức Phân Cấp

Groups tổ chức tokens theo cây phân cấp mà không ràng buộc kiểu:

```json
{
  "color": {
    "$type": "color",
    "brand": {
      "primary": { "$value": "#0066cc" },
      "secondary": { "$value": "#ff6600" }
    }
  }
}
```

- `$type` khai báo ở group → kế thừa xuống children
- `$extends`: Deep merge với group khác (override selectively)
- `$root`: Base variant trong group

## References & Aliasing

**Cú pháp curly brace** (tham chiếu toàn bộ `$value`):
```json
{
  "color-blue-500": { "$value": "#0066cc" },
  "text-primary": { "$value": "{color-blue-500}" }
}
```

**Cú pháp JSON Pointer** (truy cập thuộc tính cụ thể):
```json
{ "$ref": "#/path/to/specific/value" }
```

**Quy tắc:**
- Tên token không được bắt đầu bằng `$`
- Không chứa `{`, `}`, hoặc `.` trong tên
- Circular references không hợp lệ
- Tools phải bảo toàn `$extensions` từ vendor khác
