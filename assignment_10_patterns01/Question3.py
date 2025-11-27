






n=int(input("Enter no of rows: "))
x=1
for i in range(n):
    for j in range(n):
        print(x,end=" ")
        x+=2
    print()
    x-=4
