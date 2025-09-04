import math



class HinhVuong():
	def __init__(self, canh):
		self.canh = canh
	def chuvi(self):
		return self.canh*4
	def dientich(self):
		return self.canh*self.canh
	def dodaiduongcheo(self):
		return math.sqrt(math.pow(self.canh,2)+math.pow(self.canh,2))
l_hv = []
while True:
	try:
		n = int(input("Nhap n hinh vuong :"))
		if n < 0:
			print("n phai la so nguyen duong!")
		else:
			for i in range(n):
				print(f"===Nhap thong so hinh {i+1}===")
				while True:
					try:
						canh = float(input("Nhap do dai canh:"))
						if canh < 0:
							print("canh phai la so thuc duong!")
						else:
							l_hv.append(HinhVuong(canh))
							break
					except ValueError:
						print("Nhap khong hop le, nhap lai!")
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")

tongdientich = 0
duongcheolonnhat = - math.inf
cnt = 0
print("Chu vi cac hinh la: ")
for i in l_hv:
	cnt +=1
	print(i.chuvi(), end = " ")
	tongdientich += i.dientich()
	if i.dodaiduongcheo() > duongcheolonnhat:
		duongcheolonnhat = i.dodaiduongcheo()
	
print(f"Tong dien tich cua {n} hinh vua nhap la: {tongdientich}")
print(f"Hinh co do dai duong cheo lon nhat la hinh {cnt} voi chieu dai: {duongcheolonnhat}")


	




