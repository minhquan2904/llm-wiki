---
title: "TanStack Query"
source: "compiled"
date_added: 2026-04-29
tags: [tool, react, state-management]
aliases: [React Query, TanStack React Query]
status: draft
related:
  - "[[jotai]]"
summary: "Thư viện quản lý trạng thái máy chủ (Server State) độc lập cho ứng dụng web, nổi bật với cơ chế caching tự động và kiến trúc Observer."
---

# TanStack Query

## Tổng Quan

TanStack Query (trước đây là React Query) là một công cụ mạnh mẽ đóng vai trò như một lớp quản lý trạng thái máy chủ (Server State Management layer) trong kiến trúc ứng dụng hiện đại. Nó giải quyết triệt để bài toán tìm nạp dữ liệu (data fetching), lưu vào bộ nhớ tạm (caching), đồng bộ hóa và cập nhật dữ liệu từ máy chủ, tách biệt hoàn toàn với trạng thái giao diện (Client State) do các công cụ như Jotai hay Redux đảm nhiệm. Về bản chất, TanStack Query hoạt động như một cỗ máy trạng thái (state machine) độc lập, tồn tại bên ngoài vòng đời của React.

## Vai Trò Trong Kiến Trúc Ứng Dụng

TanStack Query nằm ở lớp kết nối dữ liệu (Data Access Layer), đóng vai trò trung gian giữa giao diện người dùng và API bên dưới. Các thành phần lõi của nó bao gồm:

- **QueryClient:** "Bộ não" trung tâm tồn tại xuyên suốt vòng đời ứng dụng, quản lý bộ nhớ đệm (cache) và các cấu hình toàn cục.
- **QueryCache:** Bộ nhớ in-memory dạng hash map lưu trữ trạng thái máy chủ, dùng `query hash` để ánh xạ và ngăn chặn các request mạng trùng lặp (deduplication).
- **Query:** Đối tượng đại diện cho một phần dữ liệu cụ thể, chịu trách nhiệm thực thi hàm fetch, quản lý vòng đời (stale, fresh, inactive), và thông báo cho các người đăng ký (Observers).

Thông qua **mô hình Observer**, khi component sử dụng hook `useQuery`, một Observer được tạo ra để đăng ký theo dõi vào cache. Khi cache thay đổi, Observer kích hoạt re-render component, giúp giao diện luôn đồng bộ hoàn hảo với dữ liệu ngầm mà không cần dựa vào `useState` hay `useEffect`.

## Lợi Thế / Hạn Chế

**Lợi Thế:**
- **Stale-While-Revalidate:** Cơ chế caching xuất sắc cho phép ngay lập tức hiển thị dữ liệu cũ (stale) cho người dùng trong khi âm thầm gọi lại dữ liệu mới (fresh) ở chế độ nền, mang lại trải nghiệm mượt mà không bị gián đoạn bởi các biểu tượng loading.
- **Quản lý tài nguyên tự động:** Tích hợp sẵn cơ chế khử trùng lặp request (Deduplication) nếu nhiều component gọi cùng một API, và dọn dẹp bộ nhớ (Garbage Collection) đối với các query không còn người theo dõi để chống tràn bộ nhớ.
- **Tự động đồng bộ:** Khả năng background refetch tự động khi người dùng quay lại tab trình duyệt (Window Focus) hoặc khi mạng kết nối lại.

**Hạn Chế:**
- Chuyên biệt hóa: TanStack Query chỉ quản lý Server State, không phù hợp để quản lý Client State (như trạng thái mở/đóng modal hay form UI cục bộ). Thường phải dùng kết hợp với Jotai hoặc Zustand.
- Cần thời gian làm quen (learning curve) đối với việc thiết kế Query Keys chuẩn xác để tránh xung đột cache trong các ứng dụng quy mô lớn.

## Nguồn Tham Khảo

- [[raw/articles/tanstack-query-architecture.md]]
