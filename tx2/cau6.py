import math


class TamGiacVuong():
	def __init__(self, canhgocvuong1, canhgocvuong2):
		self.canhgocvuong1 = canhgocvuong1
		self.canhgocvuong2 = canhgocvuong2	
	def canhhuyen(self):
		return math.sqrt(self.canhgocvuong1**2 + self.canhgocvuong2**2)
	def dientich(self):
		return self.canhgocvuong1*self.canhgocvuong2
	def chuvi(self):
		return self.canhgocvuong1 + self.canhgocvuong2 + self.canhhuyen()
		
tamgiacvuong_l = []	
def nhapcanh(n):
	for i in range(n):
		print(f"Nhap thong so hinh {i+1}: ")
		while True:
			try:
				canhgocvuong1 = float(input("Nhap canh goc vuong 1: "))
				canhgocvuong2 = float(input("Nhap canh goc vuong 2: "))
				if canhgocvuong1*canhgocvuong2 <=0:
					print("Cac canh phai la so thuc duong!")
				else:
					h = TamGiacVuong(canhgocvuong1, canhgocvuong2)
					tamgiacvuong_l.append(h)
					break
					
			except ValueError:
				print("Nhap khong dung, nhap lai!")
				
while True:
	try:	
		n = int(input("Nhap so luong tam giac vuong n = "))
		if n <= 0:
			print(" n phai la so nguyen duong!")
		else:
			nhapcanh(n)
			break
	except ValueError:
		print("Nhap khong dung, nhap lai!")

tongdientich = 0
cnt = 0
tenhinh = math.inf
chuvilonnhat = -math.inf
print("Do dai canh huyen cua cac hinh lan luot la: ")
for i in tamgiacvuong_l:
	cnt+=1
	print(i.canhhuyen(), end=" ")
	tongdientich += i.dientich()
	if chuvilonnhat <= i.chuvi():
		tenhinh = cnt
		chuvilonnhat = i.chuvi()
print(f"\nTong dien tich cua {n} hinh vua nhap la: {tongdientich}")
print(f"Hinh {tenhinh} la hinh co chu vi lon nhat = {chuvilonnhat}")

