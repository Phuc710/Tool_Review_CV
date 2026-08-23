# Chính Sách Bảo Toàn Sự Thật & Chống Bịa Đặt (Evidence Policy & Anti-Hallucination)

Quy tắc tối thượng của `cv-experience-refinement` là: **SỰ THẬT LÀ BẤT BIẾN (FACTS ARE IMMUTABLE)**. Skill này chỉ làm nhiệm vụ tái cấu trúc ngữ nghĩa, nâng cao độ sắc bén trong hành văn và tổ chức logic theo chuẩn Tech Lead, **tuyệt đối không bịa đặt thêm dữ kiện**.

---

## 1. Phân Tách 3 Tầng Dữ Liệu

Mọi thông tin xuất hiện trong bản tinh chỉnh kinh nghiệm bắt buộc phải thuộc một trong ba nhóm sau:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. SỰ THẬT KHẢ DỤNG (AVAILABLE FACTS)                                  │
│    - Thông tin đã được kiểm chứng trực tiếp từ CV, source code, cache  │
│    - Được phép sử dụng trực tiếp trong câu chữ                         │
├────────────────────────────────────────────────────────────────────────┤
│ 2. MỤC CẦN XÁC NHẬN (CONFIRM REQUIRED / PLACEHOLDERS)                  │
│    - Thiếu số liệu đo lường, quy mô, thời gian nhưng cần thiết         │
│    - BẮT BUỘC dùng cú pháp: [CẦN XÁC NHẬN: ...]                        │
├────────────────────────────────────────────────────────────────────────┤
│ 3. GIẢ ĐỊNH BỊ CẤM (FORBIDDEN ASSUMPTIONS)                             │
│    - Tự ý bịa đặt số liệu %, người dùng, quy mô đội ngũ, công nghệ mới │
│    - CẤM TUYỆT ĐỐI KHÔNG ĐƯỢC XUẤT HIỆN TRONG OUTPUT                   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Bảng Đối Chiếu Hành Vi Vi Phạm & Chuẩn Hóa

| Trường hợp | Cách viết vi phạm (BỊ CẤM ❌) | Cách viết chuẩn hóa (BẮT BUỘC ✅) |
|---|---|---|
| **Chỉ số % hiệu năng** | Tối ưu hệ thống giúp giảm **40%** latency và tăng **2x** throughput. | Tối ưu pipeline xử lý dữ liệu và giảm overhead trong luồng giao tiếp `[CẦN XÁC NHẬN: latency/throughput cải thiện thực tế]`. |
| **Quy mô người dùng / Thiết bị** | Hệ thống phục vụ **10.000 người dùng hoạt động hàng ngày** và **500 thiết bị**. | Triển khai hệ thống kết nối thiết bị với máy chủ trung tâm `[CẦN XÁC NHẬN: số lượng thiết bị/người dùng thực tế]`. *(Nếu trong facts có 500 thiết bị thì được dùng 500 thiết bị, không được tự tăng lên 10.000)* |
| **Công nghệ không có trong facts** | Xây dựng pipeline CI/CD với **Docker & Kubernetes** cho vi điều khiển ESP32. | Xây dựng pipeline tự động hóa nạp firmware và kiểm thử cho ESP32 `[CẦN XÁC NHẬN: công cụ CI/CD sử dụng thực tế]`. *(Cấm tự điền Docker/K8s nếu CV chỉ ghi nạp qua PlatformIO)* |
| **Nâng cấp vai trò (Fake Seniorize)** | **Dẫn dắt đội ngũ 5 kỹ sư**, thiết kế toàn bộ kiến trúc microservices phân tán. | Tham gia phát triển các module dịch vụ backend và phối hợp tích hợp trong nhóm `[CẦN XÁC NHẬN: phạm vi phụ trách kiến trúc]`. *(Cấm biến "Implemented" thành "Architected/Led")* |
| **Chỉ số thời gian / Độ sẵn sàng** | Đạt **99.9% uptime**, giảm **50%** chi phí hạ tầng AWS. | Cấu hình cơ chế tự động kết nối lại (Auto-reconnect) nhằm duy trì tính ổn định của luồng dữ liệu `[CẦN XÁC NHẬN: chỉ số uptime/chi phí tiết kiệm thực tế]`. |

---

## 3. Quy Tắc Placeholder Chuẩn

Khi cần bổ sung số liệu định lượng để tăng sức thuyết phục nhưng ứng viên chưa cung cấp, hãy sử dụng các placeholder theo đúng định dạng sau:

* `[CẦN XÁC NHẬN: số lượng thiết bị hoạt động đồng thời]`
* `[CẦN XÁC NHẬN: mức cải thiện latency trước/sau tối ưu]`
* `[CẦN XÁC NHẬN: số lượng request/giây hoặc tần suất gửi gói tin]`
* `[CẦN XÁC NHẬN: thời gian xử lý trung bình mỗi khung hình]`
* `[CẦN XÁC NHẬN: công cụ đo lường / profiling sử dụng]`

> [!WARNING]
> Tuyệt đối không dùng các ký tự chung chung vô nghĩa như `XX%`, `YY devices`, `N customers`, `10x` mà không có nhãn chỉ dẫn `[CẦN XÁC NHẬN: ...]`.

---

## 4. Quy Tắc Phòng Vệ "Fake Seniorize" (Không Thổi Phồng Trách Nhiệm)

Một lỗi rất phổ biến khi AI viết lại CV là tự ý "thổi phồng" ứng viên bằng các động từ đao to búa lớn. Cần phân định rạch ròi:

1. **Nếu nguồn ghi "Tham gia / Phát triển / Cài đặt (Implemented / Developed)"**:
   - ✅ Sử dụng: `Triển khai...`, `Xây dựng module...`, `Lập trình cơ chế...`, `Tích hợp...`, `Debug và xử lý...`
   - ❌ CẤM sử dụng: `Kiến trúc toàn bộ... (Architected)`, `Lãnh đạo đội ngũ... (Led team)`, `Chịu trách nhiệm toàn diện hệ thống... (Owned end-to-end architecture)`.

2. **Nếu nguồn ghi "Thiết kế / Quản lý kỹ thuật (Designed / Tech Lead)"**:
   - Chỉ được dùng khi trong `Available Facts` hoặc `cv_profile.json` có bằng chứng rõ ràng (ví dụ: Chức danh Tech Lead, Leader CLB, Thiết kế PCB/Architecture đã được xác nhận).
