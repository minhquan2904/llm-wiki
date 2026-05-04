---
title: "NGINX - Động cơ bí ẩn và chiếc dao Thụy Sỹ"
source: "d:\\9. Learn\\12. llm wiki\\temp\\nginx.md"
date_added: 2026-04-24
tags: [article, devops, nginx, web-server, load-balancing, proxy]
aliases: [Nginx, engine x]
status: draft
summary: "Tổng quan kiến trúc, chức năng phổ biến (proxy, load balancer, caching) và mẫu cấu hình NGINX điển hình cho Web Frontend."
---

NGINX - Động cơ bí ẩn và chiếc dao Thụy Sỹ
Nội dung
Tổng quan Nginx
Chức năng phổ biến
Chức năng khác
Cấu hình hay dùng cho team Web Frontend
Tùy chỉnh tối ưu hiệu năng

1. Tổng quan NGINX
Tên gọi: engine X => nginx
Trang chủ: nginx.org | nginx.com
Đặc điểm kiến trúc:
Xử lý request sử dụng cơ chế asynchronous event-driven (bất đồng bộ, hướng sự kiện) thay vì dùng threads (luồng) truyền thống.
Một số tính năng phổ biến:
Reverse proxy
Load Balancer
Caching
Hỗ trợ FastCGI
WebSockets
Hỗ trợ TLS/SSL

Kiến trúc Process (Quy trình hoạt động):
MASTER PROCESS: Quản lý chung.
Child Processes:
Bộ nhớ chia sẻ (Shared memory) được dùng cho cache, session persistence, rate limits, session log.
CM (Cache Manager): Quản lý bộ nhớ đệm.
CL (Cache Loader): Tải bộ nhớ đệm.
W (Worker processes): Xử lý HTTP và các network traffic khác.

2. Chức năng phổ biến
Proxy
Forward Proxy: Trung gian giữa User (Client) và Internet. (Client -> Forward Proxy -> Internet)
Reverse Proxy: Trung gian giữa Internet và Backend Servers. (Internet -> Reverse Proxy -> Server)

As a Web Server / Beyond Web Serving
Hỗ trợ WebSocket, HTTP/2, gRPC, và streaming các định dạng media khác nhau (HDS, HLS, RTMP, ...).
Handle (xử lý) các static files, index files...
HTTP Caching để tăng hiệu năng cho các Web Server/Container khác.
Ghi chú: NGINX chiếm thị phần cực kỳ lớn và tăng trưởng liên tục so với các Web Server khác như Apache, Microsoft IIS,... (Theo thống kê của Netcraft).

Load Balancer
Thường phân nhóm theo Layer 4 (Transport) và Layer 7 (Application) của mô hình OSI.
Các kỹ thuật (Technique) phổ biến:
Round robin
Weighted round robin
Least connections
Least response time
Nginx hỗ trợ các thuật toán: Round robin, Hash, IP Hash, Least Connections, Least time (chỉ có trên bản Nginx Plus).

Tham khảo Mô hình OSI:
LayerNameExample protocols
7 Application Layer HTTP, FTP, DNS, SNMP, Telnet
6 Presentation Layer SSL, TLS
5 Session Layer NetBIOS, PPTP
4 Transport Layer TCP, UDP
3 Network Layer IP, ARP, ICMP, IPSec
2 Data Link Layer PPP, ATM, Ethernet
1 Physical Layer Ethernet, USB, Bluetooth, IEEE 802.11

3. Chức năng khác
Caching: Lưu trữ đệm nội dung tĩnh/động.
Rate limiting: Giới hạn tốc độ/số lượng request.
Mail proxy: Hỗ trợ giao thức SMTP/POP3/IMAP.
Basic authentication: Xác thực người dùng cơ bản.
API Gateway: Đóng vai trò làm cổng giao tiếp API (hỗ trợ cả JWT).
Media Streaming: Truyền phát tệp tin đa phương tiện.

4. Cấu hình hay dùng cho team Web Frontend
Dưới đây là một mẫu cấu hình điển hình cho các dự án Web Frontend (đã được chuẩn hóa cú pháp):

