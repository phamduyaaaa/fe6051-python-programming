import math
from colorama import Fore, init

init(autoreset=True)

def make_a_dictionary(mang):
	new_dict = {}
	for i in mang:
		new_dict[i] = math.sqrt(i)
		
	return new_dict
		
def check_scp(num):
	check = 0
	if num == 0 or num == 1:
		check = 1
	else:
		for i in range(num):
			if i*i == num:
				check = 1
				break
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
scp_dict = {}
non_scp_dict = []

for key, value in new_dict.items():
	if check_scp(key):
		scp_dict[key] = value
	else:
		non_scp_dict.append(key)

print (Fore.GREEN + f"{scp_dict}")
print("Tuple chứa các số không chính phương trong danh sách đã nhập:")
print(Fore.GREEN + f"{tuple(non_scp_dict)}")
		
	
	
