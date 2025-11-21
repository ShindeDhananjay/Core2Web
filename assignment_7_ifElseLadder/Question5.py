





a=int(input("Enter Temp: "))

if a>0:
    if a>10:
        if a>20:
            if a>30:
                if a>40:
                    print("Extreme Heat")
                else:
                    print("Hot")
            else:
                print("Warm")
        else:
            print("Cold")
    else:
        print("Very Cold")
else:
    print("Freezing Cold")
