class Date:
    def __init__(self, day=1, month=1, year=2000):
        '''Khởi tạo ngày, tháng, năm với các giá trị mặc định'''
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        '''In thông tin về ngày ra màn hình'''
        print(f'Ngày: {self.day:02d}/{self.month:02d}/{self.year}')

    def isLeapYear(self, year):
        '''Kiểm tra năm nhuận'''
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def daysInMonth(self, month, year):
        '''Trả về số ngày trong tháng'''
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.isLeapYear(year) else 28
        return 0

    def next(self):
        '''Tính ngày tiếp theo'''
        self.day += 1
        if self.day > self.daysInMonth(self.month, self.year):
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1


date = Date(28, 10, 2024)  
date.display()  

date.next()   
date.display()  
