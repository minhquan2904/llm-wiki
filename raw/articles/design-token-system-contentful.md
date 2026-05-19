---
title: "Design Token System — Architecture & Implementation (Contentful)"
source: "https://www.contentful.com/blog/design-token-system/"
date_added: 2026-05-19
tags: [autoresearch, design-tokens, design-system, frontend]
aliases: []
status: draft
summary: "Ba tầng kiến trúc design token (Primitive → Semantic → Component), naming conventions, modes, themes và tích hợp tooling."
confidence: high
---

# Design Token System — Architecture & Implementation

## Ba Tầng Kiến Trúc Token

Design tokens là các đơn vị dữ liệu được chuẩn hóa để lưu trữ các quyết định thiết kế (màu sắc, typography, spacing, borders, animations), thường được lưu dưới dạng JSON.

### 1. Primitive Tokens (Base layer)
- Biểu diễn các giá trị thô của brand palette.
- Thu gọn từ vô hạn khả năng xuống vài chục đến vài trăm giá trị cụ thể.
- Ví dụ: `color-blue-500: #0066cc`

### 2. Semantic Tokens (Mid layer)
- Tham chiếu đến primitive và nhúng ngữ nghĩa sử dụng.
- `text-default` cho người dùng biết *khi nào* và *cách nào* áp dụng màu, không chỉ màu gì.
- Thay vì chọn từ 5 màu chấp nhận được, designer chỉ cần gọi `text-default`.

### 3. Component Tokens (Application layer)
- Tham chiếu semantic tokens; dành riêng cho từng component.
- Cho phép multi-brand theming: Brand A có `button-radius: 4px`, Brand B có `button-radius: 50px` — cùng một component structure.

## Naming Convention

Tiếp cận dạng lưới 2 chiều:
- **Trục X**: Các state/property đơn giản (default, hover, active)
- **Trục Y**: Các biến thể phức tạp cần thêm state

Nguyên tắc: không tạo `disabled-hover` nếu không cần thiết — tránh bùng nổ tổ hợp (combinatorial explosion).

## Modes, Collections, Themes

- **Mode**: Biến thể giá trị trong cùng một collection (ví dụ: light / dark). Token `background-primary` trỏ đến giá trị khác nhau tùy context.
- **Token Collection**: Nhóm token dùng chung mode. Color collection có thể có light/dark, typography collection thì không cần.
- **Theme**: Duplicate toàn bộ token set với giá trị khác — dùng cho multi-brand scenarios.

## Distribution & Tooling

Hub-and-spoke architecture: token là trung tâm, được transform ra nhiều đầu ra.

| Tool | Vai trò |
|------|---------|
| Style Dictionary | Transform aliases và output (CSS vars, Swift, XML...) |
| Knapsack | Token aliasing và output generation |
| Tokens Studio (Figma) | Quản lý comprehensive themes trong Figma |
| Figma Variables | Hỗ trợ native variables + alias (gray box indicator) |
| Contentful Studio | Nhận tokens ở tầng semantic để guide visual editor |

## Best Practices

1. **Tầng semantic giảm ambiguity**: Nhúng design rules vào system, không để designer tự chọn.
2. **Selective abstraction**: Không phải attribute nào cũng cần component token — giữ button background gắn với semantic primary color.
3. **Leverage aliasing**: CSS variables tham chiếu lẫn nhau → update đồng loạt.
4. **Balance expansion**: System quá rộng → khó dùng; quá hẹp → frustrate users.
5. **Tokens as source files**: Đặc biệt quan trọng khi AI sẽ amplify design system.
