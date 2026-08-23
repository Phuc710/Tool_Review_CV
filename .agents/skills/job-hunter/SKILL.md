---
name: job-hunter
description: Kỹ năng tìm kiếm việc làm, nghiên cứu thị trường tech, xây dựng chuỗi toán tử Boolean search đa nền tảng (LinkedIn, Google, ATS Lever/Greenhouse/Ashby/Workday, ITviec, TopCV), thu thập và khử trùng lặp (Deduplication), bóc tách JD 4 tầng và đối sánh ứng viên dựa trên bằng chứng (Evidence-based Matching) chuẩn Senior.
---

# job-hunter (Săn Việc & Nghiên Cứu Thị Trường Chuẩn Senior)

Skill này chuyển đổi toàn diện phương thức tìm việc từ **thụ động (Keyword Matching & Spray-and-Pray)** sang **nghiên cứu thị trường sâu, truy xuất ngữ nghĩa (Semantic Retrieval), kiểm định tính xác thực (Freshness Verification) và đối sánh năng lực dựa trên bằng chứng (Evidence-based Match & Gap Analysis)**.

**QUY TẮC BẮT BUỘC: TOÀN BỘ KẾT QUẢ ĐÁNH GIÁ, BÁO CÁO VÀ HƯỚNG DẪN XUẤT BẰNG TIẾNG VIỆT (OUTPUT ALWAYS = VN).**

---

## 1. Đọc Tài Liệu Tham Khảo & Công Cụ (References & Test Suite)

Trước khi thực hiện bất kỳ tác vụ tìm kiếm hoặc thẩm định nào, bắt buộc phải tham khảo:
1. [references/market-mapping.md](references/market-mapping.md): Bản đồ phân khúc doanh nghiệp Tech & Embedded tại VN (Tier 1 Global/Automotive/Chip, Tier 2 Product Houses/IoT, Tier 3 Outsourcing/Services) kèm chuỗi kiểm định năng lực tuyển dụng thực tế và phân tách Company Fit vs Job Fit.
2. [references/canonical-identity.md](references/canonical-identity.md): Kiến trúc tạo mã định danh duy nhất (Canonical Job UID) và quy tắc khử trùng lặp đa nền tảng (Deduplication).
3. [references/evidence-layer.md](references/evidence-layer.md): Tầng bằng chứng 5 cấp (Claim → Evidence → Source → Timestamp → Confidence) và cơ chế phát hiện Bằng chứng tiêu cực (Negative Evidence).
4. [references/boolean-search-playbook.md](references/boolean-search-playbook.md): Sổ tay toán tử Boolean Search bao phủ toàn diện các hệ thống ATS (Lever, Greenhouse, Ashby, Workday, SmartRecruiters), LinkedIn và sàn việc làm Tech.
5. [references/jd-audit-matrix.md](references/jd-audit-matrix.md): Ma trận 4 tầng bóc tách JD (Hard Reqs vs Preferred, Responsibilities vs Requirements, Tín hiệu văn hóa kỹ thuật, Hệ số phạt Hard Blockers).
6. [references/direct-outreach-templates.md](references/direct-outreach-templates.md): Khung thông điệp tiếp cận trực tiếp (Direct Outreach) dựa trên bằng chứng thực tế, không spam.
7. [scripts/evaluate_matching.py](scripts/evaluate_matching.py): Bộ công cụ kiểm thử benchmark đánh giá thuật toán phân loại và phát hiện Hard Blocker trên tập dữ liệu [scripts/dataset_jds.json](scripts/dataset_jds.json).

---

