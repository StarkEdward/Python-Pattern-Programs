# Python Pattern Program Printing Stars in "T" Shape

for r in range(6):
	for  c in range(5):
		if r == 0 or (c == 2 and r >0):
			print("*", end=" ")
		else:
			print(end="  ")
	print()