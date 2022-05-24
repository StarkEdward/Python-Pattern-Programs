
n = input("Enter an odd length numbers: ")
length = len(n)
for r in range(length):
    for c in range(length):
        if (r == c) or (r+c == length -1):
            print(n[r],end=" ")
        else:
            print(end="  ")
    print()