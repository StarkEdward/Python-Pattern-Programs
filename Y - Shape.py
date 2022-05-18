#Python Pattern Program that prints "Y" letter

for r in range(5):
	for c in range(5):
		if (r==c and c < 2) or (r+c == 4 and c>2) or (c ==2 and (r > 1)):
			print("*",end=" ")
		else:
			print(end="  ")
	print()