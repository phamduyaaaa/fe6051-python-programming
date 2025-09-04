import math


class PTBacHai():
	def __init__(self, a,b,c):
		self.a = a
		self.b = b
		self.c = c
		
	def tinhnghiem(self):
		if self.a == 0 and self.b == 0 and self.c == 0:
			return "Phuong trinh vo so nghiem"
		elif self.a == 0 and self.b == 0 and self.c != 0:
			return "Phuong trinh vo nghiem"
		elif self.a == 0 and self.b != 0:
			return (-self.c/self.b,)
		else:
			delta = self.b**2 - 4*self.a*self.c
			if delta < 0:
				return "Phuong trinh vo nghiem"
			elif delta == 0:
				x = -self.b/2*self.a
				return (x,)
			else:
				x1 = (-self.b + math.sqrt(delta))/2*self.a
				x2 = (-self.b - math.sqrt(delta))/2*self.a
				return (x1,x2,)
	
l = []
def nhapso(n):
	for i in range(n):
		while True:
			try:
				print(f"Nhap thong so phuong trinh {i+1}:")
				a = float(input("Nhap a = "))
				b = float(input("Nhap b = "))
				c = float(input("Nhap c = "))
				l.append(PTBacHai(a,b,c))
				break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
def inthongso():
	for i in range(n):
		print(f"PT {i+1}: a = {l[i].a} | b = {l[i].b} | c = {l[i].c } | Nghiem PT: {l[i].tinhnghiem()} ")

def demvonghiem():
	cnt = 0
	for i in l:
		if i.tinhnghiem() == "Phuong trinh vo nghiem":
			cnt +=1
	if cnt == n:
		print(f"Tat ca {n} phuong trinh deu vo nghiem")
	elif cnt != 0:
		print(f"Co {cnt} phuong trinh vo nghiem")
	else:
		print("Khong co phuong trinh nao vo nghiem")
		
def demnghiemduong():
	tuple_nghiem = ()
	cnt = 0
	for i in l:
		if i.tinhnghiem() == "Phuong trinh vo so nghiem":
			cnt = math.inf
			break
		if i.tinhnghiem() != "Phuong trinh vo nghiem" and i.tinhnghiem() != "Phuong trinh vo so nghiem":
			tuple_nghiem += i.tinhnghiem()
	for i in tuple_nghiem:
		if i > 0:
			cnt +=1
	if cnt == 0:
		print("Cac phuong trinh khong co nghiem duong")
	elif cnt == math.inf:
		print("Cac phuong trinh co vo so nghiem duong")
	else:
		print(f"Cac phuong trinh co {cnt} nghiem duong")
		
			
while True:
	try:
		n = int(input("Nhap so luong phuong trinh 'n': "))
		if n <= 0:
			print("'n' phai la so nguyen duong")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
		
inthongso()
demvonghiem()
demnghiemduong()

				
	
	
	
