---
title: "Tailwind Themes with Design Tokens (Lab #037)"
source: "https://www.lloydrichards.dev/labs/037-theming-design-tokens"
date_added: 2026-05-19
tags: [autoresearch, design-tokens, tailwind, shadcn, next-themes, theming]
aliases: []
status: draft
summary: "Case study triển khai hệ thống đa theme với Tailwind CSS, CSS variables và next-themes — bỏ qua external token dictionary tool."
confidence: medium
---

# Tailwind Themes with Design Tokens — Lloyd Richards Lab #037

## Mục Tiêu & Bối Cảnh

Tác giả Lloyd Richards xây dựng hệ thống đa theme cho website cá nhân (Next.js + shadcn/ui) bằng cách dùng **CSS variables làm design tokens trực tiếp trong Tailwind**, không cần Style Dictionary hay external token dictionary tool. Mục tiêu: abstract hóa các design decisions thành biến tái sử dụng được, cho phép chuyển theme dễ dàng mà vẫn giữ nhất quán visual.

## Tools & Libraries

- **Tailwind CSS** — CSS utility framework
- **shadcn/ui** — Component library xây trên Tailwind
- **next-themes** — Quản lý và persist theme state
- **Next.js** — React framework

## Cách Tiếp Cận Từng Bước

### Bước 1 — Tạo Core Design Tokens

Khai báo CSS variables nền tảng cho colors trong `global.css`. Tác giả dùng **HSL space-separated values** để Tailwind có thể compose với alpha modifier:

```css
@layer base {
  :root {
    /* Core Colors (Primitive layer) */
    --color-mono-050: 210 40% 98%; /* #f8fafc */
    --color-mono-100: 210 40% 96.1%; /* #f1f5f9 */
    --color-mono-200: 214.3 31.8% 91.4%; /* #e2e8f0 */
    /* ... */

    /* Functional Colors (Semantic layer) */
    --card: var(--background);
    --card-foreground: var(--color-mono-900);
    --popover: var(--color-mono-050);
    --popover-foreground: var(--color-mono-900);
    --muted: var(--color-mono-100);
    --muted-foreground: var(--color-mono-900);
  }
}
```

**Hai tầng rõ ràng:**
- **Core (Primitive):** `--color-mono-050` đến `--color-mono-950` — giá trị thô.
- **Functional (Semantic):** `--card`, `--popover`, `--muted` — tham chiếu primitive, mang ngữ nghĩa.

### Bước 2 — Map Tokens vào Tailwind Config

Kết nối CSS variables với Tailwind's color system trong `tailwind.config.ts`:

```typescript
const config = {
  theme: {
    extend: {
      colors: {
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
      },
    },
  },
} satisfies Config;
```

`hsl(var(--popover))` wrapper là pattern shadcn/ui chuẩn — cho phép Tailwind apply opacity modifier như `bg-card/50`.

### Bước 3 — Implement Theme Provider

Setup `next-themes` trong layout, khai báo danh sách theme dự kiến:

```typescript
import { ThemeProvider } from "./theme_provider";

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <ThemeProvider
          defaultTheme="light"
          enableSystem
          enableColorScheme
          themes={[
            "light-classic",
            "dark-classic",
            "light-professional",
            "dark-professional",
          ]}
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
```

### Bước 4 — Tạo Theme Variants

Mỗi theme là một file CSS riêng, dùng `data-theme` attribute selector (không phải class):

```css
html[data-theme="dark-professional"] {
  color-scheme: dark;

  /* Core Colors override */
  --color-stone-050: 60 9.1% 97.8%;
  --color-stone-100: 60 4.8% 95.9%;
  /* ... */

  /* Functional Colors override */
  --popover: var(--color-stone-900);
  --popover-foreground: var(--color-stone-050);
  --card: var(--color-stone-800);
  --card-foreground: var(--color-stone-050);
  --muted: var(--color-stone-800);
  --muted-foreground: var(--color-stone-050);
}
```

`color-scheme: dark` — hint cho browser render native UI elements (scrollbar, form controls) theo dark scheme.

### Bước 5 — Configure Dark Mode Detection

Override Tailwind's `darkMode` để recognize dark-prefixed themes:

```typescript
const config = {
  darkMode: ["class", '[data-theme^="dark-"]'],
} satisfies Config;
```

Pattern `^=` (starts-with) cho phép vô hạn dark themes — `dark-classic`, `dark-professional`, `dark-anything`. Component code chỉ cần `dark:bg-card`, Tailwind sẽ apply khi `data-theme` bắt đầu bằng `dark-`.

### Bước 6 — Theme Toggle Component

```typescript
"use client";

import { useTheme } from "next-themes";

export function ThemeToggle() {
  const { setTheme } = useTheme();

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="icon">
          <SunIcon className="size-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90" />
          <MoonIcon className="absolute size-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0" />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem onClick={() => setTheme("light-classic")}>
          Classic (Light)
        </DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme("dark-classic")}>
          Classic (Dark)
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
```

## Key Insights & Tradeoffs

### Triết Lý Design Token

Tác giả trích Salesforce: *"Design tokens are the visual design atoms of the design system — specifically, they are named entities that store visual design attributes."*

Thay vì adopt external token dictionary tool, tác giả tận dụng CSS variables trực tiếp trong Tailwind — đơn giản hơn, dễ maintain hơn cho dự án solo/small team.

### Two-Tier Abstraction Benefits

Hệ thống Core → Functional đạt được:
- **Scalability** — thêm theme không cần thay component
- **Consistency** — đồng bộ với conventions của shadcn/ui
- **Decoupling** — đổi theme không sửa code component

### Theme Extensibility

Approach hỗ trợ unlimited theme variants ngoài light/dark:
- `data-theme` attribute → phân tách namespace
- `[data-theme^="dark-"]` prefix matcher → vô hạn dark theme variants
- Mỗi theme một file CSS riêng → tránh xung đột

## Liên Hệ Với Wiki Hiện Có

- **[[design-tokens]]** — Concept gốc về design tokens
- **[[style-dictionary]]** — Tool transform engine; bài này chứng minh có thể bỏ qua khi dùng CSS-native + Tailwind
- **Câu hỏi mở từ research trước:** "Tailwind v4 dùng CSS variables native — liệu có thể bỏ Style Dictionary không?" — Bài này trả lời: **Có, cho dự án nhỏ/solo.** Nhưng cho design system enterprise multi-platform (iOS, Android, web), Style Dictionary vẫn cần để transform tokens ra platform-specific format.

## Đánh Giá

- **Confidence: medium** — Đây là personal blog/lab, không phải official docs. Approach hoạt động tốt cho use case của tác giả (personal site) nhưng cần kiểm chứng cho production-grade enterprise design system.
- **Recency: 2025** — Phản ánh pattern Tailwind + shadcn hiện đại.
- **Tính ứng dụng cao:** Code mẫu copy-paste được, có thể adapt ngay.
