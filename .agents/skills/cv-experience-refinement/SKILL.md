---
name: cv-experience-refinement
description: Tinh chỉnh và tái cấu trúc các đoạn kinh nghiệm CV thành câu chữ sắc bén chuẩn Senior/Tech Lead dựa trên Handoff Packet từ cv-reviewer và JSON cache. Tuân thủ 100% nguyên tắc bảo toàn sự thật (Anti-Hallucination), không tự bịa đặt số liệu/công nghệ, hỗ trợ 3 chế độ final/enhanced-draft/incomplete và bảo toàn Interview Hooks.
---

# cv-experience-refinement (Tinh Chỉnh & Tái Cấu Trúc Trải Nghiệm CV)

Skill này là **bộ xử lý hạ nguồn (downstream processor)** của `cv-reviewer`. Nhiệm vụ cốt lõi là tiếp nhận các quyết định chiến lược, phân bổ vai trò và ranh giới sự thật từ `cv-reviewer` (hoặc từ `cache/cv_profile.json`), sau đó biên tập và tái cấu trúc từng trải nghiệm thành nội dung CV sắc bén, thể hiện chiều sâu kỹ thuật chuẩn Tech Lead nhưng **tuyệt đối không bịa đặt dữ kiện**.

**QUY TẮC BẮT BUỘC: TOÀN BỘ NỘI DUNG PHÂN TÍCH, CẢNH BÁO VÀ KẾT QUẢ REFINED PHẢI XUẤT BẰNG TIẾNG VIỆT (OUTPUT ALWAYS = VN).**

---

## 1. Đọc Tài Liệu Tham Khảo (References)

Trước khi thực hiện tinh chỉnh, bắt buộc tham khảo các tài liệu chuyên môn sau:
1. [references/refinement-framework.md](references/refinement-framework.md): Khung cấu trúc 2 tầng (1 dòng Tổng quan + 2–4 Bullets chuyên sâu) và quy định phân bổ dung lượng theo 4 vai trò (*Trụ cột, Bằng chứng, Bổ sung, Xóa bỏ*).
2. [references/evidence-policy.md](references/evidence-policy.md): Chính sách bảo toàn sự thật, phân tách 3 tầng dữ liệu (*Available Facts, Confirm Required, Forbidden Assumptions*) và nguyên tắc chống "Seniorize giả".
3. [references/bullet-patterns.md](references/bullet-patterns.md): Thư viện mẫu câu hành động chuẩn Senior theo 4 nhóm năng lực (*System Design, Technical Depth, Reliability & Performance, Delivery & Ownership*).
4. [references/handoff-schema.md](references/handoff-schema.md): Đặc tả hợp đồng gói bàn giao từ `cv-reviewer` và cơ chế lưu trữ mở rộng cache JSON.

---

## 2. Thứ Tự Ưu Tiên Đầu Vào (Input Resolution Contract)

Khi bắt đầu phiên làm việc, Agent nạp dữ liệu theo thứ tự ưu tiên:

