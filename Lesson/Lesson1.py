# print('Hello world')

# # Variables - Biến số
#     # Dùng để lưu trữ dữ liệu
#     # Có thể thay đổi được trong khi lập trình
# name = 'Bui Duc Trung'
# a, b, c = 1, 2, 3

# # Data types - Kiểu dữ liệu
#     # String: xâu/chuỗi ký tự, đưuọc đặt trong dấu nháy
# name = 'Bui Duc Trung'
#     # Int: số nguyên
# age = 25
#     # Float: số thực
# score = 9.6
#     # Bool/Boolean: True/False - Đúng/Sai
# male = True

# # Các cách hiển thị dữ liệu
#     # Cách 1: dùng dấu cộng
# print('Họ tên: ' + name)
# print('Tuổi: ' + str(age))      # Ép kiểu
#     # Cách 2: Dùng dấu phẩy
# print('Điểm:', score)
#     # Cách 3: Viết f ở trước string - truyền tham số vào string
# print(f'Giới tính nam: {male}')
#     # Cách 4: Hiển thị trên nhiều dòng
# print("""
# 1
# 2
# 3
# 4
# """)

# # type() - Kiểm tra kiểu dữ liệu
# print(type(name), type(age), type(score), type(male))

# # Input() - nhập dữ liệu
#     # Mặc định khi input, data type = string
# class1 = input('Nhập tên lớp: ')
# print(type(class1))
#     # Xác định data type khi nhập
# height = float(input('Nhập chiều cao: '))

# Câu điều kiện
    # Dạng thiếu
# age = int(input('Nhập tuổi: '))
# if age >= 18:
#     print('Bạn đã đủ 18 tuổi.')

    # Dạng đủ
        # Đề bài: Nhập 1 số nguyên, kiểm tra chẵn lẻ và in ra kết quả
# num = int(input('Nhập 1 số nguyên: '))
# if num%2 == 0:
#     print(num, 'là số chẵn')
# else:
#     print(num, 'là số lẻ')

    # Dạng đa nhánh
        # Xếp hạng học lực
        # Giỏi: [8,10], Khá: [6.5, 8), TB: [5, 6.5), Yếu: [0, 5)
# score = float(input('Nhập điểm: '))
# if score >=0 and score <= 10:
#     if score >= 8:
#         print('học lực: Giỏi')
#     elif score >= 6.5:
#         print('học lực: Khá')
#     elif score >= 5:
#         print('học lực: TB')
#     else:
#         print('học lực: yếu')
# else:
#     print('Sai thông tin')

# Bài tập: in giấy
# ptype = int(input('Nhập loại giấy: '))
# page = int(input('Nhập số trang cần in: '))
# paper = 0

# if ptype == 1:      # In trên 1 mặt
#     # Số trang = số giấy cần dùng
#     paper = page
# elif ptype == 2:
#     # Cách 1:
#     if page%2 == 0:
#         paper = page/2
#     else:
#         paper = (page +1)/2

#     # Cách 2:
#     paper = page//2 + page%2

#     # Cách 3:
#     paper = (page + 1) // 2

# Bài tập 2: Quy đổi thời gian
    # Input: số giây
    # Output: định dạng: giờ - phút - giây
    # Ví dụ: 3661s = 1h 1p 1s

time = int(input('Nhập thời gian (giây): '))

h = time // 3600
m = (time % 3600) // 60
s = time % 60

print(f'{time}s = {h}h {m}m {s}s ')