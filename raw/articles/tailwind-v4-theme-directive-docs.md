---
title: "Tailwind CSS v4 — @theme Directive (Official Docs)"
source: "https://tailwindcss.com/docs/theme"
date_added: 2026-05-19
tags: [autoresearch, design-tokens, tailwind, tailwind-v4, css-variables]
aliases: []
status: draft
summary: "Tài liệu chính thức Tailwind v4 về @theme directive — cơ chế CSS-first đưa design tokens thành utility classes tự động."
confidence: high
---

# Tailwind CSS v4 — @theme Directive (Official Documentation)

## @theme Directive Là Gì?

`@theme` là directive đặc biệt của Tailwind v4 để khai báo **theme variables** — không chỉ là CSS variables thường mà còn ra lệnh cho Tailwind sinh utility classes tương ứng. Đây là thay đổi kiến trúc lớn nhất từ v3 sang v4: **chuyển từ JavaScript config (`tailwind.config.ts`) sang CSS config (`globals.css`)**.

**Khác biệt giữa `@theme` và `:root`:**
- `@theme` → tạo CSS variables **+** sinh utility classes
- `:root` → chỉ tạo CSS variables, không sinh utility
- Dùng `@theme` cho design tokens map tới utility; dùng `:root` cho biến không cần utility

## Syntax Cơ Bản

```css
@import "tailwindcss";

@theme {
  --color-mint-500: oklch(0.72 0.11 178);
  --font-script: Great Vibes, cursive;
  --spacing: 0.25rem;
}
```

Tự động sinh utilities: `bg-mint-500`, `text-mint-500`, `fill-mint-500`, `font-script`, `px-4`, `m-8`...

## Namespaces & Utility Mapping

| Namespace | Utility sinh ra | Ví dụ |
|-----------|-----------------|-------|
| `--color-*` | Color utilities | `bg-red-500`, `text-sky-300` |
| `--font-*` | Font families | `font-sans`, `font-serif` |
| `--text-*` | Font sizes | `text-xl`, `text-2xl` |
| `--font-weight-*` | Font weights | `font-bold` |
| `--tracking-*` | Letter spacing | `tracking-wide` |
| `--leading-*` | Line heights | `leading-tight` |
| `--radius-*` | Border radius | `rounded-sm`, `rounded-lg` |
| `--shadow-*` | Box shadows | `shadow-md` |
| `--blur-*` | Blur filters | `blur-md` |
| `--breakpoint-*` | Responsive variants | `sm:*`, `md:*` |
| `--container-*` | Container queries | `@sm:*` |
| `--spacing-*` | Spacing/sizing | `px-4`, `gap-2` |
| `--aspect-*` | Aspect ratios | `aspect-video` |
| `--ease-*` | Timing functions | `ease-out` |
| `--animate-*` | Animations | `animate-spin` |

## Extending vs Overriding

**Extend (thêm mà không xóa default):**

```css
@theme {
  --font-poppins: Poppins, sans-serif;
  --color-brand-primary: oklch(0.65 0.25 280);
}
```

**Override một giá trị cụ thể:**

```css
@theme {
  --breakpoint-sm: 30rem;
}
```

**Override toàn bộ namespace (asterisk syntax):**

```css
@theme {
  --color-*: initial;  /* Xóa toàn bộ default colors */
  --color-white: #fff;
  --color-purple: #3f3cbb;
  --color-midnight: #121063;
}
```

**Disable mọi default:**

```css
@theme {
  --*: initial;
  --spacing: 4px;
  --font-body: Inter, sans-serif;
  --color-lagoon: oklch(0.72 0.11 221.19);
}
```

## @theme inline — Resolve Variables Khi Build

Khi theme variable reference đến variable khác, dùng `inline`:

```css
@theme inline {
  --font-sans: var(--font-inter);
}
```

`inline` ngăn vấn đề cascading: nếu không có, biến sẽ resolve ở scope sai (e.g. khi component nằm trong context có override khác).

## Runtime Theme Switching

Vì theme tokens đều là CSS custom properties, **chuyển theme runtime không cần rebuild**. Override `@theme` variables tại selector level:

```css
@theme {
  --color-primary: oklch(0.205 0 0);
}

.dark {
  --color-primary: oklch(0.922 0 0);
}
```

Mọi utility dùng `--color-primary` (e.g. `bg-primary`) sẽ tự động cập nhật khi class `.dark` được thêm/bớt.

## Animation Keyframes Trong @theme

```css
@theme {
  --animate-fade-in-scale: fade-in-scale 0.3s ease-out;

  @keyframes fade-in-scale {
    0% { opacity: 0; transform: scale(0.95); }
    100% { opacity: 1; transform: scale(1); }
  }
}
```

Sinh utility `animate-fade-in-scale`.

## Dùng Theme Variables Trong CSS / JS

**Trong custom CSS:**

```css
@layer components {
  .typography p {
    font-size: var(--text-base);
    color: var(--color-gray-700);
  }
}
```

**Trong arbitrary values:**

```html
<div class="rounded-[calc(var(--radius-xl)-1px)]"></div>
```

**Trong JavaScript:**

```javascript
const styles = getComputedStyle(document.documentElement);
const shadow = styles.getPropertyValue("--shadow-xl");
```

## Sharing Theme Across Projects

```css
/* packages/brand/theme.css */
@theme {
  --*: initial;
  --color-lagoon: oklch(0.72 0.11 221.19);
}
```

```css
/* packages/admin/app.css */
@import "tailwindcss";
@import "../brand/theme.css";
```

Có thể publish lên NPM để share design tokens giữa các project trong tổ chức.

## Constraints

- `@theme` phải ở **top-level** — không nested dưới selector hay media query
- Theme variables phải dùng `@theme` syntax — declare trong `:root` không sinh utility
- Tên biến phải theo namespace convention (e.g. `--color-*`) để map tới utility

## Performance

- Full builds nhanh hơn **5x** vs v3
- Incremental builds nhanh hơn **100x** vs v3
- Rust-powered engine parse CSS-first

## Ý Nghĩa Kiến Trúc

Tailwind v4 + `@theme` là một bước hợp nhất design tokens vào CSS native:
- **Không cần JS config** — không có `tailwind.config.ts`
- **CSS là single source of truth** — design tokens và utility generation cùng nằm trong CSS
- **Runtime theming free** — không phải rebuild khi đổi theme
- **DTCG-compatible** — JSON tokens có thể export ra `@theme` block dễ dàng
