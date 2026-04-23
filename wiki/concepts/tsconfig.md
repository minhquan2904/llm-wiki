---
title: "Khảo Sát Cấu Hình Hệ Thống TypeScript (tsconfig.json)"
source: "compiled"
date_added: 2026-04-23
tags: [typescript, tsconfig, strict-mode, concept]
aliases: [tsconfig.json, compiler-options, Strict Mode]
status: canonical
related:
  - "[[typescript]]"
  - "[[typescript-type-narrowing]]"
summary: "Phân tích cấu hình cốt lõi tsconfig.json quản lý trình biên dịch TypeScript, với trọng tâm vào hệ quy tắc khắt khe Strict Mode."
---

# Khảo Sát Cấu Hình Hệ Thống TypeScript (tsconfig.json)

## Định Nghĩa
Nếu các tệp tin `.ts` là cấu trúc mã nguồn, thì `tsconfig.json` hoạt động như hạt nhân (Kernel) hay hệ điều hành trung tâm quản lý bộ biên dịch `tsc`. Tệp tin này định nghĩa các chuẩn xuất mã nguồn (chuẩn hóa vật lý), thiết lập quy tắc an ninh mạng (Strict Mode), và quy định cấu trúc JavaScript cuối cùng sẽ được tạo ra thông qua quá trình biên dịch.

## 1. Compiler Options Cơ Bản
Các tùy chọn hạt nhân giúp điều hướng đầu ra tương thích với hệ thống đích (Runtime Environment).

*   **`target` (Tiêu chuẩn ECMA):** Xác định phiên bản JavaScript mục tiêu. Biên dịch ra `ES5` giúp tương thích với các nền tảng rất cũ nhưng làm phình mã nguồn (Bloatware) với polyfill. Các phiên bản hiện đại như `ES2022` hoặc cao hơn (v.d. `ES2024` trên TypeScript 5.7+) tận dụng tối đa sức mạnh của Engine JS (hàm mũi tên, `Promise.withResolvers`).
*   **`module` (Cấu trúc mạng lưới):** Định nghĩa cách các module liên kết với nhau. Lựa chọn `CommonJS` phù hợp cho môi trường Node.js kiểu cũ (đồng bộ), trong khi `NodeNext` hay `ESNext` là chuẩn hiện đại, hỗ trợ hiệu quả cơ chế "Tree-shaking" (loại bỏ mã thừa) và bảo mật khi tải module.

## 2. Hệ Quy Tắc Strict Mode
Cờ `strict: true` là rào chắn quan trọng nhất trong cấu hình, kích hoạt chuỗi kiểm tra thiết quân luật lên toàn bộ Codebase nhằm ngăn chặn các lỗ hổng tại thời điểm biên dịch. Tài liệu *"Sinh Tồn Trong Kỷ Nguyên Kỹ Thuật Số"* gọi cờ này là "Bộ luật Samurai" không thể bỏ qua đối với bất kỳ dự án mới nào.

*   **`noImplicitAny`:** Ngăn chặn việc khai báo biến mà không xác định kiểu rõ ràng (TypeScript sẽ ngầm đoán thành `any`). Cờ này bắt buộc lập trình viên phải định nghĩa kiểu tường minh để tránh các "sương mù chiến thuật" che lấp rủi ro.
*   **`strictNullChecks`:** Ngăn cấm việc gán giá trị `null` hoặc `undefined` vào một biến có kiểu dữ liệu khác (ví dụ: `string`). Nó buộc hệ thống phải đánh giá tính tồn tại của dữ liệu (bằng If Guard) để triệt tiêu lỗi Runtime khét tiếng: *"Cannot read property of undefined"*.
*   **`strictPropertyInitialization`:** Yêu cầu các thuộc tính của `Class` phải được khởi tạo giá trị rõ ràng ngay tại lúc khai báo hoặc thông qua constructor.
*   **`exactOptionalPropertyTypes`:** Tách biệt rõ ràng ranh giới giữa một thuộc tính tuỳ chọn bị bỏ trống (`property?: string`) và một thuộc tính bị cố tình gán chuỗi rỗng phi thực tế (`property: undefined`).

## 3. Các Công Nghệ Trình Biên Dịch Đột Phá (TS 5.7/5.8)
TypeScript liên tục tiến hóa các cờ mới nhằm giải quyết các rào cản phát triển.

*   **`--rewriteRelativeImportExtensions` (TS 5.7+):** Cho phép lập trình viên tự do nhập (import) các module nội bộ dưới đuôi `.ts` ngay trong mã nguồn. Trình biên dịch sẽ tự động phiên dịch đồng loạt chúng thành đuôi `.js` trong luồng đầu ra, giải quyết rắc rối hậu cần đối với các nền tảng như Node.js hay Deno.
*   **`--erasableSyntaxOnly` (TS 5.8):** Được mệnh danh là "Chế độ tàng hình Node.js". Cờ này ép buộc chỉ được phép sử dụng các cú pháp có thể bị xóa thẳng mà không để lại tác động (Type Erasure). Nó cấm sử dụng `enum` hoặc `parameter properties`, giúp mã chạy siêu tốc trực tiếp trên engine mới (ví dụ: cờ `--experimental-strip-types` của Node).
*   **`noUncheckedIndexedAccess` (Khuyến nghị bổ sung):** Cảnh báo bắt buộc kiểm tra điều kiện an toàn khi truy cập một phần tử vào mảng (Array) hoặc đối tượng (Object) bằng tham số động, do rủi ro kết quả trả về `undefined` tiềm tàng.

## Nguồn Tham Khảo
- [[raw/articles/ts-module-03.md]]
