# Ask the user to input operation or read equations
menu = input('\nChoose to do an arithmetic operation(o) or to read the equations(r):\n')

while menu.lower() == 'o':
    # Ask the user for two numbers and an operator
    try:
        firstNum = float(input('\nPlease enter a number:\t'))
        operator = input('Please enter the operator:\t')
        secondNum = float(input('Please enter an other number:\t'))
        result = round(eval(f'{firstNum} {operator} {secondNum}'), 2)
        print(result)       # Display the result
        with open('calculator.txt', 'a+') as file:      # Open or create the file
            file.write(f'{firstNum} {operator} {secondNum} = {result}\n\n')     # Append the data into the file
        # Ask the user to continue with the operations or exit the program
        e = input('\nWould you like to continue(c) or exit the program(e)?\n')
        if e.lower() == 'e':
            break
        else:
            continue
    except ValueError:      # Avoid the program to crash if entered an invalid number
        print('That was not a valid number. Please try again!')
    except ZeroDivisionError:       # Avoid the program to crash if entered an invalid division
        print('Cannot divide a number by zero. Please try again!')
    except OverflowError:       # Avoid the program to crash if the result is too large
        print('Result is too large to be displayed. Please try again!')
    except SyntaxError:     # Avoid the program to crash if entered an invalid operator
        print('Invalid operator. Please use one of the following operators:\n'
              '+ Addiction\n'
              '- Subtraction\n'
              '* Multiplication\n'
              '/ Division\n'
              '% Modulus\n'
              '** Exponent')

while menu.lower() == 'r':
    # Ask the user to input the file name and display the content
    try:
        fileName = input('\nEnter the name of the txt file:\t')

        with open(fileName, 'r') as file:

            print(f'\n{file.read()}')
        break
    except FileNotFoundError:       # Avoid the program to crash if the file does not exist
            print('The file does not exist. Please try again!')

