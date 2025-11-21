





a=int(input("Enter income: "))

if a>= 250000:
    if a>=500000:
        if a>=1000000:
            print("Tax to be paid: ",a+0.03*a)
        else:
            print("Tax to be paid: ",a+0.2*a)

    else:
        print("Tax to be paid: ",a+0.05*a)
else:
    print(a)
