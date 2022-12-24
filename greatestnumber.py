print("Enter any three integers:")
num1 = int(input(" "))
num2 = int(input(" "))
num3 = int(input(" "))
if(num1>num2 and num1>num3):
    print(num1, " is the greatest of the three")
else:
    if(num2>num1 and num2>num3):
        print(num2, " is the greatest of the three")
    else:
        if(num3>num1 and num3>num2):
            print(num3, " is the greatest of the three")
        else:
            print("Atleast one number is equal to another")