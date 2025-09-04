import math



class SoNguyen():
	def __init__(self, songuyen):
		self.songuyen = songuyen
	def check_amduong(self):
		check = math.inf
		if self.songuyen == 0:
			check = 0
		elif self.songuyen < 0:
			check = 1	
		else:
			check = 2
		return check
		
	def check_sodoixung(self):
		if self.songuyen >= 0 :
			s = str(abs(self.songuyen))
			return self.songuyen == s[::-1]
		return False
	def check_sohoanthien(self):
		tong_uoc = 0
		for i in range(1,self.songuyen+1):
			if self.songuyen % i == 0:
				tong_uoc += i
		return self.songuyen == tong_uoc
l = []
def nhapso(n):
	for i in range(n):
		while True:
			try:
				num = int(input(f"Nhap so nguyen thu {i+1}: "))
				l.append(SoNguyen(num))
				break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
def in_cac_so_duong(mang):
	cnt = 0
	for i in mang:
		if i.check_amduong() == 2:
			cnt += 1
	if cnt != 0:
		print("Cac so nguyen duong trong mang la: ", end="")
		for i in mang:
			if i.check_amduong() == 2:
				print(i.songuyen, end = " ")
	else:
		print("Khong co so nguyen duong trong mang!")
	print("\n")
	
def tong_cac_so_hoan_thien(mang):
	cnt = 0
	tong = 0
	for i in mang:
		if i.check_sohoanthien():
			cnt +=1
			tong += i.songuyen
	if cnt != 0:
		print(f"Tong cac so hoan thien la: {tong}")
	else:
		print("Khong co so hoan thien trong list")

def in_gia_tri_l(mang):
	new_l = []
	for i in mang:
		new_l.append(i.songuyen)
	return new_l

def so_doi_xung_lon_nhat(mang):
	cnt = 0
	max_sdx = -math.inf
	for i in mang:
		if i.check_sodoixung():
			cnt+= 1
	for i in mang:
		if i.check_sodoixung() and max_sdx <= i.songuyen:
			max_sdx = i.songuyen
	if cnt != 0:
		print(f"So doi xung lon nhat la: {max_sdx}")
	else:
		print("Khong co so doi xung!")
while True:
	try:
		n = int(input("Nhap so luong so nguyen 'n': "))
		if n <= 0:
			print("'n' phai la so nguyen duong!")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
print(f"Ket thuc nhap, cac gia tri da nhap la: {in_gia_tri_l(l)}")
in_cac_so_duong(l)
tong_cac_so_hoan_thien(l)
so_doi_xung_lon_nhat(l)


