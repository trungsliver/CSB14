# Lập trình hướng đối tượng
    # Khởi tạo đối tượng
class Dog():
    # Hàm khởi tạo: self-đối tượng. name/age-thuộc tính
    def __init__(self, name, age):
        # Tạo thuộc tính và gán giá trị
        self.name = name
        self.age = age
        self.__sound = 'gâu gâu' # Tính đóng gói, private 

    # Phương thức __str__ dùng để print()
    def __str__(self):
        return f'{self.name} {self.age}'
    
    # Phương thức - method
    def get_description(self):
        return f'{self.name} is {self.age} years old'
    
    def speak(self):
        pass

# Khởi tạo đối tượng
dog1 = Dog('Lu', 3)
print(dog1)
print(dog1.get_description())
print(dog1.name)
# print(dog1.__sound)

# Các tính chất của OOP
    # 1. Tính đóng gói (Encapsulation)
    # 2. Tính kế thừa (Inheritance) 
class Shiba(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

        # override
    def get_description(self):
        return f'{self.name} is {self.age} years old corgi'
    
    def speak(self):
        print('haha')
    
sb1 = Shiba('Chó', 5)
print(sb1.get_description())
    # 3. Tính đa hình (Polymorphism)
    # 4. Tính trừu tượng (Abstraction)
class Husky(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print('hihi')

hs1 = Husky('Mèo', 6)
hs1.speak()
sb1.speak()
dog1.speak()