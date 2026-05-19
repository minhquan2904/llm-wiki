---
title: "shadcn/ui Theming — Official Documentation"
source: "https://ui.shadcn.com/docs/theming"
date_added: 2026-05-19
tags: [autoresearch, design-tokens, shadcn, tailwind, theming, dark-mode]
aliases: []
status: draft
summary: "Tài liệu chính thức shadcn/ui về theming — semantic token pairs, dark mode qua .dark class, tích hợp Tailwind v4 @theme inline."
confidence: high
---

# shadcn/ui — Official Theming Documentation

## Triết Lý Token: Surface + Foreground Pairs

shadcn/ui dùng pattern **semantic token pairs** — mỗi surface color luôn đi kèm foreground color (text/icon trên surface đó):

- Surface: `--primary`, `--card`, `--background`
- Foreground: `--primary-foreground`, `--card-foreground`, `--foreground`

Quote từ docs: *"The background suffix is omitted for the surface token. For example, `primary` pairs with `primary-foreground`."*

## Core Theme Tokens

| Token | Vai trò | Sử dụng |
|-------|---------|---------|
| `background` / `foreground` | App shell, text mặc định | Page sections |
| `card` / `card-foreground` | Surface elevated | Card components, panels |
| `primary` / `primary-foreground` | High-emphasis action | Default button, badge, active state |
| `secondary` / `secondary-foreground` | Lower-emphasis action | Secondary button |
| `muted` / `muted-foreground` | Subtle surface | Placeholder, helper text |
| `accent` / `accent-foreground` | Interactive state | Ghost button, hover state |
| `destructive` | Error emphasis | Destructive button, invalid state |
| `border` | Separator/divider | Card, table, menu |
| `input` | Form control | Input, textarea, select |
| `ring` | Focus indicator | Focus rings |

## Dark Mode: `.dark` Class Override

**Phương án chính thức:** override CSS variables trong `.dark` selector — KHÔNG dùng `data-theme` attribute.

```css
:root {
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
}

.dark {
  --primary: oklch(0.922 0 0);
  --primary-foreground: oklch(0.205 0 0);
}
```

Tên token và utility classes (`bg-primary`, `text-primary-foreground`) giữ nguyên — chỉ giá trị thay đổi khi `.dark` class được apply.

## Tích Hợp Tailwind v4 — @theme inline

CSS variables expose tới Tailwind qua `@theme inline`:

```css
@theme inline {
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --radius-sm: calc(var(--radius) * 0.6);
  --radius-md: calc(var(--radius) * 0.8);
  --radius-lg: var(--radius);
}
```

Pattern này map design tokens tới Tailwind utilities: `bg-primary`, `text-primary-foreground`, `border-border`.

**Lý do dùng `inline`:** Cần thiết để Tailwind resolve `--primary` ở scope hiện tại (root hoặc `.dark`), không phải scope khi utility được sinh ra.

## Radius Scale — Single Source of Truth

Toàn bộ radius scale derive từ một biến `--radius`:

```css
--radius-sm: calc(var(--radius) * 0.6);
--radius-md: calc(var(--radius) * 0.8);
--radius-lg: var(--radius);
--radius-xl: calc(var(--radius) * 1.4);
--radius-2xl: calc(var(--radius) * 1.8);
--radius-3xl: calc(var(--radius) * 2.2);
--radius-4xl: calc(var(--radius) * 2.6);
```

Đổi `--radius` → toàn bộ scale tự scale theo.

## Thêm Custom Tokens

Pattern 3 bước: declare trong `:root` + `.dark`, expose qua `@theme inline`:

```css
:root {
  --warning: oklch(0.84 0.16 84);
  --warning-foreground: oklch(0.28 0.07 46);
}

.dark {
  --warning: oklch(0.41 0.11 46);
  --warning-foreground: oklch(0.99 0.02 95);
}

@theme inline {
  --color-warning: var(--warning);
  --color-warning-foreground: var(--warning-foreground);
}
```

Dùng: `<div className="bg-warning text-warning-foreground" />`

## Base Color Options

Trong `components.json`, set `tailwind.baseColor` — chọn 1 trong: Neutral, Stone, Zinc, Mauve, Olive, Mist, Taupe.

```json
{
  "tailwind": {
    "cssVariables": true
  }
}
```

`cssVariables: true` là default; `false` sẽ generate component với inline Tailwind utilities (e.g. `bg-zinc-950 dark:bg-white`) thay vì CSS variables.

## Best Practices

1. **Maintain semantic pairs** — luôn declare foreground cùng surface
2. **Dùng OKLCH** — perceptually consistent qua light/dark
3. **Single source of truth** — derive scale từ base token
4. **CSS-first** — đổi theme không recompile component

## So Sánh Với Approach `data-theme` (Lloyd Richards Lab)

Approach chính thức shadcn/ui (`.dark` class) chỉ hỗ trợ 2 mode — light & dark.

Approach `data-theme` (Lloyd Richards) hỗ trợ N theme (`light-classic`, `dark-classic`, `light-professional`, `dark-professional`...) qua attribute selector `[data-theme^="dark-"]`.

**Khi nào dùng `data-theme`:** Multi-brand hoặc multi-personality themes vượt quá light/dark.
**Khi nào dùng `.dark` class:** Use case đơn giản, theo convention shadcn chuẩn.
