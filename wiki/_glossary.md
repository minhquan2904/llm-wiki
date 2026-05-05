# Glossary

Danh sách các thuật ngữ và khái niệm cốt lõi được sử dụng trong hệ thống tri thức, đặc biệt trong lĩnh vực Kiểm soát Truy cập (Access Control), Lập trình JavaScript và Kiến trúc Java/Spring.

## A
- **ABAC (Attribute-Based Access Control):** Kiểm soát truy cập dựa trên thuộc tính. Mô hình định tuyến quyền hạn dựa trên đánh giá linh hoạt các đặc tính của người dùng, đối tượng, thao tác và môi trường xung quanh.
- **ACL (Access Control List):** Danh sách kiểm soát truy cập. Biểu diễn lưu trữ theo định hướng Đối tượng, nơi mỗi tài nguyên sẽ lưu lại một danh sách chứa tên Chủ thể kèm theo quyền tương ứng.
- **ApplicationContext:** Container cốt lõi của Spring Framework đảm nhiệm việc khởi tạo, quản lý vòng đời và kết nối các Spring Beans dựa trên cơ chế IoC.
- **Architectural Hallucination:** Ảo giác kiến trúc. Rủi ro khi AI tự ý đưa ra quyết định sai lệch về yêu cầu nghiệp vụ hoặc mẫu thiết kế do tiếp nhận các câu lệnh mơ hồ.
- **Assignment (NGAC):** Cạnh liên kết trên đồ thị quyền NGAC nối từ người dùng (U) tới nhóm người dùng (UA), đại diện cho việc gán thành viên vào nhóm/vai trò.
- **Association (NGAC):** Cạnh liên kết trên đồ thị quyền NGAC nối từ nhóm người dùng (UA) tới nhóm tài nguyên (OA), quy định danh sách các thao tác (operations) được phép.
- **Async/Await:** Cú pháp khai báo giúp viết mã bất đồng bộ trông giống như đồng bộ, giải quyết triệt để tình trạng Callback Hell trong JavaScript.
- **Authentication:** Xác thực. Quá trình kiểm chứng danh tính của một thực thể để trả lời câu hỏi "Bạn là ai?".
- **Authorization:** Ủy quyền. Quá trình kiểm tra và quyết định quyền hạn để trả lời câu hỏi "Bạn được phép làm gì?".

## B
- **Bucket Locking:** Cơ chế khóa cục bộ phân mảnh, cho phép khóa từng phần nhỏ của bộ nhớ thay vì toàn bộ cấu trúc, tối ưu hiệu suất trong xử lý đa luồng (ví dụ: ConcurrentHashMap).

## C
- **Call Stack:** Ngăn xếp gọi hàm. Cấu trúc dữ liệu LIFO ghi nhận các hàm đang được thực thi trong JavaScript.
- **Capability List:** Danh sách khả năng. Biểu diễn lưu trữ theo định hướng Chủ thể, nơi hệ thống cấp cho mỗi người dùng một danh sách gồm các Đối tượng và quyền hạn tương ứng trên Đối tượng đó.
- **CAS (Compare-And-Swap):** Thuật toán lõi trong các thư viện nguyên tử (Atomic), hoạt động theo cơ chế khóa lạc quan (lock-free) bằng cách liên tục kiểm tra và đối chiếu bộ nhớ.
- **Cgroups (Control Groups):** Cơ chế lõi của nhân Linux giúp giới hạn và giám sát lượng tài nguyên vật lý (CPU, RAM, I/O) mà một tiến trình hoặc container được phép tiêu thụ.
- **Closure:** Bao đóng. Hiện tượng một hàm ghi nhớ và có thể truy cập các biến nằm ở phạm vi bên ngoài của nó ngay cả khi hàm bên ngoài đã thực thi xong.
- **Content OA / Members UA:** Cặp thực thể trên đồ thị quyền NGAC đại diện cho một kênh giao tiếp (Channel) trong hệ thống nhắn tin, giúp kiểm soát quyền đọc/ghi mà không cần ACL.
- **Cognitive Routing:** Định tuyến nhận thức đa chiều. Cơ chế tự động nhận diện ý định ẩn từ mô tả tự nhiên để ánh xạ công việc tới chuyên gia AI phù hợp.
- **Composition:** Lắp ráp. Kỹ thuật thiết kế phần mềm kết hợp các đối tượng hoặc kiểu dữ liệu để tạo ra cấu trúc dữ liệu phức tạp hơn, ưu tiên sử dụng thay thế cho Kế thừa.
- **ConcurrentHashMap:** Cấu trúc dữ liệu từ điển hỗ trợ đa luồng tốc độ cao dựa trên cơ chế Bucket Locking và thuật toán CAS, không cho phép chứa khóa (key) hoặc giá trị (value) null.
- **Container:** Môi trường đóng gói ứng dụng cô lập, bao gồm mã nguồn và mọi phụ thuộc, chia sẻ chung nhân hệ điều hành với máy chủ để đạt được tính linh hoạt và tối ưu tài nguyên hơn máy ảo. **Xem thêm:** [[docker]]

