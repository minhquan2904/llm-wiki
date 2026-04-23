---
title: "DELETE vs TRUNCATE"
source: "compiled"
date_added: 2026-04-23
tags: [comparison, database, sql, dml, ddl]
aliases: [so sánh delete và truncate, khác biệt giữa delete và truncate]
status: canonical
related:
  - "[[oracle-database]]"
  - "[[acid-properties]]"
  - "[[soft-delete-anti-pattern]]"
  - "[[flashback-data-archive]]"
summary: "Phân tích sự khác biệt cốt lõi giữa lệnh xóa mềm dẻo (DELETE) và lệnh dọn dẹp cấu trúc (TRUNCATE) trong cơ sở dữ liệu quan hệ."
---

## Bối Cảnh

Trong quá trình quản trị và vận hành các hệ thống cơ sở dữ liệu quan hệ (như [[oracle-database]], PostgreSQL, SQL Server), việc dọn dẹp hoặc xóa bỏ dữ liệu là một thao tác thường xuyên. Có hai lệnh cơ bản nhất được sử dụng cho mục đích này là `DELETE` và `TRUNCATE`. Mặc dù kết quả cuối cùng có vẻ tương đồng (dữ liệu biến mất), hai lệnh này lại thuộc hai nhóm thao tác hoàn toàn khác nhau (DML và DDL), dẫn đến sự khác biệt sâu sắc về cơ chế hoạt động, hiệu suất, và khả năng phục hồi. Việc hiểu rõ khi nào nên dùng lệnh nào là kỹ năng cốt lõi để duy trì tính toàn vẹn của [[acid-properties]] và tối ưu hóa tài nguyên hệ thống.

## Bảng So Sánh

| Tiêu chí | `DELETE` | `TRUNCATE` |
| :--- | :--- | :--- |
| **Phân loại lệnh** | DML (Data Manipulation Language) | DDL (Data Definition Language) |
| **Cơ chế hoạt động** | Xóa từng dòng dữ liệu (Row-by-row). | Xóa bằng cách giải phóng (deallocate) toàn bộ trang dữ liệu (Data Pages). |
| **Ghi Log (Logging)** | Ghi chi tiết từng dòng (Row-level logging) vào transaction log (undo/redo). | Ghi log tối thiểu (chỉ ghi nhận việc giải phóng các trang dữ liệu). |
| **Điều kiện xóa** | Hỗ trợ mệnh đề `WHERE` để xóa có chọn lọc. | Không hỗ trợ `WHERE`, xóa toàn bộ dữ liệu trong bảng. |
| **Hiệu suất & Tốc độ** | Chậm hơn, đặc biệt trên các bảng lớn. Tiêu thụ nhiều CPU, I/O và dung lượng Log. | Nhanh hơn đáng kể (gần như tức thời). |
| **Khả năng Rollback** | CÓ. Hoạt động trong một transaction, có thể rollback nếu chưa commit. | KHÔNG (hầu hết các RDBMS). Tự động commit ngầm (Implicit Commit). |
| **Giải phóng không gian**| Không tự động giải phóng bộ nhớ vật lý (High Water Mark không đổi). | Lập tức giải phóng không gian vật lý (Reset High Water Mark). |
| **Kích hoạt Trigger** | Kích hoạt các trigger DML (`BEFORE DELETE`, `AFTER DELETE`). | KHÔNG kích hoạt các trigger DML thông thường. |
| **Reset Identity** | Không reset bộ đếm tự tăng (AUTO_INCREMENT/Identity). | CÓ. Reset bộ đếm tự tăng về giá trị gốc (seed). |
| **Ràng buộc khóa ngoại** | Có thể thực hiện nếu không vi phạm dữ liệu tham chiếu cụ thể. | Bị từ chối ngay lập tức nếu bảng đang bị tham chiếu bởi một khóa ngoại. |

## Phân Tích

