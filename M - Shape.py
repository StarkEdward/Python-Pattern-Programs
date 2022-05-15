# Python Pattern Program Printing Stars in "M" Shape

for r in range(7):
    for c in range(7):
        if (c == 0 or c == 6) or (r==c and (c>0 and c<4)) or ((r==1 and c == 5) or (r == 2 and c == 4)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()