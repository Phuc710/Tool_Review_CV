# Thang Đo & Tiêu Chí Đánh Giá Phỏng Vấn (Scoring Rubric & Assessment)

Tài liệu này quy định thang điểm 3 trục, các cấp độ tin cậy của bằng chứng và tiêu chuẩn ra quyết định tuyển dụng sau phiên phỏng vấn.

---

## 1. Ba Trục Đánh Giá Cốt Lõi (3-Axis Scoring Matrix)

Mỗi ứng viên được đánh giá độc lập trên thang điểm từ **0 đến 10** theo 3 tiêu chí:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. CHIỀU SÂU KỸ THUẬT (TECHNICAL DEPTH) — [0 - 10]                      │
│    - Tính chính xác của kiến thức nền tảng (C/C++, Concurrency, OS)    │
│    - Độ am hiểu về Trade-offs, Edge cases và Quản lý tài nguyên       │
│    - Khả năng giải thích cặn kẽ bản chất luồng dữ liệu & phần cứng     │
├────────────────────────────────────────────────────────────────────────┤
│ 2. KHẢ NĂNG GIAO TIẾP & TRÌNH BÀY (COMMUNICATION) — [0 - 10]           │
│    - Cấu trúc câu trả lời mạch lạc (Bottom-line first, STAR, Top-down) │
│    - Trả lời trúng trọng tâm câu hỏi, không lan man, không né tránh    │
│    - Giải thích các vấn đề phức tạp một cách trong sáng, dễ hiểu       │
├────────────────────────────────────────────────────────────────────────┤
│ 3. TƯ DUY GIẢI QUYẾT VẤN ĐỀ (PROBLEM SOLVING) — [0 - 10]               │
│    - Khả năng bóc tách vấn đề phức tạp thành các bài toán nhỏ hơn      │
│    - Phương pháp khoanh vùng lỗi và tìm nguyên nhân gốc rễ (Root Cause)│
│    - Tính thực tế trong việc lựa chọn công cụ và giải pháp kỹ thuật    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Phân Tách 3 Cấp Độ Tin Cậy Của Bằng Chứng

Khi đưa ra bất kỳ nhận xét nào, Interviewer bắt buộc phân loại rõ:

* **🟢 ĐÃ QUAN SÁT THẤY (Observed)**: Ứng viên đã chứng minh trực tiếp qua câu trả lời chính xác, rõ ràng và có logic kỹ thuật vững chắc.
* **🟡 SUY LUẬN (Inferred)**: Nhận định có cơ sở từ các chi tiết ứng viên chia sẻ nhưng chưa được kiểm chứng đầy đủ (không được coi là sự thật tuyệt đối).
* **🔴 CHƯA RÕ (Unknown)**: Ứng viên chưa trả lời hoặc chưa có dữ liệu kiểm chứng trong buổi phỏng vấn.

---

## 3. Phân Loại Kết Quả Tuyển Dụng Tổng Thể (Overall Recommendation)

| Xếp loại | Tiêu chuẩn điểm số | Mô tả năng lực |
|---|---|---|
| **🌟 Strong Hire** | Cả 3 trục ≥ 8.5/10 | Nắm cực vững kiến thức chuyên sâu, giải thích sắc bén mọi Trade-offs, chủ động đề xuất giải pháp tối ưu và thể hiện tư duy Tech Lead rõ nét. |
| **✅ Hire** | Cả 3 trục ≥ 7.0/10 | Đáp ứng tốt mọi yêu cầu cốt lõi của JD, tư duy giải quyết vấn đề tốt, giao tiếp rõ ràng, có tiềm năng phát triển nhanh. |
| **⚠️ Borderline** | Điểm trung bình 5.5 – 6.9/10 | Nắm được kiến thức thực hành nhưng còn lúng túng ở các câu hỏi đào sâu kiến trúc hoặc xử lý sự cố; cần phỏng vấn thêm vòng 2. |
| **❌ Weak** | Điểm trung bình 4.0 – 5.4/10 | Trả lời chung chung, thiếu kiến thức nền tảng quan trọng hoặc gặp khó khăn khi bóc tách bài toán. |
| **⛔ No Hire** | < 4.0/10 hoặc vi phạm nghiêm trọng | Sai kiến thức cơ bản nghiêm trọng, nói quá năng lực (Bluffing) hoặc mâu thuẫn lớn với các thông tin đã ghi trên CV. |

---

## 4. Mẫu Báo Cáo Đánh Giá Cuối Cùng (Final Assessment Report)

```markdown
# Báo Cáo Đánh Giá Phỏng Vấn (Interview Assessment Report)

## 1. Tổng Quan & Điểm Số
- **Vị trí mục tiêu:** [Tên vị trí từ JD]
- **Chế độ phỏng vấn:** full-mock / technical-deep-dive / cv-defense / pressure-test / weakness-drill
- **Điểm số 3 trục:**
  - 🛠️ **Chiều sâu kỹ thuật (Technical Depth):** [X]/10
  - 💬 **Kỹ năng giao tiếp (Communication):** [Y]/10
  - 🧠 **Tư duy giải quyết vấn đề (Problem Solving):** [Z]/10
- **Kết luận tuyển dụng:** **Strong Hire / Hire / Borderline / Weak / No Hire**

## 2. Điểm Mạnh Nổi Bật (Strengths)
- [Liệt kê 2–3 điểm mạnh kỹ thuật đã được kiểm chứng bằng câu trả lời xuất sắc]

## 3. Điểm Cần Cải Thiện (Areas for Improvement)
- [Liệt kê các chủ đề ứng viên còn lúng túng hoặc giải thích chưa sâu]

## 4. Rủi Ro Tuyển Dụng & Các Claim Cần Xác Minh Thêm (Interview Risks & Gaps)
- [Cảnh báo về mâu thuẫn giữa CV và câu trả lời thực tế, hoặc các công nghệ chưa chứng minh được kinh nghiệm thực chiến]

## 5. Danh Sách Câu Hỏi Khuyến Nghị Luyện Thêm
1. [Câu hỏi 1]
2. [Câu hỏi 2]
3. [Câu hỏi 3]
```
