# Khung Tinh Chỉnh Trải Nghiệm Chuẩn Senior (Refinement Framework)

Tài liệu này quy định cấu trúc chuẩn hóa, số lượng bullet và phương pháp viết lại từng đoạn kinh nghiệm dựa trên vai trò do `cv-reviewer` chỉ định.

---

## 1. Cấu Trúc Tổng Quát: "1 Dòng Tổng Quan + 2–4 Bullets Chuyên Sâu"

Mỗi kinh nghiệm Trụ cột hoặc Bằng chứng được cấu trúc thành 2 tầng:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. DÒNG TỔNG QUAN (1-LINE OVERVIEW)                                    │
│    Trả lời: "Dự án/Kinh nghiệm này thực chất giải quyết bài toán gì?"  │
├────────────────────────────────────────────────────────────────────────┤
│ 2. CÁC GẠCH ĐẦU DÒNG NĂNG LỰC CHUYÊN SÂU (2-4 TECHNICAL BULLETS)       │
│    Mỗi bullet thể hiện: Bối cảnh → Vấn đề → Hành động & Công nghệ      │
│    → Kết quả đo lường → Tác động nghiệp vụ                             │
└────────────────────────────────────────────────────────────────────────┘
```

### Tiêu Chuẩn Cho Dòng Tổng Quan
- **❌ Tránh viết chung chung:**
  - *Lập trình viên tham gia dự án IoT.*
  - *Chịu trách nhiệm phát triển phần mềm.*
  - *Tham gia xây dựng ứng dụng cho công ty.*
- **✅ Viết có định vị và phạm vi nghiệp vụ:**
  - *Phát triển hệ sinh thái IoT giám sát giao thông đô thị dựa trên vi điều khiển ESP32-S3, giao thức MQTT thời gian thực và pipeline Edge AI nhận diện phương tiện.*
  - *Thiết kế và triển khai kiến trúc đa luồng (Multi-threading) kiểm soát 4 cổng bãi xe tự động, tích hợp mô hình ALPR và cơ chế đồng bộ hóa tài nguyên không khóa.*

---

## 2. Quy Tắc Phân Bổ Dung Lượng Theo Vai Trò (Role Partitioning)

### 📌 A. Trụ Cột (Pillar) — Trọng tâm cốt lõi của CV
* **Vị trí & Dung lượng:** Chiếm 40–50% dung lượng phần kinh nghiệm.
* **Cấu trúc bắt buộc:**
  * 1 dòng Tổng quan sắc bén.
  * **3–4 Bullets chuyên sâu** bao phủ đa dạng các chủ đề: *Kiến trúc/Hệ thống, Chiều sâu kỹ thuật, Tối ưu hóa/Độ tin cậy, Phối hợp & Bàn giao*.
  * Mục **Khoảng trống bằng chứng (Evidence Gaps)** nếu có thông tin cần bổ sung.
  * Mục **Điểm đào sâu phỏng vấn (Interview Hooks)** được kế thừa từ `cv-reviewer`.

### 📌 B. Bằng Chứng (Proof) — Củng cố năng lực then chốt
* **Vị trí & Dung lượng:** Chiếm 20–30% dung lượng.
* **Cấu trúc bắt buộc:**
  * 1 dòng Tổng quan.
  * **2–3 Bullets kỹ thuật** tập trung vào năng lực bổ trợ quan trọng mà Pillar chưa thể hiện hết (ví dụ: Kỹ năng vi điều khiển khác, kỹ năng cơ sở dữ liệu, kỹ năng làm việc quy trình).

### 📌 C. Bổ Sung (Supplement) — Tạo độ phủ nền tảng
* **Vị trí & Dung lượng:** Tối đa 1–2 dòng ngắn gọn.
* **Cấu trúc bắt buộc:**
  * 1 dòng cô đọng duy nhất tóm tắt vai trò, công nghệ chính và phạm vi đóng góp.
  * **CẤM:** Không viết thành nhiều bullet dài làm loãng trục tự sự chính.

### 📌 D. Xóa Bỏ (Delete) — Loại bỏ để tránh loãng tín hiệu
* **Xử lý:** Không biên tập lại nội dung.
* **Cấu trúc output:**
  ```text
  ### [Tên Kinh Nghiệm] — [Vai trò: DELETE]
  
  **Trạng thái:** LOẠI BỎ (DELETE)
  **Lý do:** [Trùng lặp kỹ năng / Không liên quan tới vị trí mục tiêu / Tín hiệu yếu]
  ```

---

## 3. Ba Chế Độ Xuất Bản (Refinement Output Modes)

### 🟢 1. Chế độ `final`
* **Điều kiện:** Có đầy đủ dữ liệu sự thật (*Available Facts*) và các chỉ số đo lường thực tế từ CV/source.
* **Mục tiêu:** Tạo phiên bản hoàn thiện có thể copy ngay vào CV cuối cùng.

### 🟡 2. Chế độ `enhanced-draft`
* **Điều kiện:** Có đủ ít nhất 2 hành động kỹ thuật cụ thể, nhưng thiếu một số số liệu đo lường hoặc chi tiết môi trường.
* **Mục tiêu:** Tạo bản thảo cấu trúc hoàn hảo kèm theo các thẻ `[CẦN XÁC NHẬN: ...]` để ứng viên rà soát và điền số liệu thật trước khi nộp.

### 🔴 3. Chế độ `incomplete`
* **Điều kiện:** Thiếu thông tin bối cảnh nền tảng (không rõ đối tượng phục vụ, không rõ hành động kỹ thuật chính).
* **Mục tiêu:** Liệt kê các thông tin đã xác thực, chỉ rõ khoảng trống dữ liệu và đưa ra danh sách câu hỏi truy vấn cụ thể cho ứng viên, **tuyệt đối không bịa trải nghiệm giả**.
