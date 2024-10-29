import math

class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input('Nhập tử số: '))
        self.mau_so = int(input('Nhập mẫu số: '))
        while not self.kiem_tra_hop_le():
            print('Mẫu số phải khác 0. Vui lòng nhập lại.')
            self.mau_so = int(input('Nhập mẫu số: '))

    def in_phan_so(self):
        if self.kiem_tra_hop_le():
            ucln = math.gcd(self.tu_so, self.mau_so)
            tu = self.tu_so // ucln
            mau = self.mau_so // ucln

            if mau == 1:
                print(f'Phân số là: {tu}')
            elif mau < 0:  
                print(f'Phân số là: {-tu}/{-mau}')
            else:
                print(f'Phân số là: {tu}/{mau}')
        else:
            print('Phân số không hợp lệ (mẫu số bằng 0).')
