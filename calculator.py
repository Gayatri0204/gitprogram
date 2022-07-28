
print("Welcome to calculator world")
while True:
    print("Menu drive program")
    print(" 1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Power")
    print("5.Division")
    print("6. Moduls")
    print("7.Exit")
    choice=int(input("Enter the choice"))
    num=int(input("Enter the num"))
    num1=int(input("Enter the num1"))
    if choice ==1:
        ans=num+num1
        print(f"Addition {ans}")
    elif choice ==2:
        ans=num-num1
        print(f"Subtraction {ans}")
    elif choice ==3:
        ans=num*num1
        print(f"multiplion {ans}")
    elif choice ==4:
        ans=num**num1
        print(f"power {ans}")
    elif choice ==5:
        ans=num/num2
        print(f"division{ans}")
    elif choice ==6:
        ans=num%num2
        print(f"moduls {ans}")
    elif choice ==7:
        break
    else:
        print("please enter the correct choice")
    
    
    
    
    
    