import math

	
class SoNguyen():
	def __init__(self, songuyen):
		self.songuyen = songuyen
	def check_am_duong(self):
		check = math.inf
		if self.songuyen == 0:
			check = 0
		elif self.songuyen % 2 != 0:
			check = 1
		else:
			check = 2
		return check
	def check_sodoixung(self):
		if self.songuyen >= 0:
			s = str(abs(self.songuyen))
			return s == s[::-1]
		return False
	def check_sohoanthien(self):
		if self.songuyen <= 0:
			return False
		tong_uoc = 0
		for i in range(1, self.songuyen):
			if self.songuyen % i == 0:
				tong_uoc += i
		return tong_uoc == self.songuyen

def nhapso(n):
	for i in range(n):
		while True:
			try:
				songuyen = int(input(f"Nhap so nguyen thu {i+1}: "))
				l.append(SoNguyen(songuyen))
				break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")

l = []
cnt_am = 0
cnt_sodoixung = 0
cnt_sohoanthien = 0
tong_sodoixung = 0
min_sohoanthien = math.inf
while True:
	try:
		n = int(input("Nhap so luong so nguyen 'n': "))
		if n<= 0:
			print("'n' phai la so nguyen duong!")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
print("Ket thuc nhap, list da nhap la: ", end="")
for i in l:
	print(i.songuyen, end=" ")
	if i.check_am_duong() == 1:
		cnt_am +=1
	if i.check_sodoixung():
		cnt_sodoixung +=1
		tong_sodoixung += i.songuyen
	if i.check_sohoanthien():
		cnt_sohoanthien +=1
for i in l:
	if i.check_sohoanthien() and i.songuyen <= min_sohoanthien:
		min_sohoanthien = i.songuyen
if cnt_sodoixung != 0:
	print("\nCac so doi xung la:", end = " ")
	for i in l:
		if i.check_sodoixung():
			print(i.songuyen, end = " ")
	print(f"\nTong cac so doi xung la: {tong_sodoixung}")
else:
	print("\nKhong co so doi xung trong danh sach")

if cnt_sohoanthien != 0:
	print("Cac so hoan thien la:", end = " ")
	for i in l:
		if i.check_sohoanthien():
			print(i.songuyen, end = " ")
	print(f"\nSo hoan thien nho nhat la: {min_sohoanthien}")
else:
	print("Khong co so hoan thien trong danh sach")	

