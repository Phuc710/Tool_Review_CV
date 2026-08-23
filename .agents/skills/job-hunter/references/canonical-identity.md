# Định Danh Duy Nhất Cho Công Việc (Canonical Job Identity & Deduplication)

Tài liệu này quy định kiến trúc tạo mã định danh duy nhất (Canonical Identity) cho từng công việc để **khử trùng lặp (Deduplication)** khi cùng một tin tuyển dụng được đăng tải chéo trên nhiều nền tảng (LinkedIn, TopCV, ITviec, Careers page).

---

## 1. Hệ Phân Cấp Ưu Tiên Định Danh (Identity Priority Hierarchy)

Tuyệt đối không chỉ dùng `hash(Company + Title + Location)` vì một công ty có thể mở nhiều Requisition khác nhau cho cùng một chức danh tại cùng một thành phố.

Thứ tự ưu tiên trích xuất định danh:

```
Priority 1: source_job_id (Requisition ID chính thức từ hệ thống ATS / Company)
Priority 2: canonical_url (Đường link chuẩn gốc từ trang tuyển dụng của công ty)
Priority 3: SHA256(company + source + source_job_id)
Fallback:   SHA256(company + normalized_title + location + normalized_description)
```

---

## 2. Công Thức Sinh Mã Định Danh (Canonical UID Generation)

```python
import hashlib

def compute_canonical_job_identity(company: str, source: str, source_job_id: str, canonical_url: str, title: str, location: str, description: str = "") -> str:
    company_clean = company.strip().lower()
    source_clean = source.strip().lower()
    source_id_clean = source_job_id.strip()
    
    if source_id_clean:
        raw_key = f"{company_clean}::{source_clean}::{source_id_clean}"
    elif canonical_url:
        raw_key = canonical_url.strip()
    else:
        desc_snippet = description.strip()[:100].lower()
        raw_key = f"{company_clean}::{title.strip().lower()}::{location.strip().lower()}::{desc_snippet}"
        
    uid_hash = hashlib.sha256(raw_key.encode("utf-8")).hexdigest()[:16].upper()
    return f"JOB-{uid_hash}"
```

---

## 3. Quy Tắc Khử Trùng Lặp (Deduplication Rules)

1. **Cùng Requisition ID:** Nếu 2 bài đăng từ 2 nguồn khác nhau (ví dụ: 1 link từ LinkedIn, 1 link từ TopCV) có cùng `source_job_id` của công ty → Hợp nhất thành **1 bản ghi duy nhất**.
2. **Cập nhật độ tươi mới (Freshness):** Khi hợp nhất, giữ lại URL có nguồn gốc chính thức nhất (Official Career Page > LinkedIn > ATS > Job Aggregator) và cập nhật thời điểm `last_verified_at`.
