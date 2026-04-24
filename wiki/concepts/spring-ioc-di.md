---
title: "Spring IoC và Dependency Injection"
source: "compiled"
date_added: 2026-04-24
tags: [concept, java, spring, architecture, dependency-injection]
aliases: [spring-ioc-di, ioc-container, dependency-injection, applicationcontext]
status: draft
related:
  - "[[java-immutability]]"
  - "[[spring-annotations]]"
summary: "Kiến trúc cốt lõi của Spring Framework dựa trên cơ chế Đảo ngược Điều khiển (IoC) và Tiêm Phụ thuộc (DI) thông qua ApplicationContext."
---

# Spring IoC và Dependency Injection

Spring Framework được xây dựng trên một triết lý thiết kế cơ bản nhằm giải quyết sự phụ thuộc vòng lặp và tính kết dính lỏng lẻo thông qua hai khái niệm cốt lõi: Đảo ngược Điều khiển (Inversion of Control - IoC) và Tiêm Phụ thuộc (Dependency Injection - DI).

## Đảo Ngược Điều Khiển (IoC)

Inversion of Control (IoC) là một mô hình kiến trúc trong đó luồng điều khiển của ứng dụng bị đảo ngược. Thay vì mã nguồn của nhà phát triển chủ động khởi tạo và quản lý vòng đời của các đối tượng (thông qua từ khóa `new`), tác vụ này được giao lại cho một thực thể bên ngoài gọi là IoC Container. 

Trong hệ sinh thái Spring, `ApplicationContext` chính là triển khai cao cấp nhất của IoC Container. Nó đảm nhận vai trò phân tích mã nguồn, khởi tạo, kết nối và tiêu hủy các đối tượng do Spring quản lý (hay còn gọi là Spring Beans). Lợi ích của IoC là giúp tách biệt logic nghiệp vụ khỏi quá trình quản lý tài nguyên.

## Tiêm Phụ Thuộc (Dependency Injection)

Dependency Injection (DI) là phương pháp thực hành IoC, trong đó các thành phần phụ thuộc của một đối tượng được tiêm vào từ bên ngoài thay vì được tự khởi tạo bên trong đối tượng đó. Các chiến lược DI phổ biến bao gồm:

- **Constructor Injection:** Phương pháp được khuyến nghị mạnh mẽ nhất. Các thành phần phụ thuộc được truyền thông qua hàm khởi tạo. Điều này đảm bảo tính toàn vẹn (không bị null), tạo ra các đối tượng bất biến (Immutable) nhờ từ khóa `final`, và hỗ trợ viết kiểm thử vòng đời dễ dàng hơn.
- **Field Injection (`@Autowired` trên biến):** Phương pháp này tiêm thẳng đối tượng vào biến toàn cục. Mặc dù cú pháp ngắn gọn, giới kiến trúc sư phần mềm khuyên tránh sử dụng do nó che giấu sự phức tạp của các mối phụ thuộc và tạo ra trạng thái khả biến (Mutable state).

## Ứng Dụng Cấu Hình Tự Động (Auto-configuration)

Spring Boot tự động hóa phần lớn quá trình cấu hình IoC Container thông qua cơ chế Auto-configuration. Bằng cách sử dụng các điều kiện đánh giá ngữ cảnh như `@ConditionalOnClass` hoặc `@ConditionalOnMissingBean`, Spring Boot quyết định xem có nên cấu hình các Beans mặc định hay không. Điều này tạo nên đặc tính "Opinionated Defaults" - cung cấp những lựa chọn thiết lập chủ quan ban đầu giúp hệ thống có thể vận hành ngay lập tức.

Ngoài ra, DI trong Spring còn hỗ trợ triển khai Strategy Pattern một cách tinh tế. Bằng cách tiêm một danh sách các hiện thực cụ thể (`List<Interface>`), hệ thống tự động tập hợp tất cả các Beans tuân theo hợp đồng đó, cho phép mở rộng tính năng mà không vi phạm nguyên lý Open/Closed.

## Nguồn Tham Khảo
- `raw/papers/nhập-môn-spring-boot-bí-kíp-nấu-code-chuẩn-5-sao.md`
- `raw/papers/đa-luồng-chân-kinh.md`
- `raw/papers/mutable-vs-immutabletác-động-kiến-trúc-trong-java-spring-từ-cơ-chế-jvm-đến-thiết.md`
