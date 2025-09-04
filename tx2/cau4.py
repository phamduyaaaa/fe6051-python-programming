import math

l_hinhthangvuong = []

class HinhThangVuong():
	def __init__(self, daylon, daynho, chieucao, canhxien):
		self.daylon = daylon
		self.daynho = daynho
		self.chieucao = chieucao
		self.canhxien = canhxien
	def chuvi(self):
		return self.daylon + self.daynho + self.chieucao + self.canhxien
	def dientich(self):
		return ((self.daylon + self.daynho)* self.chieucao)/2
		

def nhapcanh(n):
	for i in range(n):
		while True:
			print(f"Nhap thong so hinh {i+1}:")
			try:
				daylon = float(input("Nhap day lon: "))
				daynho = float(input("Nhap day nho: "))
				chieucao = float(input("Nhap chieu cao: "))
				canhxien = float(input("Nhap canh xien: "))
				if daylon*daynho*chieucao*canhxien <=0:
					print("Do dai cac canh phai la so thuc duong!")
				else:
					hinhthangvuong = HinhThangVuong(daylon, daynho, chieucao, canhxien)
					l_hinhthangvuong.append(hinhthangvuong)
					break
			except ValueError:
				print("Nhap khong hop le, nhap lai: ")
			
while True:
	try:
		n = int(input("Nhap so luong hinh thang vuong n: "))
		if n < 0:
			print("n la phai so nguyen duong!")
		else:
			nhapcanh(n)
			break
	except ValueError:
		print("Nhap khong hop le, vui long nhap lai!")

tongdientich = 0
dientichnhonhat = math.inf
cnt = 0
tenhinh = math.inf
print(f"Chu vi hinh thang cac hinh thang vuong vua nhap la:")
for i in l_hinhthangvuong:
	cnt += 1
	print(i.chuvi(), end = " ")
	tongdientich += i.dientich()
	if dientichnhonhat >= i.dientich():
		dientichnhonhat = i.dientich()
		tenhinh = cnt
print(f"\nTong dien tich cua n hinh vua nhap la: {tongdientich}")
print(f"Hinh {tenhinh} co dien tich nho nhat = {dientichnhonhat}")

		
		

