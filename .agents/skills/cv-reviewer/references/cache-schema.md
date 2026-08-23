# Đặc Tả Cấu Trúc Cache JSON (CV & Job Cache Schema)

Dự án chuẩn hóa **duy nhất định dạng JSON** để lưu trữ cache dữ liệu giữa các phiên làm việc của Agent. Hai file cache chính gồm:
1. `cache/cv_profile.json`: Lưu trữ toàn bộ dữ liệu đã thẩm định và bóc tách từ CV của ứng viên.
2. `cache/job_profile.json`: Lưu trữ bài toán và tiêu chuẩn tuyển dụng từ mô tả công việc (JD).

---

## 1. Cấu trúc `cache/cv_profile.json` (Hồ Sơ CV Ứng Viên)

```json
{
  "version": "1.0",
  "updated_at": "2026-08-22",
  "candidate_name": "Tên ứng viên",
  "candidate_tier": "Khởi đầu | Tăng trưởng | Bứt phá",
  "tier_rationale": "Căn cứ phân loại cấp độ ứng viên",
  "material_density": {
    "total_volume": "Quá ít | Vừa phải | Quá nhiều",
    "section_density": "Đơn điệu | Vừa phải | Phong phú | Hỗn hợp"
  },
  "core_narrative": {
    "target_direction": "Hướng đi nghề nghiệp mục tiêu",
    "statement": "Tuyên ngôn năng lực cốt lõi trong 1 câu",
    "growth_path": "Lộ trình trưởng thành hoặc chuỗi bằng chứng"
  },
  "personal_anchor": "Điểm độc đáo có liên quan và có bằng chứng chứng minh",
  "experiences": [
    {
      "id": "exp-1",
      "company": "Tên công ty / Đơn vị / Dự án",
      "role": "Chức danh đảm nhiệm",
      "period": "MM/YYYY - MM/YYYY",
      "role_partition": "Trụ cột | Bằng chứng | Bổ sung | Xóa bỏ",
      "proof_task": "Nhiệm vụ chứng minh chính của đoạn này",
      "available_facts": [
        "Sự thật 1 đã được kiểm chứng từ nguồn",
        "Sự thật 2 đã được kiểm chứng từ nguồn"
      ],
      "to_confirm": [
        "Chi tiết cần ứng viên xác nhận thêm trước khi viết lại"
      ],
      "closed_loop": {
        "context": "Bối cảnh & Điều kiện tiền đề",
        "problem": "Vấn đề cần giải quyết",
        "actions_and_tools": "Hành động then chốt và bộ công cụ sử dụng",
        "results_and_impact": "Sản phẩm bàn giao, chỉ số và tác động thực tế",
        "competency_themes": [
          "Chủ đề năng lực 1",
          "Chủ đề năng lực 2"
        ],
        "interview_hooks": [
          "Điểm đào sâu khi phỏng vấn 1"
        ]
      }
    }
  ],
  "skills_and_tools": [
    "Kỹ năng / Công cụ 1",
    "Kỹ năng / Công cụ 2"
  ]
}
```

---

## 2. Cấu trúc `cache/job_profile.json` (Hồ Sơ Yêu Cầu Tuyển Dụng JD)

```json
{
  "version": "1.0",
  "updated_at": "2026-08-22",
  "job_title": "Chức danh tuyển dụng mục tiêu",
  "company_name": "Tên công ty / Doanh nghiệp",
  "industry": "Lĩnh vực hoạt động",
  "seniority_level": "Junior | Middle | Senior | Lead | Manager",
  "core_business_problem": "Bài toán nghiệp vụ trọng tâm mà doanh nghiệp cần nhân sự này giải quyết",
  "requirements": {
    "must_have": [
      "Yêu cầu bắt buộc 1",
      "Yêu cầu bắt buộc 2"
    ],
    "nice_to_have": [
      "Điểm cộng ưu tiên 1",
      "Điểm cộng ưu tiên 2"
    ]
  },
  "target_lexicon": [
    "Thuật ngữ chuyên ngành 1",
    "Thuật ngữ chuyên ngành 2"
  ],
  "key_screening_filters": [
    "Tiêu chí sàng lọc CV trong 5 giây đầu của HR"
  ]
}
```

---

## 3. Quy Tắc Sử Dụng Cache Của Agent

1. **Pre-check**: Trước khi bắt đầu phiên đánh giá, Agent kiểm tra xem `cache/cv_profile.json` hoặc `cache/job_profile.json` đã tồn tại chưa:
   - Nếu `cv_profile.json` đã có và người dùng chỉ gửi JD mới → Tự động nạp dữ liệu CV từ cache để so khớp với JD mới.
   - Nếu `job_profile.json` đã có và người dùng gửi bản CV mới → Tự động nạp dữ liệu JD từ cache để đánh giá bản CV mới.
2. **Auto-update**: Sau khi phân tích thành công CV hoặc JD, Agent tự động cập nhật hoặc tạo mới file JSON tương ứng trong thư mục `cache/`.
3. **Data Integrity**: Tuyệt đối bảo toàn dữ liệu `available_facts` trong cache, không ghi các giả định chưa được kiểm chứng vào cache.