## D
- **DAC (Discretionary Access Control):** Kiểm soát truy cập tùy ý. Mô hình kiểm soát linh hoạt cho phép người tạo/chủ sở hữu tài nguyên tự ý quản lý và chia sẻ lại quyền truy cập cho người khác.
- **Dependency Injection (DI):** Tiêm phụ thuộc. Mô hình thực hành IoC trong đó các thành phần phụ thuộc của một đối tượng được tiêm vào từ bên ngoài (ưu tiên qua Constructor) thay vì đối tượng tự khởi tạo.
- **Digital Divide:** Khoảng cách kỹ thuật số. Sự phân hóa về lợi thế và hiệu suất giữa người dùng thành thạo công nghệ (như AI) và người không sử dụng. **Xem thêm:** [[ai-users-vs-non-users]]
- **Docker:** Nền tảng điều phối ảo hóa cấp hệ điều hành (OS-level virtualization) chuyên biệt sử dụng Namespaces và Cgroups để triển khai ứng dụng bằng container. **Xem thêm:** [[docker]]
- **Dynamic Approval Workflow:** Luồng phê duyệt động. Kiến trúc lợi dụng cơ chế tìm kiếm phạm vi (Scope Finding) của đồ thị NGAC để tìm kiếm người duyệt theo thời gian thực thay vì phân công cứng. **Xem thêm:** [[ngac-approval-workflow]]

## E
- **EPP (Event Processing Point):** Điểm xử lý sự kiện. Thành phần trong mô hình NGAC, chịu trách nhiệm nhận diện và phản ứng với các thay đổi trạng thái trong môi trường theo thời gian thực để cập nhật chính sách.
- **Event Loop:** Vòng lặp sự kiện. Cơ chế điều phối cốt lõi của JavaScript giúp ngôn ngữ luồng đơn này xử lý các tác vụ bất đồng bộ mà không bị chặn (non-blocking).

## F
- **Forward Proxy:** Proxy thuận. Cổng trung gian đứng giữa người dùng (client) và Internet, hoạt động thay mặt người dùng để truy xuất tài nguyên từ bên ngoài.

## G
- **Generic Repository Pattern:** Mẫu thiết kế trừu tượng hóa các thao tác cơ sở dữ liệu chung (CRUD) vào một lớp duy nhất sử dụng tham số kiểu (Generics) để giảm thiểu mã lặp lại.
- **Generics:** Hệ gen nhân tạo. Khái niệm sử dụng tham số kiểu (Type Parameter) để xây dựng cấu trúc dữ liệu và hàm linh hoạt, đảm bảo an toàn tĩnh (Compile-time) nhưng bị Xóa kiểu (Type Erasure) lúc chạy.
- **Grouped-Query Attention (GQA):** Biến thể của cơ chế tự chú ý (self-attention) giúp tăng tốc độ suy luận và tiết kiệm bộ nhớ, đặc biệt quan trọng cho các mô hình ngôn ngữ nhỏ gọn chạy trên thiết bị cá nhân. **Xem thêm:** [[llama-3.2-3b-instruct]]

## H
- **Hoisting:** Cơ chế kéo phần khai báo biến (var) hoặc hàm lên đầu phạm vi (scope) trong giai đoạn biên dịch trước khi thực thi.
- **Hybrid NGAC:** NGAC lai. Mô hình kiến trúc phân tách vai trò: NGAC hoạt động như một "Guard" (bảo vệ các tác vụ trong in-memory graph), còn hệ thống RDBMS đóng vai trò "Store" nhằm tối ưu các truy vấn liệt kê (list) và phân trang (pagination). **Xem thêm:** [[ngac-practical-implementation]]

