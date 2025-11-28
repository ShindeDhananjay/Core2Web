


def decorFunc(funRef):
    def wrapper(*args,**kwargs):
        specialRequest=input("Enter speacial request if you have any: ")
        funRef(*args,**kwargs)
        print("Speacial Request are : ",specialRequest)
    return wrapper

@decorFunc
def reserveTable(x):
    print("Reserved Table number is: ",x)
x=input("Enter Table number you want to reserve: ")
reserveTable(x)
