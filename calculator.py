while True:
        status = input('Press any key to start or Q to quit: ')
        if status == "q":
            quit()
        else:
            selection1 =input('Please input the first number: ')
        if not selection1.isdigit():
            print('Please enter a number next time!')
            quit()
        else:
            number1 = int(selection1)
        conditions = ["+", "-", "/", "*", "%"]
        operation = input('Please enter an operation ( + , - , / , * , %): ')
        if operation not in conditions:
            print ('Please type in a valid operation!')
        else:
            selection2 =input('Please input the Second number: ')
        if not selection2.isdigit():
            print('Please enter a number next time!')
            quit()
        else:
            number2 = int(selection2)
        
        if operation == "+":
            print(selection1, operation , selection2 , " = ", (number1 + number2))
        elif operation == "-":
            print(selection1, operation , selection2 , " = ", (number1 - number2))
        elif operation == "/":
            print(selection1, operation , selection2 , " = ", (number1 / number2))
        elif operation == "*":
            print(selection1, operation , selection2 , " = ", (number1 * number2))
        elif operation == "%":
            print(selection1, operation , selection2 , " = ", (number1 % number2))
    