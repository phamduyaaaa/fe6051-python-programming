import math




class HinhTron():
	def __init__(self, bankinh):
		self.bankinh = bankinh	
	
	def tinhchuvi(self):
		return 2*math.pi*self.bankinh
	
	def tinhdientich(self):
		return math.pi * self.bankinh * self.bankinh
		


l = []
def nhapso(n):
	for i in range(n):
		while True:
			try:
				bankinh = float(input(f"Nhap ban kinh hinh {i+1}: "))
				if bankinh <= 0:
					print("ban kinh phai la so duong")
				else:
					l.append(HinhTron(bankinh))
					break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
			
			
while True:
	try:
		n = int(input("Nhap so hinh tron 'n': "))
		if n <= 0:
			print("'n' phai la so nguyen duong")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")		


tongdientich = 0
chuvi = []
min_dientich = math.inf
idx_min_dientich = math.inf
min_chuvi = math.inf
idx_min_chuvi = math.inf
cnt = 0
for i in l:
	cnt +=1
	tongdientich += i.tinhdientich()
	chuvi.append(i.tinhchuvi())
	if min_dientich >= i.tinhdientich():
		min_dientich = i.tinhdientich()
		idx_min_dientich = cnt
	if min_chuvi >= i.tinhchuvi():
		min_chuvi = i.tinhchuvi()
		idx_min_chuvi = cnt
for i in range(n):
	print(f"Hinh {i+1}: BanKinh = {l[i].bankinh} | Chuvi = {l[i].tinhchuvi()} | Dien tich = {l[i].tinhdientich()}")
print("Chu vi cua 'n' hinh tron vua nhap la: ")
for i in range(n):
	print(f"Chu vi hinh tron {i+1}: {chuvi[i]}")

print(f"Tong dien tich cac hinh tron la {tongdientich}")
print(f"Hinh tron co chu vi nho nhat la {idx_min_chuvi} voi {min_chuvi}")
print(f"Hinh tron co dien tich nho nhat la {idx_min_dientich} voi {min_dientich}")

	
	
	
		
	
	
	
