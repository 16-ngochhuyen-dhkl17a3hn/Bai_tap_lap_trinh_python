class Polygon:
    def __init__(self, sides):
        '''Khởi tạo đa giác với số cạnh'''
        self.sides = sides  

    def input_sides(self):
        '''Nhập độ dài các cạnh'''
        self.sides = []
        for i in range(self.sides):
            length = float(input(f'Nhập độ dài cạnh thứ {i + 1}: '))
            self.sides.append(length)

    def perimeter(self):
        '''Tính chu vi của đa giác'''
        return sum(self.sides)

    def display_info(self):
        '''Hiển thị thông tin chu vi'''
        print(f'Chu vi của đa giác: {self.perimeter()}')


class Parallelogram(Polygon):
    def __init__(self, base, height):
        '''Khởi tạo hình bình hành'''
        super().__init__(4)  
        self.base = base
        self.height = height

    def area(self):
        '''Tính diện tích của hình bình hành'''
        return self.base * self.height

    def display_info(self):
        '''Hiển thị thông tin chu vi và diện tích'''
        print(f'Chu vi của hình bình hành: {self.perimeter()}')
        print(f'Diện tích của hình bình hành: {self.area()}')


class Rectangle(Parallelogram):
    def __init__(self, length, width):
        '''Khởi tạo hình chữ nhật'''
        super().__init__(length, width)
        self.length = length
        self.width = width

    def perimeter(self):
        '''Tính chu vi của hình chữ nhật'''
        return 2 * (self.length + self.width)

    def area(self):
        '''Tính diện tích của hình chữ nhật'''
        return self.length * self.width

    def display_info(self):
        '''Hiển thị thông tin chu vi và diện tích'''
        print(f'Chu vi của hình chữ nhật: {self.perimeter()}')
        print(f'Diện tích của hình chữ nhật: {self.area()}')


class Square(Rectangle):
    def __init__(self, side):
        '''Khởi tạo hình vuông'''
        super().__init__(side, side)  

    def display_info(self):
        '''Hiển thị thông tin chu vi và diện tích'''
        print(f'Chu vi của hình vuông: {self.perimeter()}')
        print(f'Diện tích của hình vuông: {self.area()}')


base = float(input('Nhập độ dài đáy của hình bình hành: '))
height = float(input('Nhập chiều cao của hình bình hành: '))
parallelogram = Parallelogram(base, height)
parallelogram.display_info()

length = float(input('Nhập chiều dài của hình chữ nhật: '))
width = float(input('Nhập chiều rộng của hình chữ nhật: '))
rectangle = Rectangle(length, width)
rectangle.display_info()

side = float(input('Nhập độ dài cạnh của hình vuông: '))
square = Square(side)
square.display_info()
