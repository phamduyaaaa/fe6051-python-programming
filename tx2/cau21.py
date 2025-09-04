import math



class LuyThua():
	def __init__(self, giatri):
		self.giatri = giatri
	
	def binhphuong(self):
		return self.giatri**2
	
	def lapphuong(self):
		return self.giatri**3
	
	def giaithua(self):
		result = 1
		if self.giatri == 0:
			return 1
		else:
			for i in range(self.giatri+1):
				result *= self.giatri
		
		return result
def tao_dict():
	dict = {}
	for i in l:
		dict[i.giatri] = i.lapphuong()
	print(dict)

def in_giaithua():
	for i in range(n):
		print(f"Giai thua so nguyen thu {i+1}: {l[i].giaithua()}")

def tong_lapphuong():
	result = 0
	for i in l:
		result += i.lapphuong()
	print(f"Tong lap phuong cac so vua nhap la: {result}")

l = []
def nhapso(n):
	for i in range(n):
		while True:
			print(f"Nhap gia tri so nguyen thu {i+1}:")
			try:
				giatri = int(input("Gia tri = "))
				l.append(LuyThua(giatri))
				break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
def inthongso():
	for i in range(n):
		print(f"So nguyen thu {i+1}: Gia tri = {i.giatri} | Binh phuong = {i.binhphuong} | Lap phuong = {i.lapphuong} | Giai thua = {i.giaithua}")
while True:
	try:
		n = int(input("Nhap so luong so nguyen 'n': "))
		if n <= 0:
			print("'n' phai la so nguyen duong.")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
		
		
tao_dict()
in_giaithua()
tong_lapphuong()


	




	
				
			
