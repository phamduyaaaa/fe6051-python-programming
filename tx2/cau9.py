import math


class DuongThang():
	def __init__(self, x1, y1, x2, y2):
		self.x1 = math.abs(x1)
		self.y1 = math.abs(y1)
		self.x2 = math.abs(x2)
		self.y2 = math.abs(y2)
	def dodaidoanthang(self):
		return (sqrt((self.x1-self.x2)**2 + (self.y1-self.y2)**2))
	def inthongso(self):
		print("-----")
		print(f"Toa do: Diem 1 ({self.x1},{self.y1}) | Diem 2({self.x2}, {self.y2})")
 l = []
def nhapdiem(n):
	for i in range(n):
		while True:
			try:
				x1 = float(input("Nhap x1: "))
				y1 = float(input("Nhap y1: "))
				x2 = float(input("Nhap x2: "))
				y2 = float(input("Nhap y2: "))
				h = DuongThang(x1, y1, x2, y2)
				l.append(h)
			except ValueError:
				print("Nhap khong hop le, nhap lai!")

for i in range(3):
	nhapdiem(3)

for i in l:
	i.inthongso()
	
	


	
		
