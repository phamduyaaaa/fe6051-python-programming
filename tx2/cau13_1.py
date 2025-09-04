class SoNguyen():
	def __init__(self, giatri):
		self.giatri = giatri
		
	def check_amduong(self):
		if self.giatri == 0:
			return 0
		elif self.giatri > 0:
			return 1
		else:
			return -1
			
	def check_sodoixung(self):
		check = str(self.giatri[::-1])
		if check == self.giatri:
			return True
		return False
		
	def check_sohoanthien(self):
		tong = 0
		for i in range(self.giatri+1):
			if self.giatri % i == 0:
				tong += i
		if tong == self.giatri:
			return True
		return False
	
	def check_sochinhphuong(self):
		if self.giatri == 0 or self.giatri == 1:
			return True
		else:
			for i in range(self.giatri+1):
				if i**2 == self.giatri:
					return True
		return False
	
	def check_songuyento(self):
		if self.giatri <= 0:
			return False
		else:
			for i in range(self.giatri):
				if self.giatri % i == 0:
					return False
		return True
	
	def check_chanle(self):
		return self.giatri % 2 == 0

class SoThuc():
	def __init__(self, giatri):
		self.giatri = giatri
	def dem_saudauphay(self):
		check = str(self.giatri)
		if '.' in check:
			cnt = len(check.split(".")[1])
			return cnt
		else:
			return 0
		


a = SoThuc(12)
print(a.dem_saudauphay())
				
		
	
	
