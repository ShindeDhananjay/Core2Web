







def decorFunc(funRef):
    def wrapper(*args,**kwargs):
        toppings=input("Enter additional toppings if you want : ")
        funRef(*args,**kwargs)
        print("Additional Toppings are: ",toppings)
    return wrapper

@decorFunc
def orderPizza(a):
    print("Ordered Pizza is: ",a)
pizza=input("Enter the pizza you wanna order: ")
orderPizza(pizza)

