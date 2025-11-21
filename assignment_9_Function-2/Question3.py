






x=int(input("Enter The number: "))

def cube(x):
    res=1
    temp=1
    while res<=3:
        temp*=x
        res+=1
    return temp

print(f"Cube of {x} is {cube(x)}")


