A=int(input("Enter a Year="))
if((A%4==0 and A%100!=0)  or (A%400==0)):
    print("Year is Leap")
else:
    print("Year is not leap")

