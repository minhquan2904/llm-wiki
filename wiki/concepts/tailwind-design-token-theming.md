---
title: "Tailwind Design Token Theming"
source: "compiled"
date_added: 2026-05-19
tags: [concept, design-tokens, tailwind, shadcn, theming, css-variables, frontend]
status: draft
related:
  - "[[design-tokens]]"
  - "[[style-dictionary]]"
  - "[[dom-performance-optimization]]"
summary: "Pattern triển khai design tokens trong stack Tailwind CSS + shadcn/ui, kết hợp CSS custom properties và cơ chế chuyển theme runtime không cần rebuild."
---

## Tổng Quan

Tailwind Design Token Theming là pattern triển khai [[design-tokens]] trực tiếp trong stack Tailwind CSS + shadcn/ui, sử dụng CSS custom properties làm transport layer thay vì phụ thuộc vào external transform engine như [[style-dictionary]]. Cách tiếp cận này khả thi nhờ Tailwind v4 đưa toàn bộ design tokens vào CSS qua directive `@theme`, và shadcn/ui chuẩn hóa convention semantic token pairs (surface + foreground).

Điểm cốt lõi: vì tokens là CSS variables, **chuyển theme tại runtime không cần rebuild** — chỉ thay class hoặc attribute trên `<html>`, browser re-evaluate cascade, mọi utility class tự động cập nhật.

## Tiến Hóa Pattern Qua Ba Thế Hệ

### Pattern A — Tailwind v3 + `tailwind.config.ts` (Legacy)

CSS variables khai báo trong `:root`, `tailwind.config.ts` map từng biến vào color system. Pattern này yêu cầu wrap mỗi biến trong `hsl(var(--token))` để Tailwind có thể compose với alpha modifier:

```typescript
colors: {
  popover: {
    DEFAULT: "hsl(var(--popover))",
    foreground: "hsl(var(--popover-foreground))",
  },
}
```

CSS variables dùng **HSL space-separated values** (`210 40% 98%`) thay vì `hsl(210, 40%, 98%)` để hỗ trợ Tailwind opacity modifier (`bg-popover/50`).

### Pattern B — Tailwind v4 + `@theme` (Modern)

Tailwind v4 loại bỏ `tailwind.config.ts`. Toàn bộ config nằm trong CSS qua directive `@theme`. Mỗi token có namespace prefix sẽ tự sinh utility class tương ứng — `--color-primary` sinh `bg-primary`, `text-primary`, `border-primary`.

```css
@import "tailwindcss";

@theme {
  --color-primary: oklch(0.205 0 0);
  --radius-md: 0.5rem;
}
```

Khác biệt với khai báo trong `:root`: `@theme` tạo CSS variables **và** sinh utility, `:root` chỉ tạo variables. Đây là cơ chế khiến Tailwind v4 trở thành một transform engine built-in cho web — vai trò trước đây cần Style Dictionary đảm nhiệm.

### Pattern C — shadcn/ui + `@theme inline` (Hybrid Best Practice)

shadcn/ui tách layer logic ra khỏi layer expose-to-Tailwind. Tokens semantic (`--primary`) khai báo trong `:root` và `.dark`. `@theme inline` chỉ expose chúng cho Tailwind:

```css
:root {
  --primary: oklch(0.205 0 0);
}

.dark {
  --primary: oklch(0.922 0 0);
}

@theme inline {
  --color-primary: var(--primary);
}
```

`inline` keyword là yếu tố quyết định: nó buộc Tailwind resolve biến tại use-site (scope hiện tại của element), không phải tại define-site. Nếu thiếu `inline`, dark mode sẽ không hoạt động đúng vì utility class sẽ dùng giá trị `--primary` được resolve khi build, không phải khi render.

## Surface + Foreground Pair Convention

