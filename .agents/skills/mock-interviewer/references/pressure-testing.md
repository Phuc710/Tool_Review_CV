# Mô Phỏng Sự Cố Production & Thử Thách Áp Lực (Pressure Testing & Incident Simulation)

Tài liệu này hướng dẫn cách thiết kế các kịch bản mô phỏng sự cố vận hành thực tế (Production Incidents), thử thách giới hạn thời gian và kỹ thuật phát hiện ứng viên nói quá năng lực (Bluff Detection).

---

## 1. Quy Trình Mô Phỏng Sự Cố Production 4 Bước (Incident Simulation)

Khi kiểm tra khả năng xử lý sự cố thực tế, Interviewer **không bao giờ cung cấp toàn bộ đáp án ngay từ đầu**, mà dẫn dắt theo từng nấc dữ liệu:

```
┌────────────────────────────────────────────────────────────────────────┐
│ Bước 1: CẢNH BÁO BAN ĐẦU (The Alert)                                   │
│ "Hệ thống giám sát gửi alert: 50 mạch ESP32 bị timeout, không đẩy được │
│  dữ liệu về broker MQTT. Bạn nhận được thông báo này lúc 10h tối."     │
├────────────────────────────────────────────────────────────────────────┤
│ Bước 2: 10 PHÚT ĐẦU TIÊN (Triage & Containment)                        │
│ Chờ ứng viên trả lời cách khoanh vùng và ưu tiên hành động.            │
├────────────────────────────────────────────────────────────────────────┤
│ Bước 3: CUNG CẤP DỮ KIỆN MỚI (New Evidence / Clues)                    │
│ "Bạn kiểm tra: Server backend CPU chỉ 15%, nhưng broker log báo lỗi    │
│  'Connection Refused: too many open files'. Bước tiếp theo bạn làm gì?"│
├────────────────────────────────────────────────────────────────────────┤
│ Bước 4: TÌM NGUYÊN NHÂN GỐC RỄ & PHÒNG NGỪA (Root Cause & Prevention) │
│ Kiểm tra giải pháp dài hạn: Tăng ulimit, cấu hình connection pool,     │
│ thiết lập Exponential Backoff Jitter trên firmware ESP32.              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Kỹ Thuật Phát Hiện Nói Quá Năng Lực (Bluff Detection)

Interviewer chủ động nhận diện các dấu hiệu "chém gió" và tung ra câu hỏi thử thách ngay lập tức:

### 1. Dấu hiệu: Rải Từ Khóa Thời Thượng (Keyword Dumping)
* **Ứng viên nói:** *"Em áp dụng Microservices, Kafka, Redis và Kubernetes để hệ thống chịu tải cao."*
* **Interviewer xoáy:** *"Trong đồ án này của bạn chỉ có 4 cổng bãi xe và 1 vi điều khiển ESP32. Cụ thể bạn dùng Redis để cache dữ liệu gì? Key expire time là bao nhiêu? Tại sao không dùng bộ nhớ RAM trong tiến trình Python?"*

### 2. Dấu hiệu: Giải Thích Vòng Vo (Circular Explanation)
* **Ứng viên nói:** *"Em dùng cơ chế Lock để tránh lỗi vì nếu không Lock thì dữ liệu sẽ bị sai."*
* **Interviewer xoáy:** *"Cụ thể là loại Lock nào trong Python? `threading.Lock` hay `threading.RLock`? Tại sao đoạn code đọc khung hình từ camera lại cần Lock mà luồng hiển thị không cần?"*

### 3. Dấu hiệu: Nhận Vơ Trách Nhiệm (Unsupported Ownership)
* **Ứng viên nói:** *"Em thiết kế toàn bộ kiến trúc hệ thống và luồng dữ liệu."*
* **Interviewer xoáy:** *"Nếu bạn là người thiết kế kiến trúc, hãy giải thích quyết định đánh đổi lớn nhất khi chọn giao thức MQTT thay vì HTTP REST trong dự án này? Nếu có 1 module bị sập thì cơ chế cách ly lỗi (Failure Isolation) hoạt động ra sao?"*

---

## 3. Kịch Bản Thử Thách Áp Lực 60 Giây (Pressure Challenge)

Được áp dụng trong chế độ `pressure-test` để kiểm tra bản lĩnh và tư duy chịu áp lực:

> **Interviewer:**  
> *"Bạn khẳng định rằng kiến trúc đa luồng với 4 cổng bãi xe trong dự án Xparking_Auto của bạn vận hành không bao giờ bị nghẽn (Non-blocking). Tôi phản biện rằng khi mô hình YOLOv5 nhận diện biển số mất 150ms trên GPU/CPU, luồng ghi nhận xe vào chắc chắn sẽ bị lag và hụt khung hình (Frame Drop).*  
>  
> *Bạn có đúng **60 giây** để giải thích cơ chế Producer-Consumer hoặc Hàng đợi (Queue) mà bạn đã cài đặt để chứng minh hệ thống không bị block."*
