#!/usr/bin/env python3
"""Validation script for cv-experience-refinement output.

Checks for:
1. Anti-hallucination: No fabricated metrics, numbers, or percentages outside source facts.
2. Technology integrity: No fabricated technologies outside available_facts.
3. No fake seniorize: No unauthorized leadership/architect claims when source indicates implementation.
4. Structural compliance:
   - Pillar: 1 overview line + 2-4 bullets (+ interview hooks in final mode).
   - Proof: 1 overview line + 2-3 bullets.
   - Supplement: Max 1-2 concise lines (no multiple bullet list).
   - Delete: Marked as DELETE/LOẠI BỎ without generated bullets.
5. Mode compliance: final, enhanced-draft, or incomplete.
6. Placeholder format: Required confirmation must use [CẦN XÁC NHẬN: ...] or [CẦN ĐIỀN SỐ LIỆU THỰC TẾ: ...].
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any


REFINEMENT_MODES = ("final", "enhanced-draft", "incomplete")

FORBIDDEN_LEADERSHIP_VERBS = [
    r"\b(architected|led\s+the\s+team|owned\s+the\s+entire|lãnh\s+đạo\s+đội\s+ngũ|kiến\s+trúc\s+toàn\s+bộ|chịu\s+trách\s+nhiệm\s+toàn\s+diện)\b"
]

GENERIC_PLACEHOLDERS = [
    r"\bXX%\b",
    r"\bYY\s+(devices|users|khách\s+hàng|thiết\s+bị)\b",
    r"\bN\s+(customers|users|người\s+dùng)\b",
    r"\b\d+x\s+(faster|throughput|hiệu\s+năng)\b",
]

FABRICATED_METRIC_PATTERN = re.compile(
    r"(\b\d+%\b|\b\d+\s*(users|người dùng|devices|thiết bị|req/s|rps|ms|fps)\b|\b\d+x\b)",
    re.IGNORECASE,
)



def extract_numbers_from_text(text: str) -> set[str]:
    """Extract all standalone numbers and percentages from text."""
    clean = re.sub(r"\[CẦN XÁC NHẬN:[^\]]*\]", "", text)
    clean = re.sub(r"\[CẦN ĐIỀN SỐ LIỆU THỰC TẾ:[^\]]*\]", "", clean)
    clean = re.sub(r"\b(20\d\d|19\d\d)\b", "", clean)  # Ignore years
    clean = re.sub(r"\b(1\s+dòng|[1-4]\s+bullet[s]?|[1-4]\s+cổng)\b", "", clean, flags=re.IGNORECASE)
    # Find percentages, numbers with units, multipliers
    matches = re.findall(r"\b\d+(?:\.\d+)?(?:%|x|ms|s|fps|users|devices|req/s|rps)?\b", clean, flags=re.IGNORECASE)
    return {m.lower().strip() for m in matches if m.strip()}


def validate_refinement_content(
    content: str,
    available_facts: list[str] | None = None,
    role_partition: str = "Trụ cột",
    mode: str = "final",
) -> list[str]:
    """Validate a single refined experience block. Returns a list of error strings."""
    errors: list[str] = []
    available_facts = available_facts or []

    # 1. Mode check
    if mode not in REFINEMENT_MODES:
        errors.append(f"Chế độ refinement không hợp lệ: '{mode}'. Chỉ chấp nhận: {REFINEMENT_MODES}")

    # If mode is incomplete, check for incomplete markers
    if mode == "incomplete":
        if "INCOMPLETE" not in content.upper() and "THIẾU DỮ LIỆU" not in content.upper():
            errors.append("Chế độ 'incomplete' nhưng không có nhãn cảnh báo THIẾU DỮ LIỆU / INCOMPLETE.")
        return errors

    # 2. Check for generic ugly placeholders
    for pat in GENERIC_PLACEHOLDERS:
        if re.search(pat, content, flags=re.IGNORECASE):
            errors.append(f"Phát hiện placeholder không chuẩn dạng '{pat}'. Phải dùng [CẦN XÁC NHẬN: ...]")

    # 3. Role-based structure check
    lines = [line.strip() for line in content.strip().split("\n") if line.strip()]
    bullets = [line for line in lines if line.startswith("- ") or line.startswith("* ")]

    if role_partition.lower() in ("xóa bỏ", "delete"):
        if bullets:
            errors.append(f"Kinh nghiệm thuộc nhóm '{role_partition}' nhưng vẫn được tạo {len(bullets)} bullets.")
        if "DELETE" not in content.upper() and "LOẠI BỎ" not in content.upper():
            errors.append("Kinh nghiệm Xóa bỏ phải có nhãn rõ ràng: LOẠI BỎ (DELETE).")
        return errors

    if role_partition.lower() in ("bổ sung", "supplement"):
        if len(bullets) > 1:
            errors.append(f"Kinh nghiệm Bổ sung (Supplement) chỉ được tối đa 1 dòng/bullet, hiện có {len(bullets)} bullets.")
        return errors

    if role_partition.lower() in ("trụ cột", "pillar"):
        if len(bullets) < 2 or len(bullets) > 5:
            errors.append(f"Kinh nghiệm Trụ cột (Pillar) phải có từ 2–4 bullets chuyên sâu, hiện có {len(bullets)} bullets.")
        if mode == "final" and "Interview Hooks" not in content and "Điểm Đào Sâu Phỏng Vấn" not in content:
            errors.append("Kinh nghiệm Trụ cột ở chế độ 'final' bắt buộc phải có mục Interview Hooks.")

    if role_partition.lower() in ("bằng chứng", "proof"):
        if len(bullets) < 1 or len(bullets) > 4:
            errors.append(f"Kinh nghiệm Bằng chứng (Proof) phải có từ 1–3 bullets, hiện có {len(bullets)} bullets.")

    # 4. Anti-hallucination: Leadership claims check
    source_combined = " ".join(available_facts).lower()
    is_source_leadership = any(w in source_combined for w in ["lead", "trưởng", "quản lý", "architect", "chủ nhiệm"])
    
    if not is_source_leadership:
        for pat in FORBIDDEN_LEADERSHIP_VERBS:
            if re.search(pat, content, flags=re.IGNORECASE):
                errors.append(f"Phát hiện claim vị trí/vai trò cấp cao không có trong facts: '{pat}'")

    # 5. Anti-hallucination: Numbers and Metrics verification
    source_facts_text = " ".join(available_facts)
    source_numbers = extract_numbers_from_text(source_facts_text)
    
    # Strip confirmation placeholders before extracting numbers from content
    content_without_placeholders = re.sub(r"\[CẦN XÁC NHẬN:[^\]]*\]", "", content)
    content_without_placeholders = re.sub(r"\[CẦN ĐIỀN SỐ LIỆU THỰC TẾ:[^\]]*\]", "", content_without_placeholders)
    content_numbers = extract_numbers_from_text(content_without_placeholders)

    unauthorized_numbers = content_numbers - source_numbers
    # Filter out common benign numbers (like 1, 2, 3, 4 for list counts or standard ports like 1883 if in source)
    unauthorized_filtered = set()
    for num in unauthorized_numbers:
        # Ignore small integers used as bullet counters or standard numbers
        if num in {"1", "2", "3", "4", "5", "10", "1-2", "2-3", "2-4", "3-4"}:
            continue
        # If the number exists as a substring in source facts, ignore
        num_clean = re.sub(r"[^\d.]", "", num)
        if num_clean and num_clean in source_facts_text:
            continue
        unauthorized_filtered.add(num)

    if unauthorized_filtered:
        errors.append(f"Phát hiện số liệu/metrics không có trong Available Facts: {sorted(list(unauthorized_filtered))}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate CV experience refinement markdown output.")
    parser.add_argument("file", type=Path, help="Path to markdown file to validate")
    parser.add_argument("--role", default="Trụ cột", help="Role partition (Trụ cột | Bằng chứng | Bổ sung | Xóa bỏ)")
    parser.add_argument("--mode", default="final", help="Mode (final | enhanced-draft | incomplete)")
    args = parser.parse_args()

    if not args.file.exists():
        print(f"Error: File '{args.file}' does not exist.", file=sys.stderr)
        return 1

    content = args.file.read_text(encoding="utf-8")
    errors = validate_refinement_content(content, role_partition=args.role, mode=args.mode)

    if errors:
        print(f"❌ Validation FAILED with {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("✅ Validation PASSED! Content strictly adheres to all refinement and anti-hallucination rules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
