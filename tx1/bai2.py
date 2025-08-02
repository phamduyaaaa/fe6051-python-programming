def make_a_tuple(l):
	return tuple(l)

def check_snt(snt):
	check = 1
	for i in range(2,snt):
		if(snt%i==0):
			check = 0
			break
	return check
			

l = []
while True:
	try:
		num = input("nhap n so nguyen, ket thuc nhap khi bam phim 't': ")
		if (num =='t'):
			print("Ket thuc nhap!")
			break
		f = int(num)
		l.append(f)
	except:
		print("Nhap so khong hop le, nhap lai!")
l_snt = []
for i in l:
	if check_snt(i):
		l_snt.append(i)
		

print("Tuple chứa các số trong danh sách vừa nhập: ")
print(make_a_tuple(l))
print(f"tuple chứa các số nguyên tố trong danh sách đã nhập: ")
print(make_a_tuple(l_snt))

			

		
