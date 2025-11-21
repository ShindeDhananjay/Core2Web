


year =int(input())
if year %400:
    print(year,"is leep Year")
else:
    if(year%4==0) and (year%100!= 0):
        print(year,"is leep Year")
    else:
        print(year,"is not a leep Year")

