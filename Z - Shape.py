#Python Pattern Program that prints "Z" letter

for r in range(6):
	for c in range(6):
		if (r == 0 or r == 5) or (r + c == 5):
			print("*", end=" ")
		else:
			print(end="  ")
	print()