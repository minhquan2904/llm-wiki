---
title: "TypeScript"
source: "compiled"
date_added: 2026-04-23
tags: [typescript, concept, programming-language]
aliases: [TS, TypeScript Compiler, tsc]
status: canonical
related:
  - "[[typescript-basic-types]]"
  - "[[typescript-oop]]"
  - "[[tsconfig]]"
summary: "Ngôn ngữ lập trình bổ sung hệ thống định kiểu tĩnh nghiêm ngặt vào JavaScript, loại bỏ lỗi runtime thông qua quá trình Type Erasure."
---

# TypeScript

## Định Nghĩa
TypeScript là một ngôn ngữ lập trình mã nguồn mở do Microsoft phát triển và duy trì. Nó là một siêu tập (superset) của JavaScript, bổ sung thêm hệ thống định kiểu tĩnh (Static Typing) tùy chọn. Đoạn mã TypeScript không thể chạy trực tiếp trên trình duyệt hoặc Node.js mà phải trải qua quá trình biên dịch (transpile) để chuyển đổi thành JavaScript thuần túy.

Tài liệu *"TypeScript: Sinh Tồn Trong Kỷ Nguyên Kỹ Thuật Số"* mô tả sự khác biệt giữa hai ngôn ngữ này thông qua một phép ẩn dụ: JavaScript được ví như một "miền đất hoang" (Runtime Wasteland) linh hoạt nhưng chứa đầy rủi ro tiềm ẩn, trong khi TypeScript đóng vai trò như một "bộ giáp Exoskeleton" giúp bảo vệ lập trình viên khỏi các chấn thương chí mạng do lỗi runtime gây ra.

## Cơ Chế Type Erasure (Loại Bỏ Kiểu)
Một đặc điểm cốt lõi của TypeScript là cơ chế **Type Erasure**. Quá trình này diễn ra khi trình biên dịch `tsc` (TypeScript Compiler) dịch mã từ TypeScript sang JavaScript.

Tất cả các định nghĩa kiểu dữ liệu (như `Type`, `Interface`, hay các chú thích kiểu `Type Annotations`) sẽ bị loại bỏ hoàn toàn khỏi mã nguồn sau khi build. Hệ thống định kiểu chỉ tồn tại trong thời gian thiết kế (Compile Time) để báo lỗi và hỗ trợ lập trình viên. Tại thời điểm chạy (Runtime), chúng không còn tồn tại, đảm bảo hiệu suất không bị ảnh hưởng. Điều này đồng nghĩa với việc TypeScript không thực hiện kiểm tra kiểu ở môi trường runtime.

## Kiến Trúc Phân Hệ
Hệ thống TypeScript bao gồm nhiều phân hệ để giải quyết các vấn đề khác nhau của JavaScript:
- **[[typescript-basic-types|Basic Types]]**: Quản lý các kiểu dữ liệu cơ sở như `string`, `number`, `boolean`, `void`, `any`.
- **[[typescript-oop|Lập Trình Hướng Đối Tượng (OOP)]]**: Cung cấp cấu trúc Class và các bộ điều khiển truy cập (Access Modifiers).
- **[[tsconfig|TSConfig và Strict Mode]]**: Cấu hình hạt nhân (Kernel) quản lý hành vi của trình biên dịch.
- **[[typescript-functions|Functions]]**: Kiểm soát định dạng tham số đầu vào và kết quả đầu ra của hàm.
- **[[typescript-type-narrowing|Type Narrowing]]**: Kỹ thuật thu hẹp kiểu và quản lý đa hình với Union Types.
- **[[interface-vs-type-alias|Interface vs Type Alias]]**: Kiến trúc định nghĩa hình dáng dữ liệu (Data Shape).
- **[[typescript-generics|Generics]]**: Kiến tạo kiểu dữ liệu linh hoạt, có thể tái sử dụng.

## Nguồn Tham Khảo
- [[raw/articles/ts-summary.md]]
- [[raw/articles/ts-module-01.md]]
