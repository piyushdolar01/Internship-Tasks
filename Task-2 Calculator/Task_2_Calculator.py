def Calculator():
    print("----- SIMPLE CALCULATOR -----")

    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))

    print("\nSelect operation:")
    print("1 - Addition (+)")
    print("2 - Subtraction (-)")
    print("3 - Multiplication (*)")
    print("4 - Division (/)")

    choice = input("Enter choice (1/2/3/4) : ")

    if choice == "1":
        result = num1 + num2
        print(f"Result : {num1} + {num2} = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"Result : {num1} - {num2} = {result}")

    elif choice == "3":
        result = num1 * num2  
        print(f"Result :{num1} * {num2} = {result}") 
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"Result : {num1} / {num2} = {result}")   
        else:
            print(" Error: Division by zero is not allowed.")     
    else:
        print("Invalid operation choice. Please select 1, 2, 3, or 4.")        
    
    

Calculator()    