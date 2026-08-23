#!/usr/bin/env python3
"""Check tier coverage, density routing, lexicon breadth, cache schema, and source anonymization."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def require(text: str, phrases: tuple[str, ...], label: str) -> None:
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, f"{label} missing: {missing}"


def main() -> int:
    skill = read("SKILL.md")
    routing = read("references/candidate-routing.md")
    method = read("references/methodology.md")
    output = read("references/output-template.md")
    cache_schema = read("references/cache-schema.md")
    lexicons = "\n".join(
        [
            read("references/lexicon-business.md"),
            read("references/lexicon-product-tech.md"),
            read("references/lexicon-sector.md"),
        ]
    )
    package_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix in {".md", ".py", ".json"}
    )

    require(skill + routing, ("Khởi đầu", "Tăng trưởng", "Bứt phá"), "candidate tiers")
    require(skill + routing, ("Quá ít + Đơn điệu", "Quá ít + Phong phú", "Quá nhiều + Đơn điệu", "Quá nhiều + Phong phú", "Hỗn hợp"), "material routing")
    require(method + skill, ("Vấn đề", "Bộ công cụ", "Kết quả", "Tổng — Phân", "Điểm nhấn cá nhân", "Hook"), "methodology")
    require(
        skill + output,
        (
            "cv-experience-refinement",
            "Trụ cột",
            "Bằng chứng",
            "Bổ sung",
            "Xóa bỏ",
            "final",
            "enhanced-draft",
            "incomplete",
            "Sự thật khả dụng",
            "Cần xác nhận / Cấm tự ý bổ sung",
            "Câu lệnh gọi mẫu",
        ),
        "experience refinement handoff",
    )
    require(
        cache_schema,
        (
            "cache/cv_profile.json",
            "cache/job_profile.json",
            "candidate_tier",
            "available_facts",
            "must_have",
            "nice_to_have",
            "target_lexicon",
        ),
        "cache schema fields",
    )
    require(
        lexicons,
        (
            "Marketing, Thương Hiệu, Tăng Trưởng & Nội Dung",
            "Bán Hàng, Phát Triển Kinh Doanh & Quản Trị Khách Hàng",
            "Chiến Lược, Tư Vấn, Phân Tích Kinh Doanh & Tài Chính",
            "Quản Trị Sản Phẩm & Vận Hành Sản Phẩm",
            "Phân Tích Dữ Liệu, Khoa Học Dữ Liệu & Thử Nghiệm",
            "Trí Tuệ Nhân Tạo & Ứng Dụng Thông Minh",
            "Chuỗi Cung Ứng, Sản Xuất & Kiểm Soát Chất Lượng",
            "Giáo Dục, Đào Tạo & Thiết Kế Trải Nghiệm Học Tập",
            "Y Tế, Dược Phẩm & Khoa Học Đời Sống",
            "Pháp Lý, Tuân Thủ, Quản Trị Rủi Ro & Kiểm Toán",
            "Khu Vực Công, Tổ Chức Phi Lợi Nhuận & Phát Triển Quốc Tế",
        ),
        "industry lexicons",
    )

    forbidden = (
        "Ka" + "ze",
        "ME" + "XC",
        "Ku" + "Coin",
        "LX" + "DAO",
        "TEAM" + "AKING",
        "Jay" + "den",
    )
    leaked = [marker for marker in forbidden if marker.lower() in package_text.lower()]
    assert not leaked, f"candidate-specific traces found: {leaked}"

    print("OK: tier, density, lexicon, refinement handoff, cache schema, and methodology passed (Vietnamese & English)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
