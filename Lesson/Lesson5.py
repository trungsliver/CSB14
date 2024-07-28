# Quy tắc đặt tên file: [Tên lớp]_[Họ tên]_CP1.py
# VD: CSB14_BuiDucTrung_CP1.py

# Đề đã được gửi trong group zalo
# Hạn nộp: 20:20 28/07/2024
# Nộp bài: gửi file riêng qua zalo cá nhân, không gửi bài vào group

# bài 4 không cần vẽ sơ đồ thuật toán

# Gợi ý bài 7
    # Khai báo danh sách gồm n phần tử
    # Tính tổng từ phần tử thứ 1 cho đến phần tử n-1
    # Lấy tổng vừa tính được cộng phần tử cuối (index=-1) * 2
    # Lấy tổng vừa tính đưuọc chia cho (len(danh sách) + 1)

# Bài 6:
# a = '1.5 1.6 1.2 1.3 1.8'
# height = a.split()
#     # Chuyển dữ liệu trong danh sách height từ str sang float
# height = [float(item) for item in height]
# print(height)
# count = 0
# for item in height:
#     if item < 1.5:
#         count += 1      # count = count + 1
# print('Số người thấp hơn 1.5m là:', count)

# Bài 7:
# scores = [8, 9, 8, 8, 9]

# def avg_score(arr):
#     sum = 0
#     for i in range(len(arr) - 1):
#         sum = sum + arr[i]
#     sum = sum + arr[-1]*2

#     avg = sum / (len(arr)+1)
#     return avg

# print('Điểm trung bình:', avg_score(scores))

# Algorithm complexity - Độ phức tạp của thuật toán
    # Biểu diễn bằng Big-O Notation
        # Độ phức tạp (O) = n * số phép toán
        # n là kích thức dữ liệu đầu vào
    # Mô tả hành vi tính toán (thời gian tính toán, bộ nhớ cần dùng)

    # Thuật toán hằng O(1): gán, nhập, xuất, toán tử
name = 25
age = input()
print(name)

    # Thuật toán tuyến tính O(n)
arr = []        # Danh sách gồm n phần tử
for i in range(len(arr)):
    print(arr[i])

    # Thuật toán bậc 2 O(n^2)
        # In 10 bảng cửu chương từ 1 đến 10
for i in range(1,11):
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')

# Đề bài: kiểm tra số nguyên tố
def prime1(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

