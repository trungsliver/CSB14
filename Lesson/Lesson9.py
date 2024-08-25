# Kiểm tra CP2: 60p
# Tên file: [Lớp]_[Tên]_CP2.py
# Ví dụ: CSB14_DucTrung_CP2.py

# ============== TẬP HỢP ==============
# Định nghĩa:
    # - Tập hợp (set) là kiểu cấu trúc dữ liệu
    # - Tập hợp không có thứ tự
    # - Tập hợp không có phần tử trùng lặp

# Create - khởi tạo
    # Tạo tập hợp rỗng
set1 = set()
    # Tạo tập hợp có sẵn phần tử
set2 = {1, 2, 3, 4}

# Các thao tác cơ bản
    # Thêm phần tử: add()
set2.add(5)
print(set2)     # Output: {1, 2, 3, 4, 5}

    # Xóa phần tử: 
        # remove() - nếu không có phần tử sẽ gặp lỗi
set2.remove(5)
        # discard() - nếu koong có phần tử sẽ không gặp lỗi
set2.discard(6)

# Các thao tác khác
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
    # union() - Hợp: trả về tập hợp chứa tất cả phần tử của 2 tập hợp
result_u = set3.union(set4)
print('Union:',result_u)     # Output: {1, 2, 3, 4, 5, 6, 7, 8}

    # intersection() - Giao: trả về tập hợp chứa phần tử chung
result_i = set3.intersection(set4)
print('Intersection:', result_i)    # Output: {4, 5}

    # difference() - Hiệu: trả về tập hợp chỉ chứa trong set1 mà không có trong set2
result_d = set3.difference(set4)
print('Difference:', result_d)     # Output: {1, 2, 3}

# Duyệt phần tử
for item in set3:
    print(item, end = ' ')

# Kiểm tra phần tử có nằm trong tập hợp không
print(2 in set3)    # Output: True
print(9 in set3)    # Output: False

# Bài Tập 1: Tạo Tập Hợp Và Thực Hiện Các Thao Tác
# Yêu cầu: Tạo hai tập hợp A = {1, 2, 3, 4, 5} và B = {4, 5, 6, 7, 8}. Thực hiện các thao tác sau:
# 	1. Thêm phần tử 9 vào tập hợp A.
# 	2. Xóa phần tử 4 khỏi tập hợp B.
# 	3. Tìm hợp, giao, hiệu của hai tập hợp A và B.

A = {1, 2, 3, 4, 5} 
B = {4, 5, 6, 7, 8}
    # YC1: Thêm phần tử 9 vào tập hợp A.
A.add(9)
    # YC2: Xóa phần tử 4 khỏi tập hợp B.
B.remove(4)
B.discard(4)

# Bài Tập 2: Kiểm Tra Tập Hợp
# Yêu cầu: Cho tập hợp C = {'apple', 'banana', 'cherry'}. Kiểm tra xem 'banana' và 'grape' có trong tập hợp không.