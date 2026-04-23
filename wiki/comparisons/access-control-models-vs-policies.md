---
title: "Mô hình (Model) và Chính sách (Policy) Kiểm Soát Truy Cập"
source: "raw/articles/ModelsAndPolicies.md"
date_added: 2026-04-23
tags: [comparison, access-control]
aliases: [Model vs Policy]
status: draft
related:
  - "[[access-control-policy-enforcement]]"
summary: "Sự phân biệt giữa khuôn khổ thiết kế lý thuyết (Mô hình) và bộ quy tắc thực thi cụ thể (Chính sách) trong hệ thống bảo mật."
---

## Bối Cảnh

Trong kỹ thuật an toàn thông tin, các kỹ sư thường xuyên sử dụng lẫn lộn hai thuật ngữ "Mô hình kiểm soát truy cập" (Access Control Model) và "Chính sách kiểm soát truy cập" (Access Control Policy). Tuy nhiên, đây là hai lớp kiến trúc hoàn toàn tách biệt, đóng vai trò từ trừu tượng đến thực tiễn trong việc xây dựng hệ thống phân quyền.

## Bảng So Sánh

| Tiêu chí | Mô hình kiểm soát (Model) | Chính sách kiểm soát (Policy) |
|----------|---------------------------|-------------------------------|
| **Định nghĩa** | Khuôn khổ lý thuyết, phương pháp trừu tượng hóa. | Tập hợp các quy tắc, định mức bảo mật cụ thể. |
| **Mục đích** | Định nghĩa *cách thức* hệ thống xử lý quyền. | Định nghĩa *nội dung* quyền của từng cá nhân. |
| **Phạm vi** | Toàn cục, độc lập với ngữ cảnh thực tế. | Cục bộ, thay đổi theo yêu cầu tổ chức. |
| **Độ hoàn thiện** | Logic toán học chặt chẽ, có thể chứng minh. | Thường là tập hợp hướng dẫn, có thể có điểm mù. |

## Phân Tích

**Mô hình (Model)** cung cấp một cơ sở hạ tầng toán học để quản lý luồng dữ liệu. Các mô hình như DAC, MAC hay ABAC xác định sẵn các đặc tính cấu trúc. Một mô hình không quan tâm đến việc "Nhân viên A có được vào phòng B hay không", mà nó quy định "Hệ thống sẽ dùng danh sách khả năng (Capability List) hay thuộc tính (Attribute) để kiểm tra yêu cầu của nhân viên A". Bản thân các mô hình không chứa cơ chế bảo mật vật lý nào, chúng chỉ cung cấp phương tiện để diễn đạt các quy định an toàn.

**Chính sách (Policy)** là sự lấp đầy ý nghĩa vào trong mô hình đó. Chính sách phản ánh các quy tắc nghiệp vụ của một tổ chức tại một thời điểm nhất định. Ví dụ: "Chỉ các bác sĩ mới được đọc bệnh án ngoại trú" là một chính sách. Khi chính sách này được đưa vào cấu trúc của hệ thống, tổ chức cần đảm bảo tính chính xác thông qua các quy trình bảo đảm thông tin (Information Assurance).

## Kết Luận

Một tổ chức có thể thay đổi liên tục các Chính sách của mình theo từng quý mà không cần can thiệp vào mã nguồn, miễn là Mô hình bên dưới đủ linh hoạt để diễn đạt các thay đổi đó. Việc phân định rõ giữa Mô hình và Chính sách giúp hệ thống tránh được sự cứng nhắc khi đối mặt với sự thay đổi của yêu cầu kinh doanh.

## Nguồn Tham Khảo
- `raw/articles/ModelsAndPolicies.md`
