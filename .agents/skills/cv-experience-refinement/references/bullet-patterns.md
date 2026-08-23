# Mẫu Cấu Trúc Câu Chuyên Nghiệp (Bullet Patterns for Tech CVs)

Tài liệu này cung cấp các mẫu câu hành động chuẩn Senior/Tech Lead được chia theo 4 nhóm chủ đề năng lực, tuân thủ nguyên tắc **Vòng lặp nghiệp vụ đóng kín** và tương thích 100% với các hệ thống ATS.

---

## 1. Bốn Nhóm Chủ Đề Năng Lực Cốt Lõi

```
┌────────────────────────────────────────────────────────────────────────┐
│ A. KIẾN TRÚC & THIẾT KẾ HỆ THỐNG (SYSTEM DESIGN & ARCHITECTURE)        │
├────────────────────────────────────────────────────────────────────────┤
│ B. CHIỀU SÂU KỸ THUẬT & THUẬT TOÁN (TECHNICAL DEPTH & ALGORITHMS)      │
├────────────────────────────────────────────────────────────────────────┤
│ C. ĐỘ TIN CẬY, TỐI ƯU & HIỆU NĂNG (RELIABILITY & PERFORMANCE)          │
├────────────────────────────────────────────────────────────────────────┤
│ D. TÍCH HỢP, QUY TRÌNH & BÀN GIAO (DELIVERY, INTEGRATION & OWNERSHIP)  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Các Mẫu Câu Chuẩn Theo Nhóm

### Nhóm A: Kiến Trúc & Thiết Kế Hệ Thống (System Design)
* **Mẫu 1 (Thiết kế luồng dữ liệu/giao tiếp):**  
  *Thiết kế kiến trúc giao tiếp phân tán sử dụng [Giao thức: MQTT/gRPC/WebSocket] kết nối [Vi điều khiển/Node] với [Backend/Broker], đảm bảo truyền nhận gói tin telemetry định kỳ hai chiều với độ trễ thấp.*
* **Mẫu 2 (Xử lý đồng thời & Đa luồng):**  
  *Xây dựng mô hình xử lý đa luồng (Multi-threading) độc lập cho [Số lượng] luồng tác vụ, áp dụng cơ chế [threading.Lock / Mutex / Semaphore] để đồng bộ hóa tài nguyên khung hình và ngăn chặn race condition.*
* **Mẫu 3 (Module hóa & Tách lớp):**  
  *Tái cấu trúc kiến trúc firmware theo mô hình phân lớp (Layered Architecture), tách biệt tầng Driver ngoại vi [SPI/I2C/UART] và tầng logic nghiệp vụ State Machine.*

### Nhóm B: Chiều Sâu Kỹ Thuật & Thuật Toán (Technical Depth)
* **Mẫu 1 (Pipeline xử lý dữ liệu/AI):**  
  *Triển khai pipeline thị giác máy tính tích hợp mô hình [YOLO / DeepSORT / OCR], kết hợp thuật toán [Multi-frame Voting / Kalman Filter] nhằm tăng độ ổn định nhận diện trong điều kiện môi trường phức tạp.*
* **Mẫu 2 (Lập trình vi điều khiển & Ngoại vi):**  
  *Lập trình firmware C/C++ trên vi điều khiển [ESP32 / STM32], cấu hình ngoại vi [Timer / PWM / ADC / DMA] và triển khai máy trạng thái hữu hạn (FSM) điều khiển đóng/mở thiết bị chấp hành.*
* **Mẫu 3 (Cơ sở dữ liệu & Backend):**  
  *Xây dựng hệ thống RESTful API / Database Functions trên nền [PostgreSQL / FastAPI / Node.js] để xử lý truy vấn thời gian thực và quản lý nhật ký sự kiện có cấu trúc.*

### Nhóm C: Độ Tin Cậy & Tối Ưu Hiệu Năng (Reliability & Performance)
* **Mẫu 1 (Tối ưu độ trễ / Băng thông):**  
  *Tối ưu hóa pipeline mã hóa dữ liệu [WebP / MJPEG] song song với luồng suy luận, giảm tải bộ nhớ đệm và cải thiện tốc độ phản hồi `[CẦN XÁC NHẬN: thời gian xử lý / FPS thực tế]`.*
* **Mẫu 2 (Cơ chế chống lỗi & Tự phục hồi):**  
  *Thiết lập cơ chế tự động kết nối lại (Exponential Backoff Reconnection) và hàng đợi đệm (Offline Message Buffer) cho client MQTT, đảm bảo không thất thoát dữ liệu khi mạng gặp sự cố.*
* **Mẫu 3 (Độ chính xác & Lọc nhiễu):**  
  *Cải thiện độ chính xác phân loại bằng cách áp dụng bộ lọc ngưỡng tin cậy và xử lý tiền khung hình (Frame Preprocessing), loại bỏ các nhận diện sai do rung lắc hoặc ánh sáng yếu.*

### Nhóm D: Tích Hợp, Quy Trình & Bàn Giao (Delivery & Ownership)
* **Mẫu 1 (Tích hợp End-to-End):**  
  *Triển khai trọn vẹn giải pháp từ tầng nút cứng cảm biến (Firmware), cổng kết nối trung tâm (Broker) đến ứng dụng người dùng cuối (Web Dashboard / Mobile App).*
* **Mẫu 2 (Kiểm thử & Đóng gói):**  
  *Viết bộ kịch bản kiểm thử tự động (Unit Tests / Integration Tests) và đóng gói môi trường triển khai, rút ngắn thời gian phát hiện lỗi tích hợp phần cứng - phần mềm.*

---

## 3. Tiêu Chuẩn Trình Bày Tương Thích ATS (ATS-Friendly Formatting)

1. **Không dùng biểu tượng trang trí phức tạp**: Tránh sử dụng emoji, icon, bảng biểu lồng nhau hoặc thanh tiến độ trong phần nội dung bullet CV chính.
2. **Dấu đầu dòng chuẩn**: Luôn sử dụng dấu gạch ngang (`-`) hoặc chấm tròn tiêu chuẩn.
3. **Động từ hành động mạnh (Strong Action Verbs)**: Mở đầu mỗi bullet bằng một động từ kỹ thuật dứt khoát (*Thiết kế, Triển khai, Xây dựng, Tối ưu hóa, Lập trình, Tích hợp, Đồng bộ hóa*).
