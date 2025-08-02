def dictionary_funct(mang):
	check = {}
	for i in mang:
		check[i] = i*i
	return check
	
def snt(songuyen):
	check = 1
	for j in range(2,songuyen):
		if songuyen%j==0:
			check = 0
			break
	return check

l = []
	
while 1:
  try:
    num=input("nhập số nguyên(nhập t để kết thúc): ")
    if num == 't':
      print("Ket thuc nhap!")
      break
    ptu=int(num)
    l.append(ptu)
  except ValueError:
    print("nhap lai")

print(f"dictionary có key là các số trong danh sách vừa nhập: {dictionary_funct(l)}")
print(f"cac so nguyen to la:", end= ' ')
for i in l:
	if(snt(i)):
		print(i, end=' ')
print()
	
