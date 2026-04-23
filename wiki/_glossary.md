# Glossary

Danh sách các thuật ngữ và khái niệm cốt lõi được sử dụng trong hệ thống tri thức, đặc biệt trong lĩnh vực Kiểm soát Truy cập (Access Control) và Lập trình JavaScript.

## A
- **ABAC (Attribute-Based Access Control):** Kiểm soát truy cập dựa trên thuộc tính. Mô hình định tuyến quyền hạn dựa trên đánh giá linh hoạt các đặc tính của người dùng, đối tượng, thao tác và môi trường xung quanh.
- **ACL (Access Control List):** Danh sách kiểm soát truy cập. Biểu diễn lưu trữ theo định hướng Đối tượng, nơi mỗi tài nguyên sẽ lưu lại một danh sách chứa tên Chủ thể kèm theo quyền tương ứng.
- **Architectural Hallucination:** Ảo giác kiến trúc. Rủi ro khi AI tự ý đưa ra quyết định sai lệch về yêu cầu nghiệp vụ hoặc mẫu thiết kế do tiếp nhận các câu lệnh mơ hồ.
- **Async/Await:** Cú pháp khai báo giúp viết mã bất đồng bộ trông giống như đồng bộ, giải quyết triệt để tình trạng Callback Hell trong JavaScript.
- **Authentication:** Xác thực. Quá trình kiểm chứng danh tính của một thực thể để trả lời câu hỏi "Bạn là ai?".
- **Authorization:** Ủy quyền. Quá trình kiểm tra và quyết định quyền hạn để trả lời câu hỏi "Bạn được phép làm gì?".

## C
- **Call Stack:** Ngăn xếp gọi hàm. Cấu trúc dữ liệu LIFO ghi nhận các hàm đang được thực thi trong JavaScript.
- **Capability List:** Danh sách khả năng. Biểu diễn lưu trữ theo định hướng Chủ thể, nơi hệ thống cấp cho mỗi người dùng một danh sách gồm các Đối tượng và quyền hạn tương ứng trên Đối tượng đó.
- **Closure:** Bao đóng. Hiện tượng một hàm ghi nhớ và có thể truy cập các biến nằm ở phạm vi bên ngoài của nó ngay cả khi hàm bên ngoài đã thực thi xong.
- **Cognitive Routing:** Định tuyến nhận thức đa chiều. Cơ chế tự động nhận diện ý định ẩn từ mô tả tự nhiên để ánh xạ công việc tới chuyên gia AI phù hợp.

## D
- **DAC (Discretionary Access Control):** Kiểm soát truy cập tùy ý. Mô hình kiểm soát linh hoạt cho phép người tạo/chủ sở hữu tài nguyên tự ý quản lý và chia sẻ lại quyền truy cập cho người khác.

## E
- **EPP (Event Processing Point):** Điểm xử lý sự kiện. Thành phần trong mô hình NGAC, chịu trách nhiệm nhận diện và phản ứng với các thay đổi trạng thái trong môi trường theo thời gian thực để cập nhật chính sách.
- **Event Loop:** Vòng lặp sự kiện. Cơ chế điều phối cốt lõi của JavaScript giúp ngôn ngữ luồng đơn này có thể xử lý các tác vụ bất đồng bộ mà không bị chặn (non-blocking).

## H
- **Hoisting:** Cơ chế kéo phần khai báo biến (var) hoặc hàm lên đầu phạm vi (scope) trong giai đoạn biên dịch trước khi thực thi.

## I
- **Immutability:** Tính bất biến. Trạng thái không thể bị thay đổi sau khi đã được khởi tạo, đóng vai trò quan trọng trong việc quản lý bộ nhớ và kiến trúc State Management.

## M
- **MAC (Mandatory Access Control):** Kiểm soát truy cập bắt buộc. Mô hình nghiêm ngặt nơi mọi quyền truy cập đều bị chi phối bởi các quy tắc trung tâm, bất kể ý chí của người dùng sở hữu tài nguyên.
- **Macrotask / Microtask:** Hàng đợi tác vụ vĩ mô (setTimeout, setInterval) và vi mô (Promise.then, quy trình DOM). Microtask luôn được ưu tiên thực thi trước Macrotask trong Event Loop.
- **Mark-and-Sweep:** Thuật toán Đánh dấu và Quét. Cơ chế thu gom rác (Garbage Collection) mặc định của V8 Engine nhằm tìm và xóa các đối tượng không còn khả năng truy cập từ rễ (Roots).
- **MLS (Multilevel Security):** Bảo mật Đa mức. Một phương pháp triển khai MAC phổ biến, gán các cấp độ bảo mật theo thứ bậc và phân loại, thường áp dụng quy tắc "không đọc lên" và "không ghi xuống".

