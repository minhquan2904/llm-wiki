# Glossary

Danh sách các thuật ngữ và khái niệm cốt lõi được sử dụng trong hệ thống tri thức, đặc biệt trong lĩnh vực Kiểm soát Truy cập (Access Control).

## A
- **ABAC (Attribute-Based Access Control):** Kiểm soát truy cập dựa trên thuộc tính. Mô hình định tuyến quyền hạn dựa trên đánh giá linh hoạt các đặc tính của người dùng, đối tượng, thao tác và môi trường xung quanh.
- **ACL (Access Control List):** Danh sách kiểm soát truy cập. Biểu diễn lưu trữ theo định hướng Đối tượng, nơi mỗi tài nguyên sẽ lưu lại một danh sách chứa tên Chủ thể kèm theo quyền tương ứng.
- **Authentication:** Xác thực. Quá trình kiểm chứng danh tính của một thực thể để trả lời câu hỏi "Bạn là ai?".
- **Authorization:** Ủy quyền. Quá trình kiểm tra và quyết định quyền hạn để trả lời câu hỏi "Bạn được phép làm gì?".

## C
- **Capability List:** Danh sách khả năng. Biểu diễn lưu trữ theo định hướng Chủ thể, nơi hệ thống cấp cho mỗi người dùng một danh sách gồm các Đối tượng và quyền hạn tương ứng trên Đối tượng đó.

## D
- **DAC (Discretionary Access Control):** Kiểm soát truy cập tùy ý. Mô hình kiểm soát linh hoạt cho phép người tạo/chủ sở hữu tài nguyên tự ý quản lý và chia sẻ lại quyền truy cập cho người khác.

## E
- **EPP (Event Processing Point):** Điểm xử lý sự kiện. Thành phần trong mô hình NGAC, chịu trách nhiệm nhận diện và phản ứng với các thay đổi trạng thái trong môi trường theo thời gian thực để cập nhật chính sách.

## M
- **MAC (Mandatory Access Control):** Kiểm soát truy cập bắt buộc. Mô hình nghiêm ngặt nơi mọi quyền truy cập đều bị chi phối bởi các quy tắc trung tâm, bất kể ý chí của người dùng sở hữu tài nguyên.
- **MLS (Multilevel Security):** Bảo mật Đa mức. Một phương pháp triển khai MAC phổ biến, gán các cấp độ bảo mật theo thứ bậc và phân loại, thường áp dụng quy tắc "không đọc lên" và "không ghi xuống".

## N
- **NGAC (Next-Generation Access Control):** Kiểm soát truy cập thế hệ tiếp theo. Mô hình truy cập dựa trên biểu đồ và cấu trúc dữ liệu thuộc tính, cho phép biểu diễn các chính sách phức tạp và đồng nhất.

## O
- **Object:** Đối tượng. Các tài nguyên thụ động trong hệ thống như tập tin, cơ sở dữ liệu hoặc thiết bị, là mục tiêu của các yêu cầu thao tác.

## P
- **PAP (Policy Administration Point):** Điểm quản trị chính sách. Nơi các quản trị viên tạo lập, chỉnh sửa và quản lý vòng đời của các quy tắc kiểm soát quyền hạn.
- **PDP (Policy Decision Point):** Điểm quyết định chính sách. "Khối óc" của hệ thống phân quyền, nơi thực hiện đánh giá các yêu cầu truy cập dựa trên các chính sách đã được định cấu hình.
- **PEP (Policy Enforcement Point):** Điểm thực thi chính sách. "Trạm kiểm soát" đầu tiên chặn các luồng yêu cầu từ người dùng, gửi dữ liệu đến PDP để chờ quyết định, sau đó cấp hoặc từ chối quyền truy cập tương ứng.
- **PIP (Policy Information Point):** Điểm thông tin chính sách. Cầu nối dữ liệu làm nhiệm vụ thu thập và cung cấp các thuộc tính từ nhiều nguồn (Cơ sở dữ liệu, dịch vụ danh bạ) để PDP có thông tin ra quyết định.

## R
- **RAP (Resource Access Point):** Điểm truy cập tài nguyên. Giao diện trực tiếp bảo vệ và quản lý các tài nguyên, thường phối hợp với PEP để thực thi quyết định cho các gói dữ liệu cụ thể.
- **RBAC (Role-Based Access Control):** Kiểm soát truy cập dựa trên vai trò. Mô hình truyền thống định nghĩa quyền truy cập dựa trên chức danh công việc của người dùng trong hệ thống.

## S
- **Subject:** Chủ thể. Các thực thể chủ động (như người dùng, tiến trình máy tính) đóng vai trò yêu cầu hoặc thực hiện các hoạt động lên các Đối tượng.
