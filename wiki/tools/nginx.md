---
title: "NGINX"
source: "compiled"
date_added: 2026-04-24
tags: [tool, web-server, proxy, load-balancer]
status: draft
related:
  - "[[apache-kafka]]"
  - "[[rabbitmq]]"
  - "[[docker]]"
summary: "Máy chủ web mã nguồn mở nổi bật với cơ chế xử lý bất đồng bộ, thường được ứng dụng làm Reverse Proxy và Load Balancer."
---

## Tổng Quan

**NGINX** (phát âm là "engine-x") là một phần mềm mã nguồn mở được thiết kế ban đầu để phục vụ nội dung web. Trong môi trường kiến trúc hiện đại, nền tảng này phát triển vai trò thành một Reverse Proxy, Load Balancer, và HTTP Cache. Khác với các mô hình máy chủ web truyền thống vốn tạo ra một luồng (thread) mới cho mỗi yêu cầu, NGINX sử dụng kiến trúc bất đồng bộ và hướng sự kiện (asynchronous event-driven architecture). Thiết kế này cung cấp khả năng xử lý đồng thời hàng chục ngàn kết nối mạng trong khi tiêu thụ rất ít tài nguyên hệ thống.

## Kiến Trúc và Cơ Chế Hoạt Động

Kiến trúc hệ thống của NGINX được phân tách thành các quy trình chuyên biệt nhằm tối ưu hóa hiệu năng:

*   **Master Process:** Đóng vai trò quản lý trung tâm, chịu trách nhiệm đọc cấu hình và điều phối các quy trình con.
*   **Child Processes:**
    *   **Worker Processes (W):** Đảm nhận nhiệm vụ cốt lõi là xử lý trực tiếp các HTTP request và các luồng giao tiếp mạng khác.
    *   **Cache Manager (CM) & Cache Loader (CL):** Quản lý vòng đời và tải dữ liệu vào bộ nhớ đệm.
    *   **Shared Memory:** Vùng nhớ dùng chung giữa các quy trình con. Khu vực này lưu trữ thông tin về bộ nhớ đệm, giới hạn lưu lượng (rate limits), và duy trì trạng thái phiên làm việc (session persistence).

## Vai Trò Trong Hệ Thống

NGINX cung cấp một hệ sinh thái chức năng đa dạng cho các kiến trúc mạng máy tính:

*   **Web Server & Streaming:** Nền tảng phục vụ nội dung tĩnh (static files) và hỗ trợ các giao thức giao tiếp hiện đại bao gồm WebSocket, HTTP/2, gRPC. Hệ thống cũng cung cấp khả năng truyền phát đa phương tiện với các định dạng như HDS, HLS, RTMP.
*   **Cổng Trung Gian (Proxy):** NGINX hoạt động như một cổng trung gian với chức năng Forward Proxy hoặc Reverse Proxy. Khi triển khai dưới dạng Reverse Proxy, hệ thống đứng trước các máy chủ backend để nhận yêu cầu từ Internet và chuyển tiếp lưu lượng một cách an toàn.
*   **Cân Bằng Tải (Load Balancing):** Nền tảng phân phối lưu lượng mạng đến nhiều máy chủ khác nhau để ngăn ngừa tình trạng quá tải. NGINX hỗ trợ cơ chế cân bằng tải ở cả Layer 4 (Transport Layer - TCP/UDP) và Layer 7 (Application Layer - HTTP) của mô hình OSI. Các thuật toán định tuyến phổ biến bao gồm Round robin, Hash, IP Hash, Least Connections, và Least time.
*   **Bộ Nhớ Đệm (Content Caching):** Cơ chế lưu trữ đệm các nội dung tĩnh và động giúp tăng tốc độ phản hồi cho máy khách. Hoạt động này làm giảm tải đáng kể cho các máy chủ upstream.
*   **Bảo Mật và Kiểm Soát:** Hệ thống cung cấp các phương thức cấu hình bảo mật như thiết lập HTTPS (TLS/SSL), xác thực cơ bản (Basic authentication), giới hạn tốc độ (rate limiting), và thiết lập các tiêu đề bảo mật (Content-Security-Policy, CORS).

## Các Giải Pháp Thay Thế

Mặc dù NGINX chiếm một thị phần lớn trong hệ sinh thái máy chủ mạng, một số công cụ khác cung cấp khả năng thay thế tùy thuộc vào bài toán đặc thù:

*   **HAProxy:** Giải pháp chuyên biệt cho cân bằng tải, đặc biệt cung cấp hiệu suất cao tại Layer 4.
*   **Traefik Proxy:** Nền tảng được thiết kế cho hệ sinh thái Cloud-native. Công cụ này tích hợp sâu với Docker và Kubernetes, đồng thời cung cấp khả năng cấu hình động mà không yêu cầu khởi động lại quá trình.
*   **Envoy Proxy:** Proxy thường được triển khai dưới dạng Sidecar trong kiến trúc Microservices và Service Mesh.

## Nguồn Tham Khảo
- [[raw/articles/nginx-tong-quan-va-cau-hinh.md]]
