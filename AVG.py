A=int(input("enter marks of subject 1="))
B=int(input("enter marks of subject 2="))
C=int(input("enter marks of subject 3="))
D=int(input("enter marks of subject 4="))
E=int(input("enter marks of subject 5="))
avg=(A+B+C+D+E)/5
print(avg)
if(avg)>=90:
    print("Grade A")
elif(avg)>=80:
    print("Grade B")
elif(avg)>=70:
    print("Grade C")
elif(avg)>=60:
    print("Grade D")
else:
    print("Fail")