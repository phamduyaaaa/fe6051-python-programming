import math



class HinhTru():
	def __init__ (self, ten, duongkinh, docao):
		self.ten = ten
		self.duongkinh = duongkinh
		self.docao = docao
		
	def dientichxq(self):
		return 2 * math.pi * (self.duongkinh/2) * self.docao
	def thetich(self):
		return math.pi * (self.duongkinh/2) * (self.duongkinh/2) * self.docao
	
l = []
def nhapso(n):
	for i in range(n):
		while True:
			try:
				print(f"=== Nhap thong so hinh {i+1} ===")
				ten = input("Nhap ten hinh: ")
				duongkinh = float(input(f"Nhap duong kinh: ")) 
				docao = float(input(f"Nhap do cao: "))
				if duongkinh*docao <= 0:
					print("duong kinh va do cao phai la so duong!")
				else:
					l.append(HinhTru(ten,duongkinh,docao))
					break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
				
while True:
	try:
		n = int(input("Nhap so luong hinh 'n': "))
		if n <= 0:
			print("'n' phai la so nguyen duong.")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")

for i in range(n):
	print(f"Hinh {i+1}: Ten hinh: {l[i].ten} | Duong kinh: {l[i].duongkinh} | Do cao: {l[i].docao}")
	
max_thetich = - math.inf
min_thetich = math.inf
tongdientich_xq = 0
cnt = 0
cnt_min = math.inf
cnt_max = math.inf
for i in l:
	cnt += 1
	tongdientich_xq += i.dientichxq()
	if max_thetich <= i.thetich():
		max_thetich = i.thetich()
		cnt_max = cnt
	if min_thetich >= i.thetich():
		min_thetich = i.thetich()
		cnt_min = cnt

print(f"Hinh {cnt_min} co the tich nho nhat = {min_thetich}")
print(f"Hinh {cnt_max} co the tich lon nhat = {max_thetich}")
print(f"Tong dien tich xung quanh cac hinh tru: {tongdientich_xq}")
	

