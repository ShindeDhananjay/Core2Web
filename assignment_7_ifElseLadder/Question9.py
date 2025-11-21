








a=int(input("Enter Purchase Amount: "))

dis=0
finalamt=a

if a>1000:
    if a>=5000:
        if a>=10000:
            if a>=20000:
                dis=30
                finalamt=a-0.3*a
            else:
                dis=20
                finalamt=a-0.2*a
        else:
            dis =10
            finalamt=a-0.1*a
    else:
        dis=5
        finalamt=a-0.05*a


print("Discount Applied: ",dis,"%")
print("Final Amount: ",finalamt)
