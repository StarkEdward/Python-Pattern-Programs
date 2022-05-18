#Pyt# Python Pattern Program Printing Stars in "Z" Shape

for r in range(6):
	for c in range(6):
		if (r == 0 or r == 5) or (r + c == 5):
			print("*", end=" ")
		else:
			print(end="  ")
	print()