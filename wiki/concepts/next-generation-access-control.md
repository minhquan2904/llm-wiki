---
title: "Kiểm soát truy cập thế hệ tiếp theo (NGAC)"
source: "compiled"
date_added: 2026-04-23
tags: [concept, access-control, ngac, abac]
aliases: [Next-Generation Access Control, NGAC]
status: draft
related:
  - "[[attribute-based-access-control]]"
  - "[[abac-architecture]]"
summary: "Mô hình kiểm soát truy cập linh hoạt, hỗ trợ đa chính sách và quản lý sự kiện trạng thái."
---

## Định Nghĩa

Kiểm soát truy cập thế hệ tiếp theo (Next-Generation Access Control - NGAC) là một mô hình kiểm soát quyền hạn được xây dựng nhằm khắc phục các giới hạn của mô hình phân quyền truyền thống. Dựa trên kiến trúc thuộc tính, NGAC cung cấp một bộ khung trừu tượng dữ liệu thống nhất, cho phép thực thi đồng thời và tương thích nhiều loại chính sách truy cập khác nhau (bao gồm cả các chính sách cũ) trong cùng một hệ thống.

## Kiến Trúc Cốt Lõi

Khác với các hệ thống chỉ tập trung vào việc định dạng yêu cầu truy cập, NGAC chú trọng việc quản lý cấu trúc các thuộc tính và mối quan hệ chứa đựng của chúng. NGAC kế thừa các thành phần chức năng cơ bản của [[abac-architecture]] như PEP, PDP, PIP, PAP, và RAP. Tuy nhiên, nó bổ sung thêm một yếu tố trọng yếu:
- **EPP (Event Processing Point - Điểm xử lý sự kiện):** Nơi bắt giữ các thay đổi trạng thái trong môi trường và tiến hành điều chỉnh quy tắc kiểm soát theo thời gian thực. Cơ chế này tạo ra phản ứng linh hoạt trước các sự cố hoặc sự kiện hệ thống.

Bên cạnh đó, NGAC được thiết kế dưới dạng mở (open factors), cho phép tổ chức tự do định nghĩa cấu trúc định danh, giao thức truyền thông, phương pháp mã hóa và ngôn ngữ chính sách mà không bị ràng buộc vào các tiêu chuẩn cứng nhắc.

## Lợi Thế Và Hạn Chế

Ưu điểm chính của NGAC nằm ở tính **Thống nhất** và **Mở rộng**. Nó cho phép tích hợp các quy tắc quản trị trung ương song song với các thiết lập bảo mật cục bộ của từng bộ phận. Sự tách biệt hoàn toàn giữa cấu trúc hoạt động và loại chính sách cụ thể tạo ra một hệ thống dễ dàng thích ứng với điện toán đám mây và môi trường phân tán.

Tuy nhiên, tính đa dạng này đồng nghĩa với việc **phức tạp trong triển khai**. Việc tích hợp NGAC đòi hỏi đánh giá tỉ mỉ nhằm duy trì tính tương thích giữa các thực thể hoạt động dưới nhiều bộ chính sách đan chéo. Thêm vào đó, kiến trúc xét duyệt sâu cũng cần nguồn lực tính toán lớn để không gây gián đoạn hiệu năng.

## Liên Hệ / Ứng Dụng

NGAC đặc biệt phù hợp trong cấu trúc doanh nghiệp hiện đại hoặc cơ quan công quyền, nơi mà dữ liệu phân tán ở nhiều hệ thống với quyền hạn khác nhau nhưng lại yêu cầu một cửa ngõ kiểm soát duy nhất. Ví dụ, một đám mây chia sẻ của chính phủ có thể vận hành các nguyên tắc bảo mật riêng tư cục bộ tại các chi nhánh, đồng thời tuân thủ quy tắc bảo mật an ninh quốc gia từ trung ương, tất cả được xử lý đồng bộ qua kiến trúc đa chính sách của NGAC.

## Nguồn Tham Khảo
- `raw/articles/NGAC.md`
- `raw/articles/ArchitecturesandFunctionalComponents.md`
