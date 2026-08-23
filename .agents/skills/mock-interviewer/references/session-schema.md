# Đặc Tả Cấu Trúc Phiên Phỏng Vấn JSON (Interview Session Schema)

Tài liệu này quy định cấu trúc file lưu trữ trạng thái phiên phỏng vấn `cache/interview_session.json` phục vụ việc theo dõi tiến trình tương tác giữa AI Interviewer và ứng viên.

---

## 1. Cấu Trúc `cache/interview_session.json`

```json
{
  "session_version": "1.0",
  "session_id": "session-20260823-001",
  "candidate_name": "Nguyễn Thành Phúc",
  "target_role": "Embedded Firmware / C++ Developer",
  "mode": "full-mock | technical-deep-dive | cv-defense | pressure-test | weakness-drill",
  "created_at": "2026-08-23T10:45:00Z",
  "status": "IN_PROGRESS | COMPLETED",
  "current_stage": "IDLE | INTRO | WARMUP | CV_DEEP_DIVE | TECHNICAL | SYSTEM_DESIGN | SCENARIO | PRESSURE_TEST | FINAL_EVALUATION | COMPLETE",
  "current_difficulty": 3,
  "turns": [
    {
      "turn_id": 1,
      "stage": "TECHNICAL",
      "question_type": "implementation | architecture | tradeoff | debugging | production-incident",
      "difficulty": 3,
      "question_text": "Trong dự án Camera-AI, bạn xử lý luồng stream video MJPEG từ ESP32-S3 lên máy chủ FastAPI như thế nào?",
      "is_hypothetical": false,
      "candidate_answer": "Dạ em dùng endpoint streaming multipart/x-mixed-replace...",
      "evaluation": {
        "technical_depth": 8,
        "communication": 7,
        "problem_solving": 8,
        "confidence": "Observed | Inferred | Unknown",
        "flags": [
          "Strong Answer",
          "Needs Trade-off probe"
        ],
        "notes": "Ứng viên nắm rõ cơ chế HTTP multipart streaming."
      }
    }
  ],
  "cumulative_scores": {
    "technical_depth": 8.0,
    "communication": 7.5,
    "problem_solving": 8.0,
    "overall_recommendation": "Strong Hire | Hire | Borderline | Weak | No Hire"
  },
  "identified_risks": [
    "Cần xác minh thêm kinh nghiệm thực tế với hàng đợi tin nhắn chịu tải lớn"
  ]
}
```
