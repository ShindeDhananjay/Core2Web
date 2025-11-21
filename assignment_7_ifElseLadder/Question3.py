




a=int(input("Enter units: "))
if a>100:
    if a>200:
        if a>300:
            print("Total Bill: $",a*15)
        else:
            print("Total Bill: $",a*10)
    else:
        print("Total Bill: $",a*7)
else:
    print("Total Bill: $",a*5)
