#!/usr/bin/env python3
"""Unit tests for validate_refinement.py covering Test Cases A through G."""

from __future__ import annotations

import unittest
from validate_refinement import validate_refinement_content


class TestValidateRefinement(unittest.TestCase):

    def test_case_a_full_facts_allowed_metrics(self):
        """Test A: Facts đầy đủ (chấp nhận metrics có sẵn từ source facts)."""
        facts = [
            "ESP32-S3 vi điều khiển",
            "FreeRTOS và MQTT protocol",
            "Hệ thống vận hành 500 thiết bị đồng thời",
            "Giảm độ trễ từ 800ms xuống 300ms",
        ]
        content = """### Camera-AI — Edge AI & Traffic Monitoring
*Vai trò: Trụ cột (Pillar)*

Phát triển hệ thống giám sát giao thông thông minh kết nối 500 thiết bị ESP32-S3 qua MQTT và FreeRTOS.

- Triển khai firmware ESP32-S3 kết nối 500 thiết bị truyền nhận dữ liệu telemetry qua MQTT.
- Tối ưu hóa thời gian phản hồi tín hiệu giảm từ 800ms xuống 300ms trên luồng điều khiển thời gian thực.
- Xây dựng pipeline xử lý ảnh và đồng bộ trạng thái đèn tín hiệu.

**Điểm Đào Sâu Phỏng Vấn (Interview Hooks):**
- Cơ chế xử lý mất gói tin khi kết nối đồng thời 500 thiết bị qua MQTT.
"""
        errors = validate_refinement_content(content, available_facts=facts, role_partition="Trụ cột", mode="final")
        self.assertEqual(errors, [], f"Test A failed: {errors}")

    def test_case_b_no_metric_blocks_fabrication(self):
        """Test B: Không có metric trong source thì CẤM tự bịa số liệu +30% hoặc 2x."""
        facts = [
            "ESP32-S3",
            "MQTT protocol",
            "Tối ưu hóa luồng giao tiếp truyền nhận",
        ]
        # Bị lỗi vì tự bịa "40% latency" và "2x throughput"
        content_fabricated = """### IoT Telemetry
*Vai trò: Trụ cột (Pillar)*

Dự án IoT tối ưu hóa truyền thông.

- Tối ưu hóa luồng giao tiếp giúp giảm 40% latency và tăng 2x throughput.
- Triển khai MQTT trên ESP32-S3.
- Xây dựng module kết nối.

**Điểm Đào Sâu Phỏng Vấn (Interview Hooks):**
- Tối ưu MQTT.
"""
        errors = validate_refinement_content(content_fabricated, available_facts=facts, role_partition="Trụ cột", mode="final")
        self.assertTrue(len(errors) > 0, "Test B should detect fabricated metrics!")

        # Hợp lệ khi dùng placeholder chuẩn
        content_valid_placeholder = """### IoT Telemetry
*Vai trò: Trụ cột (Pillar)*

Dự án IoT tối ưu hóa truyền thông.

- Tối ưu hóa luồng giao tiếp giúp giảm overhead [CẦN XÁC NHẬN: mức cải thiện latency và throughput thực tế].
- Triển khai MQTT trên ESP32-S3 kết nối máy chủ.
- Xây dựng module kết nối ổn định.

**Điểm Đào Sâu Phỏng Vấn (Interview Hooks):**
- Tối ưu MQTT.
"""
        errors_valid = validate_refinement_content(content_valid_placeholder, available_facts=facts, role_partition="Trụ cột", mode="final")
        self.assertEqual(errors_valid, [], f"Test B placeholder failed: {errors_valid}")

    def test_case_c_unauthorized_leadership_claim(self):
        """Test C: Cấm tự nâng cấp 'Implemented' thành 'Led/Architected'."""
        facts = [
            "Implemented backend RESTful API using FastAPI",
            "Wrote unit tests and integrated database",
        ]
        content_fabricated_lead = """### Backend API System
*Vai trò: Trụ cột (Pillar)*

Hệ thống API backend.

- Lãnh đạo đội ngũ 5 kỹ sư thiết kế kiến trúc toàn bộ hệ thống API backend bằng FastAPI.
- Triển khai unit tests và database.

**Điểm Đào Sâu Phỏng Vấn (Interview Hooks):**
- Kiến trúc API.
"""
        errors = validate_refinement_content(content_fabricated_lead, available_facts=facts, role_partition="Trụ cột", mode="final")
        self.assertTrue(any("claim vị trí/vai trò" in e for e in errors), "Test C should catch fake seniorize/leadership claim!")

    def test_case_d_pillar_structure(self):
        """Test D: Pillar phải có từ 2–4 bullets và có Interview Hooks."""
        facts = ["ESP32", "MQTT", "Python"]
        content_too_few_bullets = """### Mini Project
*Vai trò: Trụ cột (Pillar)*

Dự án mini.

- Chỉ có đúng một bullet duy nhất này.
"""
        errors = validate_refinement_content(content_too_few_bullets, available_facts=facts, role_partition="Trụ cột", mode="final")
        self.assertTrue(any("phải có từ 2–4 bullets" in e for e in errors), "Test D should enforce 2-4 bullets for Pillar!")

    def test_case_e_supplement_one_line(self):
        """Test E: Supplement chỉ được tối đa 1 dòng, cấm tạo danh sách bullet dài."""
        facts = ["Tham gia câu lạc bộ học thuật", "Hỗ trợ thành viên mới"]
        content_supplement_too_long = """### CLB Học Thuật
*Vai trò: Bổ sung (Supplement)*

- Bullet 1 hỗ trợ thành viên.
- Bullet 2 tổ chức workshop.
- Bullet 3 viết tài liệu.
"""
        errors = validate_refinement_content(content_supplement_too_long, available_facts=facts, role_partition="Bổ sung", mode="final")
        self.assertTrue(any("chỉ được tối đa 1 dòng" in e for e in errors), "Test E should catch oversized Supplement!")

    def test_case_f_delete_no_bullets(self):
        """Test F: Kinh nghiệm Xóa bỏ (Delete) không được rewrite thành bullets."""
        facts = ["Dự án cũ không liên quan"]
        content_delete_with_bullets = """### Dự án Cũ
*Vai trò: Xóa bỏ*

- Viết lại bullet cho dự án cần xóa.
- Bullet thứ hai.
"""
        errors = validate_refinement_content(content_delete_with_bullets, available_facts=facts, role_partition="Xóa bỏ", mode="final")
        self.assertTrue(any("vẫn được tạo" in e for e in errors), "Test F should forbid generating bullets for deleted items!")

        content_delete_correct = """### Dự án Cũ — [Vai trò: DELETE]
**Trạng thái:** LOẠI BỎ (DELETE)
**Lý do:** Tín hiệu yếu, công nghệ lạc hậu không khớp với JD mục tiêu.
"""
        errors_correct = validate_refinement_content(content_delete_correct, available_facts=facts, role_partition="Xóa bỏ", mode="final")
        self.assertEqual(errors_correct, [], f"Test F correct delete failed: {errors_correct}")

    def test_case_g_incomplete_mode(self):
        """Test G: Missing handoff / Incomplete mode must declare incomplete status."""
        content_incomplete_correct = """### Dự Án Chưa Đủ Thông Tin
**Trạng thái:** THIẾU DỮ LIỆU (INCOMPLETE)

- **Dữ liệu đã có:** ESP32 vi điều khiển.
- **Khoảng trống:** Chưa rõ bài toán và kết quả đầu ra.
"""
        errors = validate_refinement_content(content_incomplete_correct, role_partition="Trụ cột", mode="incomplete")
        self.assertEqual(errors, [], f"Test G incomplete mode failed: {errors}")


if __name__ == "__main__":
    unittest.main()
