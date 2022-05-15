# Python Pattern Program Printing Stars in "N" Shape

for r in range(6):
    for c in range(6):
        if (c == 0 or c == 5) or (r == c and (c > 0 and c < 5)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()