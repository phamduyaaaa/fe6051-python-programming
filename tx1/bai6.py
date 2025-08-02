import math
from colorama import Fore, init

init(autoreset=True)

def make_a_dictionary(mang):
	new_dict = {}
	for i in mang:
		new_dict[i] = tinh_tong(i)
		
	return new_dict
		
def tinh_tong(songuyen):
	check = 0
	if songuyen > 1:
		for i in range(1,songuyen+1):
			check += i
	else:
		for i in range(songuyen,2):
			check += i
	return check
		
		
l = []

while True:
	try:
		num = input("Nhap so nguyen, ket thuc nhap khi bam phim 't: ")
		if num == 't':
			print(f"Ket thuc nhap, dictionary có key là các số trong danh sách vừa nhập: ")
			break
		l.append(int(num))
	except ValueError:
		print("Nhap khong dung, vui long nhap lai!")
	
new_dict = make_a_dictionary(l)
tong_dict = []

for key, value in new_dict.items():
	tong_dict.append(tinh_tong(key))
	


print(Fore.GREEN + f"{new_dict}")
print("Tuple chứa tổng các số từ 1 đến từng số có trong danh sách đã nhập: ")
print(Fore.GREEN + f"{tuple(tong_dict)}")
		
	
	
