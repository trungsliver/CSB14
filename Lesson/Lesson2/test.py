# file = open('test.txt', 'r')

# # Đọc file
# # Đọc toàn bộ nội dung file
# content = file.read()
# # Đọc một dòng
# # line = file.readline()
# # Đọc tất cả các dòng
# # lines = file.readlines()
# print(content)
# with open("grades.txt", "a") as file:
#     file.write('10')


# # # Viết file
# # file = open('test.txt', 'w')
# # file.write(9.5, '\n')
# # # hoặc
# # file = open('test.txt', 'a')
# # file.write(8, '\n')

# Bài tập 1: Viết một chương trình cho phép người dùng nhập n phần tử
# Sau đó thêm các phần tử vừa nhập vào mảng và in ra màn hình mảng đó.
n =  int(input('Nhập n: '))
arr = []
for i in range(n):
    item = input(f'Nhập phần tử thứ {i}: ')
    arr.append(item)
    # print(arr)
print(arr)
