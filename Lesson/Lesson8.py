# Bài 1: Cho hai mảng số nguyên nums1 và nums2.
# Viết chương trình trả về mảng là phép giao tập hợp của hai mảng trên.
# Đánh giá độ phức tạp của thuật toán
# arr1 = [i for i in range(5,16)]
# arr2 = [i for i in range(10,21)]
# arr3 = []
# for item1 in arr1:
#     for item2 in arr2:
#         if item1 == item2:
#             arr3.append(item1)
# print(arr3)
    # Gọi n là kích thước dữ liệu đầu vào (len(arr1) và len(arr2))
        # Vòng for item1 in arr1: độ phức tạp = n
        # Vòng for item2 in arr2: độ phức tạp = n
        # 2 vòng lặp lồng nhau +> độ phức tạp = n*n = n**2

# Bài 2: Cho mảng nums gồm n quả bóng có màu đỏ, trắng, xanh.
    # Viết chương trình sắp xếp mảng này sao cho:
    # những quả bóng có màu giống nhau thì được sắp xếp cạnh nhau
    # có thứ tự từ đỏ đến trắng đến xanh
    # Đánh giá độ phức tạp của thuật toán.
# nums = ['red', 'white', 'blue', 'red', 'white', 'blue', 'red', 'white', 'blue']
# count_r, count_w, count_b = 0, 0, 0
# for item in nums:   
#     # Đếm số lượng bóng mỗi loại
#     if item == 'red': count_r += 1
#     if item == 'white': count_w += 1
#     if item == 'blue': count_b += 1

#     # Tạo mảng mới đã sắp xếp theo yêu cầu red - white - blue
# sorted_nums = ['red']*count_r + ['white']*count_w + ['blue']*count_b
# print(sorted_nums)
#     # Đánh giá độ phức tạp của thuật toán: O(n)

# ============= Luyện Tập ==============
# Xác định độ phức tạp thuật toán của các bài tập sau

# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
def sum_odd(numbers):   # Độ phức tạp: O(n)
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
def is_prime(n:int):    # Độ phức tạp O(n)
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1
    if count == 2: 
        return True
    else: 
        return False

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
def count_word(s):      # Độ phức tạp: O(n)
    return len(s.split())
# print(count_word('Tôi học lớp CSB14'))

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n):   # Độ phức tạp: O(log(n))
    total = 0
    for i in range(len(str(n))):
        total += int(str(n)[i])
    return total
    # Độ phức tạp của hàm phụ thuộc vào độ dài của số nguyên n
    # Số lượng chữ của 1 số nguyên n là logarit cơ số 10 của n
# print(sum_of_digits(1234))

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
def find_max(numbers):      # Độ phức tạp: O(n) - n là độ dài danh sách
    max_index = 0
    for i in range(len(numbers)):
        if numbers[i] == max(numbers):
            max_index = i
    return max_index

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.

    # Cách 1:
def sum_to_n(n):    # Độ phức tạp: O(n)
    total = 0
    for i in range(1, n+1):
        total += i
    return total

    # Cách 2: Dùng công thức Gauss
def sum_to_n_2(n):  # Độ phức tạp: O(1)
    return n * (n + 1) // 2