## I
- **Immutability:** Tính bất biến. Trạng thái không thể bị thay đổi sau khi đã được khởi tạo, đóng vai trò quan trọng trong việc bảo vệ an toàn bộ nhớ khi lập trình đa luồng (Race Condition).
- **Inheritance:** Kế thừa. Cơ chế cốt lõi của OOP cho phép một lớp (class) dựa trên một lớp khác, kế thừa trạng thái và hành vi của nó, biểu diễn mối quan hệ "is-a".
- **Inversion of Control (IoC):** Đảo ngược điều khiển. Triết lý kiến trúc mà trong đó luồng điều khiển và việc quản lý vòng đời đối tượng được giao lại cho một Container trung tâm (như Spring).

## J
- **Jackson (Databind):** Thư viện xử lý JSON tiêu chuẩn trong hệ sinh thái Java, nổi bật với hiệu năng cao và tính tích hợp sâu sắc với Spring Boot.
- **Jagged Technological Frontier:** Biên giới công nghệ lởm chởm. Khái niệm mô tả năng lực không đồng đều của AI khi xử lý các tác vụ có độ phức tạp tương đương. **Xem thêm:** [[jagged-technological-frontier]]
- **Jotai:** Thư viện quản lý trạng thái (state management) cho React theo mô hình nguyên tử (Atomic).

## K
- **Kafka:** Nền tảng xử lý luồng sự kiện phân tán, lưu trữ dữ liệu theo thời gian thực với thông lượng cực cao.
- **Knowledge Distillation:** Chưng cất tri thức. Quá trình chuyển giao kiến thức từ một mô hình lớn (teacher) sang một mô hình nhỏ gọn hơn (student) để duy trì chất lượng đầu ra trong khi giảm đáng kể dung lượng. **Xem thêm:** [[llama-3.2-3b-instruct]]

## L
- **Leaky Abstraction:** Trừu tượng bị rò rỉ. Hiện tượng xảy ra khi một lớp trừu tượng không thể che giấu hoàn toàn sự phức tạp của hệ thống bên dưới, buộc người sử dụng phải can thiệp trực tiếp vào chi tiết thực thi.
- **Load Balancing:** Cân bằng tải. Kỹ thuật phân phối lưu lượng mạng đến nhiều máy chủ khác nhau nhằm tối ưu hóa việc sử dụng tài nguyên và ngăn ngừa tình trạng quá tải.

## M
- **MAC (Mandatory Access Control):** Kiểm soát truy cập bắt buộc. Mô hình nghiêm ngặt nơi mọi quyền truy cập đều bị chi phối bởi các quy tắc trung tâm, bất kể ý chí của người dùng sở hữu.
- **Macrotask / Microtask:** Hàng đợi tác vụ vĩ mô (setTimeout) và vi mô (Promise.then). Microtask luôn được ưu tiên thực thi trước Macrotask trong Event Loop.
- **Mark-and-Sweep:** Thuật toán Đánh dấu và Quét. Cơ chế thu gom rác (Garbage Collection) mặc định của V8 Engine nhằm tìm và xóa các đối tượng không còn rễ (Roots) truy cập.
- **Materialized Views:** Vật chất hóa bộ đệm. Kỹ thuật lưu trữ trước kết quả của một truy vấn tính toán phức tạp (như bao đóng bắc cầu) vào cơ sở dữ liệu để tối ưu hóa tốc độ đọc (truy vấn quyền), đánh đổi bằng chi phí bảo trì và độ trễ khi cập nhật. **Xem thêm:** [[ngac-transitive-closure]]
- **Message Broker:** Trạm trung chuyển tin nhắn. Thành phần kiến trúc đứng giữa các ứng dụng để tiếp nhận, giữ an toàn và định tuyến thông điệp dựa trên các quy tắc xác định.
- **MLS (Multilevel Security):** Bảo mật Đa mức. Một phương pháp triển khai MAC phổ biến, gán các cấp độ bảo mật theo thứ bậc, thường áp dụng quy tắc "không đọc lên" và "không ghi xuống".

