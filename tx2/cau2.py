import math


class HinhChuNhat():
	def __init__(self, chieu_dai, chieu_rong):
		self.chieu_dai = chieu_dai
		self.chieu_rong = chieu_rong
	def tinh_chuvi(self):
		return 2*(self.chieu_dai * self.chieu_rong)
	def dodai_duongcheo(self):
		return math.sqrt(self.chieu_dai * self.chieu_rong)
	def tinh_dientich(self):
		return self.chieu_dai * self.chieu_rong
	
	
cnt = 0
l_hcn = []
while True:
	try:
		n = int(input("Nhap n: "))
		if n < 0:
			print("n phai la so duong, nhap lai!")
		else:
			for i in range(n):
				while True:
					try:
						cnt +=1
						print(f"Nhap thong so HCN {cnt}:")
						chieu_dai = int(input("Nhap chieu dai: "))
						chieu_rong = int(input("Nhap chieu rong: "))
						hcn = HinhChuNhat(chieu_dai, chieu_rong)
						if chieu_dai * chieu_rong  <= 0:
							print("Canh phai la so duong, nhap lai!")
						else:
							l_hcn.append(hcn)
							break
					except ValueError:
						print("Nhap khong dung, nhap lai canh!")
			break
	except ValueError:
		print("Nhap khong dung, nhap lai n!")

tong_dien_tich = 0
min_duong_cheo = math.inf
index_min_duong_cheo = math.inf
cnt = 0
print("Chu vi cua n hinh chu nhat vua nhap la:", end = " ")
for i in l_hcn:
	cnt +=1
	print(f"HCN {cnt}: {i.tinh_chuvi()}", end = " ")
	tong_dien_tich += i.tinh_dientich()
	if i.dodai_duongcheo() <= min_duong_cheo:
		min_duong_cheo = i.dodai_duongcheo()
		index_min_duong_cheo = cnt
	
print(f"\nTong dien tich cua n hinh chu nhat la: {tong_dien_tich}")
print(f"Hinh chu nhat co duong cheo nho nhat la: {index_min_duong_cheo} voi do dai {min_duong_cheo}")
	
	
