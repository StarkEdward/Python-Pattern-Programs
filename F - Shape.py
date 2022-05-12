# Python Pattern Program Printing Stars in "F" Shape

for r in range(7):
    for c in range(5):
        if c == 0 or r == 0 or (r == 3 and c < 4 ):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
print()