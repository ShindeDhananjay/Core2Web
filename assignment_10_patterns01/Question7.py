






n=int(input("Enter no of rows: "))
x=n
for i in range(n):
    for j in range(n-i):
        print(x,end=" ")
        
    print()
    x-=1
