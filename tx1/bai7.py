import math
from colorama import Fore, init

init(autoreset=True)

def make_a_dictionary(mang):
	cnt_am, tong_am, cnt_duong, tong_duong = am_duong(mang)
	new_dict = {cnt_am:tong_am,cnt_duong:tong_duong}	
	return new_dict

def am_duong(mang):
	cnt_am = 0
	cnt_duong = 0
	tong_am = 0
	tong_duong = 0
	for i in mang:
		if i < 0:
			cnt_am += 1
			tong_am +=i
		else:
			cnt_duong += 1
			tong_duong +=i
	return cnt_am, tong_am, cnt_duong, tong_duong
				
		
l = []

while True:
	try:
		num = input("Nhap so nguyen, ket thuc nhap khi bam phim 't: ")
		if num == 't':
			print(f"Ket thuc nhap, dictionary có key là các số trong danh sách vừa nhập: ")
			print("{Số lượng số âm:Tổng âm, Số lượng số dương:Tổng dương}")
			break
		l.append(float(num))
	except ValueError:
		print("Nhap khong dung, vui long nhap lai!")
	
new_dict = make_a_dictionary(l)
print(Fore.GREEN + f"{new_dict}")
print("Tuple chứa tổng âm và tổng dương có trong danh sách đã nhập: ")
print("{Tổng âm, Tổng dương}")
print(Fore.GREEN + f"{tuple(new_dict.values())}")


		
	
	
