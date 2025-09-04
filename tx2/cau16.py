import math



class SoThuc():
	def __init__(self, giatri):
		self.giatri = giatri
	
	def check_am(self):
		return self.giatri < 0
	
	def check_duong(self):
		return self.giatri > 0
	
	def demso_saudauphay(self):
		cnt = 0
		cnt_nguyen = 0
		str_giatri = str(self.giatri)
		if '.' in str_giatri:
			return len(str_giatri.split('.')[1])
		else:
			return 0
				
l = []		
def nhapso(n):
	for i in range(n):
		while True:
			try:
				giatri = float(input(f"Nhap gia tri so thu {i+1}: "))
				l.append(SoThuc(giatri))
				break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
		

while True:
	try:
		n = int(input("Nhap so luong so thuc 'n': "))
		if n <= 0:
			print("'n' phai la so nguyen duong.")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")


for i in range(n):
	print(f"So thu {i+1}: Gia tri = {l[i].giatri} | check am = {l[i].check_am()} | check duong = {l[i].check_duong()}")

print("Cac so duong la:")
tich_am = 1
cnt = 0
for i in l:
	if i.check_duong() == True:
		print(i.giatri)
	if i.check_am() == True:
		tich_am *= i.giatri
		cnt += 1

if cnt != 0:
	print(f"Tich cac so am la: {tich_am}")
else:
	print("Khong co so am trong danh sach.")
	
		
		
		
	
	
	
