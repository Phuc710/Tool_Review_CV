# Chiến Lược Đặt Câu Hỏi Thích Ứng (Adaptive Questioning Strategy)

Tài liệu này quy định logic phân nhánh câu hỏi thích ứng (Adaptive Questioning), 5 cấp độ khó và cách biến `Interview Hooks` thành các chuỗi câu hỏi đào sâu liên hoàn (Question Chains).

---

## 1. Năm Cấp Độ Khó (Question Difficulty Levels)

```
┌────────────────────────────────────────────────────────────────────────┐
│ Level 1: CƠ BẢN (Fundamental)     │ Cú pháp, định nghĩa, cơ chế cơ sở  │
├───────────────────────────────────┼────────────────────────────────────┤
│ Level 2: THỰC HÀNH (Practical)    │ Cách implement, cấu hình ngoại vi  │
├───────────────────────────────────┼────────────────────────────────────┤
│ Level 3: CHUYÊN SÂU (Deep Tech)   │ Quản lý bộ nhớ, Race condition, FSM│
├───────────────────────────────────┼────────────────────────────────────┤
│ Level 4: KIẾN TRÚC (Architecture) │ Đánh đổi (Trade-offs), Giao thức   │
├───────────────────────────────────┼────────────────────────────────────┤
│ Level 5: TECH LEAD / SCALE        │ Phân tán, Xử lý sự cố, Scale x100  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Logic Phân Nhánh Thích Ứng (Adaptive Branching Engine)

Tùy theo chất lượng câu trả lời của ứng viên, Interviewer lập tức điều chỉnh chiến thuật:

| Loại câu trả lời | Đánh giá nội bộ | Hành động tiếp theo của Interviewer |
|---|---|---|
| **Rất sắc bén, đúng trọng tâm, có số liệu/cơ chế** | `Strong Answer` | **Tăng độ khó (+1 cấp)**: Đặt câu hỏi về Edge Case, Trade-off hoặc nâng tải hệ thống lên gấp 10–100 lần. |
| **Chung chung, chỉ nêu keyword, thiếu chiều sâu** | `Weak / Vague Answer` | **Khoan sâu làm rõ (Clarification)**: *"Cụ thể bạn cấu hình thông số nào? 'Nhẹ' ở đây là nhẹ về bộ nhớ RAM hay băng thông mạng?"* |
| **Sai kiến thức cơ bản** | `Wrong Answer` | **Dò đáy kiến thức (Fundamental Probe)**: Lùi 1 bước để kiểm tra xem ứng viên nắm đến đâu trước khi chuyển chủ đề. |
| **Né tránh câu hỏi, nói vòng vo sang chủ đề khác** | `Avoidance / Bluffing` | **Cắm cờ & Ép trực diện**: *"Tôi đang hỏi về cơ chế Lock khung hình trong Python, bạn chưa trả lời phần race condition. Hãy giải thích trực tiếp phần này."* |

---

## 3. Chuyển Đổi Interview Hooks Thành Chuỗi Câu Hỏi (Question Chains)

Mọi `interview_hooks` trong [cache/cv_profile.json](file:///c:/Users/Phucx/Desktop/Review_cv/cache/cv_profile.json) đều được khai thác thành chuỗi 3–5 câu hỏi liên hoàn:

### Ví dụ: Hook *"Cơ chế xử lý mất kết nối và truyền lệnh MQTT xuống ESP32 PCB"*

* **Câu 1 (Implementation - Level 2):**  
  *Trong dự án Camera-AI, bạn thiết lập cơ chế kết nối MQTT giữa máy chủ và mạch ESP32 PCB như thế nào? QoS bạn chọn là mức mấy và tại sao?*
* **Câu 2 (Deep Technical - Level 3):**  
  *Nếu vi điều khiển ESP32 PCB bị mất sóng WiFi trong 30 giây, các lệnh điều khiển khẩn cấp gửi từ backend trong thời gian này sẽ được xử lý ra sao? Bạn dùng Retained Message hay Offline Buffer trên RAM?*
* **Câu 3 (Edge Case & Trade-off - Level 4):**  
  *Nếu hàng trăm thiết bị cùng mất kết nối và đồng loạt gửi bản tin Reconnect trong 1 giây (Reconnect Storm), broker của bạn có nguy cơ bị sập không? Bạn thiết kế cơ chế Exponential Backoff Jitter như thế nào ở phía firmware?*
* **Câu 4 (Observability - Level 5):**  
  *Làm thế nào để hệ thống giám sát trung tâm phát hiện một mạch ESP32 bị treo (Hard Fault hoặc deadlock) chứ không phải do mất mạng thông thường?*

---

## 4. Bản Đồ Động Từ CV (CV Action Verbs Mapping)

Interviewer tự động nhận diện các động từ hành động trong CV để tung ra các câu hỏi đối kháng:

| Động từ trong CV | Mục tiêu kiểm chứng | Mẫu câu hỏi truy vấn |
|---|---|---|
| **`Designed / Thiết kế`** | Kiểm tra quyền quyết định và sự hiểu biết về giải pháp thay thế. | *Bạn là người trực tiếp ra quyết định thiết kế kiến trúc này hay làm theo tài liệu có sẵn? Các phương án thay thế bạn đã cân nhắc là gì? Đánh đổi lớn nhất là gì?* |
| **`Optimized / Tối ưu hóa`** | Kiểm tra phương pháp đo lường khoa học và chỉ số thực tế. | *Trước khi tối ưu, điểm nghẽn (Bottleneck) nằm ở đâu và bạn đo bằng công cụ gì? Bạn đã thay đổi logic nào và con số cải thiện chính xác là bao nhiêu?* |
| **`Led / Dẫn dắt`** | Kiểm tra quy mô trách nhiệm và khả năng xử lý xung đột kỹ thuật. | *Bạn dẫn dắt bao nhiêu thành viên? Khi có bất đồng về kiến trúc kỹ thuật giữa các bạn trong nhóm, bạn giải quyết như thế nào?* |
| **`Integrated / Tích hợp`** | Kiểm tra hiểu biết về giao thức và xử lý ngoại lệ giao tiếp. | *Khi tích hợp giữa 2 module khác nhau, rủi ro lớn nhất về sai lệch dữ liệu là gì và bạn thiết kế cơ chế Handshake / Validation thế nào?* |
