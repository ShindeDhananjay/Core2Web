





n=int(input("Enter no of rows: "))
for i in range(n):
    x=n
    for j in range(n):
        if ( j<n-i-1 ) :
            print(end="  ")
        else:
            print(x,end=" ")
            x-=1
    print()
