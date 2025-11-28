







def eventBooking(eventType):
    def calculateFinalPrice():
        match eventType:
            case 'concert':
                ticketPrice=1200
            case 'seminar':
                ticketPrice=800
            case 'workshop':
                ticketPrice=500
            case _:
                print("Invalid Event Type")
                return None


        noOfTickets=int(input("Enter the Number of Tickets for your Event: "))

        totalPrice=noOfTickets * ticketPrice

        discount=0
        finalAmount=totalPrice
        if noOfTickets>5:
            discount=totalPrice*0.1
            finalAmount=totalPrice-discount

        return ticketPrice,discount,finalAmount
    
    retVal=calculateFinalPrice()
    if retVal==None:
        return None

    ticketPrice=retVal[0]
    discount=retVal[1]
    finalAmount=retVal[2]
    print("Event Type is: ",eventType)
    print("Ticket Price for",eventType,"is: ",ticketPrice)
    print("Discount Applied : ",discount)
    print("Final Amount: ",finalAmount)

eventType=input("Enter the Event Type :")
eventBooking(eventType)
