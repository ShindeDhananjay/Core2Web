




a=int(input("Enter marks of first Subject: "))
b=int(input("Enter marks of second Subject: "))
c=int(input("Enter marks of third Subject: "))
d=int(input("Enter marks of fourth Subject: "))
e=int(input("Enter marks of fifth Subject: "))

def avg(*args):
    calc=1
    temp=5
    while temp>=1:
        calc+=args[temp-1]
        temp-=1
    return calc/5

print(f"Avg of all subjects is {avg(a,b,c,d,e)}")