```nginx
# 1. Khai báo upstream cho load balancing
upstream api_gateways {
    server 10.22.10.98:8080;
}

# 2. Server block xử lý request
server {
    listen 443 ssl; # Hoặc listen 9092 theo ví dụ
    server_name eibomni.kylantest.vn;

    root /home/dvnh/EIB_OMNI/ib-web;
    index index.html;

    # 3. Khai báo các response header toàn cục cho server block (VD: CSP)
    set $CSP_image   "img-src 'self' 'unsafe-inline' blob: data: *.kylan.vn;";
    set $CSP_script  "script-src 'self' 'unsafe-inline';";
    set $CSP_style   "style-src 'self' 'unsafe-inline' fonts.googleapis.com;";
    set $CSP_font    "font-src 'self' data: fonts.gstatic.com;";
    set $CSP_connect "connect-src 'self' 'unsafe-inline' blob: data: *.kylantest.vn;";

    set $CSP "default-src 'self'; ${CSP_connect} ${CSP_image} ${CSP_script} ${CSP_style} ${CSP_font}";

    add_header Content-Security-Policy $CSP;
    add_header X-Content-Security-Policy $CSP;

    # 4. Cấu hình Serve Static Frontend (SPA - Single Page Application)
    location / {
        try_files $uri $uri/ /index.html;
    }

    # 5. Cấu hình Reverse Proxy cho API (Pass hoặc filter header từ client lên server)
    location /ib/ {
        proxy_pass http://api_gateways/ib/;
        proxy_redirect off;

        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-NginX-Proxy true;

        client_max_body_size 10m;
        client_body_buffer_size 128k;

        # Khai báo các response header theo từng location (CORS)
        add_header 'Access-Control-Allow-Origin' '*';
        add_header 'Access-Control-Allow-Credentials' 'true';
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
        add_header 'Access-Control-Allow-Headers' 'Authorization, DNT, X-Mx-Reqtoken, Keep-Alive, User-Agent, X-Requested-With, If-Modified-Since, Cache-Control, Content-Type';
    }
}
```

Content Caching (Lưu bộ nhớ đệm)
Cơ chế: Client -> (1a) Caching Nginx (Key) -> (1b) Upstream -> (1c) Trả về Caching -> (1d/2a) Trả về Client.
Lưu ý khi cấu hình:
Sử dụng proxy_cache_path để enable chế độ caching trong Nginx.
Có thể sử dụng thư mục /dev/shm nếu muốn cache trực tiếp trên RAM (tốc độ cao hơn đĩa cứng).
Lưu ý: Cần whitelist IP cho phép purge (xóa) cache.
Kết hợp Strong Caching Header và Weak Caching Header cho từng loại file khác nhau.
Sử dụng tham số version trên URL (VD: ?v=1.5.0) để invalidate (làm mới) cache từ phía frontend.

Cấu hình mẫu:
```nginx
http { 
    # Cấu hình đường dẫn lưu cache
    proxy_cache_path /data/nginx/cache levels=1:2 keys_zone=mycache:10m purger=on;

    # Cấu hình IP được phép xóa cache
    geo $purge_allowed {
        default         0;
        10.0.0.1        1;
        192.168.0.0/24  1;
    }

    map $request_method $purge_method {
        PURGE   $purge_allowed;
        default 0;
    }

    server {
        listen 80;
        server_name www.example.com;

        location / {
            proxy_pass http://localhost:8002;
            proxy_cache mycache;
            proxy_cache_purge $purge_method;
        }
    }
}
```

Ví dụ về các file tĩnh thường được cache:
| Tên File | HTTP Status | Loại |
|---|---|---|
| custom1.css?v=1.5.0 | 200 | stylesheet |
| Roboto-Regular.ttf | 200 | font |
| Roboto-Bold.ttf | 200 | font |
| Roboto-Medium.ttf | 200 | font |
| jquery.bundles.js?v=1.5.0 | 200 | script |
| momentis.bundles.js?v=1.5.0 | 200 | script |
| styles.[hash].css?v=1.5.0 | 200 | stylesheet |
| main-es2015.[hash].js?v=1.5.0 | 200 | script |

5. Alternatives? (Các giải pháp thay thế)
Nếu không sử dụng NGINX, bạn có thể cân nhắc các công cụ khác có chức năng tương đương:
HAProxy: Rất mạnh mẽ trong việc Load Balancing (đặc biệt ở Layer 4).
Traefik Proxy: Sinh ra cho kỷ nguyên Cloud-native / Docker / Kubernetes, cấu hình dynamic cực tốt.
Envoy: Thường dùng làm Sidecar Proxy trong kiến trúc Microservices (Service Mesh).

Tham khảo thêm
Nginx Admin Guide - Content Caching
Nginx Caching Guide
Cấu hình HTTP Caching cho Nginx (Viblo)
Hướng dẫn cấu hình cache cho Nginx (Cloudcraft)
Increasing Application Performance with HTTP Cache Headers (Heroku)
Tuning NGINX for Performance
Nginx Boilerplate / Gist tham khảo

HỎI / ĐÁP
(Phần dành cho câu hỏi từ người tham dự)
CHỦ ĐỀ TIẾP THEO?
(Kết thúc)
