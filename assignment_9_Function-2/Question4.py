







start=int(input("Enter Start:"))
end=int(input("Enter End: "))

def calc(start,end):
    sum=0
    while (start<=end):
        sum +=start
        start+=1
    return sum
print(f"Sum of range between {start} and {end} is {calc(start,end)}")
