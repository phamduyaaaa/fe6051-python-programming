import math



class DoiThiRobocon():
	def __init__(self, tendoi, sodiem, thoigian, diemtuyetdoi = 100):
		self.tendoi = tendoi
		self.sodiem = sodiem
		self.thoigian = thoigian
		self.diemtuyetdoi = diemtuyetdoi
		
	def tb_diem(self):
		return (self.sodiem/(self.thoigian*60))*10

l = []	
def nhapso(n):
	for i in range(n):
		while True:
			try:
				print(f"Nhap thong so doi {i+1}:")
				tendoi = input("Nhap ten doi: ")
				sodiem = float(input("Nhap so diem: "))
				thoigian = float(input("Nhap thoi gian: "))
				if thoigian > 3:
					print("Thoi gian toi da la 3 phut")
				elif sodiem < 0:
					print("So diem phai >= 0")
				else:
					l.append(DoiThiRobocon(tendoi,sodiem,thoigian))
					break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
def inthongso():
	for i in range(n):
		print(f"Doi Robocon {i+1}: Ten doi = {l[i].tendoi} | So Diem = {l[i].sodiem} | Thoi Gian = {l[i].thoigian} | TrungBinh 10 Giay = {l[i].tb_diem()}")
		
def dem_diemtuyetdoi():
	cnt = 0
	l_tuyetdoi = []
	for i in range(n):
		if l[i].sodiem == l[i].diemtuyetdoi:
			cnt +=1
			l_tuyetdoi.append(i+1)
	
	if cnt == 0:
		print("Khong co doi nao dat diem tuyet doi")
	elif cnt == n:
		print(f"Tat ca cac doi deu dat diem tuyet doi = {l[i].diemtuyetdoi}")
	else:
		print(f"Co {cnt} doi dat diem tuyet doi: {l_tuyetdoi}")

def sapxepgiamdan():
	l.sort(key = lambda i: i.tb_diem(), reverse = True)
	for i in range(n):
		print(f"Doi Robocon {i+1}: Ten doi = {l[i].tendoi} | So Diem = {l[i].sodiem} | Thoi Gian = {l[i].thoigian} | TrungBinh 10 Giay = {l[i].tb_diem()}")

while True:
	try:
		n = int(input("Nhap so doi 'n': "))
		if n <= 0:
			print("'n' phai la so nguyen duong")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
		

inthongso()
dem_diemtuyetdoi()
sapxepgiamdan()	