### 1. Cơ Chế Xóa và Quản Lý Không Gian Bộ Nhớ

Lệnh `DELETE` tìm kiếm và xóa từng bản ghi. Nó không thực sự xóa dữ liệu trên ổ cứng ngay lập tức mà đánh dấu các bản ghi đó là "đã xóa". Trong kiến trúc [[oracle-database]], điều này có nghĩa là "High Water Mark" (HWM) — điểm đánh dấu khối dữ liệu xa nhất từng được sử dụng — không được dời lại. Do đó, các truy vấn quét toàn bảng (Full Table Scan) vẫn phải đọc qua các khối trống này, gây lãng phí I/O.

Ngược lại, `TRUNCATE` là một lệnh can thiệp vào cấu trúc. Nó bỏ qua dữ liệu bên trong và trực tiếp ra lệnh cho hệ thống lưu trữ thu hồi (deallocate) các trang nhớ đang được cấp phát cho bảng. Hành động này đồng thời reset HWM, trả lại không gian đĩa vật lý ngay lập tức cho Database.

### 2. Chi Phí Giao Dịch và Khả Năng Phục Hồi

Bảo vệ tính toàn vẹn [[acid-properties]] là nhiệm vụ sống còn của CSDL. 
- Khi chạy `DELETE`, hệ thống phải chuẩn bị cho tình huống xấu nhất (lỗi hệ thống, người dùng hủy lệnh). Nó sẽ sao chép dữ liệu cũ vào Undo/Redo log. Điều này tạo ra một lượng I/O khổng lồ với các bảng hàng triệu dòng. Tuy nhiên, đổi lại, bạn có thể dễ dàng khôi phục bằng `ROLLBACK` hoặc các công cụ như [[flashback-data-archive]].
- `TRUNCATE` vượt qua lớp bảo vệ này. Nó thực hiện "Implicit Commit", chốt giao dịch ngay lập tức. Đánh đổi lại tốc độ chớp nhoáng là rủi ro mất dữ liệu vĩnh viễn nếu thao tác nhầm.

### 3. Tương Tác Với Ràng Buộc (Constraints) và Logic Ứng Dụng (Triggers)

Trong một hệ thống nghiệp vụ (Core Banking, E-commerce), việc xóa dữ liệu hiếm khi đứng độc lập.
- Lệnh `DELETE` an toàn hơn về mặt logic nghiệp vụ vì nó tuần tự chạy qua các quy tắc: kiểm tra khóa ngoại cho từng dòng, và kích hoạt các Triggers (`AFTER DELETE`). Đây là lý do nhiều hệ thống ưu tiên sử dụng thiết kế [[soft-delete-anti-pattern]] thay vì `DELETE` trực tiếp để bảo toàn lịch sử.
- Ngược lại, `TRUNCATE` là một con dao sắc bén nhưng mù lòa. Nó phớt lờ mọi DML Triggers. Để bảo vệ dữ liệu, hệ quản trị CSDL sẽ cấm chạy `TRUNCATE` ngay từ đầu nếu bảng đang là mục tiêu tham chiếu của một khóa ngoại, bất kể bảng đó hiện có dữ liệu hay không.

## Kết Luận

- **Sử dụng DELETE khi:** Cần xóa dữ liệu có chọn lọc (dùng `WHERE`), bảng có kích thước nhỏ/vừa, cần kích hoạt các trigger DML để thực thi logic nghiệp vụ, hoặc khi tính an toàn và khả năng khôi phục (Rollback) được đặt lên hàng đầu.
- **Sử dụng TRUNCATE khi:** Cần làm sạch toàn bộ dữ liệu của một bảng lớn một cách tức thì (ví dụ: bảng log tạm thời, bảng staging trong ETL), muốn giải phóng ngay dung lượng lưu trữ vật lý, và chắc chắn rằng dữ liệu đó không cần khôi phục hay kích hoạt trigger.
