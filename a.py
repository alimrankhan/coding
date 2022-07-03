k= int(input())

if k>=60:
	if (k-60)>9:
		print(f"22:{k-60}")
	else:
		print(f"22:0{k-60}")
else:
	if(k>9):
		print(f"21:{k}")
	else:
		print(f"21:0{k}")