## 2. Quy Trình 6 Bước Chuẩn Senior (Job Research & Matching Pipeline)

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. PROFILE EXTRACTION & HARD CONSTRAINTS                               │
│    (Khai thác hồ sơ, sự thật khả dụng, giới hạn vị trí & thâm niên)    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ 2. TARGETED DISCOVERY & MULTI-ATS QUERYING                             │
│    (Sinh truy vấn Boolean đa kênh: ATS, LinkedIn, Google, Tech Boards) │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ 3. NORMALIZATION, DEDUPLICATION & FRESHNESS VERIFICATION               │
│    (Chuẩn hóa tiêu đề, khử trùng lặp theo ID/Hãng, kiểm tra trạng thái)│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ 4. 4-TIER JD DECONSTRUCTION                                            │
│    (Bóc tách: Hard Requirements, Preferred, Responsibilities, Signals) │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ 5. MULTI-DIMENSIONAL WEIGHTED MATCHING & GAP ANALYSIS                  │
│    (Chấm điểm 7 chiều, phân loại: Strong / Gaps / Stretch / Reject)    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ 6. EVIDENCE-BASED RECOMMENDATION & TAILORED OUTREACH                   │
│    (Giải trình Why Match / Gap / Action, tạo Elevator Pitch chuẩn xác) │
└────────────────────────────────────────────────────────────────────────┘
```

### Bước 1: Khai Thác Hồ Sơ Ứng Viên & Giới Hạn Cứng (Profile Extraction)
- Đọc dữ liệu từ `cache/cv_profile.json` (hoặc CV người dùng cung cấp).
- Trích xuất:
  - **Sự thật khả dụng (Available Facts):** Ngôn ngữ thành thạo, vi điều khiển đã lập trình, giao thức đã chạy thực tế, dự án có mã nguồn kiểm chứng.
  - **Cấp độ ứng viên (Candidate Tier):** `Khởi đầu (Entry-level) / Tăng trưởng (Growth) / Bứt phá (Sprint)`.
  - **Giới hạn cứng (Hard Constraints):** Địa điểm làm việc (On-site TP.HCM, Hybrid, Remote), mức độ sẵn sàng chuyển vùng (Relocation).

### Bước 2: Khám Phá Mục Tiêu & Truy Vấn Đa Kênh (Targeted Discovery)
- Áp dụng các toán tử trong `boolean-search-playbook.md` để quét:
  - Hệ thống ATS trực tiếp của doanh nghiệp (Lever, Greenhouse, Ashby, Workday).
  - Bài đăng tuyển dụng của Engineering Managers / Tech Leads trên LinkedIn.
  - Các sàn việc làm kỹ thuật: ITviec, TopCV, VietnamWorks, GitHub Jobs.

### Bước 3: Chuẩn Hóa, Khử Trùng Lặp & Kiểm Tra Tính Xác Thực (Normalization & Deduplication)
- **Chuẩn hóa (Normalization):** Đưa chức danh về dạng chuẩn (ví dụ: `Embedded Firmware Engineer`, `Junior C++ Developer`).
- **Khử trùng lặp (Deduplication):** Hai đường dẫn khác nhau (ví dụ 1 link trên TopCV, 1 link trên ITviec) nhưng cùng một công ty, cùng tiêu đề và địa điểm phải được hợp nhất thành **1 Job Identity duy nhất**:
  `Job_ID = hash(Company_Name + Normalized_Title + Location)`
- **Kiểm tra trạng thái (Freshness Verification):**
  - Gán nhãn `STATUS = VERIFIED_OPEN` nếu tin còn hạn đăng tuyển.
  - Gán nhãn `STATUS = UNVERIFIED` nếu là dữ liệu nghiên cứu lịch sử tuyển dụng.

### Bước 4: Bóc Tách JD 4 Tầng (JD Deconstruction)
Khi phân tích một JD cụ thể, phân rã thông tin theo ma trận `jd-audit-matrix.md`:
1. **Yêu cầu bắt buộc (Hard Requirements):** Năm kinh nghiệm, bằng cấp, ngôn ngữ bắt buộc, MCU/OS bắt buộc, địa điểm, chế độ làm việc.
2. **Điểm cộng ưu tiên (Preferred / Nice-to-Have):** Kỹ năng mở rộng, công cụ đo kiểm, kiến thức domain đặc thù.
3. **Trách nhiệm thực tế (Responsibilities):** Tách bạch giữa việc "Phải làm gì hàng ngày" và "Cần có năng lực gì".
4. **Tín hiệu văn hóa kỹ thuật (Engineering Signals):** Code review, Git flow, CI/CD, tài liệu kỹ thuật, quy mô team.
5. **Cập nhật Cache:** Tự động đồng bộ các yêu cầu này vào `cache/job_profile.json`.

### Bước 5: Đối Sánh Đa Chiều & Phân Tích Khoảng Trống (Weighted Matching & Gap Analysis)
Tuyệt đối không dùng tỷ lệ trùng từ khóa đơn thuần. Đánh giá độ khớp theo 7 chiều có trọng số:
- **Yêu cầu bắt buộc (Hard Requirements):** Trọng số 30% *(Nếu vi phạm điều kiện cứng → lập tức xếp vào nhóm Reject hoặc Stretch)*.
- **Kỹ năng kỹ thuật cốt lõi (Core Tech Skills):** Trọng số 25%.
- **Bằng chứng dự án thực tế (Project Evidence & Codebase):** Trọng số 15%.
- **Thâm niên & Cấp bậc (Seniority & Experience Match):** Trọng số 15%.
- **Lĩnh vực chuyên môn (Domain Fit):** Trọng số 5%.
- **Văn hóa kỹ thuật & Công cụ phát triển (Tools & Workflow Fit):** Trọng số 5%.
- **Địa điểm & Chế độ làm việc (Location Fit):** Trọng số 5%.

**Phân loại mức độ phù hợp (Fit Category):**
- `STRONG MATCH` (Đạt ≥ 85% điểm trọng số, không có Hard Blocker): Đủ điều kiện ứng tuyển ngay.
- `MATCH WITH GAPS` (Đạt 65% – 84%, thiếu một số kỹ năng có thể tự học bù đắp trong 30 ngày): Đề xuất ứng tuyển kèm chiến lược tinh chỉnh CV.
- `STRETCH` (Đạt 50% – 64%, thiếu thâm niên hoặc domain đặc thù nhưng có năng lực chuyển đổi tốt): Ứng tuyển dạng thử thách, cần thư ngỏ mạnh.
- `REJECT / DO NOT APPLY` (< 50% hoặc vi phạm Hard Blocker nghiêm trọng): Không khuyến nghị nộp để tránh lãng phí thời gian.

### Bước 6: Khuyến Nghị Dựa Trên Bằng Chứng & Kịch Bản Tiếp Cận (Evidence-Based Recommendation)
- Giải trình rõ: **Tại sao khớp (Why Match)**, **Tại sao không khớp (Why Not Match)**, **Khoảng trống kỹ thuật là gì (What is Missing)**, **Mức độ nghiêm trọng của khoảng trống (Gap Impact)**.
- Tạo kịch bản kết nối ngắn gọn (Elevator Pitch) gửi Tech Lead/Recruiter theo mẫu trong `direct-outreach-templates.md`.

---

## 3. Mẫu Báo Cáo Xuất Chuẩn Của job-hunter

Khi thực hiện nghiên cứu việc làm hoặc thẩm định JD, bắt buộc xuất theo mẫu sau:

```markdown
# Báo Cáo Nghiên Cứu Việc Làm & Thẩm Định Cơ Hội Chuẩn Senior

