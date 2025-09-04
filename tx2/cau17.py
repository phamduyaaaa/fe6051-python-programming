import math


class PTBacHai():
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def timnghiem(self):
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
				x = (-self.b)/2*self.a
				return (x,)
			else:
				x1 = (- self.b + math.sqrt(delta))/2*self.a
				x2 = (- self.b - math.sqrt(delta))/2*self.a
				return (x1,x2,)
l = []
def nhapso(n):
	for i in range(n):
		while True:
			try:
				print(f"Nhap thong so phuong trinh {i+1}")
				a = float(input("Nhap a = "))
				b = float(input("Nhap b = "))
				c = float(input("Nhap c = "))
				l.append(PTBacHai(a,b,c))
				break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
def inthongso():
	for i in range(n):
		print(f"Phuong trinh {i+1}: a = {l[i].a} | b = {l[i].b} | c = {l[i].c} | Nghiem: {l[i].timnghiem()}")

def tao_tuple():
	result = ()
	check = 0
	for i in l:
		if i.timnghiem() == "Phuong trinh vo nghiem":
			continue
		elif i.timnghiem() == "Phuong trinh vo so nghiem":
			check = 2
			break
		else:
			result += i.timnghiem()
			check = 1
	if check == 0:
		print(f"Tuple: {result} | Ca 2 phuong trinh deu vo nghiem")
	elif check == 1:
		print(f"Tuple: {result}")
	elif check == 2:
		print(f"Tuple: {result} | Ton tai phuong trinh vo so nghiem ")

def nghiemlonnhat():
	result = ()
	check = 0
	for i in l:
		if i.timnghiem() == "Phuong trinh vo nghiem":
			continue
		elif i.timnghiem() == "Phuong trinh vo so nghiem":
			check = 2
			break
		else:
			result += i.timnghiem()
			check = 1
	if check == 0:
		print(f"Khong co nghiem lon nhat | Ca 2 phuong trinh deu vo nghiem")
	elif check == 1:
		print(f"Nghiem lon nhat la: {max(result)}")
	elif check == 2:
		print(f"Khong co nghiem lon nhat | Ton tai phuong trinh vo so nghiem ")
		
while True:
	try:
		n = int(input("Nhap so luong phuong trinh 'n': "))
		if n<= 0:
			print("'n' phai la so nguyen duong")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
		
# In thong tin PT + Nghiem
inthongso()
tao_tuple()
nghiemlonnhat()

		
