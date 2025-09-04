import math

l_hinhtamgiac =[]
class HinhTamGiac():
	def __init__ (self, canh1, canh2, canh3):
		self.canh1 = canh1
		self.canh2 = canh2
		self.canh3 = canh3
		
	def chuvi(self):
		return self.canh1 + self.canh2 + self.canh3
		
	def dientich(self):
		nuachuvi = self.chuvi()/2
		return math.sqrt(nuachuvi*(nuachuvi-self.canh1)*(nuachuvi-self.canh2)*(nuachuvi-self.canh3))
		
def nhapcanh(n):
	for i in range(n):
		print(f"Nhap thong so hinh {i+1}: ")
		while True:
			try:
				canh1 = float(input("Nhap canh 1: "))
				canh2 = float(input("Nhap canh 2: "))
				canh3 = float(input("Nhap canh 3: "))
				if canh1*canh2*canh3 <= 0:
					print("Canh phai la so duong!")
				else:
					h = HinhTamGiac(canh1, canh2, canh3)
					l_hinhtamgiac.append(h)
					break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")

while True:
	try:
		n = int(input("Nhap so luong n: "))
		if n <= 0:
			print("n phai la so duong!")
		else:
			nhapcanh(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
		
tongdientich = 0
cnt = 0
tenhinh = math.inf
dientichnhonhat = math.inf
print("Chu vi cua cac hinh vua nhap la:")
for i in l_hinhtamgiac:
	print(i.chuvi(), end=" ")
	tongdientich += i.dientich()
	cnt +=1
	if i.dientich() <= dientichnhonhat:
		dientichnhonhat = i.dientich()
		tenhinh = cnt
print(f"\nHinh {tenhinh} la hinh co dien tich nho nhat: {dientichnhonhat}")
	




