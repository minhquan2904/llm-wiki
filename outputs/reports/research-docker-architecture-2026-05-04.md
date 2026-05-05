---
title: "Research: Kiến trúc cốt lõi Docker"
source: "autoresearch"
date_added: 2026-05-04
tags: [research, autoresearch, docker]
status: draft
related: ["[[nginx]]", "[[n8n]]"]
summary: "Báo cáo nghiên cứu tự động về kiến trúc cốt lõi của Docker: Cơ chế cô lập và quản lý tài nguyên qua Namespaces & Cgroups."
---

## Bối Cảnh
Hệ thống Second Brain trước đây chỉ nhắc đến Docker như một công cụ hạ tầng trong các bài viết về Nginx và n8n, nhưng thiếu đi sự giải phẫu chi tiết về kiến trúc nền tảng và cách thức hoạt động ở cấp độ nhân hệ điều hành. Mục tiêu nghiên cứu này nhằm bù đắp khoảng trống kiến thức về cơ chế ảo hóa cấp hệ điều hành (OS-level virtualization) của Docker.

## Phát Hiện Chính
- **Không phải máy ảo (VM):** Docker không ảo hóa phần cứng mà chỉ điều phối các tính năng sẵn có của nhân Linux (Kernel features) để cung cấp môi trường chạy độc lập cho ứng dụng. (Nguồn: [[docker-architecture-core]])
- **Hai trụ cột kiến trúc:** Sức mạnh của Docker nằm ở việc sử dụng hai công nghệ cốt lõi của Linux Kernel: **Namespaces** và **Control Groups (cgroups)**. (Nguồn: [[docker-architecture-core]])

## Thực Thể & Khái Niệm Mới
- **Concept - Namespaces:** Lớp "cô lập" (Isolation Layer). Giới hạn tầm nhìn của một container đối với hệ thống, đảm bảo nó có một File system, PID (Process ID), không gian mạng, và hostname độc lập.
- **Concept - Cgroups:** Lớp "quản lý tài nguyên" (Resource Management Layer). Xác định lượng tài nguyên phần cứng (CPU, RAM, Disk I/O) tối đa mà một container được phép tiêu thụ để tránh chiếm dụng.
- **Tool - dockerd & containerd:** Tiến trình ngầm (Daemon) tiếp nhận lệnh và phối hợp với runtime (như `containerd` và `runc`) để tạo các Namespaces và Cgroups thông qua Kernel.

## Mâu Thuẫn (nếu có)
- Không có mâu thuẫn lớn. Các tài liệu kỹ thuật đều đồng thuận về vai trò của Namespaces và cgroups. 

## Câu Hỏi Mở
- Cơ chế mạng nội bộ (Docker Networking) như Bridge, Host, Overlay hoạt động như thế nào và có sự khác biệt gì về luồng dữ liệu?
- Docker Image Layers (Lớp hình ảnh) được cấu trúc và quản lý qua hệ thống file đặc thù (UnionFS) như thế nào để tối ưu hóa không gian lưu trữ?

## Nguồn Đã Nạp
- [[docker-architecture-core.md]]
