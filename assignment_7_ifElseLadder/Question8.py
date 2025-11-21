








a=int(input("Enter Number: "))
if a!=0 and a>=0 and a%2==0:
    print("Positive Even")
elif a!=0 and  a>=0 and a%2!=0:
    print("Positive Odd")
elif a<0 and a%2==0:
    print("Negetive Even")
elif a<0 and a%2!=0:
    print("Negetive Odd")
else:
    print("Zero")