## N
- **NGAC (Next-Generation Access Control):** Kiểm soát truy cập thế hệ tiếp theo. Mô hình truy cập dựa trên biểu đồ và cấu trúc dữ liệu thuộc tính, cho phép biểu diễn các chính sách phức tạp và đồng nhất.
- **NgRx:** Thư viện quản trị trạng thái (State Management) dành cho Angular, dựa trên mô hình Redux Pattern và RxJS.

## O
- **Object:** Đối tượng. Các tài nguyên thụ động trong hệ thống như tập tin, cơ sở dữ liệu hoặc thiết bị, là mục tiêu của các yêu cầu thao tác.
- **Observable:** Khái niệm cốt lõi của RxJS đại diện cho một luồng dữ liệu (Data Stream) phát sóng theo thời gian, có tính chất lười biếng (lazy) và có thể hủy ngang.

## P
- **PAP (Policy Administration Point):** Điểm quản trị chính sách. Nơi các quản trị viên tạo lập, chỉnh sửa và quản lý vòng đời của các quy tắc kiểm soát quyền hạn.
- **PDP (Policy Decision Point):** Điểm quyết định chính sách. "Khối óc" của hệ thống phân quyền, nơi thực hiện đánh giá các yêu cầu truy cập dựa trên các chính sách đã được định cấu hình.
- **PEP (Policy Enforcement Point):** Điểm thực thi chính sách. "Trạm kiểm soát" đầu tiên chặn các luồng yêu cầu từ người dùng, gửi dữ liệu đến PDP để chờ quyết định, sau đó cấp hoặc từ chối quyền truy cập tương ứng.
- **PIP (Policy Information Point):** Điểm thông tin chính sách. Cầu nối dữ liệu làm nhiệm vụ thu thập và cung cấp các thuộc tính từ nhiều nguồn (Cơ sở dữ liệu, dịch vụ danh bạ) để PDP có thông tin ra quyết định.
- **Progressive Disclosure:** Tải động lũy tiến. Cơ chế phân mảnh và chỉ tải tri thức vào bộ nhớ của mô hình ngôn ngữ khi thực sự cần thiết, giúp tránh tình trạng khủng hoảng do nhồi nhét ngữ cảnh.
- **Promise:** Đối tượng đại diện cho sự hoàn thành hoặc thất bại của một tiến trình bất đồng bộ trong tương lai.
- **Prop Drilling:** Hiện tượng truyền dữ liệu qua nhiều tầng Component trung gian từ cha xuống cháu, gây khó khăn cho việc gỡ lỗi và bảo trì.
- **Prototypal Inheritance:** Kế thừa nguyên mẫu. Cơ chế chia sẻ thuộc tính và phương thức giữa các object trong JavaScript thông qua một chuỗi liên kết ngầm.

## R
- **RAP (Resource Access Point):** Điểm truy cập tài nguyên. Giao diện trực tiếp bảo vệ và quản lý các tài nguyên, thường phối hợp với PEP để thực thi quyết định cho các gói dữ liệu cụ thể.
- **RBAC (Role-Based Access Control):** Kiểm soát truy cập dựa trên vai trò. Mô hình truyền thống định nghĩa quyền truy cập dựa trên chức danh công việc của người dùng trong hệ thống.
- **Reactive Programming:** Lập trình phản ứng. Mô hình lập trình xoay quanh việc thiết lập các luồng dữ liệu bất đồng bộ (Data Streams) và phản ứng khi có dữ liệu mới.
- **Reducer:** Hàm thuần túy (Pure Function) trong mô hình Redux/NgRx chịu trách nhiệm tiếp nhận trạng thái hiện tại và một hành động (Action) để trả về một trạng thái hoàn toàn mới.

## S
- **Sequential Multi-Domain Execution:** Thực thi đa miền tuần tự. Kiến trúc điều phối ép các tác tử AI làm việc theo các giai đoạn phân tầng có tính trật tự thời gian khắt khe nhằm giải quyết các dự án phức tạp.
- **Skills System:** Hệ thống Kỹ năng. Lớp hạ tầng chuyên biệt tổ chức và phân tán cơ sở tri thức cho tác tử AI thành các mô-đun biệt lập.
- **Socratic Gate Protocol:** Giao thức Cổng Socrates. Cơ chế kiểm duyệt ý định tiền thực thi buộc AI đặt câu hỏi ngược lại người dùng thay vì tự động sinh mã vô căn cứ nhằm triệt tiêu ảo giác kiến trúc.
- **Store:** "Kho thóc trung ương" trong kiến trúc State Management, là nơi duy nhất (Single Source of Truth) lưu trữ toàn bộ dữ liệu (State) của ứng dụng.
- **Subject:** Chủ thể. Các thực thể chủ động (như người dùng, tiến trình máy tính) đóng vai trò yêu cầu hoặc thực hiện các hoạt động lên các Đối tượng.

## T
- **Type Coercion:** Ép kiểu ngầm. Cơ chế tự động chuyển đổi từ kiểu dữ liệu này sang kiểu dữ liệu khác của JavaScript khi thực hiện tính toán giữa hai giá trị không đồng nhất.
