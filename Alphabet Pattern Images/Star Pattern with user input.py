# star shape pattern by user input

n = int(input("Enter number of rows (grater than 5): "))
col = n + n - 5
mid = col // 2

for r in range(n):
    for c in range(col):
        if (r == 2 or r == n-3) or(r + c == mid) or (c - r == mid) or(r - c == 2) or (r + c == col + 1):
            print("*", end="")
        else:
            print(end=" ")
    print()