# so nguyen to phai lon hon 1
# so chinh phuong phai lon hon 0
# so hoan hao == so hoan thien (tonguoccon == chinh no)
class So():
	def __init__(self, giatri):
		self.giatri = giatri
	
	def check_chinhphuong(self):
		if self.giatri <= 0:
			return False
		else:
			for i in range(self.giatri+1):
				if i*i == self.giatri:
					return True
		return True
	
	
	def check_songuyento(self):
		if self.giatri <= 1:
			return False
		else:
			for i in range(2,self.giatri):
				if self.giatri % i == 0:
					return False
		return True
	
	def check_amduong(self):
		if self.giatri == 0:
			return "Gia tri bang 0"
		elif self.giatri < 0:
			return "So am"
		else:
			return "So duong"
	
	def dem_thapphan(self):
		check = str(self.giatri)
		if '.' in check:
			cnt = len(check.split(".")[1])
			return cnt
		else:
			return 0
	
	def check_sohoanhao(self):
		tonguoccon = 0
		for i in range(self.giatri):
			if self.giatri % i == 0:
				tonguoccon += i
		
		return tonguoccon == self.giatri
	
	def check_sodoixung(self):
		check = str(self.giatri)
		return check[::-1] == check
		
	
		
		
		
		
		
		
		
				
		
