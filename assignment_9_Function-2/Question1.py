



a=int(input("Enter First Num: "))
b=int(input("Enter Second Num: "))
c=int(input("Enter Third Num: "))

def Max(a,b,c):
    if (a>b and a>c):
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return "All are equal"
print(Max(a,b,c))