## 1. Định Vị Ứng Viên & Tiêu Chí Sàng Lọc
- **Ứng viên:** [Họ tên / Chức danh mục tiêu / Cấp độ]
- **Core Stack đã kiểm chứng:** [C/C++, ESP32, I2C/SPI/UART, MQTT, FreeRTOS...]
- **Giới hạn cứng (Hard Constraints):** [Địa điểm: TP.HCM | Hình thức: On-site/Hybrid]

## 2. Bản Đồ Cơ Hội & Truy Vấn Tìm Kiếm Trực Tiếp
| Nền tảng / ATS | Phân khúc doanh nghiệp | Link tìm kiếm đã lọc sẵn | Trạng thái xác thực |
|---|---|---|---|
| ... | ... | ... | VERIFIED / LIVE |

## 3. Bóc Tách & Thẩm Định JD Chi Tiết (Khi có JD cụ thể)
- **Công ty & Vị trí:** [Tên công ty — Chức danh]
- **Mức độ phù hợp tổng thể:** [STRONG MATCH / MATCH WITH GAPS / STRETCH / REJECT] — **Điểm trọng số: [XX / 100]**
- **Bóc tách 4 tầng:**
  - **Bài toán kỹ thuật cốt lõi:** [R&D mới / Bảo trì tối ưu / Gia công theo yêu cầu]
  - **Hard Requirements:** [Đáp ứng: X/Y yêu cầu]
  - **Preferred & Domain:** [Đáp ứng: A/B điểm cộng]
  - **Tín hiệu văn hóa kỹ thuật:** [Git flow, Code review, CI/CD...]
- **Cảnh báo Red Flags:** [Không có / Chi tiết rủi ro nhận diện được]

## 4. Giải Trình Khớp Năng Lực Dựa Trên Bằng Chứng (Evidence Breakdown)
- **Điểm khớp mạnh nhất (Why Match):**
  - *Bằng chứng 1:* ...
  - *Bằng chứng 2:* ...
- **Khoảng trống & Rào cản (Gaps & Blockers):**
  - *Khoảng trống:* ... | *Mức độ nghiêm trọng:* [Cao / Trung bình / Thấp] | *Giải pháp khắc phục:* ...

## 5. Kịch Bản Kết Nối Trực Tiếp Cá Nhân Hóa (Direct Outreach Pitch)
> [Đoạn văn ngắn < 150 từ gửi Tech Lead / Hiring Manager dựa trên JD và dự án thực tế]

## 6. Kế Hoạch Hành Động & Chuyển Tiếp Hồ Sơ
- [ ] Bước 1: Cập nhật `cache/job_profile.json`.
- [ ] Bước 2: Sử dụng `cv-reviewer` để kiểm tra độ khớp CV với các từ khóa bóc tách.
- [ ] Bước 3: Gửi tin nhắn kết nối trực tiếp đến Tech Lead trên LinkedIn.
```
