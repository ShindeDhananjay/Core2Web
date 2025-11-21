





a=input("Enter Character: ")
if 65<=ord(a)<=90:
    print("Uppercase Letter")
elif(97<=ord(a)<=122):
    print("LoweCase Letter")
elif(48<=ord(a)<=57):
    print("Digit")
else:
    print("Special Character")
