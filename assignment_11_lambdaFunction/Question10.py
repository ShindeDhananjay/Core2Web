



leep = lambda a : True if a%400==0 or (a%4==0 and a%10!=0) else False

a=int(input("Enter Year: "))
print(a,"is Leep year: ",leep(a))
