






a=int(input("Enter First side of triangle: "))
b=int(input("Enter Second side of triangle: "))
c=int(input("Enter Third side of triangle: "))

if a+b+c==180:
    if a<90 and b<90 and c<90:
        print("Acute Angle")
    elif a >90 or b>90 or c>90:
        print("Obtus angle")
    else:
        print("Notan Acute nor Obtus")
else:
    print("Invalid Triangle")

