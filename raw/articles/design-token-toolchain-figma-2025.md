---
title: "Design Token Toolchain — Figma Variables, Style Dictionary & Workflow 2025"
source: "https://styledictionary.com/info/tokens/ | https://www.figma.com/resource-library/design-tokens/"
date_added: 2026-05-19
tags: [autoresearch, design-tokens, figma, style-dictionary, toolchain, workflow]
aliases: []
status: draft
summary: "Luồng công việc thực tế: từ Figma Variables đến production code thông qua Style Dictionary và Tokens Studio."
confidence: medium
---

# Design Token Toolchain — Figma Variables, Style Dictionary & Workflow 2025

## Phân Biệt Token vs Figma Variables

| | Design Tokens | Figma Variables |
|--|---------------|-----------------|
| Bản chất | Vendor-neutral recipe (JSON) | Cách cook trong Figma kitchen |
| Phạm vi | Cross-platform | Figma-only |
| Dùng khi | Cần scalability, governance, multi-platform | Quick setup trong Figma |
| Sync | Cần pipeline (Tokens Studio, CI/CD) | Không tự sync ra code |

Tokens = recipe; Variables = how you cook it in one kitchen.

## Style Dictionary — Token Transformer

Style Dictionary là tool phổ biến nhất để transform design tokens:

- **Transforms**: Áp dụng rules khi build — chuyển font size từ px sang rem cho CSS, hex sang UIColor cho iOS.
- **Name transforms**: Mapping `spacing.small` sang naming convention phù hợp từng platform.
- **Output formats**: CSS custom properties, SCSS variables, iOS Swift, Android XML, JSON.

### Ví dụ output theo platform:
```
tokens/
├── css/variables.css
├── ios/tokens.swift
├── android/tokens.xml
└── js/tokens.js
```

## Tokens Studio — Figma ↔ Code Bridge

Tokens Studio là plugin Figma đóng vai trò cầu nối:
1. Quản lý token tiers (core/semantic/component) trong Figma
2. Export ra JSON format
3. Sync với Style Dictionary để generate platform outputs
4. Hỗ trợ theme management: generate file riêng cho mỗi theme (light_casual.css, dark_casual.css...)

## Workflow Đầy Đủ

```
Figma Variables
    ↓ (Tokens Studio plugin)
JSON token files (.tokens.json)
    ↓ (Style Dictionary + sd-transforms)
Platform outputs (CSS / Swift / XML / JS)
    ↓ (CI/CD pipeline)
Production code
```

## Token Tier Naming Pattern

```
category/role/variant
```
Ví dụ:
- `color/background/primary`
- `color/text/default`
- `spacing/component/button-padding`

## Governance at Scale

| Role | Trách nhiệm |
|------|-------------|
| Design System Lead | Định hướng chiến lược token |
| Token Guardian | Duy trì tính nhất quán, chặn token bloat |
| UX Designers/Devs | Sử dụng và đề xuất token mới |

Token bloat và inconsistency là rủi ro lớn khi scale — cần governance rõ ràng.

## Figma Native Variables (2023+)

- Figma hỗ trợ native variables với gray box indicator cho aliases.
- Variables trong Figma không tự động sync ra code → cần pipeline.
- Phần lớn team dùng Tokens Studio hoặc CI/CD webhook để maintain sync.
