---
name: web-portfolio-builder
description: Chuyên gia thiết kế, xây dựng và tối ưu hóa Web CV / Trang Portfolio cá nhân tương tác cao từ dữ liệu cache JSON. Tự động căn chỉnh bố cục in ấn A4 chuẩn mực không rớt trang (Zero-Overflow Print Engine), tích hợp showcase dự án GitHub kèm metrics thực chiến, xuất bản mã nguồn HTML/CSS/JS thuần hiện đại và hỗ trợ triển khai nhanh lên GitHub Pages / Vercel.
---

# web-portfolio-builder (Kiến Trúc Sư Web CV & Portfolio Cá Nhân)

Kỹ năng này chuyên trách chuyển hóa hồ sơ dữ liệu thô hoặc dữ liệu đã thẩm định từ `cache/cv_profile.json` thành các sản phẩm Web CV / Portfolio cá nhân trực quan, thẩm mỹ cao và chuẩn mực in ấn A4.

**QUY TẮC BẮT BUỘC: TOÀN BỘ KẾT QUẢ VÀ HƯỚNG DẪN PHẢI XUẤT BẰNG TIẾNG VIỆT (OUTPUT ALWAYS = VN).**

---

## 1. Nguồn Dữ Liệu & Quy Trình Khép Kín

1. **Đọc Cache Dữ Liệu (`cache/cv_profile.json`):**
   - Trích xuất thông tin cá nhân, học vấn (GPA, học bổng).
   - Nạp các kỹ năng kỹ thuật đã phân nhóm.
   - Nạp kinh nghiệm thực tập và các dự án đã gắn nhãn vai trò (`Trụ cột`, `Bằng chứng`, `Bổ sung`) kèm theo các số liệu đo lường thực tế (Metrics).
2. **Đối Chiếu Tiêu Chuẩn Thiết Kế:**
   - Tuân thủ nghiêm ngặt quy tắc tại [.agents/rules/web-cv-design.md](../../rules/web-cv-design.md).
   - Sử dụng bảng màu cao cấp: Navy `#0F2747` (chủ đạo) + Accent Blue `#2563EB` (công nghệ) + Dark Slate `#172033` (nội dung).

---

## 2. Hai Kiến Trúc Trang Web Hỗ Trợ

### Loại 1: Single-Page Executive A4 (Web CV In Ấn & Xem Trực Tuyến)
* **Mục đích:** Vừa xem đẹp mắt trên trình duyệt (Live Server, GitHub Pages), vừa in hoặc xuất PDF chuẩn khít đúng **1 trang A4 duy nhất**.
* **Đặc điểm kỹ thuật:**
  - Bố cục container `.page` giới hạn `max-width: 840px`, nền trắng `#FFFFFF`, bóng mờ tinh tế.
  - Sử dụng CSS `@media print` và `@page` với lề `7mm 11mm 6mm 11mm`.
  - Kiểm soát chiều cao để nội dung chiếm **90% – 95%** chiều cao trang, không rớt dòng sang trang 2.

### Loại 2: Interactive Tech Portfolio (Trang Web Trình Diễn Tương Tác)
* **Mục đích:** Tạo website cá nhân độc lập để ứng viên gửi đường link trực tiếp cho nhà tuyển dụng xem chi tiết demo, video và mã nguồn.
* **Đặc điểm kỹ thuật:**
  - Tích hợp điều hướng mượt mà (Smooth Scroll), các tab lọc dự án (Embedded / IoT / Backend / AI).
  - Tích hợp Modal xem nhanh kiến trúc hệ thống (Mermaid Diagram / System Architecture).
  - Hỗ trợ Dark Mode / Light Mode chuyển đổi mượt mà.

---

## 3. Công Thức Tính Toán Dung Lượng Trang A4 (A4 Dimension Budgeting)

Để đảm bảo CV chứa đầy đủ 1 Kinh nghiệm thực tế + 4 Dự án + 6–7 dòng Skills mà vẫn **vừa khít 1 trang A4**:

| Phần Tử Giao Diện | Cấu Hình Màn Hình (Screen) | Cấu Hình Bản In (@media print) | Ghi Chú Kỹ Thuật |
| :--- | :--- | :--- | :--- |
| **Body Font Size** | `11.6px – 11.8px` | `11.0px – 11.2px` | Đảm bảo chữ to, sắc nét, dễ đọc |
| **Line Height** | `1.40 – 1.42` | `1.34 – 1.37` | Giãn dòng thoáng mắt |
| **Section Margin Top** | `9px – 11px` | `6.5px – 7.5px` | Nhịp ngắt giữa các khối |
| **Bullet Margin Bottom**| `1.5px – 1.8px` | `1.2px – 1.4px` | Không quá dính, không quá thưa |
| **Item Container Margin**| `6.5px – 7.5px` | `4.5px – 5.2px` | Khoảng cách giữa các dự án |
| **Page Padding** | `34px 42px` | `0` (quản lý qua `@page margin`) | Tránh chừa đáy trắng mênh mông |

---

## 4. Quy Trình Triển Khai Nhanh Lên GitHub Pages (Free Hosting)

Khi người dùng muốn đưa Web CV hoặc Portfolio lên mạng internet để gửi kèm trong Email xin việc:

1. **Khởi tạo file web chính:** Đặt tên là `index.html` tại thư mục gốc hoặc thư mục docs.
2. **Kích hoạt GitHub Pages:**
   - Vào mục **Settings** của repository trên GitHub.
   - Chọn tab **Pages** -> Tại mục **Source**, chọn nhánh `main` và thư mục `/(root)`.
   - Bấm **Save**.
3. **Đường link kết quả:**
   - Trang web sẽ hiển thị trực tiếp tại địa chỉ: `https://<username>.github.io/<repo-name>/`
   - Đính kèm trực tiếp đường link này vào phần Header của CV và nội dung Email ứng tuyển.

---

## 5. Danh Mục Kiểm Tra Chất Lượng (Quality Checklist)

Trước khi bàn giao mã nguồn Web CV/Site cho người dùng:
- [ ] Font chữ sử dụng Inter từ Google Fonts, không dùng font hệ thống mặc định.
- [ ] Tất cả icon liên hệ (Phone, Location, GitHub, Email) sử dụng SVG đồng bộ kích thước (11.5px).
- [ ] Tất cả liên kết ngoài (GitHub, Email) có thuộc tính `target="_blank"` và hiển thị trạng thái `:hover`.
- [ ] Nhãn kỹ năng `.skill-group-name` có độ rộng cố định (`width: 175px – 180px`) không bị gãy dòng.
- [ ] Thử nghiệm `Ctrl + P`: Kiểm tra trang in A4 xem có bị tràn sang trang thứ 2 hay không.
- [ ] Kết thúc bằng dòng khuyến cáo bắt buộc:
  `> Kết quả chỉ mang tính tham khảo, cần được chỉnh sửa thủ công`
