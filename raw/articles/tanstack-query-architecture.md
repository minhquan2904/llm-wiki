---
title: "Kiến trúc TanStack React Query"
source: "Vertex AI Search"
date_added: 2026-04-29
tags: [autoresearch, tanstack-query, react, architecture]
aliases: []
status: draft
summary: "Tổng hợp kiến thức nền tảng về kiến trúc và cách thức hoạt động (under the hood) của TanStack Query."
confidence: high
---

# Kiến trúc TanStack React Query

Kiến trúc của **TanStack React Query** (trước đây là React Query) không được định nghĩa là một kiến trúc ứng dụng cứng nhắc, mà nó đóng vai trò là một **lớp quản lý trạng thái máy chủ (Server State Management layer)** trong kiến trúc tổng thể của ứng dụng.

## 1. Vị trí trong kiến trúc ứng dụng (Layered Architecture)
Trong một ứng dụng hiện đại, TanStack Query thường nằm ở lớp kết nối dữ liệu (Data Access Layer), tách biệt giữa giao diện (UI) và API bên dưới:
*   **UI Layer (Components):** Chỉ quan tâm đến việc hiển thị dữ liệu và gửi các tương tác người dùng. Các component gọi các hooks của TanStack Query (`useQuery`, `useMutation`).
*   **Data Layer (TanStack Query):** Đảm nhận việc fetch, caching, đồng bộ hóa và quản lý trạng thái của dữ liệu từ server.
*   **API/Gateway Layer:** Chứa các hàm thực hiện request thực tế (sử dụng `fetch`, `axios`, v.v.). TanStack Query gọi các hàm này thông qua `queryFn`.

## 2. Các thành phần lõi (Under the Hood)
React Query hoạt động như một state machine độc lập nằm ngoài vòng đời của React. Nó được xây dựng dựa trên ba thành phần chính:
*   **`QueryClient`:** Là "bộ não" trung tâm, nơi quản lý cache và cấu hình toàn cục. Tất cả các dữ liệu đều được lưu trữ trong `QueryClient`. Nó được thiết kế để tồn tại xuyên suốt vòng đời của ứng dụng.
*   **`QueryCache`:** Một đối tượng in-memory (hash map) lưu trữ tất cả server state. Nó sử dụng **serialized query key** (mã băm của query key) làm khóa tra cứu để đảm bảo mỗi request duy nhất được map với đúng một instance `Query`, ngăn chặn các request mạng trùng lặp.
*   **`Query`:** Mỗi `Query` instance là một class chịu trách nhiệm cho một phần dữ liệu. Nó đóng gói trạng thái của dữ liệu (loading, success, error), quản lý hàm fetch thực tế, xử lý retries, deduplication, và duy trì một danh sách các **Observers** (người đăng ký theo dõi).

## 3. Sự tương tác Component (Mô hình Observer)
React Query sử dụng **Observer Pattern** để làm cầu nối giữa state machine lõi của nó và các React components.
*   Khi một component gọi `useQuery`, nó tạo ra một **Observer**.
*   Observer này đăng ký (subscribe) vào `Query` instance tương ứng trong `QueryCache`.
*   Bất cứ khi nào trạng thái nội bộ của `Query` thay đổi (vd: fetch xong dữ liệu, xảy ra lỗi), `Query` sẽ thông báo cho tất cả Observers của nó.
*   Khi Observer nhận được thông báo, nó sẽ kích hoạt re-render trong React component đang subscribe với trạng thái mới nhất, đảm bảo UI luôn đồng bộ hoàn hảo với cache bên dưới.

## 4. Chiến lược Caching "Stale-While-Revalidate"
*   **Fresh vs. Stale:** Dữ liệu trong cache không chỉ "tồn tại"; nó có trạng thái. Khi dữ liệu mới fetch, nó được đánh dấu là `fresh`. Sau một thời gian được cấu hình (`staleTime`), dữ liệu chuyển thành `stale` (cũ/lỗi thời).
*   **Revalidation (Tái kiểm tra):** Khi một component yêu cầu dữ liệu stale, React Query ngay lập tức trả về dữ liệu cũ đó (giúp UI phản hồi nhanh và tránh màn hình loading). Đồng thời, nó kích hoạt một refetch ở chế độ nền để lấy dữ liệu mới nhất từ server. Khi dữ liệu mới về, cache được cập nhật và component re-render với dữ liệu fresh.

## 5. Quản lý tài nguyên thông minh
*   **Deduplication (Khử trùng lặp):** Nếu nhiều component cùng mount và gọi cùng một query key, React Query gộp chúng thành 1 request mạng duy nhất.
*   **Garbage Collection (Dọn rác):** Các query không còn Observer sẽ bị xóa khỏi bộ nhớ sau một khoảng thời gian (`gcTime`) để chống tràn bộ nhớ (memory leaks).
*   **Window Focus/Reconnect:** Lắng nghe các sự kiện trình duyệt (như focus lại cửa sổ hoặc kết nối lại mạng) để tự động background refetch, đảm bảo ứng dụng luôn cập nhật.

## Kết luận
React Query hiệu quả vì nó coi **React chỉ là một view layer (lớp hiển thị)**. Nó không phụ thuộc vào `useState` hay `useEffect` nội bộ của React cho các logic lõi của mình. Bằng cách duy trì state ở một external cache ổn định và chỉ dùng hooks để "subscribe", nó vượt qua những phức tạp và cạm bẫy hiệu năng của việc quản lý dữ liệu bất đồng bộ truyền thống.
