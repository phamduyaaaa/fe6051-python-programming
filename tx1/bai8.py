import math
from colorama import Fore, init

init(autoreset=True)

def max_am_min_duong(mang):
	check_max_am = -math.inf
	check_min_duong = math.inf
	index_max_am = 0
	index_min_duong = 0
	index = 0
	for i in mang:
		index +=1
		if i < 0 and i > check_max_am:
			check_max_am = i
			index_max_am = index
		elif i > 0 and i < check_min_duong:
			check_min_duong = i	
			index_min_duong = index
	return index_max_am, check_max_am, index_min_duong, check_min_duong
		
def trungbinhcong(mang):
	cnt_am = 0
	cnt_duong = 0
	tong_am = 0
	tong_duong = 0
	for i in mang:
		if i < 0:
			cnt_am +=1
			tong_am +=i
		else:
			cnt_duong +=1
			tong_duong +=i
	tbc_am = tong_am/cnt_am
	tbc_duong = tong_duong/cnt_duong
	return tbc_am, tbc_duong

def make_a_dictionary(mang):
	index_max_am, check_max_am, index_min_duong, check_min_duong = max_am_min_duong(mang)
	new_dict = {index_max_am:check_max_am,index_min_duong:check_min_duong}
	return new_dict
	
	
	
l = []
while True:
	try:
		num = input("Nhap n số thực (n là tùy ý, kết thúc nhập khi bấm phím ‘t’: ")
		if num == "t":
			print(f"Ket thuc nhap, dictionary có key là các số trong danh sách vừa nhập: ")
			print("{Vị trí số âm lớn nhất:Số âm lớn nhất,Vị trí số dương lớn nhất:Số dương lớn nhất}")
			break
		l.append(float(num))
		
	except ValueError:
		print("Nhap khong dung, vui long nhap lai!")

new_dict = make_a_dictionary(l)
print(Fore.GREEN + f"{new_dict}")
print("Các tuple chứa số âm lớn nhất và số dương nhỏ nhất có trong danh sách đã nhập: ")
print("{Số âm lớn nhất, Số dương lớn nhất}")
print(Fore.GREEN + f"{tuple(new_dict.values())}")
