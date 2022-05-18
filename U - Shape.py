# Python Pattern Program Printing Stars in "U" Shape

for r in range(6):
	for c in range(5):
		if ((c == 0 or c == 4) and r != 5) or (r == 5 and (c>0 and c<4)) :
			print("*", end=" ")
		else:
			print(end="  ")
	print()