









def decorFunc(funRef):
    def wrapper(*args,**kwargs):
        wrapping=input("Do you need Wrapping? : ")
        funRef(*args,**kwargs)
        print("Wrapping Needed: ",wrapping)
    return wrapper

@decorFunc
def placeOrder(x):
    print("Order Placed: ",x)

x=input("Enter the Item you want to order: ")
placeOrder(x)

