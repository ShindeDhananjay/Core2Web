




def decorFunc(funRef):
    def wrapper(*args,**kwargs):
        seatType=input("Enter Seat Type: ")
        funRef(*args,**kwargs)
        print("Seat Type is: ",seatType)
    return wrapper

@decorFunc
def bookTicket(x):
    print("Movie booked is: ",x)

x=input("Enter the Movie name for which you want to Book ticket: ")
bookTicket(x)
