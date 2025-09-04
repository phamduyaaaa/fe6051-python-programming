class SinhVien():
	def __init__(self, ten, msv, diemthuctap, diemdoan):
		self.ten = ten
		self.msv = msv
		self.diemthuctap = diemthuctap
		self.diemdoan = diemdoan
	
	def tinhdiemtb(self):
		return (7*self.diemthuctap + 8*self.diemdoan)/15
		

l = []
def nhapso(n):
	for i in range(n):
		while True:
			try:
				print(f"Nhap thong tin sinh vien {i+1}:")
				ten = input("Nhap ten: ")
				msv = int(input("Nhap msv: "))
				diemthuctap = float(input("Nhap diem thuc tap: "))
				diemdoan = float(input("Nhap diem do an: "))
				if diemthuctap > 10 or diemthuctap < 0 or diemdoan >10 or diemdoan < 0:
					print("Diem so phai nam trong khoang 0->10")
				elif msv < 0:
					print("Ma sinh vien phai la so nguyen duong")
				else:
					l.append(SinhVien(ten, msv, diemthuctap, diemdoan))
					break	
			except ValueError:
				print("Nhap khong hop le, nhap lai!")

def indanhsach():
	for i in range(n):
		print(f"Sinh vien {i+1}: Ten = {l[i].ten} | MSV = {l[i].msv} | Diem Thuc Tap = {l[i].diemthuctap} | Diem Do An = {l[i].diemdoan} | DiemTB = {l[i].tinhdiemtb()}")

def laydiemtb(sinhvien):
	return sinhvien.tinhdiemtb()

def sapxep():
	l.sort(key = laydiemtb, reverse = True)
	for i in l:
		print(i.ten, end = " ")

def xoaten():
	global l
	l = [sv for sv in l if sv.tinhdiemtb() < 4.0]
	for i in l:
		print(i.ten, end = " " )


while True:
	try:
		n = int(input("Nhap so sinh vien 'n': "))
		if n <= 0:
			print("'n' phai la so nguyen duong")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
		
indanhsach()
sapxep()
xoaten()
