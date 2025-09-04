import math

class SinhVien():
	def __init__(self, diem):
		self.diem = diem
	
	
	def tinhdiemtb():
		return self.diem*2
		

a1 = SinhVien(10)
a2 = SinhVien(9)
a3 = SinhVien(5)
a4 = SinhVien(11)

l = [a1, a2, a3, a4]

for i in l:
	print(i.diem, end = " ")


#Sap xep theo diem trung binh giam dan
#Cach 1
l.sort(key = lambda i: i.tinhdiemtb, reverse=False)

#Cach 2
def laydiemtb(i):
	return i.tinhdiemtb()
l.sort(key = laydiemtb, reverse=False)

print()


	

