class Stack:
    def __init__(self, capacity):
        'Khởi tạo ngăn xếp với kích thước tối đa'
        self.capacity = capacity  
        self.stack = []           
    def isEmpty(self):
        'Kiểm tra ngăn xếp có trống hay không'
        return len(self.stack) == 0  

    def isFull(self):
        'Kiểm tra ngăn xếp có đầy hay không'
        return len(self.stack) == self.capacity  
    def push(self, value):
        'Đưa một phần tử vào ngăn xếp'
        if self.isFull():
            print('Ngăn xếp đã đầy, không thể thêm phần tử!')
        else:
            self.stack.append(value)  
            print(f'Đã đưa {value} vào ngăn xếp.')

    def pop(self):
        'Lấy một phần tử ra từ đỉnh ngăn xếp'
        if self.isEmpty():
            print('Ngăn xếp trống, không thể lấy phần tử!')
            return None
        else:
            value = self.stack.pop()  
            print(f'Đã lấy {value} ra khỏi ngăn xếp.')
            return value

    def peek(self):
        'Xem phần tử ở đỉnh ngăn xếp mà không lấy ra'
        if self.isEmpty():
            print('Ngăn xếp trống!')
            return None
        else:
            return self.stack[-1]  

    def size(self):
        'Trả về số lượng phần tử hiện có trong ngăn xếp'
        return len(self.stack)  

    def count(self):
        'Trả về số phần tử hiện có trên ngăn xếp'
        return len(self.stack)  
stack = Stack(5)  

stack.push(1.2)
stack.push(2.3)
stack.push(3.4)
stack.push(4.5)
stack.push(5.6)

stack.pop()  

print(f'Ngăn xếp có trống không? {stack.isEmpty()}') 
print(f'Ngăn xếp có đầy không? {stack.isFull()}')    
print(f'Kích thước ngăn xếp: {stack.isFull()}')        
print(f'Số phần tử hiện có trên ngăn xếp: {stack.count()}')  