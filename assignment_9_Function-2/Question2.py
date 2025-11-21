






x=int(input("Enter Number :"))

def square(x):
    res=1
    temp=1
    while res<=2:
        temp*=x
        res+=1
    return temp

print(f"Square of {x} is {square(x)}")
