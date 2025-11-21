






a=int(input("Enter the Number: "))

def perfectOrNot(a):
    sum=0
    x=a
    a-=1
    while a>=1:
        if x%a==0:
            sum+=a
        a-=1
    return sum
x=perfectOrNot(a)
print(x)
if x==a:
    print("Perfect Number")
else:
    print("Not Perfect Number")

