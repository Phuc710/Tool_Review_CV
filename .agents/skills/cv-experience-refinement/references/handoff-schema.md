# Đặc Tả Giao Thức Bàn Giao (Handoff Schema & Contract)

Tài liệu này quy định cấu trúc gói bàn giao (*Handoff Packet*) được truyền từ `cv-reviewer` sang `cv-experience-refinement` và cơ chế lưu trữ kết quả tinh chỉnh ngược trở lại `cache/cv_profile.json`.

---

## 1. Hợp Đồng Đầu Vào (Input Resolution Hierarchy)

Skill `cv-experience-refinement` nạp dữ liệu đầu vào theo thứ tự ưu tiên nghiêm ngặt:

```
Priority 1: Gói bàn giao (Handoff Packet) trực tiếp trong phiên hoặc báo cáo của cv-reviewer
    │ (Nếu có → Đầy đủ context nhiệm vụ chứng minh và ranh giới sự thật)
    ▼
Priority 2: Hồ sơ đã lưu tại cache/cv_profile.json
    │ (Nếu thiếu Handoff Packet → Đọc experiences, available_facts, role_partition từ cache)
    ▼
Priority 3: Hồ sơ yêu cầu tuyển dụng tại cache/job_profile.json
    │ (Dùng để ưu tiên thứ tự từ khóa và bài toán công nghệ khớp với JD)
    ▼
Fallback Mode: Chuyển sang chế độ "incomplete" nếu cả Handoff và Cache đều thiếu dữ liệu cốt lõi
```

---

## 2. Đặc Tả JSON Schema của Handoff Packet

```json
{
  "handoff_version": "1.0",
  "source_skill": "cv-reviewer",
  "target_direction": "Hướng đi nghề nghiệp mục tiêu",
  "overall_refinement_mode": "final | enhanced-draft | incomplete",
  "experiences_to_refine": [
    {
      "experience_id": "proj-1 / exp-1",
      "company_or_project": "Tên công ty / Dự án",
      "role": "Chức danh đảm nhiệm",
      "period": "2024 - 2025",
      "role_partition": "Trụ cột | Bằng chứng | Bổ sung | Xóa bỏ",
      "proof_task": "Nhiệm vụ chứng minh cốt lõi của đoạn này",
      "suggested_overview_focus": "Định hướng trọng tâm cho câu tổng quan 1 dòng",
      "competency_themes": [
        "Chủ đề năng lực 1",
        "Chủ đề năng lực 2"
      ],
      "available_facts": [
        "Sự thật 1 đã được kiểm chứng từ nguồn",
        "Sự thật 2 đã được kiểm chứng từ nguồn"
      ],
      "to_confirm": [
        "Chi tiết cần ứng viên xác nhận thêm (số liệu, công cụ đo lường)"
      ],
      "interview_hooks": [
        "Điểm đào sâu khi phỏng vấn cần bảo toàn"
      ],
      "refinement_mode": "final | enhanced-draft | incomplete"
    }
  ]
}
```

---

## 3. Đặc Tả Bảng Markdown Handoff (Từ cv-reviewer output)

Nếu đầu vào được truyền qua định dạng Markdown của `cv-reviewer/references/output-template.md`:

```markdown
## Kết nối tinh chỉnh trải nghiệm cv-experience-refinement
- **Phạm vi xử lý đợt đầu：** Camera-AI, Xparking_Auto
- **Chế độ đợt đầu：** final / enhanced-draft / incomplete

| Mức ưu tiên | Kinh nghiệm | Vai trò rà soát | Mục tiêu tổng quan công việc | Gợi ý chủ đề năng lực | Sự thật khả dụng (Available Facts) | Cần xác nhận / Cấm tự ý bổ sung (To Confirm / Strictly Forbidden to Assume) |
|---|---|---|---|---|---|---|
| 1 | Camera-AI | Trụ cột | Giám sát giao thông Edge AI & điều khiển đèn | Tích hợp ESP32-S3; MQTT thời gian thực; YOLOv8 tracking | ESP32-S3, MQTT, YOLOv8, DeepSORT, FastAPI | Cần xác nhận FPS, độ trễ và số ngã tư thử nghiệm |
```

---

## 4. Cấu Trúc Lưu Trữ Mở Rộng Trong `cache/cv_profile.json` (Backward-Compatible)

Khi `cv-experience-refinement` hoàn tất tinh chỉnh, kết quả có thể được cập nhật vào trường mở rộng `"refinement"` trong [cache/cv_profile.json](file:///c:/Users/Phucx/Desktop/Review_cv/cache/cv_profile.json) mà **không làm thay đổi hay phá vỡ các trường dữ liệu gốc**:

```json
{
  "version": "2.0",
  "candidate_name": "...",
  "candidate_tier": "...",
  "experiences": [ ... ],
  "refinement": {
    "version": "1.0",
    "updated_at": "2026-08-23",
    "mode": "final",
    "items": [
      {
        "id": "proj-1",
        "role_partition": "Trụ cột",
        "overview": "Phát triển hệ thống giám sát giao thông thông minh...",
        "bullets": [
          "Triển khai firmware ESP32-S3...",
          "Xây dựng pipeline thị giác máy tính...",
          "Thiết lập kênh điều khiển MQTT..."
        ],
        "evidence_gaps": [
          "Cần xác nhận FPS thực tế khi chạy trên phần cứng"
        ],
        "interview_hooks": [
          "Thuật toán Multi-frame Voting lọc nhiễu nhận diện biển số"
        ]
      }
    ]
  }
}
```
