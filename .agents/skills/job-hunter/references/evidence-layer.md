# Tầng Bằng Chứng & Xác Thực Năng Lực (Structured Evidence Layer)

Tài liệu này quy định chuẩn mực trích xuất và giải trình bằng chứng cho Agent `job-hunter`, đảm bảo mọi nhận định đều có nguồn gốc kiểm chứng, loại bỏ hoàn toàn các suy đoán vô căn cứ (Anti-hallucination).

---

## 1. Cấu Trúc Bằng Chứng Chuẩn 5 Tầng (Evidence Data Schema)

Mỗi kết luận của Agent về một doanh nghiệp hoặc một vị trí tuyển dụng bắt buộc phải tuân theo cấu trúc:

```
[CLAIM]       (Nhận định của Agent)
   ↓
[EVIDENCE]    (Bằng chứng thực tế: Requisition cụ thể, Trách nhiệm trong JD, Dự án trong CV)
   ↓
[SOURCE]      (Nguồn kiểm chứng: Official Careers Page, Lever ATS, GitHub Repo, LinkedIn)
   ↓
[TIMESTAMP]   (Thời điểm xác thực: YYYY-MM-DD)
   ↓
[CONFIDENCE]  (Mức độ tin cậy: HIGH / MEDIUM / LOW)
```

---

## 2. Ví Dụ Bằng Chứng Đạt Chuẩn (Verified Real Examples)

### Ví dụ 1: Xác thực nhu cầu tuyển dụng của doanh nghiệp
```text
Company: Synopsys Vietnam
Claim: Có hoạt động tuyển dụng Kỹ thuật thực tế tại TP.HCM.
Evidence: Trang tuyển dụng chính thức niêm yết vị trí ASIC/SoC Design Verification Senior / Staff Engineer tại TP.HCM.
Source: Official Workday Careers (Job ID: 18283, URL: https://synopsys.wd1.myworkdayjobs.com)
Timestamp: 2026-08-22
Confidence: HIGH
Distinction Note: Vị trí này thuộc mảng Semiconductor/IC Design Verification (SystemVerilog/UVM), không phải vị trí Lập trình Nhúng vi điều khiển (MCU Firmware) cho ứng viên Fresher.
```

### Ví dụ 2: Đối sánh năng lực ứng viên với JD
```text
Company: Ecotek Vietnam (Vị trí: IoT Firmware Engineer)
Claim: STRONG MATCH cho ứng viên Nguyễn Thành Phúc.
Evidence: 
- JD yêu cầu: Lập trình C/C++, vi điều khiển ESP32, giao thức MQTT/Wi-Fi, FreeRTOS.
- CV ứng viên có: Dự án Smart Parking với mã nguồn GitHub (github.com/Phuc710/Xparking) triển khai ESP32 + C++ + MQTT + Web API; đạt loại Giỏi ngành Kỹ thuật Nhúng.
Source: GitHub public repository & Candidate verified CV.
Timestamp: 2026-08-22
Confidence: HIGH
Hard Blockers: NONE
```

---

## 3. Quy Tắc Bằng Chứng Tiêu Cực (Negative Evidence & Why NOT Apply)

Agent phải luôn tìm kiếm **Bằng chứng tiêu cực** để bảo vệ ứng viên khỏi việc nộp nhầm các vị trí không phù hợp:

1. **Rào cản thâm niên (Experience Blocker):** Nếu JD yêu cầu ≥ 3.5 năm kinh nghiệm thực chiến → Ghi nhận `NEGATIVE EVIDENCE: Thâm niên không tương thích`, tự động hạ cấp xuống `REJECT` bất kể điểm trùng từ khóa cao.
2. **Rào cản địa bàn (Location Blocker):** Nếu công ty yêu cầu On-site 100% tại Hà Nội/Hải Phòng mà không hỗ trợ chuyển vùng → Ghi nhận `NEGATIVE EVIDENCE: Địa điểm làm việc không khả thi`.
3. **Rào cản Domain (Domain Blocker):** Nếu chức danh là "Software Engineer" nhưng nội dung là Web Frontend React hoặc Chip Verification UVM → Ghi nhận `NEGATIVE EVIDENCE: Lệch mảng kỹ thuật cốt lõi`.
