n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == 1 or i == 5:
            print(j, end=" ")
        elif j == 6-i:
            print(6-i, end= " ")
        else:
            print(end="  ")
    print()