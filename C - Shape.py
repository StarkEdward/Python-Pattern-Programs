#Date 12/05/2022 
#Python Pattern Program that prints "C" letter

for r in range(7):
	for c in range(5):
		if (c ==0 and (r != 0 and r != 6)) or ((r ==0 or r ==6) and (c>0)):
			print("*", end= " ")
		else:
			print(end="  ")
	print()
print()