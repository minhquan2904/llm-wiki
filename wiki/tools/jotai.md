---
title: "Jotai"
source: "compiled"
date_added: 2026-04-24
tags: [tool, react, state-management]
aliases: [Jotai]
status: canonical
related:
  - "[[react-router-dom]]"
  - "[[ngrx-state-management]]"
summary: "Thư viện quản lý trạng thái (state management) cho React theo mô hình cấu trúc nguyên tử (Atomic), tối ưu vấn đề re-render của Context API."
---

# Jotai

## Tổng Quan

Jotai là một thư viện quản lý trạng thái (state management) dành cho React, hoạt động dựa trên triết lý cốt lõi là **Atomic State**. Thay vì lưu trữ toàn bộ trạng thái hệ thống trong một kho chứa (store) khổng lồ tập trung, Jotai chia nhỏ dữ liệu thành các đơn vị state nhỏ nhất, độc lập và có khả năng tổ hợp lẫn nhau được gọi là các hạt "atom".

## Vai Trò Trong Kiến Trúc Trạng Thái

Jotai được thiết kế như một biện pháp dung hòa nhằm giải quyết các yếu điểm từ các giải pháp truyền thống. Khi đối mặt với vấn đề "Prop Drilling" (khoan qua nhiều tầng component để truyền dữ liệu), Context API là giải pháp mặc định nhưng mang nhược điểm hiệu năng chí mạng: việc thay đổi một giá trị nhỏ trong Context sẽ ép toàn bộ các component đang tiêu thụ Context đó phải kết xuất lại (re-render) dù chúng không sử dụng giá trị thay đổi. Redux giải quyết được việc re-render nhưng yêu cầu kiến trúc vô cùng nặng nề (boilerplate). 

Jotai giải quyết song song hai thách thức này:
- Cho phép khởi tạo các đơn vị trạng thái siêu nhỏ bằng hàm `atom()`.
- Component chỉ đăng ký theo dõi (subscribe) đúng những hạt atom cần thiết, đảm bảo khi dữ liệu thay đổi, chỉ các khu vực bị ảnh hưởng mới được kích hoạt cập nhật giao diện.

Ngoài ra, Jotai cung cấp các mẫu thiết kế linh hoạt như `atomFamily` (tạo atom theo tham số), `atomWithReset` (cơ chế dọn dẹp state cho form) hay việc cho phép một atom được tính toán phái sinh (derived) từ giá trị của các atom khác.

## Lợi Thế / Hạn Chế

**Lợi Thế:**
- **Kích thước cực nhẹ** (chỉ khoảng 8KB) đi kèm với lượng mã khởi tạo (boilerplate) tối giản.
- Khả năng tích hợp tự nhiên một cách xuất sắc với **React Suspense** thông qua việc hỗ trợ trả về Promise ngay bên trong định nghĩa atom (`atom<Promise<T>>`), loại bỏ nhu cầu duy trì trạng thái tải dữ liệu (`isLoading`) một cách thủ công.
- Tối ưu hóa hiệu năng render tuyệt đối bằng cách giới hạn chặt chẽ phạm vi re-render.
- Giải pháp hoàn hảo cho các nền tảng có giới hạn khắt khe về cấu trúc như Zalo Mini App. 

**Hạn Chế:**
- Việc thiếu vắng tính năng giám sát ngược thời gian (time-travel debugging) và hệ sinh thái phần mềm trung gian (middleware) khổng lồ khiến nó chưa thể thay thế hoàn toàn Redux trong các dự án ứng dụng doanh nghiệp (enterprise app) cực lớn.
- Yêu cầu cấu trúc Provider nghiêm ngặt trên một số nền tảng; ví dụ, với `MemoryRouter` trong Zalo Mini App, việc đặt Jotai Provider bên trong định tuyến có thể dẫn đến việc mất mát trạng thái toàn cục khi điều hướng.
- Không phù hợp với những dự án mà hệ thống trạng thái bị chia tách và liên kết phụ thuộc chéo vào nhau ở quy mô quá phức tạp.

## Nguồn Tham Khảo

- [[raw/articles/material-atom-jotai-quản-lý-state-theo-kiểu-nguyên-tử.md]]
