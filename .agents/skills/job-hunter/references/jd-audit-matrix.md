# Ma Trận 4 Tầng Bóc Tách JD & Đối Sánh Ứng Viên Chuẩn Senior

Tài liệu này cung cấp phương pháp luận **bóc tách cấu trúc Job Description (JD)** và hệ thống **chấm điểm đối sánh đa chiều có trọng số (Multi-dimensional Weighted Matching)**, giúp Agent giải trình chính xác lý do phù hợp/không phù hợp dựa trên bằng chứng kỹ thuật.

---

## 1. Ma Trận Bóc Tách JD 4 Tầng (4-Tier JD Deconstruction)

```
┌────────────────────────────────────────────────────────────────────────┐
│ TẦNG 1: BÀI TOÁN KỸ THUẬT & TRÁCH NHIỆM (RESPONSIBILITIES)             │
│   • R&D Sản phẩm mới (Greenfield) vs Bảo trì (Brownfield) vs Gia công │
│   • Trách nhiệm hàng ngày (Lập trình, gỡ lỗi, họp khách hàng, kiểm thử)│
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 2: YÊU CẦU BẮT BUỘC (HARD REQUIREMENTS - 30% TRỌNG SỐ)            │
│   • Số năm kinh nghiệm tối thiểu (Years of Exp)                        │
│   • Bằng cấp / Chuyên ngành (Degree/Major)                             │
│   • Ngôn ngữ cốt lõi (C, C++, Assembly, Python)                        │
│   • Dòng vi điều khiển (ARM Cortex, ESP32, STM32, PIC, AVR)           │
│   • Hệ điều hành nhúng (FreeRTOS, Embedded Linux, Zephyr, Bare-metal)  │
│   • Giao thức truyền thông (I2C, SPI, UART, CAN, BLE, MQTT)            │
│   • Ngoại ngữ & Địa điểm làm việc (English, TP.HCM On-site/Hybrid)     │
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 3: ĐIỂM CỘNG ƯU TIÊN (PREFERRED / NICE-TO-HAVE - 25% TRỌNG SỐ)   │
│   • Nền tảng Cloud/IoT (AWS IoT, Azure IoT, Firebase)                  │
│   • Kỹ năng đọc Schematic, Layout PCB, sử dụng máy hiện sóng (OSC)     │
│   • Kiến thức về kiến trúc phần mềm, Design Patterns cho Embedded      │
├────────────────────────────────────────────────────────────────────────┤
│ TẦNG 4: TÍN HIỆU VĂN HÓA KỸ THUẬT (ENGINEERING SIGNALS)                │
│   • Có quy trình Git (PR, Branching, Code Review) không?               │
│   • Có hệ thống CI/CD & Automated Testing cho Firmware không?         │
│   • Nhận diện Red Flags (JD tạp hóa, ôm đồm, yêu cầu phi thực tế)     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Hệ Thống Chấm Điểm Đối Sánh Đa Chiều (Weighted Scoring Framework)

Tuyệt đối không dùng tỷ lệ phần trăm trùng từ khóa đơn thuần. Đánh giá hồ sơ dựa trên 7 tiêu chí có trọng số:

| Tiêu chí đối sánh | Trọng số | Nội dung đánh giá | Điều kiện Blocker |
|---|---|---|---|
| **1. Yêu cầu bắt buộc (Hard Requirements)** | **30%** | Đáp ứng về bằng cấp, ngôn ngữ cốt lõi, vi điều khiển cơ bản, địa điểm làm việc | Nếu thiếu điều kiện tiên quyết → Xếp ngay vào **Reject** hoặc **Stretch** |
| **2. Kỹ năng kỹ thuật cốt lõi (Core Stack)** | **25%** | Mức độ thành thạo C/C++, RTOS, các giao thức phần cứng và mạng IoT | Thiếu 1 giao thức có thể học bù; thiếu C/C++ là rào cản lớn |
| **3. Bằng chứng dự án (Project Evidence)** | **15%** | Có sản phẩm thực tế, demo, mã nguồn GitHub kiểm chứng giải quyết bài toán tương tự | Rất quan trọng với Fresher/Junior để bù đắp số năm kinh nghiệm |
| **4. Thâm niên & Cấp bậc (Seniority Match)** | **15%** | Khoảng cách giữa yêu cầu JD và thực tế của ứng viên (Fresher vs 0-1 năm vs 3+ năm) | Fresher nộp job yêu cầu > 3 năm kinh nghiệm sẽ bị trừ tối đa mục này |
| **5. Lĩnh vực chuyên môn (Domain Fit)** | **5%** | Automotive vs Smart Home IoT vs Telecom vs Semiconductor | Có kinh nghiệm làm đúng domain là điểm cộng lớn |
| **6. Văn hóa & Công cụ (Tools & Culture)** | **5%** | Git workflow, Clean code, Debugging tools, Linux terminal | Thể hiện qua phong cách viết mã trên GitHub |
| **7. Địa điểm & Chế độ làm việc (Location Fit)** | **5%** | Khớp địa bàn (TP.HCM), chế độ On-site/Hybrid phù hợp khả năng di chuyển | Sai địa điểm mà không thể chuyển vùng → Hard Blocker |

---

## 3. Phân Loại Mức Độ Phù Hợp (4-Tier Decision Taxonomy)

Mọi báo cáo thẩm định phải đưa ra kết luận rõ ràng thuộc một trong 4 nhóm:

```text
┌─────────────────┬──────────────┬────────────────────────────────────────────────────────────────┐
│ Mức độ phù hợp  │ Điểm số      │ Ý nghĩa & Hành động khuyến nghị                                │
├─────────────────┼──────────────┼────────────────────────────────────────────────────────────────┤
│ STRONG MATCH    │ 85 – 100     │ Đủ điều kiện nộp ngay; không có Hard Blocker; bằng chứng mạnh. │
│ MATCH WITH GAPS │ 65 – 84      │ Khớp nền tảng cốt lõi; thiếu một số kỹ năng có thể học nhanh   │
│                 │              │ trong 30 ngày. Đề xuất nộp kèm CV đã tối ưu hóa.               │
│ STRETCH         │ 50 – 64      │ Thiếu thâm niên hoặc domain đặc thù; chỉ nên nộp nếu có        │
│                 │              │ dự án cá nhân xuất sắc bù đắp.                                 │
│ REJECT          │ Dưới 50      │ Vi phạm Hard Blocker (kinh nghiệm > 4 năm, sai địa điểm...).  │
│                 │ (hoặc Block) │ KHÔNG khuyến nghị nộp để tránh lãng phí thời gian.             │
└─────────────────┴──────────────┴────────────────────────────────────────────────────────────────┘
```

---

## 4. Chuẩn Mực Giải Trình Khớp Năng Lực (Explainability Standard)

Mỗi đánh giá JD phải trả lời đầy đủ 4 câu hỏi:

1. **WHY MATCH (Tại sao phù hợp?):** Liệt kê các bằng chứng thực tế từ hồ sơ (dự án, mã nguồn, công nghệ) tương thích trực tiếp với bài toán JD.
2. **WHY NOT MATCH (Tại sao chưa phù hợp?):** Liệt kê chính xác những yêu cầu trong JD mà ứng viên chưa từng làm hoặc chưa có sản phẩm chứng minh.
3. **WHAT IS MISSING (Đang thiếu những gì?):** Chỉ ra cụ thể các công cụ, chuẩn giao tiếp hoặc kiến thức domain còn khuyết.
4. **HOW IMPORTANT IS THE GAP (Mức độ nghiêm trọng của khoảng trống):**
   - *Rào cản tuyệt đối (Hard Blocker):* Ví dụ: Yêu cầu 5 năm làm AUTOSAR / Linux Kernel.
   - *Khoảng trống có thể đào tạo (Teachable Gap):* Ví dụ: Ứng viên đã vững C++ và ESP32 nhưng chưa từng dùng chuẩn giao tiếp CAN bus → Có thể tự học trong 2 tuần.
