






n=int(input("Enter no of rows: "))
for i in range(n):
    x=n
    for j in range(i+1):
        print(x,end=" ")
        x-=1
    print()
