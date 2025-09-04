import math

class ThiSinh():
	def __init__(self, ten, namsinh, diemtoan, diemvan, diemngoaingu):
		self.ten = ten
		self.namsinh = namsinh
		self.diemtoan = diemtoan
		self.diemvan = diemvan
		self.diemngoaingu = diemngoaingu
	def tinhtuoi(self):
		return 2025 - self.namsinh
	def tongdiem(self):
		return self.diemtoan + self.diemvan + self.diemngoaingu
		
l = []
def nhapso(n):
	for i in range(n):
		print(f"Nhap thong tin thi sinh {i+1}: ")
		while True:
			try:
				ten = input("Nhap ten: ")
				namsinh = int(input("Nhap nam sinh: "))
				diemtoan = float(input("Nhap diem toan: "))
				diemvan = float(input("Nhap diem van: "))
				diemngoaingu = float(input("Nhap diem anh: "))
				if diemtoan * diemvan * diemngoaingu <= 0:
					print("diem cac mon phai la so nguyen duong")
				elif diemtoan > 10 or diemvan > 10 or diemngoaingu > 10:
					print("diem cac mon phai < 10")
				else:
					l.append(ThiSinh(ten, namsinh, diemtoan, diemvan, diemngoaingu))
					break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
def it_tuoi_nhat():
	check = math.inf
	idx = math.inf
	for i in range(n):
		if check >= l[i].tinhtuoi():
			check = l[i].tinhtuoi()
			idx = i
	print(f"Thi sinh {idx+1} la thi sinh it tuoi nhat")

def diem_toan_lon_nhat():
	check = - math.inf
	idx = math.inf
	for i in range(n):
		if check <= l[i].diemtoan:
			check = l[i].diemtoan
			idx = i
	print(f"Thi sinh {idx+1} la thi sinh co diem toan lon nhat = {check}")

def in_thong_tin():
	for i in range(n):
		print(f"Thong tin thi sinh thu {i+1}: Ten: {l[i].ten} | Nam sinh: {l[i].namsinh} | Diem Toan: {l[i].diemtoan} | Diem Van: {l[i].diemvan} | Diem Anh: {l[i].diemngoaingu} | Tuoi: {l[i].tinhtuoi()} | Tong Diem: {l[i].tongdiem()}")
	
while True:
	try:
		n = int(input("Nhap so luong thi sinh 'n': "))
		if n < 0:
			print("'n' phai la so nguyen duong.")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
	
in_thong_tin()
it_tuoi_nhat()
diem_toan_lon_nhat()

	
	



