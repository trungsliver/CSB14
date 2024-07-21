# Ôn tập:
# Bài 1: Nhập vào từ bàn phím các thông tin các nhân: 
    # Họ tên, Tuổi, Trường học, giới tính, điểm trung bình.
    # In ra màn hình các thông tin vừa nhập
# name = input('Nhập họ tên: ')
# age = int(input('Nhập tuổi: '))
# school = input('Nhập trường học: ')
# gender = input('Nhập giới tính: ')
# score = input('Nhập điểm: ')
# print(f'{name} - {age} tuổi - {school} - {gender} - Điểm TB: {score}')
# print('Họ tên: ' + name)
# print('Tuổi: ' + str(age))

# Bài 2: Nhập vào chiều dài và chiều rộng hình chữ nhật
    # In ra màn hình chu vi và diện tích hình chữ nhật đó.
# a = float(input('Nhập chiều dài: '))
# b = float(input('Nhập chiều rộng: '))
# cvi = 2*(a+b)
# s = a*b
# print(f'Chu vi: {cvi} - Diện tích: {s}')

# Bài 3: Nhập số nguyên n từ bàn phím.
    # Kiểm tra xem n có phải là số chẵn hay không.
# num = int(input('Nhập 1 số nguyên bất kì: '))
# if num%2 == 0:
#     print('Đây là số chẵn')
# else:
#     print('Đây là số lẻ')

# Bài 4: Nhập điểm số từ bàn phím. Hãy in ra mà hình xếp hạng học lực, biết rằng:
    # 8-10: Giỏi, 6.5-8: Khá, 5-6.5: Trung Bình, 0-5: Yếu
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

# Bài 5: Nhập 2 số nguyên a và b từ bàn phím
    # Yêu cầu 1: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
    # Yêu cầu 2: Tính tổng các số chia hết cho 3 trog khoảng vừa in
    # Yêu cầu 3: In ra số lượng số lẻ có trong khoảng trên
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# sum3 = 0
# odd = 0
# if a <= b:
#     for i in range(a, b+1):
#         print(i)
#         # Tính tổng các số chia hết cho 3
#         if i%3 == 0:
#             sum3 = sum3 + i
#         # Tính số lượng số lẻ
#         if i%2 == 1:
#             odd = odd + 1
# else:
#     for i in range(b, a+1):
#         print(i)
#         # Tính tổng các số chia hết cho 3
#         if i%3 == 0:
#             sum3 = sum3 + i
#         # Tính số lượng số lẻ
#         if i%2 == 1:
#             odd = odd + 1
# print('Tổng các số chia hết cho 3:', sum3)
# print('Số lượng số lẻ:', odd)

# Bài 6: In ra bảng cửu chương từ 5 đến 9
# for i in range(5,10):
#     print("\nBảng cửu chương", i)
#     for j in range(1,11):
#         print(f'{i} * {j} = {i*j}')

# Bài 7: Nhập số nguyên dương n. Tính tổng tất cả các chữ số của n.
    # Ví dụ: n = 123 => Tổng các chữ số = 1+2+3 = 6
# n = int(input('Nhập số nguyên dương n: '))
# sum = 0
# while n > 0:
#     sum = sum + n%10
#     n = n // 10
# print(f'Tổng các chữ số của {n} là: {sum}')

# Bài 8: Nhập n là số giây cần chuyển đổi (số nguyên)
    # In ra màn hình dạng h-m-s
    # Ví dụ: 3661s = 1h 1p 1s


# Bài 9: Danh sách
    # YC1: Nhập vào từ bàn phím 1 danh sách bao gồm 10 số nguyên
    # YC2: Thêm số '-5' vào vị trí thứ 2 (index=2) trong danh sách
    # YC3: Tính tổng các cố chẵn trong danh sách
    # YC4: Đếm số lượng số lẻ có trong danh sách
    # YC5: Tìm giá trị phần tử lớn nhất của danh sách
    # YC6: Tìm vị trí phần tử nhỏ nhất của danh sách
    # YC7: Dùng hàm tính giá trị trung bình của các phần tử trong danh sách
a = input('Nhập danh sách: ')
arr1 = a.split()
# YC2
arr1.insert(2,-5)
    # Chuyển các phần tử từ kiểu str sang int
arr = []
for item in arr1:
    x = int(item)
    arr.append(x)
print(arr)
# YC3
sum_even = 0
for item in arr:
    if item%2==0:
        sum_even = sum_even + item
print('Tổng các số chẵn:', sum_even)
# YC4
odd = 0
for item in arr:
    if item%2==1:
        odd = odd + 1
print('Số lượng số lẻ:', odd)
# YC5
print('Phần tử lớn nhất:', max(arr))
# YC6
index_min = 0
for i in range(len(arr)):
    if arr[i] == min(arr):
        index_min = i
print('Vị trí số nhỏ nhất:', index_min)
# YC7
def arr_avg(arr):
    sum = 0
    for item in arr:
        sum = sum + item
    avg = sum/len(arr)
    return sum
print('Giá trị trung bình các phần tử:', arr_avg(arr))