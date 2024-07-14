# Các thao tác với xâu ký tự
# name = 'Duc Trung'
    # Độ dài chuỗi ký tự
# print(len(name))
    # Ký tự thứ 6 của chuỗi
# print(name[6])

# 1 số lệnh thường gặp
    # Tách chuỗi - split()
# name = '1 2 3 4 5 6 7 8 9 5 5'
# arr1 = name.split()
# print(arr1)

# a = 'NN,GB,TD,QH,VA'
# arr2 = a.split(',')
# print(arr2)

    # Thay thế - replace()
# x = name.replace('5', '888')
# y = name.replace('5', '888', 2)
# print(x)
# print(y)

# Hàm - chương trình con
# def sHCN(a,b):
#     s = a * b
#     return s
# print(sHCN(3,4))
# print(sHCN(2,5))

# ================== ÔN TẬP =====================
# Bài 1: cho danh sách gồm phần tử từ 1 đến 15
        # In ra các số chẵn trong danh sách
# arr1 = []
# arr1_even = []
# for i in range(1,16):
#     arr1.append(i)
# for item in arr1:
#     if item%2 == 0:
#         arr1_even.append(item)
# print('Phần tử chẵn:', arr1_even)

# Bài 2: Nhập vào 1 danh sách bao gồm các số nguyên.
        # Tính tổng các phần tử của danh sách đó
# a = input('Nhập phần tử: ')
#     # Khi split, mặc định data type = string
# arr2_str = a.split()
# # print(arr2_str)
#     # convert các phần tử sang int
# arr2_int = []
# for item in arr2_str:
#     x = int(item)
#     arr2_int.append(x)
# # print(arr2_int)
#     # Tính tổng phần tử danh sách
# sum1 = 0
# for item in arr2_int:
#     sum1 = sum1 + item
# print('Tổng danh sách:', sum1)
# print('Tổng danh sách (2):', sum(arr2_int))


# Bài 3: Nhập vào 1 danh sách bao gồm các số nguyên.
        # Tìm phần tử lớn nhất và vị trí của phần tử đó
# arr3 = [1, 5, 2, 4, 9, 8, 6, 7]

#     # Cách 1:
# for i in range (len(arr3)):
#     # max(arr) - trả về giá trị phần tử lớn nhất của arr
#     if arr3[i] == max(arr3):
#         index = i

#     # Cách 2:
# max_item = arr3[0]
# for i in range (len(arr3)):
#     # Tìm phần tử lớn nhẩt
#     if arr3[i] > max_item:
#         max_item = arr3[i]
#         index = i

# print('Giá trị phần tử lớn nhất:', max(arr3))
# print('Vị trí phần tử lớn nhất:', index)

# Bài tập 4: Đăng ký - Đăng nhập
    # Cấu trúc tài khoản trong danh sách: 'username:password'
users = ['admin:123456']

    # Đăng ký
def register():
    username = input('Nhập username: ')
    password = input('Nhập password: ')
    check = True        # dùng để kiểm tra đăng ký thành công hay không

    # Lỗi 1: Nhập thiếu username hoặc password
    if username == '' or password == '':
        check = False
        print('Nhập thiếu thông tin!')
    else:
        # Duyệt các tài khoản trong danh sách users
        for user in users:
            # Chia 1 user thành 2 phần username và password
            stored_username, stored_password = user.split(':')
            # Lỗi 2: Trùng tên tài khoản
            if username == stored_username:
                check = False
                print('Tài khoản đã tồn tại!')
    
    #  Kiểm tra xem có đăng ký thành công hay không
    if check == True:
        # Add tài khoản vào danh sách users
        new_acc = username + ':' + password
        users.append(new_acc)
        print('Đăng ký thành công!')
    else:
        print('Đăng ký không thành công!')
    
def login():
    username = input('Nhập username: ')
    password = input('Nhập password: ')
    check = False

    for user in users:
        stored_username, stored_password = user.split(":")
        if stored_username == username and stored_password == password:
            check = True
    
    if check == True:
        print('Đăng nhập thành công!')
    else:
        print('Đăng nhập không thành công!')

def main():
    while True:
        print('\n========== Đăng ký - Đăng nhập ==========')
        print('1. Đăng ký')
        print('2. Đăng nhập')
        print('3. Thoát')
        print('=========================================')
        choice = int(input('Nhập lựa chọn của bạn: '))

        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            break
        else:
            print('Lựa chọn không hợp lệ!')
            
main()