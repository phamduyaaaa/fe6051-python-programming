import math
def make_a_dictionary(mang):
	new_dict = {}
	for i in mang:
		new_dict[i] = math.sqrt(i)
	
	return new_dict

l = []


while True:
	try:
		num = input("Nhap vao so nguyen, ket thuc nhap khi bam phim 't': ")
		if num == "t":
			print("Ket thuc nhap!")
			break
		f = int(num)
		l.append(f)
	except ValueError:
		print("Nhap khong hop le, vui long nhap lai: ")
	
print("dictionary có key là các số trong danh sách vừa nhập")
print(make_a_dictionary(l))

tong_chan = 0
tong_le = 0
for i in l:
	if i%2 == 0:
		tong_chan +=i
	else:
		tong_le +=i
		
new_tuple = (tong_chan, tong_le)
print("tuple chứa các số nguyên tố trong danh sách đã nhập: ")
print(new_tuple)
