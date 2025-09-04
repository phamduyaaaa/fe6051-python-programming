
class HinhTuGiac():
	def __init__(self, canh1, canh2, canh3, canh4):
		self.canh1 = canh1
		self.canh2 = canh2
		self.canh3 = canh3
		self.canh4 = canh4
	
	def chuvi(self):
		return self.canh1 + self.canh2 + self.canh3 + self.canh4
	
	def canhlonnhat(self):
		return max(self.canh1, self.canh2, self.canh3, self.canh4)


def nhapcanh():
	while True:
		try:
			canh1 = int(input("Nhap canh1: "))
			canh2 = int(input("Nhap canh2: "))
			canh3 = int(input("Nhap canh3: "))
			canh4 = int(input("Nhap canh4: "))
			if (canh1 <=0 or canh2 <=0 or canh3 <= 0 or canh4 <=0):
				print("Canh phai la so duong!")
			else:
				f = HinhTuGiac(canh1, canh2, canh3, canh4)
				l_hcn.append(f)
				break
		except ValueError:
			print("Nhap so khong hop le, nhap lai!")	
l_hcn = []
while True:
	try: 
		n = int(input("Nhap so hinh hcn: "))
		if n < 0:
			print("so hinh hcn phai la so duong!")
		else:
			for i in range(n):
				print(f"Nhap thong so hinh {i+1}")
				nhapcanh()		
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")


chuvi_max_value = -999
chuvi_max_index = -1
for i in l_hcn:
	cnt = 1
	print(f"Canh lon nhat cua hinh {cnt} la: {i.canhlonnhat()}")
	cnt +=1
	if (chuvi_max_value <= i.chuvi()):
		chuvi_max_value = i.chuvi()
		chuvi_max_index = cnt

print(f"Hinh co chu vi lon nhat la: {chuvi_max_index} voi chu vi la:  {chuvi_max_value}")
	
	

	
	





	
