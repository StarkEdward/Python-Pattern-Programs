
# Python Pattern Program Printing Stars in "G" Shape.

for r in range(7):
	for c in range(5):
		if (c == 0 and (r!=0 and r!= 6)) or ((r == 0 or r == 6) and(c>0 and c<4)) or (c == 4 and (r> 0 and r != 2 and r != 3 and r!=6)) or (r==4 and c> 1):
			print("*", end=" ")
		else:
			print(end="  ")
	print()
print()
