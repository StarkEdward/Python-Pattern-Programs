n = int(input("Enter number of row: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print()