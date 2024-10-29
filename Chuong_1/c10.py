import math

class Point:
    def __init__(self, x=0, y=0):
        '''Khởi tạo điểm với tọa độ (x, y)'''
        self.x = x
        self.y = y

    def display(self):
        '''Hiển thị tọa độ của điểm'''
        print(f'Tọa độ điểm: ({self.x}, {self.y})')


class Ellipse(Point):
    def __init__(self, x, y, a, b):
        '''Khởi tạo elip với tọa độ tâm (x, y), bán trục lớn a và bán trục nhỏ b'''
        super().__init__(x, y)  
        self.a = a  
        self.b = b  

    def area(self):
        '''Tính diện tích của elip'''
        return math.pi * self.a * self.b

    def display(self):
        '''Hiển thị thông tin của elip'''
        super().display()  
        print(f'Bán trục lớn: {self.a}')
        print(f'Bán trục nhỏ: {self.b}')
        print(f'Diện tích của elip: {self.area():.2f}')


class Circle(Ellipse):
    def __init__(self, x, y, radius):
        '''Khởi tạo đường tròn với tọa độ tâm (x, y) và bán kính'''
        super().__init__(x, y, radius, radius) 
        self.radius = radius

    def area(self):
        '''Tính diện tích của đường tròn'''
        return math.pi * self.radius ** 2

    def display(self):
        '''Hiển thị thông tin của đường tròn'''
        super().display()  
        print(f'Bán kính: {self.radius}')
        print(f'Diện tích của đường tròn: {self.area():.2f}')


x = float(input('Nhập tọa độ x của tâm elip: '))
y = float(input('Nhập tọa độ y của tâm elip: '))
a = float(input('Nhập bán trục lớn của elip: '))
b = float(input('Nhập bán trục nhỏ của elip: '))
ellipse = Ellipse(x, y, a, b)
ellipse.display()

radius = float(input('Nhập bán kính của đường tròn: '))
circle = Circle(x, y, radius)
circle.display()
