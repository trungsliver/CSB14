class Dog:
    # Hàm khởi tạo: self - đối tượng, name/age - thuộc tính
    def __init__(self, name, age):
        # Tạo thuộc tính và gán giá trị
        self.name = name
        self.age = age

    def get_description(self):
        return f'{self.name} is {self.age} years old'
    
    # Hàm mặc định để dùng đc lệnh print()
    def __str__(self) -> str:
        return f'{self.name} {self.age}'

# Tính đóng gói (Encapsulation)
# class Dog:
#     def __init__(self, name, age):
#             self.name = name            
#             self.age = age              
#             self.__sound = "Woof"
#     def speak(self):
#           return self.__sound
    
# Tính kế thừa (Inheritance) 
class Shiba(Dog):
      def __init__(self, name, age):
            super().__init__(name, age)

sb1 = Shiba('hihi', 5)
print(sb1.get_description())

# Tính đa hình (Polymorphism)
class Dog:
    tail = "long"
    def __init__(self, name, age):
        self.name = name              
        self.age = age              
        self.__sound = "Woof"

    def get_description(self):
        return f"{self.name} is {self.age}-year-old"
    def speak(self):
        return self.__sound


class Corgi(Dog):
    tail = "short"
    def __init__(self, name, age):
        super().__init__(name, age) 
    # override
    def get_description(self):
        return f"{self.name} is a {self.age}-year-old corgi"

# Tính trừu tượng (Abstraction)
class Dog:
      def __init__(self, name, age):
            self.name = name              
            self.age = age              


      def speak(self):
            pass

class Shiba(Dog):
      def __init__(self, name, age):
            super().__init__(name, age)
     
      def speak(self):
            print("Woof")

class Husky(Dog):
      def __init__(self, name, age):
            super().__init__(name, age)
     
      def speak(self):
            print("Howl")