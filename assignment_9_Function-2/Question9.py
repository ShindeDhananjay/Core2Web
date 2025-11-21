



x=int(input("Enter the number: "))
def check(x):
    y=x
    count=0
    while y>0:
        if x%y==0:
            count+=1
        y-=1
    if count==2:
        return "Not a Composite num"
    else:
        return "Composite num"

print(check(x))
