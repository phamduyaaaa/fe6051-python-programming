import math

class ConOng():
	def __init__(self, loaiong, vantoc, thoigian):
		self.loaiong = loaiong
		self.vantoc = vantoc
		self.thoigian = thoigian
	
	def quangduong(self):
		return math.fabs(self.vantoc * self.thoigian)
	
	
l = []
def nhapso(n):
	for i in range(n):
		while True:
			try:
				print(f"Nhap thong so con ong {i+1}:")
				loaiong = input("Nhap loai ong: ")
				vantoc = float(input("Nhap van toc: "))
				thoigian = float(input("Nhap thoi gian: "))
				if thoigian <= 0 :
					print("Thoi gian phai la so duong")
				else:
					l.append(ConOng(loaiong, vantoc, thoigian))
					break
			except ValueError:
				print("Nhap khong hop le, nhap lai!")
def indanhsach():
	for i in range(n):
		print(f"Con ong {i+1}: Loai ong = {l[i].loaiong} | Van toc = {l[i].vantoc} | Thoi gian = {l[i].thoigian} | Quang duong = {l[i].quangduong()}")

def ong_nhanhnhat():
	v_max = - math.inf
	idx = math.inf
	l_max = []
	cnt = 0
	for i in range(n):
		if l[i].vantoc >= v_max:
			v_max = l[i].vantoc
			idx = i+1
	for i in range(n):
		if l[i].vantoc == v_max:
			l_max.append(i+1)
			cnt +=1
	if cnt == 1:
		print(f"Con ong {idx} co van toc nhanh nhat = {v_max}")
	elif cnt == n:
		print(f"{n} con ong deu co van toc bang nhau = {v_max}")
	else:
		print(f"{cnt} con ong co van toc nhanh nhu nhau = {v_max} | {l_max}")
		
def quangduong_dainhat():
	l_quangduong = []
	cnt = 0
	for i in range(n):
		l_quangduong.append(l[i].quangduong())
	quangduong_max = max(l_quangduong)
	for i in l_quangduong:
		if i == quangduong_max:
			cnt +=1
	if cnt == n:
		print(f"Tat ca {cnt} con ong deu bay duoc quang duong bang nhau = {quangduong_max}")
	else:
		print(f"Co {cnt} con ong bay duoc quang duong dai nhat = {quangduong_max}")
		
while True:
	try:
		n = int(input("Nhap so luong con ong 'n': "))
		if n <= 0:
			print("'n' phai la so nguyen duong")
		else:
			nhapso(n)
			break
	except ValueError:
		print("Nhap khong hop le, nhap lai!")
		
indanhsach()
ong_nhanhnhat()
quangduong_dainhat()

		
		
		
		
		
		
		
