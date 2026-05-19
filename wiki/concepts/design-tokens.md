---
title: "Design Tokens"
source: "compiled"
date_added: 2026-05-19
tags: [concept, design-system, frontend, css, figma, W3C]
status: draft
related:
  - "[[style-dictionary]]"
  - "[[tailwind-design-token-theming]]"
  - "[[dom-performance-optimization]]"
  - "[[jotai]]"
summary: "Hệ thống lưu trữ các quyết định thiết kế dưới dạng dữ liệu có cấu trúc, đóng vai trò nguồn sự thật duy nhất cho mọi nền tảng trong một design system."
---

## Định Nghĩa

Design token là đơn vị dữ liệu nhỏ nhất và không thể phân tách của một design system, lưu trữ từng quyết định thiết kế riêng lẻ — màu sắc, typography, khoảng cách, border radius, thời gian animation — dưới dạng cặp key-value có cấu trúc. Chúng được lưu trong file JSON để có thể transform thành bất kỳ định dạng nào mà nền tảng đích yêu cầu: CSS custom properties, Swift objects, Android XML, hay Figma variables.

Khác với hard-coded values rải rác trong codebase, design tokens là nguồn sự thật duy nhất (single source of truth). Khi màu brand thay đổi, chỉ một giá trị trong token file cần cập nhật — tất cả platform tự động phản ánh thay đổi đó sau lần build tiếp theo.

## Kiến Trúc Ba Tầng

Hệ thống token hiệu quả được tổ chức thành ba tầng phân cấp, mỗi tầng tham chiếu đến tầng bên dưới.

**Tầng 1 — Primitive Tokens (Base layer):** Lưu trữ giá trị thô tuyệt đối. Tầng này không tham chiếu đến token nào khác, chỉ khai báo các giá trị cốt lõi của brand như toàn bộ bảng màu, thang khoảng cách, và bộ font. Ví dụ: `color-blue-500: #0066cc`. Một brand palette thường có vài chục đến vài trăm primitive tokens.

**Tầng 2 — Semantic Tokens (Alias layer):** Tham chiếu đến primitive tokens và bổ sung ngữ nghĩa sử dụng. `text-default` không chỉ nói màu gì mà còn nói *khi nào* và *tại đâu* dùng màu đó. Tầng này biến đổi tập hợp giá trị kỹ thuật thành ngôn ngữ thiết kế. Designer không cần chọn từ 5 màu chấp nhận được — họ chỉ cần gọi `text-default`, và quyết định thiết kế đã được nhúng vào system.

**Tầng 3 — Component Tokens (Application layer):** Tham chiếu đến semantic tokens và dành riêng cho từng UI component. `button-background-primary` có thể trỏ đến `color-action-primary` ở tầng semantic. Tầng này là điểm override cho multi-brand theming: Brand A có `button-radius: 4px`, Brand B có `button-radius: 50px` — cùng component structure, khác giá trị, không cần tạo biến thể.

## Modes, Collections và Themes

**Mode** là biến thể giá trị trong cùng một token collection. Token `background-surface` mang giá trị `#ffffff` trong light mode và `#1a1a1a` trong dark mode — cùng tên token, khác giá trị theo context.

**Token Collection** là nhóm token chia sẻ cùng một tập modes. Color collection thường có light/dark modes. Typography collection thường không cần.

**Theme** là việc duplicate toàn bộ token set với giá trị khác nhau cho từng brand. Hai brand có thể dùng chung một component library nhưng nhận các giá trị token khác nhau thông qua theme switching — không cần fork code, không cần tạo variants.

## Chuẩn W3C DTCG 2025

W3C Design Tokens Community Group (DTCG) công bố phiên bản chuẩn ổn định đầu tiên vào tháng 10/2025. Đây là định dạng JSON vendor-neutral đầu tiên được ngành thống nhất, được áp dụng bởi Figma, Adobe, Sketch, Google, Amazon, Shopify và nhiều tổ chức khác.

Cấu trúc token chuẩn DTCG:

```json
{
  "color": {
    "$type": "color",
    "brand": {
      "primary": { "$value": "#0066cc" }
    }
  },
  "text-primary": {
    "$value": "{color.brand.primary}",
    "$description": "Màu chữ chính trong toàn bộ UI"
  }
}
```

Mỗi token bắt buộc phải có `$value`. `$type` bắt buộc hoặc kế thừa từ group cha. Aliasing giữa các tầng dùng cú pháp curly brace: `{path.to.token}`.

Các loại token chuẩn bao gồm: `color`, `dimension`, `fontFamily`, `fontWeight`, `duration`, `cubicBezier`, `number`. Composite types như `border`, `shadow`, `typography`, `gradient` kết hợp nhiều thuộc tính vào một token.

## Naming Convention

Tên token hiệu quả theo pattern phân cấp `category/role/variant`. Ví dụ: `color/background/surface`, `spacing/component/button-padding`. Contentful đề xuất tiếp cận lưới hai chiều: trục X cho state đơn giản (default, hover, active), trục Y cho biến thể phức tạp — tránh tổ hợp bùng nổ như `disabled-hover` khi không cần thiết.

Quy tắc DTCG: tên token không được bắt đầu bằng `$`, không chứa `{`, `}`, hoặc `.`.

## Liên Hệ Với CSS Custom Properties

Design tokens ở tầng Semantic thường được transform thành CSS custom properties — cơ chế nền tảng cho theming trong browser. Sự khác biệt: CSS custom properties là implementation trên một platform cụ thể, design tokens là concept trừu tượng độc lập platform. Hiệu năng của CSS custom properties trong context của [[dom-performance-optimization]] liên quan trực tiếp đến cách tokens được generate và áp dụng.

Tương tự như [[jotai]] quản lý state theo mô hình nguyên tử — mỗi atom là đơn vị nhỏ nhất — design tokens áp dụng triết lý tương đương cho design decisions: mỗi token là đơn vị nhỏ nhất không thể phân tách thêm.

## Phân Phối và Toolchain

Tokens là trung tâm của kiến trúc hub-and-spoke. Từ file JSON nguồn, các transform engine (phổ biến nhất là [[style-dictionary]]) generate ra output phù hợp từng platform. Figma Variables hỗ trợ native aliasing kể từ 2023, nhưng không tự sync ra code — cần pipeline qua Tokens Studio plugin.

Với stack web-only, Tailwind CSS v4 đưa toàn bộ design tokens vào CSS qua directive `@theme` — đóng vai trò transform engine built-in, có thể thay thế Style Dictionary trong nhiều dự án. Pattern triển khai cụ thể trong stack Tailwind + shadcn/ui (bao gồm cơ chế `@theme inline`, surface + foreground convention, switching qua `.dark` class vs `data-theme` attribute) được trình bày chi tiết trong [[tailwind-design-token-theming]].

> [!note] Tokens vs Figma Variables
> Figma Variables là implementation *trong* Figma. Design tokens là concept vendor-neutral. Variables có thể export thành tokens nhưng không tương đương — tokens tồn tại độc lập với bất kỳ design tool cụ thể nào.
