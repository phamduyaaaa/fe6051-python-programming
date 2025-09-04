# 📘 Tài liệu học tập môn Lập trình Python

Repo này lưu trữ toàn bộ **code và bài tập ôn tập** trong quá trình học và chuẩn bị thi môn *Lập trình Python (FE6051)*.

---

## 📝 Thông tin kỳ thi
- **Hình thức**: Thực hành trên máy tính  
- **Thời gian**: 60 phút  
- **Phần mềm**: PyCharm IDE + Conda  
- **Nội dung thi**:  
  - Toàn bộ **64 bài tập ôn tập** trong file `tx2`  
  - Các form đề thi chính thức TX2  

---

## ⚡️ Lưu ý quan trọng khi làm bài
- **Bắt buộc** viết các yêu cầu dưới dạng **hàm**  
- Khi in, phải **hiển thị cả thuộc tính và phương thức trên cùng một dòng** (nếu đề yêu cầu)  
- Ghi nhớ các **công thức hình học**: chu vi, diện tích, thể tích, …  
- Ghi nhớ các **định nghĩa số đặc biệt**: số chính phương, số hoàn hảo, số nguyên tố, số đối xứng, …  
- Thành thạo các kỹ thuật Python:  
  - List comprehension  
  - Hàm `lambda`  
  - `sort()` 
  - `split()` và các thao tác xử lý chuỗi  
- Luôn **kiểm thử đủ trường hợp biên**:  
  - Ví dụ: đề yêu cầu sắp xếp giảm dần → phải xử lý cả trường hợp các giá trị bằng nhau.  
- **Luyện tập đa dạng đề** để làm quen tất cả dạng bài, tránh bị bỡ ngỡ khi thi.  

---

## 🎯 Mục tiêu
- Nắm chắc **cú pháp class, hàm, list/dict/tuple**  
- Thành thạo **xử lý dữ liệu, tính toán, sắp xếp, lọc**  
- Chuẩn bị sẵn các **công thức toán học** và **mẫu code chuẩn** để tiết kiệm thời gian trong phòng thi.  

---

# 📘 Cheat Sheet Công thức quan trọng

## 1. Hình học phẳng & không gian

- **Chu vi tứ giác**:  
  `P = a + b + c + d`

- **Chu vi hình chữ nhật**:  
  `P = 2 * (a + b)`

- **Diện tích hình chữ nhật**:  
  `S = a * b`

- **Đường chéo hình chữ nhật**:  
  `d = sqrt(a^2 + b^2)`

- **Chu vi hình vuông**:  
  `P = 4 * a`

- **Diện tích hình vuông**:  
  `S = a^2`

- **Đường chéo hình vuông**:  
  `d = a * sqrt(2)`

- **Hình thang vuông**:  
  `P = a + b + c + d`  
  `S = (a + b) * h / 2`

- **Tam giác**:  
  `P = a + b + c`  
  `p = (a + b + c) / 2`  
  `S = sqrt(p * (p - a) * (p - b) * (p - c))`  

- **Tam giác vuông**:  
  `c = sqrt(a^2 + b^2)`  
  `S = (a * b) / 2`  
  `P = a + b + c`

- **Tam giác đều (cạnh a)**:  
  `h = (a * sqrt(3)) / 2`  
  `P = 3 * a`  
  `S = (a^2 * sqrt(3)) / 4`

- **Đường tròn (bán kính r)**:  
  `C = 2 * π * r`  
  `S = π * r^2`

- **Hình hộp chữ nhật (a, b, h)**:  
  `V = a * b * h`  
  `Sxq = 2 * h * (a + b)`  
  `Stp = 2 * (ab + ah + bh)`

- **Hình trụ (đường kính d, chiều cao h)**:  
  `r = d / 2`  
  `V = π * r^2 * h`  
  `Sxq = 2 * π * r * h`

---

## 2. Số học

- **Chẵn/lẻ**: `n % 2 == 0 ?`  
- **Nguyên tố**: chỉ chia hết cho 1 và chính nó  
- **Chính phương**: `sqrt(n)` nguyên  
- **Hoàn thiện**: tổng ước số (trừ chính nó) = n  
- **Đối xứng**: đọc xuôi = đọc ngược  
- **Âm/dương**: `n > 0 → dương`, `n < 0 → âm`  
- **Số đảo**: viết ngược các chữ số  
- **Số thực → chữ số sau dấu phẩy**: dùng string hoặc Decimal  

- **Lũy thừa**:  
  - Bình phương: `a^2`  
  - Lập phương: `a^3`  
  - Giai thừa: `n! = 1*2*3*...*n`

- **Tổng 1→n**:  
  `S = n*(n+1)/2`

---

## 3. Phương trình

- **PT bậc nhất `ax+b=0`**  
  - `a=0, b=0 → vô số nghiệm`  
  - `a=0, b≠0 → vô nghiệm`  
  - `a≠0 → x = -b/a`

- **PT bậc 2 `ax^2+bx+c=0`**  
  - `Δ = b^2 - 4ac`  
  - `Δ < 0 → vô nghiệm`  
  - `Δ = 0 → x = -b/(2a)`  
  - `Δ > 0 → x1 = (-b+sqrt(Δ))/(2a), x2 = (-b-sqrt(Δ))/(2a)`

---

## 4. Ứng dụng đời sống

- **Nhân viên (lương)**:  
  `L = Lcb * heso + sonam * 0.1 * Lcb`

- **Sinh viên (điểm TB)**:  
  `TB = (7*thuctap + 8*doan) / 15`

- **Điện trở (3 vòng màu)**:  
  `Value = (mau1*10 + mau2) * 10^(mau3)`

- **Ong/kiến/trâu/công nhân…**:  
  `Kết quả = Hiệu suất * Thời gian`

- **Máy bơm nước**:  
  `Năng lượng = Công suất * Thời gian`

- **Mạch LC dao động**:  
  `f = 1 / (2π * sqrt(L*C))`

- **Mạch RC lọc thông thấp**:  
  `fc = 1 / (2π * R * C)`

- **Điều hòa cho phòng**:  
  `Công suất (BTU) = Thể tích phòng * 200`

- **Hoa quả (nông sản)**:  
  - Loại 1: `tiền = giá * số lượng`  
  - Loại 2: `tiền = 0.8 * giá * số lượng`

- **Tàu cá**:  
  `Chi phí = lit dầu * đơn giá`  
  `Có lãi nếu tiền bán cá ≥ k * chi phí`

- **Điện thoại / hàng hóa / linh kiện**:  
  `Tổng tiền = đơn giá * số lượng`  
  - Linh kiện: hỏng = 0, cũ = 50%, mới = 100%

---

## 5. Thao tác Python cần nhớ

- **Class + phương thức**  
- **List object → duyệt → tính toán**  
- **Tìm max/min**: `max(), min()` hoặc tự so sánh  
- **Tổng/tích**: `sum(), math.prod()`  
- **Sắp xếp**: `sorted(list, key=..., reverse=...)`  
- **Tuple/Dictionary**: lưu trữ kết quả  

---
