str1 = input("Enter String: ")
length = len(str1)
for i in range(length+1):
    for j in range(i):
        print(str1[j], end = " ")
    print()