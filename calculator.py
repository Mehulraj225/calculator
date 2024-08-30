#Message
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
x=int(input("Enter the choice :\n"))
if(x==1):
    print("add")
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    print(a+b)
elif(x==2):
    print("sub")
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    print(a-b)
elif(x==3):
    print("product")
    a=int(input("Enter the 1st number; "))
    b=int(input("Enter the 2nd number: "))
    print(a*b)
elif(x==4):
    print("divide")
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))
    print(a/b)
else:
    print("There is not any operation......!")
    print("Please enter the valid number")