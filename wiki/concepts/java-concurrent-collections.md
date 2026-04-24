---
title: "Xử Lý Tập Hợp Đồng Thời (Concurrent Collections)"
source: "compiled"
date_added: 2026-04-24
tags: [concept, java, collections, concurrency]
aliases: [java-concurrent-collections, concurrenthashmap, bucket-locking]
status: draft
related:
  - "[[java-concurrency-fundamentals]]"
  - "[[java-immutability]]"
summary: "Phân tích các chiến lược lưu trữ tập hợp an toàn luồng trong Java, trọng tâm là kiến trúc Bucket Locking của ConcurrentHashMap và nguyên tắc Defensive Copying."
---

# Xử Lý Tập Hợp Đồng Thời (Concurrent Collections)

Lưu trữ và trích xuất dữ liệu tập hợp trên môi trường đa luồng mang tính rủi ro cao vì các tập hợp cổ điển của Java được thiết kế cho quá trình xử lý tuần tự. Khi xử lý song song, các kỹ sư phần mềm phải thực hiện những sự thoả hiệp về cấu trúc nhằm duy trì sự ổn định.

## Sự Tiến Hóa của Map Đa Luồng

Trong môi trường Java, kiến trúc quản lý dữ liệu từ điển (Map) đã trải qua ba thời kỳ chuyển đổi để giải quyết bài toán đa luồng:

1. **`HashMap` (Không đồng bộ):** Mang lại tốc độ vận hành tuyệt đối nhưng hoàn toàn thiếu khả năng bảo vệ (Not Thread-Safe). Khai thác song song sẽ phá vỡ liên kết bộ nhớ, gây thất thoát dữ liệu.
2. **`Hashtable` (Khóa toàn bộ):** Xây dựng rào chắn tuyệt đối thông qua Global Lock. Khi một thao tác Đọc/Ghi được kích hoạt, hệ thống ngăn chặn tất cả các luồng khác tham gia xử lý, làm giảm nghiêm trọng tính sẵn sàng.
3. **`ConcurrentHashMap` (Thần Binh Hiện Đại):** Tối ưu hóa điểm nghẽn dựa vào thiết kế Phân mảnh Cục bộ (Bucket Locking) và các toán tử Compare-And-Swap (CAS).

Thay vì đóng toàn bộ biểu đồ, `ConcurrentHashMap` chỉ thực thi cơ chế phong tỏa nhỏ lẻ cho từng vùng phân đoạn (bucket) bị biến đổi. Khả năng đọc được giải phóng hoàn toàn và tiến trình ghi chỉ chặn một phần bộ nhớ, mang lại thông lượng ấn tượng (High Concurrency).

Tuy nhiên, cấu trúc này áp đặt một nguyên tắc cấm kỵ nghiêm ngặt: **Không bao giờ cho phép chứa Khóa (Key) rỗng hoặc Giá trị (Value) rỗng (Null)**. Việc tồn tại phần tử null trong ngữ cảnh đa luồng có thể sinh ra sự mơ hồ về trạng thái dữ liệu (Null do đối tượng không tồn tại, hay Null là giá trị thực sự?), từ đó sinh ra ngoại lệ đoạt mạng.

## Nghệ Thuật Lấp Đầy Map

Thay vì áp dụng mẫu tư duy cổ điển "Kiểm tra sau đó Hành động" (Check-then-act) dễ tạo ra rủi ro thay đổi ngầm, giao diện đa luồng đề xuất sử dụng hàm nội bộ nguyên tử:
- **`putIfAbsent`:** Tính toán trước dữ liệu và chỉ nạp vào Map nếu Khóa chưa hiện diện. Có nhược điểm về hiệu suất hệ thống khi khởi tạo trước các đối tượng cồng kềnh.
- **`computeIfAbsent`:** Khai thác tối đa chức năng của Hàm Lambda. Hàm khởi tạo chỉ kích hoạt thực thi khi Khóa hoàn toàn thiếu vắng. Giải pháp này giúp bảo tồn nguyên vẹn nội công của CPU và bộ nhớ cho đối tượng phức tạp.

## Kỹ Thuật Defensive Copying

Bên cạnh các cơ chế khóa nguyên khối của Concurrent Collections, những kỹ sư hệ thống thường xây dựng một bức tường phòng ngự bổ sung gọi là Defensive Copying (Sao chép Phòng thủ). Nguyên lý này quy định: Không bao giờ tin tưởng truyền thẳng hệ thống tập hợp (List, Map) ra thế giới bên ngoài nhằm ngăn chặn sự điều chỉnh lén lút từ các tiến trình khách (Client threads).

Theo đó, phương thức trích xuất dữ liệu không trả về con trỏ vùng nhớ thực tế. Thay vào đó, một bản sao không thể biến đổi (Unmodifiable View) thông qua lời gọi `List.copyOf()` sẽ được gửi đi, chặn đứng bất kỳ sự tiếp cận sửa đổi ngoài ý muốn nào.

## Nguồn Tham Khảo
- `raw/papers/đa-luồng-chân-kinh.md`
- `raw/papers/mutable-vs-immutabletác-động-kiến-trúc-trong-java-spring-từ-cơ-chế-jvm-đến-thiết.md`
