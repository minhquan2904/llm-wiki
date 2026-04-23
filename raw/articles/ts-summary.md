---
title: "TypeScript: Sinh Tồn Trong Kỷ Nguyên Kỹ Thuật Số"
source: "raw/misc/ts/summary.md"
date_added: 2026-04-23
tags: [typescript, overview, cyber-shogun]
aliases: [typescript-sinh-ton-trong-ky-nguyen-ky-thuat-so]
status: draft
summary: "Tổng quan series TypeScript phong cách Cyber-Shogun - Sinh tồn trong Runtime Wasteland."
---

# :material-robot-industrial: TypeScript: Sinh Tồn Trong Kỷ Nguyên Kỹ Thuật Số

!!! abstract "Giới thiệu Series"
    JavaScript là một Runtime Wasteland (Miền đất hoang) – tự do, linh hoạt nhưng đầy rẫy chấn thương chí mạng từ lỗi runtime. Để sinh tồn, bạn cần một bộ giáp. **TypeScript** chính là bộ giáp Exoskeleton đó. Series này áp dụng phương pháp Edutainment (Cyber-Shogun Metaphor) để biến các khái niệm khô khan thành những hệ thống sinh tồn tương lai.

## Lộ Trình Lắp Ráp (Roadmap)

Dự án Exoskeleton sẽ được triển khai qua các phân hệ sau:

| Module | Phân Hệ | Mục Tiêu Kỹ Thuật | Trạng Thái |
|:---:|---|---|:---:|
| **01** | [:material-tools: Lò Phản Ứng & Phân Hệ Cốt Lõi](./ts-module-01.md) | Cài đặt `tsc`. Hiểu thấu đáo về Type Erasure và các Basic Types (`string`, `number`, `boolean`, `any`, `void`). | :material-check-circle: |
| **02** | [:material-shield-link-variant: Khung Giáp Exosuit (OOP)](./ts-module-02.md) | Lập trình Hướng Đối Tượng: Class và Cơ chế phòng thủ Access Modifiers (`public`, `private`, `#private`, `protected`, `readonly`). | :material-check-circle: |
| **03** | [:material-cogs: Hệ Điều Hành Trung Tâm (tsconfig)](./ts-module-03.md) | Khám phá Kernel và Bộ luật Bushido (Strict Mode). Cấu hình sinh tồn với TS 5.7/5.8. | :material-check-circle: |
| **04** | [:material-anvil: Lò Rèn Kỹ Thuật (Functions)](./ts-module-04.md) | Giải phẫu Hàm, Optional Params, và sự phân biệt sống còn giữa `void` (không lấy sản phẩm) và `never` (hủy diệt). | :material-check-circle: |
| **05** | [:material-sword-cross: Vũ Khí Lai & Nhãn Quan (Unions & Narrowing)](./ts-module-05.md) | Khống chế đa hình với Union Types, phân tích luồng đạn đạo: `typeof`, `in`, Discriminated Unions, Exhaustiveness. | :material-check-circle: |
| **06** | [:material-matrix: Nội Chiến Kiến Trúc (Interface vs Type)](./ts-module-06.md) | Bản vẽ cơ khí (Interface) đối đầu Thuật giả kim phân tử (Type). Giải mã Declaration Merging và bức tường Red Text. | :material-check-circle: |
| **07** | [:material-dna: Hệ Gen Nhân Tạo (Generics)](./ts-module-07.md) | Kiến tạo vũ khí thích ứng qua Type Variables `<T>` và kiểm soát đột biến bằng Constraints. | :material-check-circle: |

*...Hệ thống đang tiếp tục được cập nhật...*
