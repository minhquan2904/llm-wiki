---
title: "React Router DOM"
source: "compiled"
date_added: 2026-04-24
tags: [tool, react, routing]
aliases: [react-router-dom, React Router]
status: canonical
related:
  - "[[jotai]]"
  - "[[virtual-dom-vs-real-dom]]"
summary: "Thư viện quản lý định tuyến tiêu chuẩn dành cho các ứng dụng Single Page Application (SPA) xây dựng bằng React."
---

# React Router DOM

## Tổng Quan

`react-router-dom` là một thư viện quản lý định tuyến (routing) phổ biến nhất trong hệ sinh thái React, chuyên phục vụ cho các ứng dụng trang đơn (Single Page Application - SPA). Trong một SPA thông thường, toàn bộ ứng dụng chỉ chia sẻ một tệp HTML duy nhất. Thư viện này đảm nhận nhiệm vụ ánh xạ các đường dẫn URL trên trình duyệt với các Component tương ứng trong React, cho phép điều hướng giao diện mượt mà mà không cần tải lại toàn bộ trang web.

## Vai Trò Trong Kiến Trúc React

Đóng vai trò là hệ thần kinh trung ương kiểm soát sự luân chuyển giữa các màn hình, `react-router-dom` cung cấp ba mô hình router cốt lõi phục vụ cho các môi trường khác nhau:

- **BrowserRouter**: Sử dụng HTML5 History API để quản lý lịch sử trình duyệt. Đây là mô hình tiêu chuẩn cho các ứng dụng web thông thường có sự hỗ trợ cấu hình từ máy chủ (server fallback).
- **HashRouter**: Phụ thuộc vào URL hash (`#`). Mô hình này thường được sử dụng cho việc lưu trữ trên các nền tảng tĩnh (static hosting) khi không thể cấu hình máy chủ điều hướng.
- **MemoryRouter**: Lưu trữ lịch sử điều hướng trong bộ nhớ nội bộ thay vì tương tác với thanh địa chỉ trình duyệt. Cơ chế này đặc biệt quan trọng trong quá trình kiểm thử (testing) hoặc khi ứng dụng hoạt động trong các môi trường giới hạn không có History API, chẳng hạn như Zalo Mini App hay Electron.

Thư viện cung cấp hệ thống các hooks thiết yếu giúp tương tác với hệ thống định tuyến, bao gồm `useNavigate` cho các điều hướng lập trình (programmatic navigation), `useParams` để thu thập tham số đường dẫn (path params), và `useSearchParams` để quản lý các chuỗi truy vấn (query string).

## Lợi Thế / Hạn Chế

**Lợi Thế:**
- Cung cấp mô hình Nested Routes mạnh mẽ, cho phép tổ chức cấu trúc giao diện theo dạng cha-con, giúp duy trì các layout cố định trong khi nội dung bên trong được linh hoạt thay đổi.
- Tương thích tốt với các kỹ thuật tối ưu hóa hiện đại như Lazy Loading kết hợp cùng `React.Suspense`, giúp giảm thiểu dung lượng gói phần mềm (bundle size) ở lần tải đầu tiên.
- Quản lý hiệu quả việc chặn luồng điều hướng, hỗ trợ đắc lực trong việc xây dựng hệ thống phân quyền hoặc bảo vệ đường dẫn (Protected Routes).
- Ở các phiên bản mới (từ v6 trở đi), thư viện hỗ trợ định kiểu TypeScript mặc định một cách mạnh mẽ.

**Hạn Chế:**
- Cấu hình đôi lúc phức tạp trong những kiến trúc có sự luân chuyển sâu giữa nhiều tầng Nested Routes.
- Đòi hỏi sự lựa chọn kỹ lưỡng về loại mô hình router (BrowserRouter vs MemoryRouter) tùy thuộc vào môi trường vận hành thực tế. Đối với các hệ thống WebView bị chặn History API (như Zalo Mini App), việc sơ suất sử dụng `BrowserRouter` sẽ gây sụp đổ toàn bộ hệ thống định tuyến.

## Nguồn Tham Khảo

- [[raw/articles/material-routes-react-router-dom-định-tuyến-cho-react-app.md]]
