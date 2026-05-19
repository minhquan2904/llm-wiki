---
title: "Research: Tailwind + Design Token Theming (Lab #037 deep-dive)"
source: "autoresearch"
date_added: 2026-05-19
tags: [research, autoresearch, design-tokens, tailwind, shadcn, theming]
status: draft
related:
  - "[[design-tokens]]"
  - "[[style-dictionary]]"
parent_report: "research-design-token-system-2026-05-19.md"
summary: "Báo cáo follow-up từ research design tokens — phân tích sâu việc theming bằng Tailwind + CSS variables (Lloyd Richards Lab #037), đối chiếu với Tailwind v4 @theme và shadcn/ui official theming."
---

## Bối Cảnh

Báo cáo tiếp nối từ `research-design-token-system-2026-05-19.md` — vốn đã trả lời câu hỏi *"Design token là gì? Kiến trúc 3 tầng? DTCG spec?"*.

Một trong các **Câu Hỏi Mở** từ báo cáo trước:
> *"Tailwind v4 dùng CSS variables native — liệu có thể bỏ Style Dictionary không?"*

Người dùng cung cấp URL cụ thể (Lloyd Richards Lab #037) như case study thực tế cho câu hỏi này. Mục tiêu vòng này:

1. **Trích xuất pattern thực tế** từ case study Lab #037
2. **Đối chiếu** với Tailwind v4 `@theme` (chính thức) và shadcn/ui (official)
3. **Kết luận** khi nào cần Style Dictionary, khi nào không

---

## Phát Hiện Chính

### 1. Có Thể Bỏ Style Dictionary Cho Web-Only Stack

(Nguồn: [[design-token-tailwind-theming-lloyd-richards]], [[tailwind-v4-theme-directive-docs]], [[shadcn-ui-theming-official]])

**Kết luận có điều kiện:**

| Use case | Cần Style Dictionary? | Lý do |
|----------|----------------------|-------|
| Web app solo/small team, single platform | **Không** | Tailwind v4 `@theme` + CSS variables đủ |
| Design system enterprise multi-platform (Web + iOS + Android + Figma sync) | **Có** | Cần transform JSON tokens → Swift/XML/CSS |
| Multi-brand white-label web | **Không** | `data-theme` attribute đủ flexible |
| Tokens cần version/governance qua Figma → code pipeline | **Có** | Style Dictionary handle naming/transform |

**Phát hiện cốt lõi:** Tailwind v4 `@theme` directive thực chất là **một dạng Style Dictionary built-in cho web** — nó nhận design tokens dưới dạng CSS custom properties và sinh utility classes tự động.

### 2. Ba Pattern Theming Tailwind (Tiến Hóa Theo Thời Gian)

(Nguồn: [[design-token-tailwind-theming-lloyd-richards]] vs [[shadcn-ui-theming-official]] vs [[tailwind-v4-theme-directive-docs]])

#### Pattern A — Tailwind v3 + `tailwind.config.ts` (Legacy)

Lloyd Richards Lab #037 dùng pattern này:
- CSS variables khai báo trong `:root` và `[data-theme="..."]`
- `tailwind.config.ts` map từng biến với `hsl(var(--popover))` syntax
- HSL space-separated values để hỗ trợ alpha modifier

```typescript
// tailwind.config.ts (v3 pattern)
colors: {
  popover: {
    DEFAULT: "hsl(var(--popover))",
    foreground: "hsl(var(--popover-foreground))",
  },
}
```

#### Pattern B — Tailwind v4 + `@theme` (Modern)

Từ docs Tailwind v4:
- Không còn `tailwind.config.ts`
- Mọi thứ trong CSS qua `@theme` block
- Utility classes sinh tự động từ namespace (`--color-*` → `bg-*`, `text-*`, `border-*`)

```css
/* Tailwind v4 - CSS first */
@import "tailwindcss";

@theme {
  --color-primary: oklch(0.205 0 0);
  --radius-md: 0.5rem;
}
```

#### Pattern C — shadcn/ui v4 + `@theme inline` (Hybrid Best Practice)

- Token "logic" trong `:root` và `.dark`
- `@theme inline` chỉ expose chúng cho Tailwind
- Dùng `inline` để Tailwind resolve var ở scope hiện tại (quan trọng cho dark mode toggle)

```css
:root {
  --primary: oklch(0.205 0 0);
}

.dark {
  --primary: oklch(0.922 0 0);
}

@theme inline {
  --color-primary: var(--primary);  /* inline = resolve at use-site */
}
```

**Lý do tách lớp:** Token semantic (`--primary`) độc lập với utility namespace (`--color-primary`) — cho phép có nhiều utility namespace cùng map đến một token semantic.

### 3. Hai Cơ Chế Switch Theme — Class vs Attribute

| Cơ chế | Selector | Khi nào dùng | Ví dụ |
|--------|----------|--------------|-------|
| **`.dark` class** | `.dark { ... }` | 2 mode (light/dark) — shadcn official | Mặc định shadcn/ui, next-themes default |
| **`data-theme` attribute** | `[data-theme="..."]` | N theme variants (multi-brand) | Lloyd Richards Lab |

**Critical insight cho multi-theme:** Khi cần N theme (`light-classic`, `dark-classic`, `light-professional`, `dark-professional`...), config Tailwind:

```typescript
// Cho dark variant nhận diện được mọi "dark-*"
darkMode: ["class", '[data-theme^="dark-"]'],
```

Prefix selector `^=` cho phép vô hạn dark variants.

### 4. Runtime Theme Switching Không Cần Rebuild

(Nguồn: [[tailwind-v4-theme-directive-docs]])

Vì theme tokens là CSS custom properties, **switching theme tại runtime chỉ là cascading**:
- User toggle theme → JavaScript thay đổi class/attribute trên `<html>`
- Browser re-evaluate cascade
- Toàn bộ utility classes (`bg-primary`, etc.) tự update vì underlying var đổi
- **Zero rebuild cost**

Đây là khác biệt cốt lõi giữa "design token as CSS variable" vs "design token as build-time constant" (e.g. Style Dictionary output static).

### 5. Two-Tier Token Pattern Trở Thành Convention

Lloyd Richards, shadcn/ui, và DTCG đều dùng pattern giống nhau (chỉ khác cách đặt tên):

| Vai trò | Lloyd Richards | shadcn/ui | DTCG |
|---------|---------------|-----------|------|
| **Tầng 1 (Primitive)** | `--color-mono-050` | `--color-zinc-50` | Brand palette tokens |
| **Tầng 2 (Semantic)** | `--card`, `--popover` | `--card`, `--popover` | Alias tokens |
| **Tầng 3 (Component)** | (không dùng) | (không dùng) | Component-specific tokens |

**Quan sát:** Trong Tailwind ecosystem, tầng 3 (Component tokens) thường bỏ qua — semantic tokens kết hợp utility classes là đủ. Tầng 3 chỉ thực sự cần khi multi-brand vượt quá khả năng của semantic layer.

---

## Thực Thể & Khái Niệm Mới

- **`@theme` directive** (Tailwind v4): CSS-native config replaces `tailwind.config.ts`. Sinh utility từ namespace prefix.
- **`@theme inline`**: Variant của `@theme` resolve biến tại use-site thay vì define-site — cần thiết khi biến override trong scope khác (e.g. `.dark`).
- **OKLCH color space**: Format màu perceptually-uniform, default của shadcn/ui v4 thay cho HSL.
- **`next-themes`**: Thư viện React quản lý theme state + persist trong localStorage, sync với `prefers-color-scheme`.
- **`color-scheme` CSS property**: Hint cho browser render native UI (scrollbar, form controls) theo dark hay light scheme.
- **Surface + Foreground pair convention**: shadcn pattern — mỗi `--surface` luôn đi với `--surface-foreground`.
- **`data-theme` attribute matching** `[data-theme^="dark-"]`: Prefix selector cho phép vô hạn dark theme variants.

---

## Mâu Thuẫn (nếu có)

### "Class vs Attribute" cho theme switching

**Lloyd Richards** dùng `data-theme="..."` attribute → linh hoạt cho multi-theme.
**shadcn/ui official** dùng `.dark` class → đơn giản cho 2 mode.

**Phân giải:** Không phải mâu thuẫn — chỉ là **trade-off scope**:
- 2 mode → class đơn giản hơn
- N mode → attribute linh hoạt hơn

`next-themes` hỗ trợ cả hai qua prop `attribute="class"` vs `attribute="data-theme"`.

### "Có cần Style Dictionary cho Tailwind v4?"

**Phía bỏ qua được:** Lloyd Richards (case study), Tailwind v4 docs (CSS-first philosophy).
**Phía vẫn cần:** Báo cáo gốc — Style Dictionary còn vai trò khi multi-platform.

**Phân giải:** Style Dictionary và Tailwind `@theme` **không cạnh tranh trực tiếp**:
- Style Dictionary là transform engine **producer** (JSON → CSS/Swift/XML)
- Tailwind `@theme` là **consumer** của CSS tokens

Một pipeline production có thể là: `Figma → Tokens Studio → JSON → Style Dictionary → @theme.css → Tailwind utilities`. Style Dictionary chỉ bỏ qua được khi **JSON token không tồn tại** — đội viết tokens trực tiếp trong CSS.

### Độ confidence

- **high** cho các kết luận về Tailwind v4 và shadcn (nguồn official docs)
- **medium** cho approach Lloyd Richards (personal blog, không phải tài liệu chuẩn nhưng code minh chứng rõ ràng)

---

## Câu Hỏi Mở

1. **Token versioning với @theme**: Khi token bị rename/deprecated, làm thế nào maintain backward compat trong Tailwind v4? Có cần alias layer riêng?
2. **Performance khi N theme nhiều**: 10+ themes mỗi cái có file CSS riêng — impact lên bundle size và FOUC?
3. **Server-side rendering của theme**: `next-themes` cần `suppressHydrationWarning` — nguyên nhân và cách handle correctly cho App Router?
4. **Composite tokens** (DTCG `typography`, `shadow` composite) trong Tailwind v4 — có syntax nào trong `@theme` để khai báo composite?
5. **Migration path cụ thể**: Codebase v3 với `tailwind.config.ts` 500 dòng → v4 `@theme` — strategy và automation tool?

---

## Nguồn Đã Nạp

- [[design-token-tailwind-theming-lloyd-richards]] — Case study practical Tailwind v3 + data-theme + next-themes (medium confidence)
- [[tailwind-v4-theme-directive-docs]] — Official docs Tailwind v4 `@theme` directive (high confidence)
- [[shadcn-ui-theming-official]] — Official docs shadcn/ui theming pattern (high confidence)

## Liên Kết Báo Cáo Trước

- `outputs/reports/research-design-token-system-2026-05-19.md` — Báo cáo gốc design tokens, DTCG spec, kiến trúc 3 tầng
