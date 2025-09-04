import math
class SoNguyen():
	def __init__(self, songuyen):
		self.songuyen = songuyen
	def check_chanle(self):
		return self.songuyen % 2 ==0
		
	def check_snt(self):
		if self.songuyen <=1:
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
	

def nhapso(n):
	for i in range(n):
		while True:
			try:
				songuyen = int(input(f"Nhap so nguyen thu {i+1} : "))
				l.append(SoNguyen(songuyen))
				break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
				

l = []
tong_scp = 0
snt_lonnhat = - math.inf
cnt_scp = 0
cnt_snt = 0
cnt_chan = 0
while True:
		try:
			n = int(input("Nhap so luong so nguyen 'n': "))
			if n <= 0:
				print("n phai la so nguyen duong!")
			else:
				nhapso(n)
				break
		except ValueError:
			print("Nhap khong hop le, nhap lai!")

print(f"Ket thuc nhap, danh sach da nhap la:", end=" ")
for i in l:
	print(i.songuyen,end = " ")
	if i.check_scp():
		cnt_scp += 1
	if i.check_snt():
		cnt_snt += 1
	if i.check_chanle():
		cnt_chan +=1
if cnt_chan != 0:
	print("\nCac so chan la:",end= " ")
else:
	print("\nKhong co so chan trong danh sach", end=" ")	
for i in l:
	if i.check_scp():
		tong_scp += i.songuyen
	if i.check_snt() and i.songuyen >= snt_lonnhat:
		snt_lonnhat = i.songuyen
	if i.check_chanle():
		print(i.songuyen, end = " ")
print(f"\nTong cac so chinh phuong la: {tong_scp}")
if snt_lonnhat != - math.inf:
	print(f"So nguyen to lon nhat la: {snt_lonnhat}")
else:
	print("Khong co so nguyen to trong danh sach!")
