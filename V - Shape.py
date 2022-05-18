# Python Pattern Program Printing Stars in "V" Shape
for  r in range(4):
	for  c in range(7):
		if (r == c) or ( r + c == 6):
			print("*", end =" ")
		
		else:
			print(end=" ")
	print()
		