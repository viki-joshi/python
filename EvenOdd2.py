A=int(input("Enter a number="))
if((A%2)==0 and A>=100):
    print("Number is even")
elif((A%2)!=0 and A>=100):
    print("Number is odd")
else:
    print("Please enter a number greater than 100")