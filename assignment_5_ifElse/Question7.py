


a=int(input("Enter the Number of Month"))
match a:
    case 1:
        print("January has 31 days")
    case 2:
        print("Feb has 29 days")
    case 3:
        print("March has 31 days")
    case 4:
        print("April has 30 days")
    case 5:
        print("May has 31 days")
    case 6:
        print("June has 30 days")
    case 7:
        print("July has 31 days")
    case 8:
        print("Aug has 31 days")
    case 9:
        print("Sept has 30 days")
    case 10:
        print("Oct has 31 days")
    case 11:
        print("November has 30 days")
    case 12:
        print("Dec has 31 days")
    case _:
        print("Invalid Month")
