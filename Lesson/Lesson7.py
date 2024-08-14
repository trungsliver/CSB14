# Các thuật toán sắp xếp
import random
arr = []
for i in range(10):
    arr.append(random.randint(1, 50))
print(arr)

# Sắp xếp chèn - insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr

# Ví dụ
# sorted_arr = insertion_sort(arr)
# print(sorted_arr)

# Sắp xếp bong bóng - buble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                # Hoán đổi vị trí arr[j] và arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Nếu không có phần tử hoán đổi, dừng lại
        if swapped == False:
            break
    return arr
# Ví dụ
# sorted_arr = bubble_sort(arr)
# print(sorted_arr)

# So sánh hiệu suất
import time
import random 

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Thực hiện so sánh
def compare_algorithms(size):
    # Tạo danh sách ngẫu nhiên
    arr = [random.randint(0, 10000) for i in range(size)]

    # Đảm bảo 2 danh sách cùng nhận 1 dữ liệu
    arr_insertion = arr.copy()
    arr_bubble = arr.copy()

    # Đo thời gian insertion sort
    insertion_time = measure_time(insertion_sort, arr_insertion)
    print(f'Insertion sort: {insertion_time:.8f} seconds')

    # Đo thời gian Bubble sort
    bubble_time = measure_time(bubble_sort, arr_bubble)
    print(f'Bubble sort: {bubble_time:.8f} seconds')

for size in [1000, 5000, 10000, 20000]:
    print('Size:', size)
    compare_algorithms(size)
    print('================================')