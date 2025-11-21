




a=int(input("Enter the number: "))

def fact(a):
    if a==0:
        return 1
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
print(f"Factorial of {a} is {fact(a)}")
