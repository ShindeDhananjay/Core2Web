






a=int(input("Enter Percentages: "))
b=int(input("Enter Score: "))

if a>=90 and b>=90:
    print("Elite Program")
elif a>=80 and b>= 70:
    print("Standard Program")
elif a>= 60 and b>=50:
    print("Basic Program")
else:
    print("Not Eligible")
