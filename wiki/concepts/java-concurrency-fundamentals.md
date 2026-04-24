---
title: "Nền Tảng Concurrency và Đa Luồng trong Java"
source: "compiled"
date_added: 2026-04-24
tags: [concept, java, concurrency, multithreading]
aliases: [java-concurrency, multithreading, atomic-operations, race-condition]
status: draft
related:
  - "[[java-concurrent-collections]]"
  - "[[spring-async-execution]]"
  - "[[java-virtual-threads]]"
summary: "Cơ sở lý thuyết về lập trình đa luồng trong nền tảng Java, từ vấn đề Race Condition đến các cơ chế đồng bộ hóa cốt lõi như Locks, Volatile và Atomic."
---

# Nền Tảng Concurrency và Đa Luồng trong Java

Sự khác biệt cốt lõi giữa Tiến trình (Process) và Luồng (Thread) nằm ở sự chia sẻ không gian bộ nhớ. Các luồng hoạt động nhẹ nhàng hơn nhưng lại chia sẻ chung Java Heap Memory. Đặc tính dùng chung tài nguyên này chính là nguồn cội của các bài toán kiến trúc sâu sắc, trong đó điển hình nhất là vấn đề mất đồng bộ trạng thái (Race Condition).

## Hiện Tượng Race Condition

Race Condition phát sinh khi nhiều luồng cùng thao tác đọc/ghi song song lên một tài nguyên chung mà không có sự kiểm soát tuần tự. Các thao tác tưởng chừng nguyên khối như `count++` thực chất là một chuỗi hành vi bao gồm Đọc (Read), Biến đổi (Modify) và Ghi lại (Write). Khi các tiến trình này đan xen nhau mà thiếu vắng sự bảo vệ, sự sai lệch dữ liệu sẽ xảy ra ở cấp độ phần cứng. Các hệ thống phải giải quyết bài toán này thông qua "Tam giác Đồng bộ hóa".

## Tam Giác Đồng Bộ Hóa (The Synchronization Triangle)

Kiến trúc Java cung cấp ba tầng công cụ cơ bản để bảo vệ tài nguyên chia sẻ:

1. **Khóa Độc Lập (Mutual Exclusion):** 
   Sử dụng từ khóa `synchronized` hoặc các bộ khóa nâng cao như `ReentrantLock`. Phương pháp này chặn (block) toàn bộ luồng, cung cấp sự bảo vệ an toàn tuyệt đối nhưng lại gây suy giảm hiệu năng do phải thực hiện cơ chế luân chuyển ngữ cảnh (Context Switching).
2. **Khả Năng Hiển Thị (Visibility):** 
   Từ khóa `volatile` đảm bảo biến được đọc và ghi thẳng xuống Main Memory thay vì kẹt tại CPU Cache ($L1/L2$). Điều này đảm bảo tính hiển thị nhưng không cung cấp tính nguyên tử (Atomicity) cho các phép toán phức tạp.
3. **Thao Tác Nguyên Tử (Atomic Variables):** 
   Sử dụng bộ công cụ nguyên tử (như `AtomicInteger`, `AtomicReference`). Các thư viện này ứng dụng phương thức giao tiếp trực tiếp với chỉ thị phần cứng CPU thay vì dựa vào cơ chế phong tỏa của hệ điều hành.

## Thuật Toán CAS (Compare-And-Swap)

Bên dưới các thao tác nguyên tử là vòng lặp CAS (Compare-And-Swap), hay còn gọi là Spin-loop. Thay vì yêu cầu luồng phải ngủ đông chờ tài nguyên, hệ thống liên tục kiểm tra xem bộ nhớ có còn giữ nguyên giá trị kỳ vọng ban đầu hay không. Nếu trùng khớp, biến đổi được tiến hành; nếu thất bại do bị luồng khác ghi đè, vòng lặp tự động thử lại. Giải pháp này mang lại hiệu suất cực cao thông qua cơ chế Không dùng khóa (Lock-free).

Tuy nhiên, vòng lặp CAS chứa một lỗ hổng tự nhiên gọi là "Cạm bẫy ABA". Khi một luồng thứ ba thay đổi dữ liệu từ A thành B rồi đổi lại về A, vòng lặp CAS có thể ngộ nhận không có sự thay đổi nào xảy ra. Lỗ hổng này thường được khắc phục thông qua `AtomicStampedReference` bằng cách gắn thêm thẻ phiên bản nhằm giám sát lịch sử thay đổi.

## Tối Ưu Điểm Nghẽn Nguyên Tử

Dù mạnh mẽ, hệ thống Atomic cổ điển có thể vỡ vụn trước mức độ tranh chấp (contention) cực đoan do liên tục thất bại vòng lặp. Để ứng phó, hệ sinh thái Java tiếp tục giới thiệu hai cơ chế tối ưu bậc cao:
- **`LongAdder`:** Thay vì một điểm tranh chấp duy nhất, nó áp dụng chiến lược "Chia để trị", phân tán sức ép lên một mảng các ô nhớ phân mảnh, cải thiện tốc độ thống kê tổng quy mô lớn.
- **`VarHandle`:** Tinh giản tối đa vỏ bọc cấu trúc để thao tác nguyên tử trực tiếp lên các biến nguyên thủy, tiết kiệm không gian bộ nhớ.

## Nguồn Tham Khảo
- `raw/papers/atomic-concurrency-patterns-trong-javatối-ưu-hóa-hiệu-năng-đa-luồng-từ-jvm-đến-s.md`
- `raw/papers/multithreading-concurrency-trong-spring-boot-từ-cơ-bản-đến-virtual-threads.md`
- `raw/papers/đa-luồng-chân-kinh.md`
