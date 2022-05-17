# Python Pattern Program Printing Stars in "Q" Shape

for r in range(8):
	for  c in range(5):
		if ((c == 0 or c == 4) and (r > 0 and r < 6)) or ((r ==0 or r== 6) and(c>0 and c <4)) or (r== 5 and c== 1) or ( r == 7 and c == 3) :
			print("*",end=" ")
		else:
			print(end="  ")
	print()
