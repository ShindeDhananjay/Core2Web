



def decorFunc(funRef):
    def wrapper(*args,**kwargs):
        additional=input("Enter additional details to order your coffee if you need: ")
        funRef(*args,**kwargs)
        print("Additional Details: ",additional)
    return wrapper

@decorFunc
def orderCoffee(coffeeType):
    print("Ordered Coffee is : ",coffeeType)
coffeeType=input("Enter the type of coffee you want to order: ")
orderCoffee(coffeeType)
