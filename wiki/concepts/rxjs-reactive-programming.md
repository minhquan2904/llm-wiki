---
title: "RxJS & Reactive Programming"
source: "compiled"
date_added: 2026-04-23
tags: [concept, javascript, rxjs, reactive, async]
aliases: [Observable, Observer, Subject, RxJS Operators, map, tap]
status: draft
related:
  - "[[javascript-asynchronous-programming]]"
  - "[[ngrx-state-management]]"
summary: "Phân tích mô hình Reactive Programming qua RxJS: từ khái niệm luồng dữ liệu (Data Stream), Observable, đến cách kiểm soát dữ liệu thông qua các toán tử đường ống (pipe) như map và tap."
---

# RxJS & Reactive Programming

[[javascript-asynchronous-programming|Promise và Async/Await]] là giải pháp tuyệt vời cho các tác vụ bất đồng bộ mang tính chất "một lần" (ví dụ: gửi một request, nhận một phản hồi). Tuy nhiên, Promise lộ rõ giới hạn khi ứng dụng cần xử lý một luồng dữ liệu (Data Stream) theo thời gian thực như: tọa độ chuột, thanh tìm kiếm người dùng đang gõ, hay bảng giá cổ phiếu cập nhật liên tục. Đáng chú ý, Promise không thể bị hủy ngang (cancel) một khi đã kích hoạt.

Để giải quyết bài toán luồng dữ liệu đa giá trị và có thể kiểm soát, mô hình **Reactive Programming (Lập trình phản ứng)** ra đời, với đại diện xuất sắc nhất trong hệ sinh thái JavaScript là thư viện **RxJS** (Reactive Extensions for JavaScript).

## 1. Ba Trụ Cột Cơ Bản Của RxJS

RxJS coi mọi thứ—từ các mảng tĩnh, sự kiện click chuột, đến các kết nối HTTP—đều là các luồng dữ liệu phát sóng theo thời gian.

### Observable (Kênh Phát Sóng)
Observable là đối tượng đóng vai trò phát ra (emit) các giá trị. Đặc tính cốt lõi của Observable là sự **Lười biếng (Lazy Evaluation)**: mã bên trong Observable sẽ tuyệt đối không thực thi cho đến khi có một đối tượng đăng ký lắng nghe nó. Trái ngược hoàn toàn với Promise vốn mang bản chất Eager (thực thi ngay lập tức lúc khởi tạo).

### Observer (Người Theo Dõi)
Observer là cấu trúc định nghĩa cách phản ứng với dữ liệu từ Observable. Nó chứa ba hàm callback xử lý ba tín hiệu chính:
- `next(value)`: Bắt tín hiệu khi có dữ liệu mới.
- `error(err)`: Bắt tín hiệu khi luồng bị lỗi và buộc dừng.
- `complete()`: Nhận thông báo khi luồng đã hoàn tất vòng đời và đóng lại.

### Subscription (Hợp Đồng Đăng Ký)
Subscription là sợi cáp kết nối giữa Observable và Observer thông qua hàm `.subscribe()`. Sự khác biệt vĩ đại nhất của RxJS so với Promise nằm ở đây: thông qua đối tượng Subscription, bạn có thể gọi hàm `.unsubscribe()` để **hủy bỏ hoàn toàn quá trình thực thi bất đồng bộ** vào bất kỳ lúc nào, giải phóng bộ nhớ và ngăn ngừa các hành vi không mong muốn khi giao diện đã bị hủy (unmounted).

## 2. Subject: Cầu Truyền Hình Đa Hướng (Multicasting)

Một `Observable` thông thường mang tính chất **Unicast**—mỗi khi có một đối tượng `.subscribe()`, nó sẽ tạo ra một luồng thực thi độc lập hoàn toàn mới từ đầu. 

Khi bạn muốn chia sẻ cùng một luồng dữ liệu cho nhiều Observer cùng lúc (ví dụ: trạng thái đăng nhập, dữ liệu chat realtime), bạn phải sử dụng **Subject**. Subject đóng vai trò vừa là một Observable, vừa là một Observer mang tính chất **Multicast**. Bất cứ khi nào bạn gọi `subject.next(data)`, tất cả các thành phần đang đăng ký (`subscribe`) vào Subject đó sẽ nhận được cập nhật ngay lập tức và đồng thời.

## 3. Quản Lý Luồng Bằng Operators (Toán Tử Đường Ống)

Khả năng thao túng mạnh mẽ nhất của RxJS không nằm ở việc phát dữ liệu, mà nằm ở chặng đường vận chuyển thông qua hàm khớp nối `.pipe()`. Các toán tử (Operators) hoạt động như những màng lọc, thay đổi hình thái hoặc kiểm soát dòng chảy dữ liệu trước khi nó đến tay `subscribe`.

Hai toán tử kinh điển và được ứng dụng nhiều nhất là `map` và `tap`:

### Toán Tử `map` (Kẻ Biến Hình)
Tương tự như `Array.prototype.map()`, toán tử `map` nhận dữ liệu đầu vào từ luồng, áp dụng một hàm biến đổi, và đẩy dữ liệu với cấu trúc/giá trị mới (đã được sửa đổi) xuống trạm tiếp theo của đường ống.
- **Ứng dụng thực tế:** Trích xuất lớp vỏ thừa của response HTTP, định dạng lại kiểu dữ liệu, tính toán quy đổi trước khi đưa vào giao diện. 

### Toán Tử `tap` (Tác Dụng Phụ - Side Effects)
Toán tử `tap` có một quy tắc tối thượng: **Nó tuyệt đối không làm thay đổi hay chạm vào cấu hình của dữ liệu đi qua.** Giá trị đi vào `tap` thế nào thì đi ra đường ống kế tiếp y nguyên như thế.
- **Ứng dụng thực tế:** Vì không can thiệp vào luồng chính, `tap` sinh ra để giải quyết các tác dụng phụ (side-effects). Lập trình viên sử dụng `tap` để ghi log debug (`console.log`), cất giấu dữ liệu vào `localStorage`, hay bật/tắt các trạng thái hiển thị loading spinner (`isLoading = true`) trước và sau khi luồng xử lý hoàn tất, giữ cho hàm `subscribe` cuối cùng luôn sạch sẽ và chỉ tập trung vào việc render dữ liệu.
