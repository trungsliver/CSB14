# Thuật toán tìm kiếm
arr = [2, 5, 3, 1, 9, 7, 4, 8, 6]
    # Tìm vị trí của phần tử có giá trị = 7
# for i in range(len(arr)):
#     if arr[i] == 7:
#         index_arr = i
# print(i)

# Tìm kiếm tuần tự
def sequential_search(arr, target):
    # Duyệt từng phần tử trong danh sách
    for i in range(len(arr)):
        if arr[i] == target:
            return i    # Trả về index cần tìm
    return -1       # Không tìm thấy, trả về -1

    # Ví dụ
# num_list = [2, 5, 3, 1, 9, 7, 4, 8, 6]
# target = 15
# result = sequential_search(num_list, target)

# if result == -1:
#     print(f'Phần tử {target} không có trong danh sách')
# else:
#     print(f'Phần tử {target} có index = {result}')

# Tìm kiếm nhị phân - binary search (chỉ áp dụng cho danh sách đã sắp xếp)
def binary_search(arr, target):
    # Khởi tạo chỉ số index bên trái và phải
    left = 0
    right = len(arr) - 1

    while right >= left:
        # Tìm chỉ số ở giữa
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid      # Tìm thấy kết quả
        elif target > arr[mid]:
            left = mid + 1      # Nếu giá trị giữa nhỏ hơn giá trị cần tìm, tìm bên phải
        else:
            right = mid - 1     # Nếu giá trị giữa lớn hơn giá trị cần tìm, tìm bên trái
    return -1       # Nếu không tìm thấy, trả về -1

    # Ví dụ
# num_list = [2, 5, 3, 1, 9, 7, 4, 8, 6]
# num_list.sort()
# target = 7
# result = binary_search(num_list, target)

# if result == -1:
#     print(f'Phần tử {target} không có trong danh sách')
# else:
#     print(f'Phần tử {target} có index = {result}')

# So sánh hiệu suất
import time
import random 

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Tìm kiếm tuần tự
# random_list = [random.randint(1, 200000000) for _ in range(200000000)]
# target = random.choice(random_list)
# time_seq = measure_time(sequential_search, random_list, target)
# print(f'Thời gian tìm kiếm tuần tự: {time_seq:.8f} giây')

# Tìm kiếm nhị phân
# sorted_list = sorted(random_list)
# time_bin = measure_time(binary_search, sorted_list, target)
# print(f'Thời gian tìm kiếm nhị phân: {time_bin:.8f} giây')

# Đọc - ghi file
    # Mở file để ghi
file = open('l6.txt', 'w')

    # Ghi nội dung vào file
        # Ghi 1 chuỗi
file.write('Hello world!')
        # Ghi nhiều dòng
lines = ['1st line\n', '2nd line \n', '3rd line \n']
file.writelines(lines)
        # Dùng with để ghi
with open('l6_p2.txt', 'w') as file:
    file.write('This is 2rd file!!!')

    # Mở file để đọc
file = open('l6.txt', 'r')
    # Đọc toàn bộ nội dung file
content = file.read()
print(content)
    # Đọc từng dòng
for line in file:
    print(line, end = '')
    # Dùng with để đọc
with open('l6_p2.txt', 'r') as file:
    content = file.read()
    print(content)

    # Đóng file
file.close()
