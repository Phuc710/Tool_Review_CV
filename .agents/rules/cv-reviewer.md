# Quy tắc Đánh giá CV & Tinh chỉnh Kinh nghiệm (RULE KEEP - OUTPUT ALWAYS = VN)

Khi thực hiện nhiệm vụ review CV, thẩm định hồ sơ ứng viên, tối ưu hóa kinh nghiệm hoặc tư vấn nghề nghiệp, BẮT BUỘC tuân thủ các nguyên tắc sau:

## 1. BẮT BUỘC XUẤT TIẾNG VIỆT (OUTPUT ALWAYS = VN)
- Mọi nội dung phản hồi, báo cáo đánh giá, phân tích lỗi P0/P1/P2, bảng phân loại kinh nghiệm, khuyến nghị sửa đổi và gói bàn giao (handoff packet) **LUÔN LUÔN PHẢI ĐƯỢC VIẾT BẰNG TIẾNG VIỆT**.
- Ngôn từ diễn đạt phải tự nhiên, chuyên nghiệp, phù hợp với văn hóa tuyển dụng tại Việt Nam.

## 2. Bảo Toàn Sự Thật & Chống Bịa Đặt (KEEP FACTS)
- **Không tự bịa**: Tuyệt đối không thêm thắt kinh nghiệm làm việc, tên công ty, chức danh, mốc thời gian làm việc, công nghệ hay các chỉ số kết quả mà ứng viên chưa từng đề cập.
- **Phân tách ranh giới rõ ràng**:
  1. **Sự thật khả dụng (Available Facts)**: Thông tin đã được kiểm chứng trực tiếp từ CV hoặc ghi chú của ứng viên.
  2. **Cần xác nhận / Cấm tự ý bổ sung (To Confirm / Strictly Forbidden to Assume)**: Các chi tiết suy đoán, con số ước lượng, chức danh đề xuất cần ứng viên duyệt trước.
- **Không gộp dự án chắp vá**: Tuyệt đối không ghép các phần việc của nhiều dự án/công ty khác nhau thành một dự án hư cấu.

## 3. Định Tuyến Ứng Viên 2 Trục (KEEP METHODOLOGY)
Đánh giá ứng viên độc lập theo 2 chiều:
- **Cấp độ ứng viên (Candidate Tier)**:
  - `Khởi đầu (Entry-level)`: Dựa trên đồ án trường, khóa học, dự án cá nhân, kỹ năng chuyển đổi; trả lời câu hỏi "Tại sao xứng đáng có cơ hội đầu tiên?".
  - `Tăng trưởng (Growth)`: Nhiều kinh nghiệm thể hiện rõ đà mở rộng trách nhiệm, năng lực giải quyết vấn đề phức tạp hơn; trả lời "Tại sao lộ trình này dẫn tới vị trí mục tiêu?".
  - `Bứt phá (Sprint / High-impact)`: Nhiều kinh nghiệm giá trị cao; tập trung vào tối ưu hóa mức độ khớp JD, loại bỏ trùng lặp và làm nổi bật tác động nghiệp vụ.
- **Mật độ tài liệu (Material Density)**:
  - Tổng lượng: `Quá ít` / `Vừa phải` / `Quá nhiều`
  - Mật độ từng đoạn: `Đơn điệu (mỏng)` / `Vừa phải` / `Phong phú (dày)` / `Hỗn hợp`

## 4. Phân Bổ Vai Trò Kinh Nghiệm (KEEP PROPORTION)
Gán mỗi kinh nghiệm vào 1 trong 4 nhóm vai trò:
- `Trụ cột (Pillar)`: Nhắm trúng vấn đề trọng tâm của JD; phân bổ dung lượng chi tiết nhất.
- `Bằng chứng (Proof)`: Bổ sung năng lực phụ quan trọng hoặc mốc bước ngoặt phát triển.
- `Bổ sung (Supplement)`: Cung cấp nền tảng, điểm nhấn cá nhân; tóm tắt ngắn gọn 1 dòng.
- `Xóa bỏ (Delete)`: Trùng lặp, lạc đề, tín hiệu yếu; loại bỏ để tránh loãng thông tin.

## 5. Cấu Trúc Vòng Lặp Nghiệp Vụ Đóng Kín
Mỗi đoạn kinh nghiệm giữ lại cần có đầy đủ:
`Bối cảnh/Tiền đề -> Vấn đề & Rào cản -> Bộ công cụ/Phương pháp & Hành động chính -> Kết quả/Bàn giao -> Tác động & Điểm đào sâu phỏng vấn (Interview Hook)`

## 6. Lưu Trữ Cache Dữ Liệu JSON (JSON Persistence)
- Toàn bộ kết quả phân tích CV và phân tích JD được lưu trữ có cấu trúc theo định dạng JSON duy nhất tại thư mục `cache/`:
  - `cache/cv_profile.json`: Hồ sơ ứng viên, sự thật khả dụng, vòng lặp nghiệp vụ từng đoạn.
  - `cache/job_profile.json`: Bài toán của JD, tiêu chí sàng lọc cứng/mềm, từ khóa ngành.
- Ưu tiên đọc dữ liệu từ cache trước khi yêu cầu người dùng gửi lại tài liệu cũ; tự động cập nhật cache sau mỗi lần đánh giá thành công.

## 7. Giao Thức Bàn Giao & Kết Luận
- Báo cáo tuân thủ định dạng chuẩn tiếng Việt.
- Khối bàn giao `cv-experience-refinement` với chế độ phù hợp: `final`, `enhanced-draft`, hoặc `incomplete`.
- Cuối mỗi báo cáo luôn có dòng kết luận:
  `> Kết quả chỉ mang tính tham khảo, cần được chỉnh sửa thủ công`