## N
- **n8n:** Nền tảng tự động hóa quy trình làm việc (workflow automation) kết hợp giữa cấu hình no-code và lập trình chuyên sâu, được thiết kế mạnh mẽ dành cho doanh nghiệp. **Xem thêm:** [[n8n]]
- **Namespaces:** Không gian tên. Cơ chế của Linux Kernel tạo ra lớp cô lập tài nguyên hệ thống (PID, Network, Mount), mang lại ảo giác rằng mỗi tiến trình đang chạy độc lập trên một máy chủ riêng biệt.
- **NGAC (Next-Generation Access Control):** Kiểm soát truy cập thế hệ tiếp theo. Mô hình truy cập dựa trên biểu đồ, cho phép biểu diễn các chính sách phức tạp và đồng nhất.
- **NGINX:** Máy chủ web và hệ thống proxy ngược mã nguồn mở nổi tiếng với kiến trúc xử lý bất đồng bộ và hướng sự kiện.
- **NgRx:** Thư viện quản trị trạng thái (State Management) dành cho Angular, dựa trên mô hình Redux Pattern và RxJS.

## O
- **Object:** Đối tượng. Các tài nguyên thụ động trong hệ thống như tập tin, cơ sở dữ liệu, là mục tiêu của các yêu cầu thao tác.
- **Object Attribute (OA):** Nhóm tài nguyên. Thực thể trên đồ thị NGAC đại diện cho một tập hợp các đối tượng (ví dụ: Thư mục, Dữ liệu phòng ban) có chung chính sách bảo mật.
- **ObjectMapper:** Trái tim của thư viện Jackson, chịu trách nhiệm chính trong việc chuyển đổi (Serialize/Deserialize) qua lại giữa JSON và đối tượng Java.
- **Obligation (Nghĩa vụ):** Cơ chế định tuyến động (dynamic routing) trong NGAC. Tự động kích hoạt các thao tác (như tạo/xóa Assignment) khi khớp với một mẫu sự kiện nhất định.
- **Observable:** Khái niệm cốt lõi của RxJS đại diện cho một luồng dữ liệu (Data Stream) phát sóng theo thời gian.

## P
- **PAP (Policy Administration Point):** Điểm quản trị chính sách. Nơi các quản trị viên tạo lập, chỉnh sửa và quản lý vòng đời của các quy tắc kiểm soát quyền hạn.
- **Policy Class (PC):** Đỉnh phân giải chính sách cao nhất trong đồ thị phân quyền NGAC. Trong thực tế thường đóng vai trò là ranh giới cô lập (Tenant) giữa các Không gian làm việc (Workspace).
- **PDP (Policy Decision Point):** Điểm quyết định chính sách. "Khối óc" của hệ thống phân quyền, nơi thực hiện đánh giá các yêu cầu truy cập dựa trên chính sách.
- **PECS (Producer Extends, Consumer Super):** Quy tắc cốt lõi khi sử dụng Wildcards trong Java Generics: dùng extends khi lấy dữ liệu ra và dùng super khi nạp dữ liệu vào.
- **PEP (Policy Enforcement Point):** Điểm thực thi chính sách. "Trạm kiểm soát" chặn các luồng yêu cầu từ người dùng, gửi đến PDP chờ quyết định và sau đó cấp/từ chối quyền.
- **PIP (Policy Information Point):** Điểm thông tin chính sách. Nơi thu thập và cung cấp các thuộc tính từ nhiều nguồn dữ liệu để PDP có thông tin ra quyết định.
- **Progressive Disclosure:** Tải động lũy tiến. Cơ chế phân mảnh và chỉ tải tri thức vào bộ nhớ mô hình ngôn ngữ khi thực sự cần thiết để chống ngộp ngữ cảnh.
- **Promise:** Đối tượng đại diện cho sự hoàn thành hoặc thất bại của một tiến trình bất đồng bộ trong tương lai.
- **Prop Drilling:** Hiện tượng truyền dữ liệu qua nhiều Component trung gian từ cha xuống cháu, gây khó khăn cho bảo trì.
- **Prototypal Inheritance:** Kế thừa nguyên mẫu. Cơ chế chia sẻ thuộc tính giữa các object trong JavaScript thông qua một chuỗi liên kết ngầm.
- **Productivity Tax:** Thuế năng suất. Hệ lụy (The Expert Paradox) khi chuyên gia phải mất nhiều công sức để sửa đổi kết quả của AI cho khớp với tiêu chuẩn cá nhân thay vì tự làm từ đầu.
- **Pub/Sub (Publish/Subscribe):** Mô hình giao tiếp bất đồng bộ, phân phối sự kiện thông qua các chủ đề (topics) mà không cần chỉ định đích đến.

## Q
- **Queue Mode:** Chế độ mở rộng quy mô (scaling) của n8n, phân tách thành Main Instance (đón yêu cầu), Message Broker (giữ hàng đợi qua Redis) và Workers (xử lý dữ liệu) để tăng tính ổn định của nền tảng. **Xem thêm:** [[n8n]]

