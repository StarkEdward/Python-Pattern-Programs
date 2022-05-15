# Python Pattern Program Printing Stars in "K" Shape

i = 0
j = 4
for r in range(7):
    for c in range(5):
        if c == 0 or (r == c+2 and c> 0):
            print("*", end=" ")
        elif (r == i and c == j) and (c > 0):
            print("*", end=" ")
            i += 1
            j-= 1
        else:
            print(end="  ")
    print()