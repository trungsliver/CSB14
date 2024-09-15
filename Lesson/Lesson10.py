# Dictionary
    # Create
dict1 = {}
dict2 = {
    # Cặp giá trị: key - value
    'name' : 'Duc Trung',
    'age' : 25,
    'city' : 'Hanoi',
    'work' : 'MindX Technology School'
}

    # Read
        # Duyệt toàn bộ key - value
for key, value in dict2.items():
    print(f"Key: {key}, Value: {value}")
        # Truy cập bằng key
print(dict2['name'])
        # Dùng phương thức get()
print(dict2.get('age'))
            # Không tồn tại key -> None / giá trị mặc định
print(dict2.get('hobbies'))
print(dict2.get('hobbies', '404 not found'))

