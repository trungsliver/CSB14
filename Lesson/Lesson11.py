# STACK - ngăn xếp
# Nguyên tắc: LIFO - Last in, First out
 
# Khởi tạo stack rỗng
stack = []

# Push - Thêm phần tử vào stack
stack.append(1)
stack.append(2)
stack.append(3)

# Pop - Lấy phần tử cuối cùng và loại bỏ
# print(stack.pop())  # Xóa và trả về 3

# Peek - Xem phần tử trên cùng (phần tử cuối cùng được thêm)
# print(stack[-1])  # Trả về 2

# isEmpty - Kiểm tra stack rỗng
def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
    
# Bài 1: Đảo ngược chuỗi
# Viết chương trình sử dụng stack để đảo ngược 1 chuỗi ký tự
# Gợi ý:
    # Tạo một stack và push từng ký tự của chuỗi vào stack.
    # Lần lượt pop các ký tự từ stack để tạo chuỗi đảo ngược.
name = 'DucTrung'
def reverse_string(s):
    stack = []
    # Push từng ký tự của string vào stack theo đúng thứ tự
    for item in s:
        stack.append(item)
        
    reverse_string = ''
    # Pop từng ký tự từ stack để tạo chuỗi đảo ngược
    while stack:
        reverse_string += stack.pop()
    return reverse_string
print(reverse_string(name))

# Bài 2: Kiểm tra dấu ngoặc hợp lệ
# Chuỗi được gọi là hợp lệ nếu:
    # 1. Các dấu ngoặc mở và ngoặc đóng khớp với nhau đúng thứ tự: () [] {}
    # 2. Mỗi dấu ngoặc mở phải có dấu ngoặc đóng tương ứng
# Gợi ý:
    # Dùng stack để lưu các dấu ngoặc mở.
    # Khi gặp dấu ngoặc đóng, kiểm tra xem nó có khớp với dấu ngoặc mở trên cùng của stack không.
# def is_valid_parentheses(s):
#     stack = []
#     dict = {
#         ')': '(', 
#         ']': '[',
#         '}': '{'
#     }
#     for item in s:
#         if item in dict:
#             if stack:
#                 top_element = stack.pop()
#             else:
#                 top_element = '#'
#             if dict[item] != top_element:
#                 return False
#         else:
#             stack.append(item)
#     return not stack
# # Test
# str1 = '([{}])'
# print(is_valid_parentheses(str1))   # Output: True
# str2 = '([})'
# print(is_valid_parentheses(str2))   # Output: False

# Bài trên slides: Ứng dụng web
class Browser:
    def __init__(self):
        # Lưu lịch sửa các trang đã truy cập
        self.back_stack = []
        # Lưu lịch sử forward
        self.forward_stack = []

    def visit_page(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print(f'Visitting {url}')

    def back(self):
        if len(self.back_stack) > 1:
            current_page = self.back_stack.pop()
            self.forward_stack.append(current_page)
            previous_page = self.back_stack[-1]
            print(f'Going back to {previous_page}')
        else:
            print('Cant go back')

    def forward(self):
        if self.forward_stack:
            next_page = self.forward_stack.pop()
            self.back_stack.append(next_page)
            print(f'Going forward to {next_page}')
        else:
            print('Cant go forward')

# Test
browser = Browser()

browser.visit_page('https://www.google.com')
browser.visit_page('https://www.facebook.com')
browser.visit_page('https://www.youtube.com')

browser.back()
browser.back()
browser.back()

browser.forward()
browser.forward()
browser.forward()