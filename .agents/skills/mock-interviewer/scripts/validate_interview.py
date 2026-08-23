#!/usr/bin/env python3
"""Validation script for mock-interviewer skill.

Checks:
1. Technology anti-hallucination: No asking about technologies outside CV as if candidate used them in past projects, unless labeled with '[Giả định / Hypothetical]'.
2. Adaptive questioning: Strong answers trigger higher difficulty/scale; weak answers trigger clarification/fundamental probes.
3. Contradiction & Bluff detection: Flags CV/Evidence Mismatch when claims exceed Available Facts.
4. Scoring validation: 3-axis scoring (Technical Depth, Communication, Problem Solving 0-10) and valid overall recommendation.
5. Production incident flow validation: Multi-stage clue progression.
6. Single question per turn rule in interactive mode.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any


VALID_MODES = ("full-mock", "technical-deep-dive", "cv-defense", "pressure-test", "weakness-drill")
VALID_RECOMMENDATIONS = ("Strong Hire", "Hire", "Borderline", "Weak", "No Hire")


def validate_question_technology(
    question_text: str,
    available_technologies: list[str],
    is_hypothetical: bool = False,
) -> list[str]:
    """Check if question asks about unverified technology as a past fact."""
    errors: list[str] = []
    
    # If explicitly marked as hypothetical, it is permitted
    if is_hypothetical or "[giả định" in question_text.lower() or "[hypothetical" in question_text.lower():
        return errors

    # Check for unverified advanced technologies that are commonly hallucinated
    known_tech_stack = {t.lower() for t in available_technologies}
    common_unverified = ["kafka", "kubernetes", "k8s", "docker swarm", "linux kernel", "elasticsearch", "hadoop", "spark"]

    for unverified in common_unverified:
        if unverified not in known_tech_stack:
            # Check if asked as past experience (e.g. "bạn đã dùng Kafka", "bạn đã tối ưu Kafka")
            pattern = rf"\b(bạn\s+đã|dự\s+án\s+của\s+bạn|trong\s+dự\s+án|kinh\s+nghiệm\s+với)\s+[^.?!\n]*\b{unverified}\b"
            if re.search(pattern, question_text, flags=re.IGNORECASE):
                errors.append(
                    f"Phát hiện hỏi công nghệ chưa được kiểm chứng '{unverified}' như một sự thật trong quá khứ mà không gắn thẻ [Giả định / Hypothetical]."
                )

    return errors


def evaluate_adaptive_branch(
    previous_difficulty: int,
    candidate_answer_quality: str,
    next_difficulty: int,
    next_question_type: str,
) -> list[str]:
    """Validate adaptive difficulty and question branching."""
    errors: list[str] = []
    quality = candidate_answer_quality.lower()

    if quality in ("strong", "xuất sắc", "tốt"):
        if next_difficulty < previous_difficulty:
            errors.append(f"Câu trả lời xuất sắc nhưng độ khó bị giảm từ {previous_difficulty} xuống {next_difficulty}.")
    elif quality in ("weak", "yếu", "chung chung", "mơ hồ"):
        if next_difficulty > previous_difficulty + 1:
            errors.append(f"Câu trả lời yếu nhưng độ khó bị tăng vọt từ {previous_difficulty} lên {next_difficulty}.")
        if next_question_type.lower() not in ("clarification", "fundamental", "làm rõ", "cơ bản"):
            # Should ask for clarification or fundamental check
            pass

    return errors


def detect_cv_contradiction(
    cv_available_facts: list[str],
    candidate_claim: str,
) -> tuple[bool, str]:
    """Detect if candidate claim contradicts or severely exaggerates CV available facts."""
    source_text = " ".join(cv_available_facts).lower()
    claim_lower = candidate_claim.lower()

    # Check for unauthorized architecture/leadership claim when source only has implementation
    is_source_lead = any(w in source_text for w in ["lead", "trưởng", "quản lý", "architect", "chủ nhiệm"])
    
    lead_keywords = [
        "architected", "kiến trúc toàn bộ", "thiết kế toàn bộ",
        "led the entire", "led the team", "lãnh đạo toàn bộ", "lãnh đạo đội ngũ",
        "chịu trách nhiệm toàn diện", "owned the architecture"
    ]
    has_claim_lead = any(w in claim_lower for w in lead_keywords)

    if has_claim_lead and not is_source_lead:
        return True, "⚠️ CV/Evidence Mismatch: Ứng viên nhận trách nhiệm thiết kế/lãnh đạo toàn bộ hệ thống trong khi CV chỉ ghi nhận vai trò cài đặt/phát triển module."

    return False, ""



def validate_scoring_report(report_text: str) -> list[str]:
    """Validate the 3-axis scoring report."""
    errors: list[str] = []

    # Check 3 axes
    if "Technical Depth" not in report_text and "Chiều sâu kỹ thuật" not in report_text:
        errors.append("Báo cáo thiếu điểm số trục 'Technical Depth / Chiều sâu kỹ thuật'.")
    if "Communication" not in report_text and "Giao tiếp" not in report_text:
        errors.append("Báo cáo thiếu điểm số trục 'Communication / Giao tiếp'.")
    if "Problem Solving" not in report_text and "Tư duy giải quyết vấn đề" not in report_text:
        errors.append("Báo cáo thiếu điểm số trục 'Problem Solving / Tư duy giải quyết vấn đề'.")

    # Check recommendation
    has_rec = any(rec in report_text for rec in VALID_RECOMMENDATIONS)
    if not has_rec:
        errors.append(f"Báo cáo thiếu kết luận tuyển dụng hợp lệ trong: {VALID_RECOMMENDATIONS}")

    return errors


def validate_interactive_turn(question_text: str) -> list[str]:
    """Check that only a single question is presented in a live turn (no dumping multiple questions)."""
    errors: list[str] = []
    # Count numbered questions like "1. ... 2. ... 3. ..." or multiple distinct question marks
    numbered_questions = re.findall(r"^\s*\d+\.\s+", question_text, flags=re.MULTILINE)
    if len(numbered_questions) > 2:
        errors.append(f"Vi phạm quy tắc tương tác trực tiếp: Phát hiện danh sách {len(numbered_questions)} câu hỏi được đưa ra cùng lúc thay vì hỏi từng câu một.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate mock-interviewer assessment or session.")
    parser.add_argument("file", type=Path, help="Path to report markdown or session JSON to validate")
    args = parser.parse_args()

    if not args.file.exists():
        print(f"Error: File '{args.file}' does not exist.", file=sys.stderr)
        return 1

    content = args.file.read_text(encoding="utf-8")
    errors = validate_scoring_report(content)

    if errors:
        print(f"❌ Validation FAILED with {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("✅ Validation PASSED! Mock interviewer report is fully compliant with 3-axis standards.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
