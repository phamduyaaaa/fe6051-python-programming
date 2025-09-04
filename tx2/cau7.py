import math

class HinhTamGiacDeu():
	def __init__(self, canh):
		self.canh = canh
	
	def dodaiduongcao(self):
		return math.sqrt(self.canh**2 - (self.canh/2)**2)
	
	def dientich(self):
		return (self.dodaiduongcao()*self.canh)/2
	def chuvi(self):
		return self.canh*3
hinhtamgiacdeu_l = []
def nhapcanh(n):
	for i in range(n):
		print(f"Nhap thong so hinh {i+1}: ")
		while True:
			try:
				canh = float(input("Nhap canh: "))
				if canh <= 0:
					print("Canh phai la so thuc duong!")
				else:
					h = HinhTamGiacDeu(canh)
					hinhtamgiacdeu_l.append(h)
					break
			except ValueError:
				print("Nhap khong dung, nhap lai!")
				
while True:
	try:
		n = int(input("Nhap so luong hinh tam giac deu n ="))
		if n <=0:
			print("n phai la so nguyen duong!")
		else:
			nhapcanh(n)
			break
	except ValueError:
		print("Nhap khong dung, nhap lai!")

print(f"Do dai duong cao cua {n} hinh la: ")
tongdientich = 0
chuvinhonhat = math.inf
cnt = 0
tenhinh = 0
for i in hinhtamgiacdeu_l:
	cnt +=1
	print(i.dodaiduongcao(), end=" ")
	if chuvinhonhat >= i.chuvi():
		tenhinh = cnt
		chuvinhonhat = i.chuvi()
		
	

print(f"\nHinh {tenhinh} la hinh co chu vi nho nhat = {chuvinhonhat}")
			
				
	
