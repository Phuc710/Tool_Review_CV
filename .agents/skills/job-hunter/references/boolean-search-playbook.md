# Sổ Tay Toán Tử Boolean Search Nâng Cao Cho Dân Tech / Embedded

Tài liệu này cung cấp các chuỗi toán tử logic (Boolean Strings) chuẩn xác cao, tối ưu hóa theo **độ chính xác (Precision), độ bao phủ (Recall), giảm thiểu nhiễu (Noise) và loại bỏ kết quả sai lệch (False Positives)**.

---

## 1. Bản Đồ Từ Khóa Chuẩn Hóa (Keyword Taxonomy)

### Nhóm Chức danh (Roles & Titles)
```text
"Embedded Software Engineer" OR "Embedded Engineer" OR "Firmware Engineer" OR "Firmware Developer" OR "Embedded Linux Engineer" OR "Embedded C++ Developer" OR "IoT Engineer" OR "IoT Software Developer" OR "MCU Firmware Engineer"
```

### Nhóm Công nghệ & Nền tảng (Tech Stack & Toolchain)
```text
"C++" OR "C" OR "ESP32" OR "STM32" OR "FreeRTOS" OR "Zephyr" OR "Embedded Linux" OR "ARM Cortex" OR "I2C" OR "SPI" OR "UART" OR "CAN" OR "BLE" OR "MQTT"
```

### Nhóm Địa bàn & Chế độ làm việc (Location & Work Mode)
```text
"Ho Chi Minh" OR "HCMC" OR "Ho Chi Minh City" OR "TP.HCM" OR "Thủ Đức" OR "District 9" OR "District 7" OR "Tan Binh" OR "Vietnam"
```

---

## 2. Quét Trực Tiếp Hệ Thống Quản Lý Tuyển Dụng Quốc Tế (ATS Scanning)

Nhiều tập đoàn công nghệ toàn cầu (Global Tech & Semiconductor) chỉ đăng tuyển lên hệ thống ATS riêng:

### Ashby ATS
```text
site:jobs.ashbyhq.com ("Embedded" OR "Firmware" OR "IoT") ("Vietnam" OR "Ho Chi Minh" OR "Remote")
```

### Lever ATS
```text
site:jobs.lever.co ("Embedded Software" OR "Firmware Engineer" OR "IoT Developer") ("Vietnam" OR "Ho Chi Minh")
```

### Greenhouse ATS
```text
site:boards.greenhouse.io ("Embedded" OR "Firmware" OR "C++") ("Vietnam" OR "Ho Chi Minh")
```

### Workday ATS
```text
site:myworkdayjobs.com ("Embedded Software" OR "Firmware" OR "Automotive Software") ("Ho Chi Minh" OR "Vietnam")
```

### SmartRecruiters ATS
```text
site:jobs.smartrecruiters.com ("Embedded Software" OR "Firmware" OR "IoT") "Vietnam"
```

### Recruitee ATS
```text
site:careers.recruitee.com ("Embedded" OR "C++" OR "IoT") ("Vietnam" OR "Ho Chi Minh")
```

### iCIMS ATS
```text
(site:careers-*.icims.com OR site:*.icims.com) ("Embedded" OR "Firmware") ("Vietnam" OR "Ho Chi Minh")
```

---

## 3. Tìm Tuyển Dụng Trực Tiếp Từ Tech Leads & Hiring Managers Trên LinkedIn

Tìm các bài post cá nhân của các Quản lý Kỹ thuật (Engineering Manager / Tech Lead) đang cần tuyển gấp đồng đội:

### Quét bài đăng tuyển dụng trực tiếp (LinkedIn Posts)
```text
site:linkedin.com/posts ("Embedded Software" OR "Firmware" OR "IoT") ("we are hiring" OR "hiring" OR "tuyển dụng" OR "cần tuyển" OR "join my team") ("Ho Chi Minh" OR "TP.HCM" OR "Vietnam")
```

### Quét Profile Tech Lead / Hiring Manager đang tuyển dụng
```text
site:linkedin.com/in ("Engineering Manager" OR "Tech Lead" OR "Firmware Lead" OR "Embedded Manager") ("hiring" OR "recruiting") ("Ho Chi Minh" OR "Vietnam")
```

---

## 4. Truy Vấn Theo Phân Khúc Kỹ Thuật & Cấp Bậc (Precision Queries)

### Phân khúc 1: Lập trình Nhúng C/C++ & Vi điều khiển (ESP32 / STM32 / FreeRTOS)
```text
("Embedded Software Engineer" OR "Firmware Engineer") AND ("C++" OR "C") AND ("ESP32" OR "STM32" OR "FreeRTOS") AND ("Ho Chi Minh" OR "HCMC" OR "TP.HCM") -intern
```

### Phân khúc 2: Thiết bị thông minh IoT & Giao thức truyền thông (MQTT / BLE / Wi-Fi)
```text
("IoT Engineer" OR "IoT Developer" OR "Firmware Developer") AND ("MQTT" OR "I2C" OR "SPI" OR "UART" OR "BLE") AND ("Ho Chi Minh" OR "HCMC" OR "TP.HCM")
```

### Phân khúc 3: Lập trình Linux Nhúng & Automotive (Yocto / Device Driver / CAN)
```text
("Embedded Linux" OR "Automotive Software" OR "Device Driver") AND ("C++" OR "C") AND ("CAN" OR "Kernel" OR "Yocto") AND ("Ho Chi Minh" OR "Vietnam")
```

### Phân khúc 4: Vị trí Fresher / Junior / Entry-Level
```text
("Embedded" OR "Firmware" OR "IoT") AND ("Fresher" OR "Junior" OR "Entry-level" OR "0-2 years" OR "mới tốt nghiệp") AND ("Ho Chi Minh" OR "HCMC" OR "TP.HCM")
```

---

## 5. Quét Việc Làm Remote / GitHub Awesome Jobs

### GitHub Awesome Jobs Vietnam (Lọc Issues Đang Mở)
```text
site:github.com/awesome-jobs/vietnam/issues ("Embedded" OR "C++" OR "Firmware" OR "IoT") is:open
```

### Việc Làm Tech Remote Đông Nam Á & Global
```text
("Remote" OR "Vietnam") AND ("Embedded Software" OR "Firmware Engineer" OR "IoT Developer") (site:remoteok.com OR site:weworkremotely.com OR site:wellfound.com)
```
