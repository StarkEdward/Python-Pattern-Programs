# Python Pattern Program Printing Stars in "J" Shape

for r in range(7):
    for c in range(7):
        if (r == 0 and c > 1) or ((r == 6 and c > 0 and c < 4)) or (c == 0 and(r > 3 and r < 6))or (c == 4 and (r > 0 and r < 6)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()