print("--- eymenefekarabacak Calculator v3.0 ---")

while True:
    print("\n--- New Operation ---")
    
    choice = input("Press Enter to continue or 'q' to quit: ")
    if choice.lower() == 'q':
        print("Exiting... Goodbye!")
        break

    try:
        number1 = float(input("Enter first number: "))
        operation = input("Choose operation (+, -, *, /, %): ")
        number2 = float(input("Enter second number: "))

        if operation == "+":
            print("Result: ", number1 + number2)
        elif operation == "-":
            print("Result: ", number1 - number2)
        elif operation == "*":
            print("Result: ", number1 * number2)
        elif operation == "/":
            if number2 == 0:
                print("Error: Division by zero!")
            else:
                print("Result: ", number1 / number2)
        elif operation == "%":
            print("Result: ", number1 % number2)
        else:
            print("Invalid operation!")
            
    except ValueError:
        print("Error: Please enter a valid number!")

    print("-----------------------")