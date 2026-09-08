# Quy Tắc Thiết Kế Web CV & Portfolio Cá Nhân (RULE KEEP - OUTPUT ALWAYS = VN)

Quy tắc này áp dụng cho mọi tác vụ thiết kế, xây dựng, chỉnh sửa giao diện Web CV, trang Portfolio cá nhân, trang Showcase dự án và tối ưu hóa in ấn (Print CSS) trong workspace này.

---

## 1. BẮT BUỘC XUẤT TIẾNG VIỆT (OUTPUT ALWAYS = VN)
- Mọi hướng dẫn, phân tích bố cục, giải thích mã nguồn và khuyến nghị cải tiến giao diện **LUÔN LUÔN PHẢI ĐƯỢC VIẾT BẰNG TIẾNG VIỆT**.
- Các thuộc tính CSS, thẻ HTML và thuật ngữ thiết kế kỹ thuật (như Typography, Responsive, Breakpoint, Print Media, Line-height, Box-shadow...) được giữ nguyên dạng tiếng Anh chuẩn.

---

## 2. Tiêu Chuẩn Thẩm Mỹ & Visual Hierarchy (Design Aesthetics)
- **Bảng màu cao cấp (Curated Color Palette):**
  - Màu chủ đạo (Primary): Navy đậm quyền lực (`#0F2747`) cho họ tên và tiêu đề các Section.
  - Màu điểm nhấn (Accent): Blue công nghệ (`#2563EB`) cho chức danh, liên kết GitHub/Email và icon.
  - Màu chữ nội dung (Text Main): Dark Slate/Navy dịu mắt (`#172033` hoặc `#1E293B`), độ tương phản cao, chống mỏi mắt.
  - Màu phụ (Muted Text): Xám trung tính (`#64748B`) cho timeline, địa chỉ và chú thích.
  - Đường kẻ phân cách (Divider): Light Gray (`#CBD5E1`), thanh mảnh (1.2px – 1.4px).
- **Typography hiện đại:**
  - Bắt buộc dùng font sans-serif chuẩn quốc tế (ưu tiên Google Fonts: `'Inter'`, `Roboto`, `-apple-system`, `sans-serif`).
  - Letter-spacing vi mô `-0.01em` để chữ gom gọn, sang trọng.
  - Tuyệt đối không dùng font mặc định lỗi thời (Times New Roman, Arial cơ bản) cho Web CV.

---

## 3. Quy Chuẩn In Ấn Chuẩn A4 Không Rớt Trang (Zero-Overflow Print Engine)
Khi chuyển đổi từ Web sang PDF (In ấn qua `Ctrl + P` hoặc Save as PDF), BẮT BUỘC tuân thủ công thức tính dung lượng A4:
- **Kích thước khổ giấy:** `size: A4 portrait;` (210mm x 297mm).
- **Căn lề trang in (@page):**
  - Top/Bottom: `6mm – 8mm`.
  - Left/Right: `10mm – 12mm`.
- **Tỷ lệ kích thước chữ & giãn dòng:**
  - Body font-size: `11.0px – 11.8px`.
  - Line-height: `1.36 – 1.42`.
  - Section title: `11.8px – 12.5px`, `margin-top: 8px – 10px`, `margin-bottom: 3.5px – 4.5px`.
  - Bullet lists: `margin-bottom: 1.4px – 1.8px`, padding lùi `11px – 12px`.
- **Nguyên tắc lấp đầy trang (Fill Budgeting):**
  - Nội dung phải trải đều và lấp đầy **90% – 95%** chiều cao trang A4, tuyệt đối không để khoảng trống trắng mênh mông ở đáy trang.
  - Đồng thời kiểm soát chặt chẽ để không một dòng nào bị rơi sang trang thứ 2 (`page-break-inside: avoid`).

---

## 4. Cấu Trúc Khối Nội Dung Chuẩn Tech (Single Page Architecture)
Một trang Web CV đạt chuẩn Senior phải sắp xếp theo thứ tự tối ưu trải nghiệm đọc 5 giây của Recruiter:
1. **Header:** Họ tên viết hoa đậm nét, chức danh mục tiêu rõ ràng (`EMBEDDED C/C++ & IOT ENGINEER`, `BACKEND DEVELOPER INTERN`...), thông tin liên hệ đầy đủ (SĐT, Email, GitHub link, Địa chỉ).
2. **Professional Summary:** 3–4 dòng đĩnh đạc, nêu đúng thực lực cốt lõi, không viết sáo rỗng.
3. **Technical Skills:** Phân nhóm 5–7 danh mục chuyên nghiệp (Programming, Embedded/Backend, Interfaces/Hardware, Networking, Tools, AI-Assisted Dev).
4. **Education:** Trường, ngành học, GPA, danh hiệu tốt nghiệp và các môn cốt lõi.
5. **Professional Experience:** Tên công ty, chức danh, mốc thời gian, 3–4 bullets hành động có chiều sâu kỹ thuật.
6. **Selected Projects:** 3–4 dự án nổi bật nhất kèm link GitHub, bảng công nghệ sử dụng và các chỉ số đo lường thực tế (Metrics).

---

## 5. Tương Thích Kép (Dual-Mode: Web Showcase + Print Ready)
- **Chế độ xem màn hình (Screen View):**
  - Bao bọc trong container `.page` có nền trắng (`#FFFFFF`), đổ bóng nhẹ (`box-shadow: 0 10px 25px -5px rgba(0,0,0,0.04)`), bo góc nhẹ (`border-radius: 4px`) đặt trên nền xám sáng (`#F8FAFC`) để người dùng xem trực quan trên Live Server hoặc trình duyệt.
- **Chế độ in ấn (@media print):**
  - Tự động ẩn nền body, bỏ box-shadow, đưa margin trang về 0, mở rộng width 100% để máy in hoặc tính năng Save as PDF bắt trọn khổ giấy A4 hoàn hảo.
  - Kích hoạt thuộc tính `-webkit-print-color-adjust: exact; print-color-adjust: exact;` để giữ nguyên màu sắc chữ và đường kẻ.

---

## 6. Kết Luận Bắt Buộc
Mọi phân tích hay đề xuất chỉnh sửa liên quan đến Web CV đều phải kết thúc bằng dòng:
`> Kết quả chỉ mang tính tham khảo, cần được chỉnh sửa thủ công`
