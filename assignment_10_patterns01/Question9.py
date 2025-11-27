




n=int(input("Enter no of rows: "))
for i in range(n):
    x=1
    for j in range(n):
        if j<i:
            print(end="  ")
            x+=1
        else:
            print(x,end=" ")
            x+=1
    print()
