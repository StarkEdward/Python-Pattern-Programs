# Python Pattern Program Printing Stars in "S" Shape

for r in range(7):
	for c in range(5):
		if ((r == 0 or r == 3 or  r== 6) and (c > 0 and c < 4)) or ((r == 1 or r == 2) and c == 0) or ((r == 4 or r == 5) and c == 4):
			print("*",end=" ")
		else:
			print(end="  ")
	print()