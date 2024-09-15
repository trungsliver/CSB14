# # Dictionary
#     # Create
# dict1 = {}
# dict2 = {
#     # Cặp giá trị: key - value
#     'name' : 'Duc Trung',
#     'age' : 25,
#     'city' : 'Hanoi',
#     'work' : 'MindX Technology School'
# }

#     # Read
#         # Duyệt toàn bộ key - value
# for key, value in dict2.items():
#     print(f"Key: {key}, Value: {value}")
#         # Truy cập bằng key
# print(dict2['name'])
#         # Dùng phương thức get()
# print(dict2.get('age'))
#             # Không tồn tại key -> None / giá trị mặc định
# print(dict2.get('hobbies'))                     # Output: None
# print(dict2.get('hobbies', '404 not found'))    # Output: 404 not found

#     # Update
#         # Add key - value
# dict2['hobbies'] = 'reading'
# # print(dict2)
#         # Update value
# dict2['age'] = 30
# # print(dict2)

#     # Delete
#         # del - xóa phần tử theo key
# del dict2['hobbies']
#         # pop - xóa phần tử và trả về giá trị
# work = dict2.pop('work')
# print(work)  # Output: MindX Technology School
# print(dict2)

#     # Kiểm tra key có tồn tại hay không
# print('name' in dict2)      # Output: True
# print('parents' in dict2)   # Output: False

#     # Lấy Tất Cả Key, Value Hoặc Cặp Key-Value
#         # Lấy tất cả key bằng phương thức keys()
# keys = dict2.keys()
# print(keys)
#         # Lấy tất cả values bằng phương thức values()
# values = dict2.values()
# print(values)
#         # Lấy tất cả cặp key-values bằng phương thức items()
# items = dict2.items()
# print(items)

#     # Hàm map(function, itertable)
#         # function: hàm biến đổi phần tử
#         # itertable: đối tượng dữ liệu (list, set, ...)

# # Ví dụ: Cho 1 danh sách điểm hệ số 10
# # Yêu cầu: Dùng map() để chuyển đổi danh sách trên thành hệ số 4
# gpa_10 = [5, 7, 8, 10, 9]
#     # Cách 1:
# gpa_4 = map(lambda gpa: gpa/10 * 4, gpa_10)
# print(list(gpa_4))
#     # Cách 2:
# def convert_gpa(score):
#     return score / 10 * 4
# gpa_4 = map(convert_gpa, gpa_10)
# print(list(gpa_4))

# # Ví dụ: Cho 1 danh sách gồm tên của học sinh (viết hoa lộn xộn)
# # Yêu cầu: Dùng map() để chuyển đổi danh sách trên viết hoa tất cả chữ
#     # tRunG -> TRUNG
# students = ['dUc TrUnG', 'qUaNg huY', 'gIa bInH', 'tHanh DAt']
#     # Cách 1:
# students1 = map(lambda stu: str.upper(stu), students)
# print(list(students1))
#     # Cách 2:
# def convert_to_upper(stu):
#     return str.upper(stu)
# students2 = map(convert_to_upper, students)
# print(list(students2))

# Luyện tập DICTIONARY - MAP

# Bài Tập 1: Quản Lý Thông Tin Sinh Viên
# Yêu cầu: Tạo một dictionary lưu trữ thông tin sinh viên với các khóa: name, age, và grade. 
# Thực hiện các thao tác sau:
# 1. Thêm sinh viên với thông tin name = "John", age = 22, và grade = "A".
student = {
    'name':'John',
    'age': 22,
    'grade': 'A'
}
# 2. Cập nhật grade của sinh viên thành "A+".
student['grade'] = 'A+'
# 3. Xóa thông tin age của sinh viên.
del student['age']
# 4. Kiểm tra xem name có trong dictionary không.
print('name' in student)

# Bài Tập 2: Đếm Số Lần Xuất Hiện Của Từ Trong Chuỗi
# Yêu cầu: Viết chương trình nhận vào một chuỗi và trả về một dictionary đếm số lần xuất hiện của mỗi từ trong chuỗi.
sentence = 'this is a test this is only a test'
def word_count(sentence):
    words = sentence.split()
    # mỗi từ sẽ là 1 key, số lần xuất hiện là value
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict
print(word_count(sentence))

# Bài Tập 3: Gộp Hai Dictionary
# Yêu cầu: Cho hai dictionary A và B. Viết chương trình gộp chúng lại. Nếu một key xuất hiện ở cả hai dictionary, cộng giá trị của chúng lại.
A = {'a': 100, 'b': 200, 'c': 300}
B = {'b': 250, 'c': 150, 'd': 400}
def merge_dicts(dict1, dict2):
    # Copy dict1 để đảm bảo dữ liệu không bị thay đổi
    merge_dict = dict1.copy()
    for key, value in dict2.items():
        # Nếu key đã tồn tại trong dict1, cộng giá trị
        merge_dict[key] = merge_dict.get(key, 0) + value
    return merge_dict
merged = merge_dicts(A, B)
print(merged)

# Bài Tập 4: Tìm Key Có Giá Trị Lớn Nhất
# Yêu cầu: Cho một dictionary có các cặp {key: value}. Viết chương trình để tìm key có giá trị lớn nhất.
scores = {
    'Huy': 8,
    'Bình': 10,
    'Đạt': 9.5,
    'VA': 9,
    'Nghi': 8.5
}
def find_max(dict):
    max_key = max(dict, key=dict.get)
    return max_key
print(find_max(scores))

# Bài Tập 5: Sắp Xếp Dictionary Theo Giá Trị
# Yêu cầu: Viết chương trình để sắp xếp một dictionary theo giá trị từ cao đến thấp.
scores = {
    'Huy': 8,
    'Bình': 10,
    'Đạt': 9.5,
    'VA': 9,
    'Nghi': 8.5
}
def sort_dict_by_value(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
print(sort_dict_by_value(scores))

# Bài Tập 6: Nhóm Các Phần Tử Theo Giá Trị
# Yêu cầu: Viết chương trình để nhóm các phần tử của một dictionary dựa trên giá trị của chúng. Ví dụ, các phần tử có cùng giá trị sẽ được đưa vào một danh sách.
data = {
    'apple': 1,
    'banana': 2,
    'cherry': 2,
    'date': 3,
    'elderberry': 3
}
def group_by_value(my_dict):
    grouped_dict = {}
    for key, value in my_dict.items():
        if value not in grouped_dict:
            grouped_dict[value] = []
        grouped_dict[value].append(key)
    return grouped_dict
print(group_by_value(data))

# Bài Tập 7: Tạo Dictionary Từ Danh Sách
# Yêu cầu: Viết chương trình tạo một dictionary từ hai danh sách: một danh sách chứa key và một danh sách chứa value tương ứng.
keys = ['apple', 'banana', 'cherry']
values = [1, 2, 3]
def list_to_dict(keys, values):
    # zip(): tạo ra các cặp key-value từ 2 danh sách
    # dict(): chuyển các cặp key-value thành dictionary
    return dict(zip(keys, values))
print(list_to_dict(keys, values))