import math

class Triangle:
    def __init__(self, a, b, c):
        '''Khởi tạo tam giác với ba cạnh a, b, c'''
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        '''Tính diện tích của tam giác bằng công thức Heron'''
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        '''Tính chu vi của tam giác'''
        return self.a + self.b + self.c

    def display_info(self):
        '''Hiển thị thông tin của tam giác'''
        print(f'Cạnh a: {self.a}, Cạnh b: {self.b}, Cạnh c: {self.c}')
        print(f'Chu vi: {self.perimeter()}')
        print(f'Diện tích: {self.area():.2f}')


class IsoscelesTriangle(Triangle):
    def __init__(self, base, side):
        '''Khởi tạo tam giác cân với độ dài đáy base và độ dài hai cạnh bằng nhau side'''
        super().__init__(base, side, side)

    def display_info(self):
        '''Hiển thị thông tin của tam giác cân'''
        print('Thông tin tam giác cân:')
        super().display_info()


class RightTriangle(Triangle):
    def __init__(self, base, height):
        '''Khởi tạo tam giác vuông với độ dài đáy base và chiều cao height'''
        self.base = base
        self.height = height
        self.hypotenuse = math.sqrt(base**2 + height**2)  

        super().__init__(base, height, self.hypotenuse)

    def area(self):
        '''Tính diện tích của tam giác vuông'''
        return 0.5 * self.base * self.height

    def display_info(self):
        '''Hiển thị thông tin của tam giác vuông'''
        print('Thông tin tam giác vuông:')
        print(f'Cạnh đáy: {self.base}, Chiều cao: {self.height}, Cạnh huyền: {self.hypotenuse:.2f}')
        print(f'Chu vi: {self.perimeter()}')
        print(f'Diện tích: {self.area():.2f}')


class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side):
        '''Khởi tạo tam giác đều với độ dài cạnh side'''
        super().__init__(side, side) 

    def area(self):
        '''Tính diện tích của tam giác đều'''
        return (math.sqrt(3) / 4) * (self.a ** 2)

    def display_info(self):
        '''Hiển thị thông tin của tam giác đều'''
        print('Thông tin tam giác đều:')
        super().display_info()


print('Nhập thông tin cho tam giác:')
a = float(input('Cạnh a: '))
b = float(input('Cạnh b: '))
c = float(input('Cạnh c: '))
triangle = Triangle(a, b, c)
triangle.display_info()

print('\nNhập thông tin cho tam giác cân:')
base = float(input('Độ dài đáy: '))
side = float(input('Độ dài hai cạnh: '))
isosceles_triangle = IsoscelesTriangle(base, side)
isosceles_triangle.display_info()

print('\nNhập thông tin cho tam giác vuông:')
base = float(input('Độ dài đáy: '))
height = float(input('Chiều cao: '))
right_triangle = RightTriangle(base, height)
right_triangle.display_info()

print('\nNhập thông tin cho tam giác đều:')
side = float(input('Độ dài cạnh: '))
equilateral_triangle = EquilateralTriangle(side)
equilateral_triangle.display_info()