## R
- **RabbitMQ:** Message broker mã nguồn mở linh hoạt, hỗ trợ định tuyến thông điệp phong phú qua Exchanges và Queues.
- **Race Condition:** Hiện tượng mất đồng bộ trạng thái khi nhiều luồng cùng đọc/ghi lên một tài nguyên chia sẻ mà thiếu cơ chế kiểm soát an toàn (Locks/Atomic).
- **RAP (Resource Access Point):** Điểm truy cập tài nguyên. Giao diện trực tiếp bảo vệ và quản lý tài nguyên, phối hợp với PEP để thực thi quyết định.
- **RBAC (Role-Based Access Control):** Kiểm soát truy cập dựa trên vai trò. Mô hình truyền thống định nghĩa quyền truy cập dựa trên chức danh công việc của người dùng.
- **React:** Thư viện JavaScript mã nguồn mở dùng để xây dựng giao diện người dùng dựa trên Component và Virtual DOM.
- **React Router DOM:** Thư viện quản lý định tuyến (routing) tiêu chuẩn cho các ứng dụng trang đơn (SPA) trong React.
- **Reactive Programming:** Lập trình phản ứng. Mô hình lập trình xoay quanh việc thiết lập các luồng dữ liệu bất đồng bộ (Data Streams).
- **Reducer:** Hàm thuần túy (Pure Function) trong mô hình Redux chịu trách nhiệm nhận trạng thái hiện tại và Action để trả về một trạng thái hoàn toàn mới.
- **Reconciliation Pattern:** Mẫu thiết kế đối soát. Chống phân mảnh dữ liệu bằng cách đồng bộ lại (re-sync) cấu trúc đồ thị quyền (NGAC Graph) với dữ liệu nghiệp vụ (Denormalized Store) mỗi khi xảy ra sự kiện thay đổi tổ chức như chuyển phòng ban hoặc thay đổi vai trò. **Xem thêm:** [[ngac-practical-implementation]]
- **Reverse Proxy:** Proxy ngược. Cổng trung gian đứng trước các máy chủ backend (như web server), làm nhiệm vụ nhận yêu cầu từ Internet và phân phối đến các máy chủ nội bộ một cách an toàn.

## S
- **Sequential Multi-Domain Execution:** Thực thi đa miền tuần tự. Kiến trúc điều phối ép AI làm việc theo các giai đoạn phân tầng có trật tự thời gian khắt khe.
- **Server State:** Trạng thái máy chủ. Dữ liệu lưu trữ ở máy chủ, có tính bất đồng bộ, không thuộc sở hữu độc quyền của frontend và có thể bị lỗi thời. **Xem thêm:** [[tanstack-query]]
- **Skills System:** Hệ thống Kỹ năng. Lớp hạ tầng phân tán cơ sở tri thức cho tác tử AI thành các mô-đun biệt lập.
- **Socratic Gate Protocol:** Giao thức Cổng Socrates. Cơ chế kiểm duyệt ý định tiền thực thi buộc AI đặt câu hỏi ngược lại người dùng để chống ảo giác.
- **SOLID Principles:** Các nguyên tắc SOLID. Bộ 5 nguyên tắc thiết kế hướng đối tượng (SRP, OCP, LSP, ISP, DIP) nhằm giúp phần mềm linh hoạt, dễ bảo trì và dễ mở rộng.
- **Single Page Application (SPA):** Ứng dụng trang đơn. Trang web tải một lần duy nhất và điều hướng cục bộ bằng JavaScript.
- **Share_OA:** Object Attribute Chia sẻ. Một Node (đỉnh) quy ước trong đồ thị quyền NGAC dùng làm vùng chứa đại diện cho một liên kết chia sẻ hoặc một nhóm đối tượng có chung chính sách, thay vì phải tạo Node quyền trên từng tệp tin riêng lẻ. **Xem thêm:** [[ngac-permission-graph]]
- **Skill-Leveling Effect:** Hiệu ứng san bằng kỹ năng. Hiện tượng công cụ AI tạo sinh mang lại mức tăng hiệu suất đột biến cho người có kỹ năng thấp, qua đó thu hẹp khoảng cách với các chuyên gia. **Xem thêm:** [[skill-leveling-effect]]
- **Stale-While-Revalidate:** Trả cũ tải mới. Chiến lược caching cho phép hiển thị dữ liệu cũ (stale) ngay lập tức trong lúc âm thầm tải lại dữ liệu mới (fresh) ở nền để tối ưu trải nghiệm. **Xem thêm:** [[tanstack-query]]
- **Stateless Bean:** Đối tượng phi trạng thái trong thiết kế Spring Framework, nơi dữ liệu khả biến cấp toàn cục bị cấm nhằm bảo đảm an toàn trên môi trường đa luồng (Singleton).
- **Store:** "Kho thóc trung ương" trong kiến trúc State Management, là nơi duy nhất lưu trữ toàn bộ dữ liệu (State) của ứng dụng.
- **Strict Mode:** Chế độ thiết quân luật trong TypeScript nhằm kích hoạt chuỗi kiểm tra khắt khe, triệt tiêu lỗi tiềm ẩn tại Compile-time.
- **Structured Concurrency:** Đồng thời có cấu trúc. Nguyên lý tổ chức vòng đời luồng xử lý theo các khối phân nhánh rõ ràng, tự động dọn dẹp tài nguyên con khi tác vụ cha sụp đổ.
- **Subject:** Chủ thể. Các thực thể chủ động đóng vai trò yêu cầu hoặc thực hiện các hoạt động lên Đối tượng.

