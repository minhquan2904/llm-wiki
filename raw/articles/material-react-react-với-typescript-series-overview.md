---
title: ":material-react: React với TypeScript — Series Overview"
source: "D:\9. Learn\12. llm wiki\raw\articles\react\summary.md"
date_added: 2026-04-24
tags: [articles]
status: draft
summary: ""
---

# :material-react: React với TypeScript — Series Overview

!!! abstract "Về Series này"
    Tuyển tập các tài liệu, hướng dẫn và best-practices khi xây dựng ứng dụng với **React 18** và **TypeScript**. Đặc biệt, series tập trung vào thực tiễn kỹ thuật giải quyết các bài toán khi phát triển frontend trên nền tảng **Zalo Mini App (ZMP)**.

---

## :material-layers-triple: Tech Stack cốt lõi

Công nghệ sử dụng xuyên suốt series:

- :material-react: **Framework**: React 18
- :material-language-typescript: **Ngôn ngữ**: TypeScript
- :material-routes: **Định tuyến**: `react-router-dom` v6
- :material-battery-charging: **Quản lý State**: Jotai
- :material-cellphone-link: **Nền tảng đích**: Zalo Mini App

---

## :material-bookshelf: Danh sách bài học

!!! tip "Hướng dẫn"
    Nhấn vào tiêu đề của bài học để đi tới tài liệu chi tiết.

| Bài | Tên bài học | Tóm tắt nội dung |
|:---:|-------------|------------------|
| **01** | [:material-book-open-page-variant: React Router DOM](./1.md) | Kiến thức toàn tập về định tuyến SPA: Sự khác biệt giữa các Router, hook thiết yếu, Nested route, Bảo vệ route (Protected), Lazy loading và lý do **phải dùng `MemoryRouter`** trên Zalo. |
| **02** | [:material-atom: Jotai — Quản lý State theo kiểu Nguyên Tử](./2.md) | Atomic state là gì, tại sao tốt hơn Context/Redux, so sánh các giải pháp, và 5 patterns thực chiến: `atomFamily`, `atomWithReset`, `atomWithRefresh`, `loadable`. |
| **03** | [:material-clock-outline: Đang cập nhật...](#) | *(Bài học tiếp theo)* |

---

## :material-rocket-launch: Lộ trình dự kiến

Các chủ đề tiếp theo đang được chuẩn bị lên sóng:

- [x] Định tuyến SPA với `react-router-dom` và `MemoryRouter` cho Zalo
- [x] Quản lý State toàn cục với **Jotai** và atomic patterns
- [ ] **React Query** — Quản lý Server State và Caching hiệu quả
- [ ] Tối ưu hóa hiệu năng (Re-render, Memoization) trong React
- [ ] Xây dựng Form chuẩn xác với **React Hook Form** & **Zod**
- [ ] Styling ứng dụng siêu tốc với **Tailwind CSS** & **Radix UI**