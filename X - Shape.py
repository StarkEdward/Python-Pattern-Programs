# Python Pattern Program Printing Stars in "X" Shape

for r in range(5):
	for c in range(5):
		if (r==c) or (r+c == 4):
			print("*",end=" ")
		else:
			print(end="  ")
	print()