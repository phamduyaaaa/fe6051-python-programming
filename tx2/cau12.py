import math
class SoNguyen():
	def __init__(self, songuyen):
		self.songuyen = songuyen
		
	def check_chanle(self):
		return self.songuyen % 2 == 0
	
	def check_snt(self):
		if self.songuyen <= 1:
			return False
		for i in range(2,self.songuyen):
			if self.songuyen % i == 0:
				return False
		return True
		
	def check_scp(self):
		if self.songuyen < 0:
			return False
		for i in range(self.songuyen+1):
			if i*i == self.songuyen:
				return True
		return False

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

print("Ket thuc nhap, danh sach nhap la:", end=" ")
tich_snt = 1
cnt_snt = 0
min_scp = math.inf
cnt_le = 0
for i in l:
	print(i.songuyen, end = " ")
	if not i.check_chanle():
		cnt_le +=1
if cnt_le != 0:
	print("\nCac so le la: ", end = " ")
else:
	print("\nKhong co so le nao trong danh sach", end = " ")
for i in l:
	if not i.check_chanle():
		print(i.songuyen, end =" ")
	if i.check_snt():
		tich_snt *= i.songuyen
		cnt_snt +=1
	if min_scp >= i.songuyen and i.check_scp():
		min_scp = i.songuyen
if cnt_snt != 0:
	print(f"\nTich cac so nguyen to la: {tich_snt}")
else:
	print("\nKhong co so nguyen to trong danh sach")
if min_scp != math.inf:
	print(f"So chinh phuong nho nhat la: {min_scp}")
else:
	print("Khong co so chinh phuong nao trong danh sach")
