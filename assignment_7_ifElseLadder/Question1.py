


a=int(input("Enter Age: "))
b=int(input("Enter Weight: "))
c=float(input("Enter HB: "))

if (18<=a<=65):
    if(b>=40):
        if (c>=12.5):
            print("Eligible for blood donation")
        else:
            print("Not Eligible for blood donation")
    else:
        print("Not Eligible for blood donation")
else:
    print("Not Eligible for blood donation")

