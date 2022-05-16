# Python Pattern Program Printing Stars in "O" Shape

for r in range(7):
    for c in range(7):
        if ((c ==0 or c==6) and (r>0 and r <6)) or ((r ==0 or r == 6) and (c > 0 and c< 6)) :
            print("*", end=" ")
        else:
            print(end="  ")
    print()