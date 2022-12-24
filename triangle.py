side1 = int(input("Length of Side 1 is: "))
side2 = int(input("Length of Side 2 is: "))
side3 = int(input("Length of Side 3 is: "))
if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("Yes")
else:
    print("No")