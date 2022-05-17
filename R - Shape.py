# Python Pattern Program Printing Stars in "R" Shape
for r in range(7):
	for c in range(5):
		if c== 0 or ((r == 0 or r == 3) and(c<4)) or (c == 4 and (r>0 and r< 3)) or (r == c+2 and c>0):
			print("*",end=" ")
		else:
			print(end="  ")
	print()