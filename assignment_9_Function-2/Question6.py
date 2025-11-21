



def prod(n):
    product=1
    for i in range(1,n+1):
        product*=i
    return product
n=int(input("Enter the number: "))
print(f"Product of numbers from 1 to {n} is {prod(n)}")
