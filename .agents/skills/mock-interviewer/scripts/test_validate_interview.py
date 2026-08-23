#!/usr/bin/env python3
"""Unit tests for validate_interview.py covering Test 1 through Test 7."""

from __future__ import annotations

import unittest
from validate_interview import (
    validate_question_technology,
    evaluate_adaptive_branch,
    detect_cv_contradiction,
    validate_scoring_report,
    validate_interactive_turn,
)


class TestValidateInterview(unittest.TestCase):

    def test_1_interview_hook_question_chain(self):
        """Test 1: Interview Hook tạo thành chuỗi câu hỏi đào sâu hợp lệ."""
        hook = "Cơ chế xử lý reconnect MQTT"
        # Chuỗi câu hỏi đào sâu từ hook
        q1 = "Trong dự án của bạn, bạn xử lý reconnect MQTT như thế nào?"
        q2 = "Nếu broker mất kết nối liên tục, cơ chế Exponential Backoff của bạn hoạt động ra sao?"
        self.assertIn("reconnect", q1.lower())
        self.assertIn("backoff", q2.lower())

    def test_2_weak_answer_adaptive_handling(self):
        """Test 2: Candidate trả lời yếu/mơ hồ -> Interviewer hỏi clarification/fundamental."""
        # Ứng viên trả lời yếu nhưng độ khó bị tăng vọt từ 2 lên 5 -> Báo lỗi
        errors = evaluate_adaptive_branch(
            previous_difficulty=2,
            candidate_answer_quality="weak",
            next_difficulty=5,
            next_question_type="advanced_architecture",
        )
        self.assertTrue(len(errors) > 0, "Test 2 should catch invalid jump in difficulty on weak answer!")

        # Ứng viên trả lời yếu -> Hỏi clarification ở độ khó 2 -> Hợp lệ
        valid_errors = evaluate_adaptive_branch(
            previous_difficulty=2,
            candidate_answer_quality="weak",
            next_difficulty=2,
            next_question_type="clarification",
        )
        self.assertEqual(valid_errors, [])

    def test_3_strong_answer_difficulty_scaling(self):
        """Test 3: Candidate trả lời xuất sắc -> Tăng độ khó (+1)."""
        errors = evaluate_adaptive_branch(
            previous_difficulty=3,
            candidate_answer_quality="strong",
            next_difficulty=4,
            next_question_type="tradeoff",
        )
        self.assertEqual(errors, [], f"Test 3 failed: {errors}")

        # Trả lời xuất sắc nhưng lại bị hạ độ khó -> Lỗi
        invalid_errors = evaluate_adaptive_branch(
            previous_difficulty=3,
            candidate_answer_quality="strong",
            next_difficulty=1,
            next_question_type="fundamental",
        )
        self.assertTrue(len(invalid_errors) > 0, "Test 3 should catch dropping difficulty on strong answer!")

    def test_4_cv_contradiction_detection(self):
        """Test 4: Phát hiện mâu thuẫn giữa CV và claim của ứng viên."""
        cv_facts = [
            "Implemented backend RESTful API using FastAPI",
            "Wrote unit tests and connected PostgreSQL database",
        ]
        # Ứng viên tự nhận kiến trúc toàn bộ hệ thống
        candidate_claim = "Tôi là người đã kiến trúc toàn bộ hệ thống phân tán và database này."
        is_mismatch, reason = detect_cv_contradiction(cv_facts, candidate_claim)
        self.assertTrue(is_mismatch, "Test 4 should detect CV/Evidence Mismatch!")
        self.assertIn("CV/Evidence Mismatch", reason)

    def test_5_unsupported_technology_guard(self):
        """Test 5: Chặn hỏi công nghệ không có trong CV như một sự thật trong quá khứ."""
        cv_techs = ["ESP32-S3", "FreeRTOS", "MQTT", "Python", "C++"]
        
        # Hỏi Kafka như kinh nghiệm quá khứ (trong khi CV không có) -> Phải BÁO LỖI
        invalid_question = "Bạn đã tối ưu hóa Kafka consumer trong dự án của bạn như thế nào?"
        errors = validate_question_technology(invalid_question, available_technologies=cv_techs)
        self.assertTrue(len(errors) > 0, "Test 5 should catch unverified technology Kafka!")

        # Hỏi dưới dạng câu hỏi giả định có gắn thẻ -> HỢP LỆ
        valid_hypothetical = "[Giả định / Hypothetical] Nếu hệ thống IoT mở rộng và tích hợp Kafka, bạn sẽ thiết kế consumer như thế nào?"
        valid_errors = validate_question_technology(valid_hypothetical, available_technologies=cv_techs, is_hypothetical=True)
        self.assertEqual(valid_errors, [], f"Test 5 hypothetical failed: {valid_errors}")

    def test_6_production_incident_simulation(self):
        """Test 6: Mô phỏng sự cố Production theo nhiều nấc dữ kiện."""
        clue_1 = "Alert: 50 ESP32 thiết bị mất kết nối tới broker MQTT."
        clue_2 = "Dữ kiện mới: CPU server bình thường 15%, nhưng log báo too many open files."
        self.assertIn("Alert", clue_1)
        self.assertIn("open files", clue_2)

    def test_7_scoring_rubric_validation(self):
        """Test 7: Báo cáo đánh giá phải đủ 3 trục và kết luận tuyển dụng."""
        valid_report = """# Báo Cáo Đánh Giá Phỏng Vấn
- **Chiều sâu kỹ thuật (Technical Depth):** 8/10
- **Kỹ năng giao tiếp (Communication):** 7.5/10
- **Tư duy giải quyết vấn đề (Problem Solving):** 8.5/10
- **Kết luận:** **Hire**

## Điểm mạnh
- Nắm vững FreeRTOS và cơ chế đa luồng.
"""
        errors = validate_scoring_report(valid_report)
        self.assertEqual(errors, [], f"Test 7 valid report failed: {errors}")

        invalid_report = """# Báo Cáo Thiếu Điểm
- Technical Depth: 8/10
- Kết luận: Chưa rõ
"""
        invalid_errors = validate_scoring_report(invalid_report)
        self.assertTrue(len(invalid_errors) > 0, "Test 7 should catch missing scoring axes!")


if __name__ == "__main__":
    unittest.main()
