# Queue - Hàng đợi
# Nguyên tắc: FIFO - First in First out

import queue
# Khởi tạo queue rỗng
queue1 = queue.Queue()
queue2 = [1, 2, 3]

# Thêm vào hàng đợi (enqueue)
queue1.put(1)
queue2.append(4)

# Lấy phần tử đầu tiên (peek)
first_item = queue2.pop(0)

# Kiểm tra rỗng (is_empty)
def is_empty(queue):
    if len(queue) == 0: return True
    else: return False

# print(queue1)
# print(queue2)

