#!/usr/bin/env python3
"""Regression tests across candidate tiers and material shapes (Vietnamese & English)."""

from validate_audit import DISCLAIMER, REQUIRED_VI, validate


def valid_sample_vi(tier: str, total: str, density: str) -> str:
    sections = [
        "# Báo cáo Đánh giá CV",
        "## Kết luận một câu\nỨng viên có tiềm năng tốt, cần làm nổi bật kết quả kinh doanh.",
        f"## Phân loại ứng viên & Mật độ hồ sơ\n- **Cấp độ ứng viên：** {tier}\n- **Tổng lượng kinh nghiệm：** {total}\n- **Mật độ từng đoạn：** {density}\n- **Điểm thang đo：** 85/100",
        "## Trục tự sự mục tiêu\n- **Vấn đề của vị trí mục tiêu：** Giải quyết bài toán mở rộng quy mô",
        "## P0：Cần sửa ngay lập tức\n| Vị trí | Vấn đề | Tác động | Cách sửa trực tiếp |\n|---|---|---|---|",
        "## P1：Quyết định độ chuyên nghiệp & độ khớp JD\n| Vị trí | Vấn đề | Tác động | Cách sửa trực tiếp |\n|---|---|---|---|",
        "## Dung lượng & Bố cục kinh nghiệm\n| Kinh nghiệm | Vai trò | Nhiệm vụ chứng minh | Độ sâu | Vị trí |\n|---|---|---|---|---|",
        "## Đánh giá chi tiết từng đoạn\n### Công ty A | Kỹ sư phần mềm\n- **Vấn đề：** Tối ưu hóa hiệu năng\n- **Bộ công cụ & Hành động：** Sử dụng Python và Redis\n- **Kết quả & Tác động：** Giảm độ trễ 40%\n- **Điểm đào sâu khi phỏng vấn (Hook)：** Xử lý cache invalidation",
        "## Thuật ngữ ngành & Ngôn ngữ tuyển dụng\n| Cách diễn đạt cũ | Cách diễn đạt chuẩn theo JD | Cơ chế | Điều kiện |\n|---|---|---|---|",
        "## Gợi ý trình bày & Đóng gói\n| Loại | Cách viết cũ | Cách viết đề xuất | Vấn đề | Rủi ro |\n|---|---|---|---|---|",
        "## Kết nối tinh chỉnh trải nghiệm cv-experience-refinement\n- **Có khuyến nghị tiếp tục không：** Có\n- **Phạm vi xử lý đợt đầu：** Công ty A\n- **Chế độ đợt đầu：** final\n| Mức ưu tiên | Kinh nghiệm | Vai trò | Mục tiêu | Gợi ý | Sự thật khả dụng | Cần xác nhận / Cấm tự ý bổ sung |\n|---|---|---|---|---|---|---|\n\nHãy sử dụng cv-experience-refinement để tiếp tục xử lý.",
        "## Gợi ý chuyên sâu theo cấp độ\n- **Tăng trưởng：** Tối ưu hóa lộ trình",
        "## P2：Hành động củng cố giai đoạn tiếp theo\n- Bổ sung chứng chỉ AWS",
        "## Check-list 30 giây trước khi nộp\n- [ ] Đã kiểm tra thời gian và số liệu",
        DISCLAIMER,
    ]
    return "\n\n".join(sections)


def main() -> int:
    cases = (
        ("Khởi đầu", "Quá ít", "Đơn điệu"),
        ("Khởi đầu", "Quá ít", "Phong phú"),
        ("Tăng trưởng", "Vừa phải", "Hỗn hợp"),
        ("Tăng trưởng", "Quá nhiều", "Đơn điệu"),
        ("Bứt phá", "Quá nhiều", "Phong phú"),
        ("Bứt phá", "Vừa phải", "Phong phú"),
    )
    for case in cases:
        errors = validate(valid_sample_vi(*case))
        assert errors == [], f"Validation failed for case {case}: {errors}"

    # Negative assertions
    assert any("Cấp độ ứng viên" in item for item in validate(valid_sample_vi("Không xác định", "Vừa phải", "Vừa phải")))
    assert any("Dòng cuối cùng" in item for item in validate(valid_sample_vi(*cases[0]) + "\nĐoạn thừa ở đuôi"))
    assert any("Thiếu mục bắt buộc" in item for item in validate(valid_sample_vi(*cases[0]).replace("## P0：Cần sửa ngay lập tức", "")))
    assert any("Chế độ đợt đầu" in item for item in validate(valid_sample_vi(*cases[0]).replace("**Chế độ đợt đầu：** final", "**Chế độ đợt đầu：** unknown")))
    assert any("Sự thật khả dụng" in item for item in validate(valid_sample_vi(*cases[0]).replace("Sự thật khả dụng", "Thông tin tham khảo")))

    print("OK: six routing cases, refinement handoff, and negative checks passed (Vietnamese & English)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
