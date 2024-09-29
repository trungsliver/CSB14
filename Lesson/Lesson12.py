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

# ============ LUYỆN TẬP ===========
# Bài 1: Dòng OOP và array/list để mô phỏng hoạt động của queue
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):         # Kiểm tra queue rỗng
        if len(self.items) == 0: return True
        else: return False
    def enqueue(self, item):    # Thêm phần tử vào hàng đợi
        self.items.append(item)
    def dequeue(self):          # Loại bỏ phần tử đầu tiên
        if not self.is_empty():
            return self.items.pop(0)
    def peek(self):             # Trả về phần tử đầu tiên
        if not self.is_empty():
            return self.items[0]
    def size(self):             # Trả về kích thước
        return len(self.items)
    def display(self):          # Hiển thị queue
        print(self.items)
    
# Test
# q = Queue()
# for i in range(1,6): 
#     q.enqueue(i)
# print('Xóa và lấy giá trị:' ,q.dequeue())
# print('Chỉ lấy phần tử đầu, không xóa:' ,q.peek())
# q.display()
# print('Kích thước:', q.size())

# Bài 2: Mô phỏng hệ thống hàng đợi khách hàng
# Giả sử bạn đang mô phỏng một hàng đợi khách hàng tại một siêu thị. 
# Mỗi khách hàng có một số nhận dạng duy nhất. 
# Viết chương trình sử dụng queue để quản lý khách hàng vào hàng đợi và phục vụ khách hàng.
# Gợi ý: cần 3 phương thức
    # 1. arrive: thêm khách hàng vào hàng đợi
    # 2. serve: phục vụ khách hàng đầu tiên trong hàng đợi
    # 3. waiting: số lượng khách hàng đang chờ

class SupermarketQueue:
    def __init__(self):
        self.customers = []
    def is_empty(self):
        if len(self.customers) == 0: return True
        else: return False
    def arrive(self, customer_id):
        self.customers.append(customer_id)
        print(f'Customer {customer_id} has arrived')
    def serve(self):
        if not self.is_empty():
            serve_customer = self.customers.pop(0)
            print(f'Serving customer {serve_customer}')
        else:
            print('No customers to serve')
    def waiting(self):
        if not self.is_empty():
            print('Customers are waiting:', len(self.customers))
            print(self.customers)
        else:
            print('No customers is waiting')
# Test
# supermarket = SupermarketQueue()
# for i in range(1,6): 
#     supermarket.arrive(i)   # Khách đến cửa hàng
# supermarket.serve()         # Phục vụ khách hàng 1
# supermarket.serve()         # Phục vụ khách hàng 2
# supermarket.waiting()       # Danh sách khách đang đợi

# Bài 3: Ứng dụng MP3
class MP3Player:
    def __init__(self):
        self.songs = []
        self.current_song = None
    def is_empty(self):
        if len(self.songs) == 0: return True
        else: return False
    def add_song(self, song):
        self.songs.append(song)
        print(f'{song} has been added')
    def play_next_song(self):
        if not self.is_empty():
            self.current_song = self.songs.pop(0)
            print(f'Playing {self.current_song}')
        else:
            print('No more songs to play')
    def skip_song(self):
        if not self.current_song is None:
            print(f'{self.current_song} is skipped')
            self.current_song = None
            self.play_next_song()
        else:
            print('No song to skip')
    def playlist(self):
        if not self.is_empty():
            print('\nPlaylist:')
            for i, song in enumerate(self.songs):
                print(f'\t{i+1}. {song}')
        else:
            print('\nNo songs in playlist')

# Test
mp3 = MP3Player()
mp3.add_song('Một con vịt')
mp3.add_song('She knows')
mp3.add_song('Falling down')
mp3.playlist()
mp3.play_next_song() # Playing Một con vịt
mp3.play_next_song() # Playing She knows
mp3.skip_song()
mp3.skip_song()
mp3.playlist()