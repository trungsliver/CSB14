# Vòng lặp for - Vòng lặp hữu hạn
    # Hàm range(n): lặp từ 0 đến n-1 
# for i in range(5):
#     print(i)

    # Hàm range(start, stop, step)
        # start: số bắt đầu (không bắt buộc, auto = 0)
        # stop: số kết thúc (bắt buộc)
        # step: bước nhảy (không bắt buộc, auto = 1)
# for i in range(0, 11, 2):
#     print(i)

# Đề bài: Nhập 2 số nguyên a và b từ bàn phím
    # Yêu cầu 1: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
    # Yêu cầu 2: Tính tổng các số chẵn trong khoảng vừa in
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# sum = 0

# if b >= a:
#     for i in range(a, b+1):
#         print(i)
#         if i%2 == 0:
#             sum += i    # sum = sum + i
# else:
#     for i in range(b, a+1):
#         print(i)
#         if i%2 == 0:
#             sum += i
# print('Tổng các số chẵn trong khoảng đã cho là:', sum)

# Sử dụng random
    # Khai báo thư viện
import random
    # Cú pháp sử dụng hàm: [Tên thư viện].[Tên hàm]
rd = random.randint(1,10)

# In ra bảng cửu chương dạng: 5 * 1 = 5
# for i in range(1,11):
#     print(f'{rd} * {i} = {rd*i}')

# In ra bảng cửu chương từ 2-9
# for i in range(2,10):
#     print('\nBảng cửu chương', i)
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i*j}')

# Vòng lặp while() - Vòng lặp vô hạn
# i = 0
# while i < 6:
#     print(i)
#     i = i + 1

    # Ví dụ: Nhập số nguyên n trong khoảng [0,100]
    # nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
# n = int(input('Nhập số trong khoảng [0,100]: '))

# while n<0 or n>100:
#     print('Bạn đã nhập sai, vui lòng nhập lại.')
#     n = int(input('\nNhập số trong khoảng [0,100]: '))
# print('Nhập dữ liệu thành công.')

# Danh sách - array/list
# Thao tác CRUD: Create - Read - Update - Delete

    # Create - Khởi tại danh sách
arrHS = ['Thanh Dat', 'Quang Huy', 'Viet Anh']
        # Hàm len() - trả về độ dài
# print(len(arrHS))

    # Read - Duyệt và hiển thị các phần tử
        # Hiện phần tử thông qua index
# print(arrHS[0])         # Phần tử đầu tiên
# print(arrHS[-1])        # Phần tử cuối cùng

        # Duyệt và hiển thị tất cả phần tử
            # Cách 1: Áp dụng khi lấy index và value
# for i in range(len(arrHS)):
#     print(f'[{i}] {arrHS[i]}')

            # Cách 2: áp dụng khi chỉ muốn lấy value
# for item in arrHS:
#     print(item)

            # Cách 3: dùng hàm có sẵn
# for index, item in enumerate(arrHS):
#     print(f'[{index}] {item}')

            # Cách 4: để test
# print(arrHS)

    # Update - Cập nhật phần tử
        # Thêm vào vào cuối - append()
arrHS.append('Duc Trung')
        # Thêm vào vị trí chỉ định - insert(index, value)
arrHS.insert(1, 'Imposter')
        # Chỉnh sửa phần tử
arrHS[1] = 'Imposter 666'

    # Delete - Xóa phần tử
        # Xóa phần tử bằng giá trị - remove()
arrHS.remove('Duc Trung')
        # Xóa phần tử bằng index - pop()
arrHS.pop(1)
del arrHS[1]
        #  Xóa toàn bộ danh sách - clear()
arrHS.clear()

arrNum = [5, 78, 42, 56, 12, 25]
    # Sắp xếp phần tử danh sách - sort()
        # Sắp xếp từ nhỏ tới lớn
arrNum.sort()
        # Sắp xếp từ lớn tới nhỏ
arrNum.sort(reverse=True)

# Bài tập 1: Viết một chương trình cho phép người dùng nhập n phần tử
# Sau đó thêm các phần tử vừa nhập vào mảng và in ra màn hình mảng đó.
# arr = []
# n = int(input('Số lượng phần tử muốn nhập: '))
# for i in range(n):
#     item = input(f'Phần tử thứ {i}: ')
#     arr.append(item)
# print(arr)

# Bài tập 2: cho danh sách gồm phần tử từ 1 đến 15
    # Yêu cầu 1: In ra các số chẵn trong danh sách
    # Yêu cầu 2: Tính tổng các phần tử chia hết cho 3 trong danh sách
# arr = []
# sum = 0
#     # Thêm phần tử 1-15 vào danh sách
# for i in range(1, 16):
#     arr.append(i)
# print(arr)
    
# for item in arr:
#     # In ra các phần tử chẵn trong danh sách
#     if item%2 == 0:
#         print(item)
#     # Tính tổng các phần tử chia hết cho 3
#     if item%3 == 0:
#         sum = sum + item
# print('Tổng các phần tử chia hết cho 3:', sum)

# Bài tập 3: Tìm phần tử chung của 2 danh sách
arr1 = []
arr2 = []
arr3 = []
    # Thêm phần tử vào 2 danh sách
for i in range(1,11):
    arr1.append(i)
for i in range(5,16):
    arr2.append(i)
    # Hiện 2 danh sách
print(arr1)
print(arr2)
    # Tìm phần tử chung
for item1 in arr1:
    for item2 in arr2:
        if item1 == item2:
            arr3.append(item1)
print('Phần tử chung:' ,arr3)