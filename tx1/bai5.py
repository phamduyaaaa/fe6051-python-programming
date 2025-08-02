import math
from colorama import Fore, init

init(autoreset=True)

def make_a_dictionary(mang):
	new_dict = {}
	for i in mang:
		new_dict[i] = i+1
		
	return new_dict
		
def tinh_giai_thua(songuyen):
	check = 1
	for i in range(2,songuyen+1):
		check *= songuyen
		#check = songuyen * check
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
giai_thua_dict = []

for key, value in new_dict.items():
	giai_thua_dict.append(tinh_giai_thua(key))
	


print(Fore.GREEN + f"{new_dict}")
print("Tuple chứa giai thừa của các số nguyên tố trong danh sách đã nhập: ")
print(Fore.GREEN + f"{tuple(giai_thua_dict)}")
		
	
	