1. **Ưu tiên 1 — Gói bàn giao (Handoff Packet)** từ `cv-reviewer` trong phiên trò chuyện hoặc báo cáo đánh giá gần nhất.
2. **Ưu tiên 2 — Hồ sơ [cache/cv_profile.json](file:///c:/Users/Phucx/Desktop/Review_cv/cache/cv_profile.json)**: Nạp danh sách kinh nghiệm, `available_facts`, `role_partition`, và `closed_loop`.
3. **Ưu tiên 3 — Hồ sơ [cache/job_profile.json](file:///c:/Users/Phucx/Desktop/Review_cv/cache/job_profile.json)**: Dùng để đối chiếu từ khóa và ưu tiên đưa công nghệ khớp với JD lên đầu bullet.

> [!IMPORTANT]
> **Xử lý khi thiếu Handoff Packet**: Nếu người dùng gọi trực tiếp `cv-experience-refinement` mà chưa chạy qua `cv-reviewer`:
> - Nếu có sẵn `cache/cv_profile.json` → Tự động đọc dữ liệu từ cache và xử lý ở chế độ `enhanced-draft` hoặc `final`.
> - Nếu không có cả Handoff lẫn Cache → Chuyển sang chế độ **`incomplete`**, thông báo rõ ứng viên cần cung cấp thông tin hoặc chạy `cv-reviewer` trước, **tuyệt đối không tự suy diễn thông tin**.

---

## 3. Quy Tắc Cốt Lõi: SỰ THẬT LÀ BẤT BIẾN (FACTS ARE IMMUTABLE)

1. **Chỉ dùng Sự thật khả dụng (Available Facts)**: Mọi công nghệ, giao thức, vai trò, số lượng thiết bị xuất hiện trong câu chữ bắt buộc phải có nguồn gốc từ dữ liệu ứng viên cung cấp.
2. **Cấm bịa đặt số liệu (Forbidden Metrics)**: Tuyệt đối không tự sinh các con số như `+40% latency`, `99.9% uptime`, `10.000 users`, `2x throughput`, `tiết kiệm 50% chi phí` nếu facts không có.
3. **Cơ chế Placeholder bắt buộc**: Nếu bullet cần số liệu đo lường để tăng sức nặng, bắt buộc sử dụng placeholder:
   `...nhằm tối ưu hóa hiệu năng luồng dữ liệu [CẦN XÁC NHẬN: mức cải thiện latency thực tế]`.
4. **Không "Seniorize" giả tạo**:
   - Nếu facts ghi *Lập trình / Triển khai (Implemented)* → Dùng động từ: *Triển khai, Xây dựng module, Lập trình, Tích hợp, Xử lý...*
   - CẤM biến thành *Kiến trúc toàn bộ (Architected)* hoặc *Lãnh đạo đội ngũ (Led team)* nếu không có bằng chứng.

---

## 4. Tinh Chỉnh Theo Vai Trò (Role-Aware Refinement)

### 🏆 1. Trụ Cột (Pillar) — Trọng tâm hàng đầu
* **1 dòng Tổng quan**: Trả lời rõ *"Dự án này giải quyết bài toán gì?"*.
* **3–4 Bullets chuyên sâu**: Thể hiện đầy đủ System Design, Chiều sâu kỹ thuật, Tối ưu hóa và Bàn giao.
* **Khoảng trống bằng chứng (Evidence Gaps)**: Liệt kê các chi tiết cần ứng viên xác nhận số liệu thực tế.
* **Bảo toàn Interview Hooks**: Giữ nguyên và làm sắc nét các điểm đào sâu phỏng vấn từ `cv-reviewer`.

### 🥈 2. Bằng Chứng (Proof) — Củng cố năng lực then chốt
* **1 dòng Tổng quan**.
* **2–3 Bullets kỹ thuật**: Tập trung vào khía cạnh năng lực bổ trợ mà Pillar chưa thể hiện.

### 🥉 3. Bổ Sung (Supplement) — Độ phủ nền tảng
* **Đúng 1 dòng ngắn gọn**: Tóm tắt vai trò, công nghệ cốt lõi và kết quả chính. Không tạo nhiều bullet dài.

### ❌ 4. Xóa Bỏ (Delete) — Loại bỏ để tránh loãng tín hiệu
* Không viết lại thành kinh nghiệm. Chỉ xuất thông báo:
  ```text
  ### [Tên Kinh Nghiệm] — [Vai trò: DELETE]
  **Trạng thái:** LOẠI BỎ (DELETE)
  **Lý do:** [Trùng lặp / Tín hiệu yếu / Không liên quan JD]
  ```

---

## 5. Ba Chế Độ Đầu Ra (Output Modes)

### 🟢 Mode `final` (Khi facts và số liệu đã đầy đủ)
```markdown
### [Tên Dự Án / Kinh Nghiệm] ｜ [Chức danh] (MM/YYYY - MM/YYYY)
*Vai trò: Trụ cột (Pillar)*

[1 dòng tổng quan định vị bài toán và giải pháp cốt lõi]

- [Bullet 1: Kiến trúc hệ thống / Thiết kế luồng dữ liệu]
- [Bullet 2: Chiều sâu kỹ thuật / Lập trình vi điều khiển / Thuật toán]
- [Bullet 3: Tối ưu hiệu năng / Độ tin cậy / Xử lý đồng thời]
- [Bullet 4: Tích hợp end-to-end / Đóng gói sản phẩm]

**Điểm Đào Sâu Phỏng Vấn (Interview Hooks):**
- [Hook 1: Vấn đề đánh đổi kiến trúc hoặc bài toán khó]
- [Hook 2: Cơ chế xử lý sự cố / phục hồi kết nối]
```

### 🟡 Mode `enhanced-draft` (Có đủ hành động nhưng cần chốt số liệu)
```markdown
### [Tên Dự Án / Kinh Nghiệm] ｜ [Chức danh] (MM/YYYY - MM/YYYY)
*Vai trò: Trụ cột (Pillar) — Chế độ: Bản Thảo Nâng Cao (Enhanced Draft)*

[1 dòng tổng quan]

- Triển khai cơ chế giao tiếp MQTT giữa ESP32 và máy chủ trung tâm, tối ưu hóa kích thước gói tin telemetry [CẦN XÁC NHẬN: dung lượng giảm trước/sau].
- Xây dựng kiến trúc đa luồng với cơ chế Frame Lock ngăn chặn race condition...

> ⚠️ **MỤC CẦN ỨNG VIÊN XÁC NHẬN THỰC TẾ:**
> 1. [CẦN XÁC NHẬN: Tần suất gửi gói tin và độ trễ phản hồi trung bình]
> 2. [CẦN XÁC NHẬN: Số lượng cổng bãi xe/ngã tư vận hành thực nghiệm]

**Điểm Đào Sâu Phỏng Vấn (Interview Hooks):**
- [Hook 1]
```

### 🔴 Mode `incomplete` (Thiếu dữ liệu nền tảng)
```markdown
### [Tên Kinh Nghiệm]
*Trạng thái: THIẾU DỮ LIỆU (INCOMPLETE)*

- **Dữ liệu đã có:** [Liệt kê ngắn gọn facts hiện có]
- **Khoảng trống nghiêm trọng:** [Không rõ mục tiêu dự án / Chưa rõ hành động kỹ thuật / Thiếu công nghệ]
- **Câu hỏi truy vấn cần trả lời:**
  1. Mục tiêu chính của dự án này là gì?
  2. Bạn trực tiếp làm những phần việc kỹ thuật nào và dùng công nghệ gì?
  3. Kết quả đầu ra hoặc sản phẩm bàn giao cụ thể là gì?
```

---

## 6. Giữ Gìn Ranh Giới Nhiệm Vụ (Không Làm Thay `cv-reviewer`)

Skill `cv-experience-refinement` **KHÔNG ĐƯỢC PHÉP**:
- Tự ý thay đổi `Candidate Tier` hoặc chấm điểm toàn diện CV.
- Tự ý thay đổi nhãn `Role Partitioning` (Trụ cột/Bằng chứng/Bổ sung/Xóa bỏ) đã được `cv-reviewer` quyết định.
- Tự ý bịa thêm các lỗi P0/P1 mới mang tính tổng thể hồ sơ.

Nếu phát hiện dữ liệu giữa Handoff Packet và `cache/cv_profile.json` bị mâu thuẫn:
Xuất thông báo **`⚠️ CẢNH BÁO DỮ LIỆU BẤT NHẤT`** và yêu cầu người dùng xác nhận trước khi tiếp tục.

---

## 7. Cập Nhật Cache JSON Sau Khi Tinh Chỉnh

Sau khi tinh chỉnh thành công, tự động cập nhật kết quả vào trường `"refinement"` trong [cache/cv_profile.json](file:///c:/Users/Phucx/Desktop/Review_cv/cache/cv_profile.json) theo cấu trúc chuẩn trong [references/handoff-schema.md](references/handoff-schema.md).
