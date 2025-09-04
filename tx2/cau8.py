import math



class HinhHopChuNhat():
	def __init__(self,canh1, canh2, canh3):
		self.canh1 = canh1
		self.canh2 = canh2
		self.canh3 = canh3
	def dientichxungquanh(self):
		return 2*(self.canh1+self.canh2)*self.canh3

	def thetich(self):
		return self.canh1*self.canh2*self.canh3
	
	def inthongso(self):
		print(f"Canh1: {self.canh1} | Canh2: {self.canh2} | Canh3: {self.canh3} | Dien tich xung quanh: {self.dientichxungquanh()} | The tich: {self.thetich()}")
		
		
hinhhopchunhat_l = []
def nhapcanh(n):
	for i in range(n):
		print(f"Nhap thong so hinh {i+1}:")
		while True:
			try:
				canh1 = float(input("Nhap canh 1: "))
				canh2 = float(input("Nhap canh 2: "))
				canh3 = float(input("Nhap canh 3: "))
				if canh1*canh2*canh3 <= 0:
					print("Do dai cac canh phai la so thuc duong!")
				else:
					h = HinhHopChuNhat(canh1, canh2, canh3)
					hinhhopchunhat_l.append(h)
					break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")

while True:
	try:
		n = int(input("Nhap so luong hinh hop chu nhat n = "))
		if n <= 0:
			print("n phai la so nguyen duong!")
		else:
			nhapcanh(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")

cnt = 0
tenhinh = math.inf
tongthetich = 0
thetichlonnhat = -math.inf
for i in hinhhopchunhat_l:
	cnt +=1
	print("-----")
	print(f"Thong so hinh {cnt}: ")
	i.inthongso()
	tongthetich += i.thetich()
	if thetichlonnhat <= i.thetich():
		thetichlonnhat = i.thetich()
		tenhinh = cnt
print("-----")
print(f"Hinh {tenhinh} la hinh co the tich lon nhat = {thetichlonnhat}")
	
				
				