shadcn/ui chuẩn hóa quy ước đặt tên: mỗi surface color luôn đi kèm foreground color cho text/icon hiển thị trên surface đó. Suffix `-background` bị omit cho token surface — `primary` ngầm hiểu là background, `primary-foreground` là text trên đó:

| Token | Vai trò |
|-------|---------|
| `background` / `foreground` | App shell, text mặc định |
| `card` / `card-foreground` | Surface elevated (panel, card) |
| `primary` / `primary-foreground` | High-emphasis action (button mặc định) |
| `secondary` / `secondary-foreground` | Lower-emphasis action |
| `muted` / `muted-foreground` | Surface mờ (placeholder, helper text) |
| `accent` / `accent-foreground` | Interactive state (ghost button, hover) |
| `destructive` | Error emphasis |
| `border`, `input`, `ring` | Separator, form control, focus indicator |

Convention này loại bỏ phải nhớ pair: chỉ cần biết `primary` → biết ngay tồn tại `primary-foreground`. shadcn cũng derive toàn bộ radius scale từ một biến gốc `--radius` qua `calc()`, tạo single source of truth cho corner rounding.

## Hai Cơ Chế Switch Theme — Class vs Attribute

**`.dark` class** (shadcn official, đơn giản): hai mode light/dark. CSS variables override trong `.dark { ... }`. Tailwind config: `darkMode: ["class"]`.

**`data-theme` attribute** (Lloyd Richards Lab #037, linh hoạt): N theme variants. Mỗi theme một file CSS với selector `html[data-theme="dark-professional"]`. Tailwind config: `darkMode: ["class", '[data-theme^="dark-"]']` — prefix selector `^=` cho phép vô hạn dark variants.

Tổ hợp brand × mode hoạt động qua naming convention `{mode}-{brand}` (e.g. `light-classic`, `dark-professional`). Library `next-themes` hỗ trợ cả hai cơ chế qua prop `attribute="class"` vs `attribute="data-theme"`, đồng thời handle persist trong localStorage và sync với `prefers-color-scheme`.

Tổ hợp này còn cần `color-scheme: dark;` trong mỗi dark theme variant — hint cho browser render native UI elements (scrollbar, form controls) theo dark scheme.

## Khi Nào Cần [[style-dictionary]]?

Tailwind `@theme` là transform engine built-in **chỉ cho web**. Pipeline production thực tế:

```
Figma → Tokens Studio → JSON → Style Dictionary → @theme.css → Tailwind utilities
                                       ↓
                              Swift / XML / iOS / Android
```

Quyết định bỏ Style Dictionary phụ thuộc vào scope platform:

| Use case | Cần Style Dictionary? |
|----------|----------------------|
| Web-only solo/small team | Không — `@theme` đủ |
| Multi-brand white-label web | Không — `data-theme` đủ linh hoạt |
| Design system multi-platform (Web + iOS + Android + Figma sync) | Có — Style Dictionary transform JSON → Swift/XML |
| Token versioning + governance qua Figma → code | Có — Style Dictionary handle naming/transform với audit trail |

Style Dictionary và Tailwind `@theme` **không cạnh tranh trực tiếp**: một là producer (transform JSON → CSS), một là consumer (đọc CSS → sinh utility). Stack hợp nhất khi Style Dictionary generate ra `@theme.css` thay vì `variables.css` truyền thống.

## Liên Hệ Với Hiệu Năng

Vì design tokens là CSS variables, runtime overhead gần như zero — browser đã tối ưu cascade evaluation. Chuyển theme chỉ trigger style recalculation, không trigger layout reflow (xem [[dom-performance-optimization]]). FOUC khi initial render là vấn đề chính: `next-themes` xử lý qua inline script chạy trước React hydration, set class/attribute ngay khi DOM ready.

OKLCH color space (default trong shadcn/ui v4) cải thiện perceptual consistency giữa light/dark — màu trông tương đương về độ sáng cảm nhận khi đảo mode, khắc phục bias của HSL khi pha trộn lightness.
