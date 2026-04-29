---
title: "Research: TanStack React Query Kiến Trúc"
source: "autoresearch"
date_added: 2026-04-29
tags: [research, autoresearch]
status: draft
related: ["[[jotai]]"]
summary: "Báo cáo nghiên cứu tự động về kiến trúc lõi của TanStack React Query."
---

## Bối Cảnh
Mục tiêu nghiên cứu là khám phá kiến trúc, các thành phần lõi và nguyên lý hoạt động bên dưới (under the hood) của TanStack React Query, nhằm lấp đầy khoảng trống kiến thức về mảng Server State Management trong cơ sở dữ liệu Second Brain.

## Phát Hiện Chính
- **Vị trí Kiến trúc:** Đóng vai trò là lớp quản lý trạng thái máy chủ (Server State Management layer) độc lập, tách biệt khỏi UI Layer. (Nguồn: [[tanstack-query-architecture]])
- **Các thành phần lõi:** Hoạt động như một state machine độc lập với React, dựa trên 3 trụ cột: `QueryClient` (bộ não trung tâm), `QueryCache` (lưu trữ in-memory hash map) và `Query` (đại diện cho một truy vấn dữ liệu).
- **Mô hình Observer:** Cầu nối giữa bộ máy bên ngoài và React. Khi dùng `useQuery`, một Observer được tạo ra, đăng ký theo dõi vào Query và kích hoạt re-render component khi dữ liệu cache thay đổi.
- **Cơ chế Stale-While-Revalidate:** Trả về dữ liệu cũ (stale) ngay lập tức để giữ UI mượt mà, trong khi âm thầm tải lại dữ liệu mới (fresh) ở background.
- **Tối ưu tự động:** Tích hợp sẵn deduplication (khử trùng lặp request), garbage collection (dọn rác in-memory) và background refetch khi window focus/network reconnect.

## Thực Thể & Khái Niệm Mới
- **Concept: Server State:** Trạng thái lưu trữ ở máy chủ, bất đồng bộ, không thuộc sở hữu độc quyền của frontend và có thể bị lỗi thời.
- **Concept: Stale-While-Revalidate:** Chiến lược caching cho phép hiển thị dữ liệu cũ trong lúc chờ dữ liệu mới, tối ưu trải nghiệm người dùng.
- **Tool: TanStack Query (React Query):** Công cụ quản lý Server State chuyên nghiệp, thay thế cho mô hình dùng `useEffect` + `useState` hoặc Redux/Jotai để lưu trữ dữ liệu API.

## Mâu Thuẫn
- *Không có mâu thuẫn lớn giữa các nguồn.* Mọi nguồn đều đồng thuận React Query không phải là "state manager" truyền thống mà là "server state manager".

## Câu Hỏi Mở
- Mặc dù lý thuyết kiến trúc đã rõ, việc triển khai `QueryFactory` hoặc tổ chức folder/files (`src/queries`) trong một dự án React quy mô lớn với TypeScript cụ thể diễn ra như thế nào?

## Nguồn Đã Nạp
- [[tanstack-query-architecture]]
