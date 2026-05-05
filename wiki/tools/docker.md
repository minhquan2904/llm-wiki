---
title: "Docker"
source: "compiled"
date_added: 2026-05-04
tags: [tool, virtualization, container]
aliases: [docker-architecture, dockerd, containerd]
status: canonical
related:
  - "[[nginx]]"
summary: "Nền tảng ảo hóa cấp hệ điều hành dựa trên Linux Namespaces và cgroups để triển khai ứng dụng bằng container."
---

# Docker

## Tổng Quan

Docker là một nền tảng điều phối ảo hóa cấp hệ điều hành (OS-level virtualization), cho phép đóng gói ứng dụng cùng toàn bộ môi trường và thư viện phụ thuộc vào những khối độc lập gọi là **container**. Thay vì tạo ra các máy ảo (Virtual Machines) cồng kềnh chứa toàn bộ hệ điều hành khách (Guest OS), Docker tái sử dụng trực tiếp nhân (kernel) của hệ điều hành Linux máy chủ. Điều này giúp các container có thể khởi động cực kỳ nhanh chóng và tiêu tốn rất ít tài nguyên phần cứng so với phương pháp ảo hóa truyền thống.

Về bản chất, Docker không phải là một siêu trình điều khiển ảo hóa (hypervisor). Nó hoạt động như một hệ thống điều phối, giúp đơn giản hóa việc thiết lập và quản lý hai tính năng nền tảng cốt lõi của Linux Kernel: **Namespaces** và **Control Groups (cgroups)**. 

## Cấu Trúc Kỹ Thuật Lõi

### Namespaces (Lớp Cô Lập)

Namespaces đóng vai trò phân chia tài nguyên hạt nhân, tạo ra "ảo giác" rằng mỗi container đang chạy trên một hệ thống hoàn toàn chuyên biệt và độc lập. Các tiến trình bên trong một container không thể nhìn thấy hay can thiệp vào các tiến trình của container khác hoặc của máy chủ. Cụ thể:

- **PID Namespace:** Cô lập không gian ID tiến trình. Tiến trình chính của một container sẽ trở thành PID 1 bên trong không gian của nó, hoàn toàn tách biệt với bên ngoài.
- **Network Namespace:** Cung cấp cho mỗi container một ngăn xếp mạng riêng biệt, bao gồm địa chỉ IP, bảng định tuyến và giao diện mạng độc lập.
- **Mount Namespace:** Cô lập hệ thống file, cho phép mỗi container có các điểm gắn kết (mount points) và cấu trúc thư mục root riêng.
- **Các Namespaces khác:** Bao gồm IPC (cô lập giao tiếp liên tiến trình), UTS (cô lập tên miền và hostname) và User (ánh xạ ID người dùng, giới hạn đặc quyền để tăng cường bảo mật).

### Control Groups - cgroups (Lớp Quản Lý Tài Nguyên)

Nếu Namespaces xác định những gì container có thể *thấy*, thì cgroups kiểm soát lượng tài nguyên vật lý mà container có thể *tiêu thụ*. Cơ chế này đóng vai trò sống còn trong việc ngăn chặn một container bị lỗi hoặc độc hại chiếm đoạt toàn bộ tài nguyên hệ thống (RAM, CPU, I/O), gây ảnh hưởng đến hiệu năng của các ứng dụng khác. Cgroups cung cấp khả năng áp đặt giới hạn cứng, ưu tiên phân bổ tài nguyên và giám sát quá trình sử dụng của từng container.

## Chu Trình Vận Hành

Khi một lệnh thực thi được ban hành (ví dụ: `docker run`), chu trình điều phối sẽ diễn ra tuần tự qua các thành phần:

1. **Tiếp nhận:** Docker CLI truyền chỉ thị đến Docker daemon (`dockerd`).
2. **Điều phối:** `dockerd` giao nhiệm vụ cho runtime cấp thấp (thường là `runc` thông qua `containerd`) để chuẩn bị môi trường.
3. **Tương tác Kernel:** Runtime yêu cầu nhân Linux cấp phát bộ Namespaces mới để cô lập tiến trình, thiết lập cgroups theo cấu hình tài nguyên giới hạn và gắn kết hệ thống file gốc.
4. **Thực thi:** Tiến trình lõi của ứng dụng được kích hoạt bên trong môi trường đã được cô lập và rào giậu tài nguyên này một cách an toàn.

## Nguồn Tham Khảo

- [[raw/articles/docker-architecture-core.md]]
