

for r in range(9):
    for c in range(13):
        if (r == 2 or r == 6)or (r+c == 6) or (c-r == 6) or (r+c == 14) or (r - c == 2

        ):
            print("*", end="")
        else:
            print(end=" ")
    print()