# Python Pattern Program Printing Stars in "L" Shape

for r in range(7):
    for c in range(5):
        if c == 0 or (r == 6 and c>0):
            print("*", end=" ")
        else:
            print(end = "  ")
    print()