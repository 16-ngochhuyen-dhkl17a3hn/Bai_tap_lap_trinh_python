class Stack:
    def __init__(self, capacity):
        '''Hàm tạo - khởi tạo ngăn xếp với kích thước tối đa'''
        self.capacity = capacity      
        self.stack = []               
        self.top = -1                 

    def __del__(self):
        '''Hàm hủy - giải phóng bộ nhớ (không cần thiết với Python do cơ chế garbage collection, nhưng vẫn có thể thêm)'''
        del self.stack

    def isEmpty(self):
        '''Kiểm tra ngăn xếp có trống hay không'''
        return self.top == -1

    def isFull(self):
        '''Kiểm tra ngăn xếp có đầy hay không'''
        return self.top == self.capacity - 1

    def push(self, value):
        '''Đưa một phần tử vào ngăn xếp'''
        if self.isFull():
            print('Ngăn xếp đã đầy, không thể thêm phần tử!')
        else:
            self.stack.append(value)
            self.top += 1
            print(f'Đã đưa {value} vào ngăn xếp.')

    def pop(self):
        '''Lấy một phần tử ra từ đỉnh ngăn xếp'''
        if self.isEmpty():
            print('Ngăn xếp trống, không thể lấy phần tử!')
            return None
        else:
            value = self.stack.pop()
            self.top -= 1
            print(f'Đã lấy {value} ra khỏi ngăn xếp.')
            return value

    def peek(self):
        '''Xem phần tử ở đỉnh ngăn xếp mà không lấy ra'''
        if self.isEmpty():
            print('Ngăn xếp trống!')
            return None
        else:
            return self.stack[self.top]

    def size(self):
        '''Trả về số lượng phần tử hiện có trong ngăn xếp'''
        return self.top + 1

stack = Stack(5)  

stack.push(1.2)
stack.push(2.3)
stack.push(3.4)
stack.push(4.5)
stack.push(5.6)

stack.pop()  

print(f'Ngăn xếp có trống không? {stack.isEmpty()}')  
print(f'Ngăn xếp có đầy không? {stack.isFull()}')   
print(f'Kích thước ngăn xếp: {stack.size()}')        

