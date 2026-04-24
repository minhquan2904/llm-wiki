---
title: "Kiến Trúc Tính Bất Biến (Immutability) Trong Java"
source: "compiled"
date_added: 2026-04-24
tags: [concept, java, immutability, architecture]
aliases: [java-immutability, records, stateless-beans]
status: draft
related:
  - "[[java-concurrency-fundamentals]]"
  - "[[spring-ioc-di]]"
summary: "Phân tích tác động kiến trúc của tính bất biến, từ cơ chế phòng thủ đa luồng đến việc triển khai Java Records và Stateless Spring Beans."
---

# Kiến Trúc Tính Bất Biến (Immutability) Trong Java

Trong kiến trúc hướng đối tượng của Java, cuộc đối đầu giữa Tính Khả biến (Mutable) và Tính Bất biến (Immutable) không chỉ là vấn đề cú pháp mà đại diện cho triết lý quản lý trạng thái. Tính bất biến là hòn đá tảng cho việc xây dựng các ứng dụng đồng thời (Concurrent Applications) an toàn mà không cần tới sự phức tạp của cơ chế khóa (Locks).

## Nền Tảng An Toàn Đa Luồng

Mối đe dọa sinh tử của lập trình đa luồng - Race Condition - xuất phát trực tiếp từ việc chia sẻ các thực thể trạng thái (State) có khả năng bị sửa đổi. Sự bất biến tiêu diệt triệt để nguồn cơn rủi ro này: Một đối tượng sau khi khởi tạo sẽ hoàn toàn bị đóng băng, cấm tiệt mọi can thiệp thay đổi giá trị thuộc tính. 

Vì trạng thái không bao giờ thay đổi, nhiều luồng có thể tùy ý đọc dữ liệu song song mà không cần cơ chế Đồng bộ khóa (Synchronization). Các chi phí luân chuyển ngữ cảnh (Context Switching) đắt đỏ hay hiện tượng Chặn luồng (Thread Blocking) đều bị loại bỏ, mang lại khả năng thông lượng tối ưu ở cấp độ lõi phần cứng.

## Stateless Beans: Triết Lý Thiết Kế Spring

Trong môi trường Spring Framework, thiết kế Bean mặc định tuân theo mẫu Singleton: chỉ có một hiện thân duy nhất của đối tượng phục vụ toàn bộ người dùng. Nếu Spring Bean chứa trạng thái khả biến (Ví dụ: Một biến toàn cục `int counter`), hệ thống sẽ bị phá vỡ hoàn toàn khi nhiều yêu cầu song song tương tác thay đổi giá trị biến này.

Kiến trúc chuẩn của Spring bắt buộc các thành phần hạt nhân như `@Service` hay `@Controller` phải thiết kế theo mẫu **Stateless (Phi trạng thái)**. Trạng thái không tồn tại trên lớp, mà chỉ được luân chuyển xuyên suốt qua các tham số hàm (Method Parameters) hoặc đóng gói cô lập trong các biến cục bộ cục bộ tĩnh nằm trên Thread Stack của mỗi tiến trình.

## Sự Tiến Hóa của Java Records

Từ Java 14, cấu trúc `record` được giới thiệu như một lớp cấu trúc tối ưu (First-class citizen) đại diện cho Data Carrier thuần khiết, thay thế các lớp POJO cồng kềnh với hàm Getter, Setter lặp lại.

Bằng việc ép buộc tất cả các trường dữ liệu đều là `final` một cách ẩn danh, Java Records cung cấp một lớp giáp bảo vệ tự nhiên. Record trở thành mẫu thiết kế chuẩn mực khi kiến tạo cấu trúc Data Transfer Object (DTO) nhận tải trọng trong REST API kết hợp với Validation, giúp ngăn chặn mọi ý đồ ghi đè dữ liệu ở các tầng phân xử (Layers) tiếp theo.

Mặc dù mạnh mẽ, nguyên tắc bất biến sinh ra rủi ro hao phí bộ nhớ trên không gian Heap do phải liên tục khởi tạo một bản sao đối tượng hoàn toàn mới khi cần sửa một trường nhỏ. Vấn đề Garbage Collection trở thành nỗi bận tâm đánh đổi của kiến trúc sư trước quyết định áp dụng Immutability diện rộng.

## Nguồn Tham Khảo
- `raw/papers/mutable-vs-immutabletác-động-kiến-trúc-trong-java-spring-từ-cơ-chế-jvm-đến-thiết.md`
- `raw/papers/đa-luồng-chân-kinh.md`
