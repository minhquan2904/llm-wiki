---
title: "Style Dictionary"
source: "compiled"
date_added: 2026-05-19
tags: [tool, design-tokens, design-system, frontend, build-tool, amazon]
status: draft
related:
  - "[[design-tokens]]"
  - "[[tailwind-design-token-theming]]"
  - "[[docker]]"
summary: "Build system mã nguồn mở của Amazon để transform design tokens từ JSON sang mọi định dạng platform-specific — CSS, Swift, XML, JS."
---

## Tổng Quan

Style Dictionary là build system mã nguồn mở do Amazon phát triển, chuyên dùng để transform [[design-tokens]] từ định dạng JSON trung tâm sang các output phù hợp với từng nền tảng: CSS custom properties, SCSS variables, iOS Swift objects, Android XML resources, và JavaScript modules.

Trong kiến trúc hub-and-spoke của design tokens, Style Dictionary đóng vai trò là transform engine — lớp trung gian chuyển đổi ngôn ngữ thiết kế trừu tượng thành ngôn ngữ kỹ thuật cụ thể mà mỗi platform hiểu được.

## Cơ Chế Transform

Style Dictionary hoạt động qua ba bước trong build pipeline:

**1. Parse:** Đọc các file `.tokens.json` (chuẩn DTCG) hoặc JSON tùy chỉnh từ thư mục tokens.

**2. Transform:** Áp dụng chuỗi transform rules lên từng token. Mỗi transform là một hàm thuần túy nhận token và trả về giá trị đã biến đổi. Ví dụ:
- `size/px → rem`: Chuyển `16px` thành `1rem` cho CSS
- `color/hex → UIColor`: Chuyển `#0066cc` thành `UIColor(red:0, green:0.4, blue:0.8, alpha:1)` cho iOS
- Name transforms: Mapping `color.brand.primary` thành `--color-brand-primary` (CSS) hoặc `colorBrandPrimary` (JS)

**3. Format & Output:** Generate file theo format tương ứng, tổ chức vào thư mục output.

## Cấu Trúc Output

Một Style Dictionary config điển hình generate output đa platform:

```
tokens/
├── css/
│   └── variables.css      # --color-brand-primary: #0066cc;
├── scss/
│   └── variables.scss     # $color-brand-primary: #0066cc;
├── ios/
│   └── tokens.swift       # static let colorBrandPrimary = UIColor(...)
├── android/
│   └── tokens.xml         # <color name="colorBrandPrimary">#0066cc</color>
└── js/
    └── tokens.js          # export const colorBrandPrimary = "#0066cc";
```

## Theme Generation

Best practice với multi-theme system là generate file riêng cho từng tổ hợp theme thay vì một file khổng lồ chứa tất cả:

```
css/
├── light-casual.css
├── dark-casual.css
├── light-business.css
└── dark-business.css
```

Mỗi file chứa đúng tập CSS variables cho tổ hợp đó. Browser load file phù hợp theo context — tối ưu cả về bundle size lẫn runtime performance.

## Tokens Studio — Figma ↔ Style Dictionary Bridge

Tokens Studio là Figma plugin đóng vai trò cầu nối giữa design tool và Style Dictionary. Luồng công việc đầy đủ:

```
Figma Variables
    ↓  [Tokens Studio plugin]
.tokens.json (DTCG format)
    ↓  [sd-transforms package]
Style Dictionary build
    ↓  [CI/CD — xem [[docker]]]
Platform outputs (CSS / Swift / XML / JS)
    ↓
Production code
```

Package `sd-transforms` do Tokens Studio cung cấp thêm các transform đặc thù cho tokens export từ Figma — xử lý các quirks trong format Figma không tương thích 100% với DTCG chuẩn.

## Figma Variables — Lưu Ý Quan Trọng

Figma hỗ trợ native variables từ 2023 với gray box indicator cho aliases. Tuy nhiên Figma Variables **không tự động sync** ra code — đây là điểm nhầm lẫn phổ biến. Pipeline qua Tokens Studio (hoặc webhook custom) là bắt buộc để maintain sync giữa Figma và codebase.

## Governance và Token Bloat

Khi design system scale, Style Dictionary config có thể phình to không kiểm soát — hiện tượng gọi là *token bloat*. Các role governance cần thiết:

| Role | Trách nhiệm |
|------|-------------|
| Design System Lead | Định hướng kiến trúc token |
| Token Guardian | Review token mới, chặn duplicate và inconsistency |
| UX Designers / Devs | Sử dụng và đề xuất token theo quy trình |

Token Guardian là role thực tế — không có người này, các team thường tạo token tùy tiện dẫn đến hàng trăm biến thể không nhất quán.

## Liên Hệ Với Hệ Sinh Thái Rộng Hơn

Style Dictionary là một trong nhiều transform engines, nhưng phổ biến nhất do được Amazon maintain và có ecosystem plugins lớn. Knapsack là alternative thương mại tích hợp sâu hơn với design system documentation. Supernova và Zeroheight cũng hỗ trợ transform nhưng theo hướng platform-as-a-service.

Với các dự án đơn giản không cần multi-platform, Tailwind CSS v4 sử dụng CSS custom properties native có thể thay thế một phần vai trò của Style Dictionary — nhưng mất đi khả năng generate Swift/XML cho mobile platforms. Tailwind directive `@theme` thực chất là một transform engine built-in cho web: nhận CSS variables, sinh utility classes tự động theo namespace prefix. Chi tiết pattern triển khai trong stack Tailwind + shadcn/ui xem tại [[tailwind-design-token-theming]].

Trong pipeline production multi-platform, Style Dictionary và `@theme` không cạnh tranh trực tiếp — Style Dictionary có thể generate ra `@theme.css` thay vì `variables.css` truyền thống, để Tailwind tiếp tục consume từ điểm đó.
