# Python Pattern Program Printing Stars in "W" Shape

for r in range(4):
	for c in range(7):
		if (c == 0 or c == 6) or(( r == 1 and c ==4) or (r== 2 and c == 5)) or (r+c ==3):
			print("*", end="")
		else:
			print(end=" ")
	print()