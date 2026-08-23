---
name: cv-reviewer
description: Đánh giá và định hướng cấu trúc CV tiếng Việt/tiếng Anh theo mục tiêu nghề nghiệp, lộ trình phát triển, dung lượng kinh nghiệm, ngôn ngữ ngành, khả năng đọc hiểu trong 5 giây đầu của HR và giá trị đào sâu khi phỏng vấn. Tự động xuất báo cáo 100% bằng tiếng Việt, lưu trữ cache hồ sơ JSON (cache/cv_profile.json, cache/job_profile.json) và tạo gói bàn giao tinh chỉnh trải nghiệm (handoff packet) cho cv-experience-refinement.
---

# cv-reviewer (Đánh giá CV & Định tuyến Hồ sơ)

Đầu tiên, hãy xác định ứng viên đang ở giai đoạn nào (`Khởi đầu / Tăng trưởng / Bứt phá` - `Entry-level / Growth / Sprint`) và trạng thái tư liệu ra sao (`Quá ít / Vừa phải / Quá nhiều` & `Đơn điệu / Vừa phải / Phong phú / Hỗn hợp`), sau đó mới quyết định CV cần mở rộng, tinh gọn, tái cấu trúc hay loại bỏ trùng lặp. Tuyệt đối không áp đặt một khuôn mẫu cứng nhắc cho tất cả ứng viên.

**QUY TẮC BẮT BUỘC: TOÀN BỘ KẾT QUẢ ĐÁNH GIÁ PHẢI XUẤT BẰNG TIẾNG VIỆT (OUTPUT ALWAYS = VN).**

## 1. Đọc Tài Liệu Tham Khảo (References)

1. Luôn đọc kỹ [references/methodology.md](references/methodology.md) để nắm phương pháp luận.
2. Luôn đọc kỹ [references/candidate-routing.md](references/candidate-routing.md) để phân loại cấp độ ứng viên và mật độ hồ sơ.
3. Luôn đọc kỹ [references/audit-rubric.md](references/audit-rubric.md) để chấm điểm theo thang đo tương ứng.
4. Lựa chọn bộ thuật ngữ ngành phù hợp:
   - Kinh doanh, Marketing, Sales, Chiến lược, Tài chính, HR, Content: [references/lexicon-business.md](references/lexicon-business.md)
   - Product, UX Research, Data, AI, Kỹ thuật/Lập trình, Thiết kế: [references/lexicon-product-tech.md](references/lexicon-product-tech.md)
   - Vận hành dự án, Chuỗi cung ứng, Sản xuất, Giáo dục, Y tế, Luật: [references/lexicon-sector.md](references/lexicon-sector.md)
5. Tham khảo cấu trúc Cache JSON tại [references/cache-schema.md](references/cache-schema.md).
6. Trước khi xuất báo cáo, đọc kỹ mẫu chuẩn tại [references/output-template.md](references/output-template.md).

Khi chuyển ngành: đối chiếu bộ thuật ngữ giữa ngành xuất phát và vị trí mục tiêu để thiết lập bảng ánh xạ năng lực chuyển đổi (transferable skills).

## 2. Đầu Vào & Cơ Chế Cache JSON

### Kiểm tra Cache trước khi xử lý (Pre-check Cache)
- Kiểm tra thư mục `cache/`:
  - Nếu đã có `cache/cv_profile.json` và người dùng chỉ gửi JD mới → Tự động nạp dữ liệu CV từ cache để so khớp với JD mới mà không bắt người dùng gửi lại CV.
  - Nếu đã có `cache/job_profile.json` và người dùng gửi bản CV mới → Nạp yêu cầu JD từ cache để đánh giá bản CV mới.
- Khi có mâu thuẫn thông tin, ưu tiên theo thứ tự:
  `Yêu cầu trực tiếp của người dùng trong phiên -> Dữ liệu sự thật đã kiểm chứng -> Bản CV hiện tại -> Yêu cầu JD -> Dữ liệu Cache cũ -> Bản nháp gợi ý`

Lập thẻ kinh nghiệm nội bộ cho từng mục:
`Bối cảnh/Vấn đề ｜ Đối tượng/Khách hàng ｜ Phạm vi trách nhiệm ｜ Rào cản/Khó khăn ｜ Hành động ｜ Bộ công cụ/Phương pháp ｜ Bàn giao ｜ Kết quả/Xác thực bên ngoài ｜ Điểm đào sâu (Hook) ｜ Độ khớp JD mục tiêu`

## 3. Bước 1: Định Tuyến 2 Trục (Double-Axis Routing)

