---
title: "Kiểm soát truy cập tùy ý (Discretionary Access Control - DAC)"
source: "raw/articles/dac.md"
date_added: 2026-04-23
tags: [concept, abac, dac]
aliases: [DAC, Discretionary Access Control]
status: draft
related:
  - "[[mandatory-access-control]]"
  - "[[dac-vs-mac]]"
summary: "Mô hình kiểm soát truy cập dựa trên sự phân quyền chủ động của người sở hữu đối tượng."
---

## Định Nghĩa

Kiểm soát truy cập tùy ý (Discretionary Access Control - DAC) là một mô hình kiểm soát truy cập cho phép người dùng hoặc chủ sở hữu tài nguyên trực tiếp quản lý và quyết định quyền truy cập của những người dùng khác đối với tài nguyên đó. Mô hình này ban đầu được xây dựng dựa trên khái niệm ma trận truy cập (Access Matrix), cung cấp một hệ thống quyền linh hoạt phân bổ theo quyết định cá nhân.

## Cơ Sở Lý Thuyết

Ma trận truy cập là nền tảng của DAC. Để phân tích độ phức tạp của việc tính toán các đặc tính an toàn trong mô hình này, giới nghiên cứu đã đề xuất mô hình **HRU** (Harrison, Ruzzo, Ullman). Một phát hiện quan trọng của mô hình HRU là tính chất an toàn trong các hệ thống DAC truyền thống là không thể quyết định bằng thuật toán (undecidable). Cấu trúc HRU duy trì tính trung lập về mặt chính sách và có thể ứng dụng cả ngoài phạm vi của DAC.

## DAC Trong Thực Tế

Hoạt động của DAC xoay quanh ba yếu tố cốt lõi:
- **Quyền sở hữu:** Mỗi đối tượng (tập tin, thư mục) đều có một chủ sở hữu hợp pháp. Người này nắm toàn quyền quyết định danh sách người dùng được phép truy cập.
- **Quyền hạn quản trị:** Chủ sở hữu có thể thiết lập, chỉnh sửa hoặc thu hồi các điều kiện kiểm soát truy cập đối với tài nguyên của mình.
- **Chuyển giao quyền sở hữu:** Một tính năng tiêu biểu của DAC là chủ sở hữu hiện tại có thể nhượng lại quyền sở hữu tài nguyên cho một thực thể khác.

## Phương Thức Triển Khai

Trong hệ thống máy tính, DAC được thực thi thông qua hai cấu trúc phổ biến:

- **Danh sách khả năng (Capability List):** Hệ thống cấp cho mỗi chủ thể (người dùng/tiến trình) một danh sách các quyền hạn mà nó được phép thực hiện trên các đối tượng khác nhau. Phương pháp này giúp xác minh nhanh chóng khả năng của một người dùng, nhưng lại gặp khó khăn khi muốn thống kê tất cả những ai có quyền truy cập vào một đối tượng cụ thể.
- **Danh sách kiểm soát truy cập (Access Control List - ACL):** Mỗi đối tượng lưu trữ một danh sách chi tiết các người dùng và quyền hạn tương ứng của họ. ACL giúp quản trị viên dễ dàng rà soát quyền trên từng đối tượng, nhưng có thể trở nên cồng kềnh khi hệ thống mở rộng.

## Ưu Điểm Và Hạn Chế

DAC được ứng dụng rộng rãi trong hầu hết các hệ điều hành thương mại nhờ tính **Linh hoạt**, cho phép người dùng tự trị trong việc quản lý dữ liệu cá nhân.

Tuy nhiên, sự tự do này dẫn đến một nhược điểm chí mạng: **Thiếu kiểm soát luồng dữ liệu**. Khi chủ sở hữu cấp quyền đọc cho một người dùng khác, họ không thể ngăn chặn người dùng đó sao chép và chia sẻ lại thông tin. Điểm yếu này khiến DAC dễ bị qua mặt bởi các cuộc tấn công Trojan horse, khi các tiến trình độc hại có thể mượn quyền của người dùng hợp lệ để sao chép thông tin nhạy cảm.

## Nguồn Tham Khảo
- `raw/articles/dac.md`
