class SoNguyen():
	def __init__(self, giatri):
		self.giatri = giatri
		
	def lapphuong(self):
		return self.giatri**3
		



a1 = SoNguyen(1)
a2 = SoNguyen(6)
a3 = SoNguyen(7)
a4 = SoNguyen(160)
a5 = SoNguyen(55)
l = [a1, a2, a3, a4, a5]

#C1
l.sort(key = lambda songuyen: songuyen.lapphuong(), reverse=False)

for i in l:
	print(i.giatri, end =" ")
print()
#C2
def lay_lapphuong(songuyen):
	return songuyen.lapphuong()
	
l.sort(key = lay_lapphuong, reverse=False)

for i in l:
	print(i.giatri, end =" ")
print()

# Xoa nhung so nho hon 50 hoac lon hon 2
l = [i for i in l if i.giatri < 2 or i.giatri > 50]

for i in l:
	print(i.giatri, end =" ")
print()