### Cấp độ ứng viên (Candidate Tier)
- `Khởi đầu (Entry-level)`: Ít kinh nghiệm chính thức; dựa vào đồ án trường học, khóa học, dự án cá nhân, kỹ năng chuyển đổi.
- `Tăng trưởng (Growth)`: Đã có nhiều kinh nghiệm; thể hiện rõ đà mở rộng phạm vi trách nhiệm, độ khó bài toán và chiều sâu chuyên môn.
- `Bứt phá (Sprint / High-impact)`: Nhiều kinh nghiệm nặng ký, cạnh tranh vào vị trí cao/chuẩn khắt khe; cần tối ưu hóa độ khớp JD và loại bỏ trùng lặp.

### Mật độ tài liệu (Material Density)
- Tổng lượng kinh nghiệm: `Quá ít` / `Vừa phải` / `Quá nhiều`
- Mật độ từng đoạn: `Đơn điệu (mỏng)` / `Vừa phải` / `Phong phú (dày)` / `Hỗn hợp`

## 4. Bước 2: Xác Định Trục Tự Sự & Bằng Chứng

- **Khởi đầu (Entry-level)**: Thiết lập chuỗi bằng chứng ngắn nhất: `Đam mê/Phẩm chất -> Hành động chủ động -> Dự án/Sản phẩm/Phản hồi -> Vị trí tiếp theo`. Không viết CV như một bản liệt kê thiếu sót.
- **Tăng trưởng (Growth)**: Xác định trục phát triển: độ phức tạp của bài toán, phạm vi quản lý, đối tác cộng tác, kết quả tăng dần qua từng giai đoạn.
- **Bứt phá (Sprint)**: Xuất phát từ bài toán nghiệp vụ trọng tâm của JD, chọn lọc 3–5 trải nghiệm đắt giá nhất, sử dụng cấu trúc 2 tầng "Tổng — Phân".

## 5. Bước 3: Phân Bổ Dung Lượng & Vai Trò Kinh Nghiệm

Gán nhãn rõ ràng cho từng đoạn kinh nghiệm:
- `Trụ cột (Pillar)`: Nhắm trúng vấn đề trọng yếu của JD, viết chi tiết nhất.
- `Bằng chứng (Proof)`: Chứng minh thêm năng lực quan trọng khác hoặc mốc bước ngoặt.
- `Bổ sung (Supplement)`: Giữ 1 dòng ngắn gọn để tạo độ phủ nền tảng.
- `Xóa bỏ (Delete)`: Loại bỏ các mục trùng lặp, tín hiệu yếu hoặc gây loãng thông tin.

## 6. Bước 4: Viết Theo Tiêu Chuẩn Nghiệp Vụ & Điểm Nhấn Cá Nhân

- **Cấu trúc nghiệp vụ khép kín**: `Vấn đề/Tiền đề -> Bộ công cụ/Phương pháp & Hành động -> Kết quả/Tác động`.
- **Động từ chính xác**: Phân biệt rõ giữa *tìm hiểu, sử dụng, cấu hình, phân tích, thiết kế, phát triển, triển khai, dẫn dắt, tối ưu hóa*.
- **Điểm nhấn cá nhân (Anchor)**: Phải gắn liền với bài toán của công việc, có hành động/sản phẩm thực tế chứng minh, không dùng từ sáo rỗng (như "chăm chỉ, nhiệt huyết, hòa đồng").

## 7. Bước 5: Thiết Lập Điểm Đào Sâu Phỏng Vấn (Interview Hook)

Mỗi trải nghiệm trụ cột cần chuẩn bị 1–2 điểm đào sâu (Hook) giúp phỏng vấn viên dễ dàng đặt câu hỏi thú vị:
- Đánh đổi kỹ thuật/nghiệp vụ quan trọng.
- Xử lý xung đột liên phòng ban.
- Khắc phục sự cố/thất bại và điều chỉnh sau đó.
- Insight nghiệp vụ sâu sắc mà ứng viên rút ra được.

## 8. Bước 6: Tạo Gói Bàn Giao Tinh Chỉnh & Cập Nhật Cache JSON

- Báo cáo bắt buộc có mục `Kết nối cv-experience-refinement` với các chế độ `final`, `enhanced-draft`, `incomplete`.
- Tách bạch giữa "Sự thật khả dụng" (Available facts) và "Cần xác nhận / Cấm tự ý bổ sung" (To confirm / Forbidden to assume).
- **Cập nhật Cache JSON**: Tự động lưu/cập nhật thông tin phân tích vào `cache/cv_profile.json` và `cache/job_profile.json` theo đúng cấu trúc tại [references/cache-schema.md](references/cache-schema.md).

## 9. Định Dạng Đầu Ra & Kiểm Tra

- Báo cáo phải tuân thủ nghiêm ngặt mẫu trong [references/output-template.md](references/output-template.md).
- Toàn bộ nội dung báo cáo **BẮT BUỘC BẰNG TIẾNG VIỆT**.
- Dòng cuối cùng của báo cáo luôn là:

`> Kết quả chỉ mang tính tham khảo, cần được chỉnh sửa thủ công`
