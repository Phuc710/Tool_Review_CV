#!/usr/bin/env python3
"""Validate the stable structure and routing fields of a resume audit (supports Vietnamese and English)."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_VI = (
    "# Báo cáo Đánh giá CV",
    "## Kết luận một câu",
    "## Phân loại ứng viên & Mật độ hồ sơ",
    "## Trục tự sự mục tiêu",
    "## P0",
    "## P1",
    "## Dung lượng & Bố cục kinh nghiệm",
    "## Đánh giá chi tiết từng đoạn",
    "## Thuật ngữ ngành & Ngôn ngữ tuyển dụng",
    "## Gợi ý trình bày & Đóng gói",
    "## Kết nối tinh chỉnh trải nghiệm cv-experience-refinement",
    "## Gợi ý chuyên sâu theo cấp độ",
    "## P2",
    "## Check-list 30 giây trước khi nộp",
)

REQUIRED_EN = (
    "# CV Audit Report",
    "## One-Sentence Conclusion",
    "## Candidate Tier & Material Density",
    "## Target Narrative Axis",
    "## P0",
    "## P1",
    "## Experience Volume & Arrangement",
    "## Detailed Section Audit",
    "## Industry Lexicon & Recruiting Language",
    "## Presentation & Packaging Suggestions",
    "## Connect to cv-experience-refinement",
    "## Tier-Specific Suggestions",
    "## P2",
    "## 30-Second Pre-Submission Checklist",
)

REQUIRED = REQUIRED_VI

TIERS = ("Khởi đầu", "Tăng trưởng", "Bứt phá", "Entry-level", "Growth", "Sprint")
TOTALS = ("Quá ít", "Vừa phải", "Quá nhiều", "Too Little", "Moderate", "Too Much")
DENSITIES = ("Đơn điệu", "Vừa phải", "Phong phú", "Hỗn hợp", "Thin", "Rich", "Mixed")
REFINEMENT_MODES = ("final", "enhanced-draft", "incomplete")
DISCLAIMERS = (
    "> Kết quả chỉ mang tính tham khảo, cần được chỉnh sửa thủ công",
    "> For reference only, manual editing is required",
)
DISCLAIMER = "> Kết quả chỉ mang tính tham khảo, cần được chỉnh sửa thủ công"


def has_labeled_choice(text: str, label: str, choices: tuple[str, ...]) -> bool:
    for choice in choices:
        for sep in ("：", ":"):
            variants = (
                f"**{label}{sep}** {choice}",
                f"**{label}**{sep} {choice}",
                f"**{label}{sep}**{choice}",
                f"**{label}**{sep}{choice}",
                f"{label}{sep} {choice}",
                f"{label}{sep}{choice}",
            )
            if any(v in text for v in variants):
                return True
    return False


def validate(text: str) -> list[str]:
    errors: list[str] = []

    is_en = "CV Audit Report" in text or "One-Sentence Conclusion" in text
    required_sections = REQUIRED_EN if is_en else REQUIRED_VI

    for heading in required_sections:
        if heading not in text:
            errors.append(f"Thiếu mục bắt buộc (Missing section): {heading}")

    positions = [text.find(heading) for heading in required_sections]
    found = [position for position in positions if position >= 0]
    if found != sorted(found):
        errors.append("Thứ tự các mục không đúng mẫu (Section order invalid)")

    tier_labels = ("Candidate Tier", "Cấp độ ứng viên")
    if not any(has_labeled_choice(text, lbl, TIERS) for lbl in tier_labels):
        errors.append("Cấp độ ứng viên phải chọn rõ: Khởi đầu, Tăng trưởng hoặc Bứt phá (Candidate tier must be specified)")

    total_labels = ("Total Experience", "Tổng lượng kinh nghiệm", "Volume")
    if not any(has_labeled_choice(text, lbl, TOTALS) for lbl in total_labels):
        errors.append("Tổng lượng kinh nghiệm phải chọn: Quá ít, Vừa phải hoặc Quá nhiều (Total volume must be specified)")

    density_labels = ("Section Density", "Mật độ từng đoạn", "Density")
    if not any(has_labeled_choice(text, lbl, DENSITIES) for lbl in density_labels):
        errors.append("Mật độ từng đoạn phải chọn: Đơn điệu, Vừa phải, Phong phú hoặc Hỗn hợp (Density must be specified)")

    if not ("**Điểm thang đo：**" in text or "**Điểm thang đo:**" in text or "**Rubric Score:**" in text or "**Rubric Score：**" in text or "Điểm thang đo" in text or "Rubric Score" in text):
        errors.append("Thiếu điểm thang đo đánh giá (Missing rubric score)")

    if is_en:
        if not ("Problem" in text and ("action" in text.lower() or "tool" in text.lower()) and "Result" in text):
            errors.append("Each section audit must contain Problem, Toolchain/Action, and Result")
        if not ("Hook" in text or "Interview Hook" in text):
            errors.append("Missing interview hook (Hook)")
    else:
        if not ("Vấn đề" in text and ("công cụ" in text.lower() or "hành động" in text.lower()) and "Kết quả" in text):
            errors.append("Mỗi đoạn phải có Vấn đề, Bộ công cụ/Hành động và Kết quả")
        if not ("Hook" in text or "Điểm đào sâu" in text):
            errors.append("Thiếu điểm đào sâu khi phỏng vấn (Interview Hook)")

    mode_found = any(
        f"**Chế độ đợt đầu：** {m}" in text
        or f"**Chế độ đợt đầu:** {m}" in text
        or f"**First-batch Mode:** {m}" in text
        or f"**First-batch Mode：** {m}" in text
        or f"Chế độ đợt đầu：** {m}" in text
        or f"Chế độ đợt đầu:** {m}" in text
        for m in REFINEMENT_MODES
    )
    if not mode_found:
        errors.append("Chế độ đợt đầu phải chọn: final, enhanced-draft hoặc incomplete")

    if is_en:
        if not ("Available Facts" in text or "Available facts" in text):
            errors.append("Refinement handoff must contain Available Facts")
        if not ("To Confirm" in text or "To confirm" in text or "Forbidden to Assume" in text):
            errors.append("Refinement handoff must separate To Confirm / Forbidden to Assume")
    else:
        if not ("Sự thật khả dụng" in text or "Available Facts" in text):
            errors.append("Gói bàn giao phải có Sự thật khả dụng (Available Facts)")
        if not ("Cần xác nhận" in text or "To Confirm" in text or "Cấm tự ý bổ sung" in text):
            errors.append("Gói bàn giao phải có Cần xác nhận / Cấm tự ý bổ sung (To Confirm / Forbidden to Assume)")

    if "cv-experience-refinement" not in text:
        errors.append("Thiếu câu lệnh gọi cv-experience-refinement")

    if "[ ]" not in text and "[x]" not in text.lower():
        errors.append("Thiếu các mục check-list 30 giây trước khi nộp")

    last_line = text.rstrip().split("\n")[-1].strip()
    if not any(d in last_line for d in DISCLAIMERS):
        errors.append(f"Dòng cuối cùng phải là dòng cảnh báo: {DISCLAIMER}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate CV audit reports")
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()
    errors = validate(args.audit.read_text(encoding="utf-8"))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: audit structure and routing are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