## T
- **TanStack Query:** (hay React Query). Thư viện quản lý trạng thái máy chủ chuyên nghiệp, giải quyết các vấn đề liên quan đến fetching, caching và đồng bộ dữ liệu. **Xem thêm:** [[tanstack-query]]
- **Textbook-quality synthetic data:** Dữ liệu tổng hợp chất lượng cao. Tập dữ liệu huấn luyện do AI tạo ra mô phỏng cấu trúc sách giáo khoa dày đặc logic (reasoning-dense), giúp đào tạo các mô hình ngôn ngữ nhỏ gọn đạt hiệu năng vượt trội so với kích thước thực tế. **Xem thêm:** [[phi-3.5-mini-instruct]]
- **ThreadPoolTaskExecutor:** Lớp bảo bọc (Wrapper) của Spring giúp cấu hình và giới hạn tài nguyên bể luồng nhằm thực thi các thao tác bất đồng bộ an toàn.
- **Time-of-Action Re-check:** Kiểm tra tại thời điểm hành động. Thuật toán bảo mật yêu cầu hệ thống luôn gọi NGAC kiểm tra lại quyền ngay khoảnh khắc user thực thi (như duyệt lệnh) để chống lỗ hổng do thay đổi phòng ban/vai trò.
- **Transitive Closure:** Bao đóng bắc cầu. Trong đồ thị NGAC, đây là khái niệm toán học để xác định xem có đường đi hợp lệ nào nối từ chủ thể đến đối tượng hay không. Đây là thuật toán cốt lõi ($O(V^3)$) để quyết định quyền truy cập. **Xem thêm:** [[ngac-transitive-closure]]
- **Type Coercion:** Ép kiểu ngầm. Cơ chế tự động chuyển đổi định dạng dữ liệu của JavaScript khi tính toán giữa các giá trị không đồng nhất.
- **Type Erasure:** Xóa kiểu. Việc trình biên dịch xóa bỏ định nghĩa tham số Generics (thành Object) trên Bytecode để tương thích ngược, làm mất thông tin tại Runtime.
- **Type Narrowing:** Thu hẹp kiểu. Sử dụng cấu trúc logic (typeof, in) để xác định chính xác một kiểu dữ liệu cụ thể từ một tập hợp đa hình.

## U
- **Union Types:** Kiểu hợp. Cơ chế cho phép biến/tham số nhận một trong nhiều định dạng kiểu, hỗ trợ tính đa hình tĩnh.
- **User Attribute (UA):** Nhóm người dùng. Thực thể trên đồ thị NGAC đại diện cho một tập hợp người dùng chia sẻ chung quyền hạn (ví dụ: Owners, Members, Department Chief).

## V
- **Virtual DOM:** Bản sao nháp ảo của cấu trúc HTML DOM, giúp gộp các thay đổi (Batching) để giảm thiểu tần suất tính toán đồ họa (Reflow/Repaint).
- **Virtual Threads:** Luồng ảo (Project Loom). Mẫu kiến trúc đa luồng hạng nhẹ của Java 21+ tự động ánh xạ M:N với Carrier OS Thread, cho phép chạy hàng triệu luồng đồng thời cực rẻ.
