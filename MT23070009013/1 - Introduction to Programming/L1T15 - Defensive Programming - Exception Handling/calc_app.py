# pseudo:
# This app should allow for users to perform calculations, and print previous
# calculations stored in a file called equations.txt
#
# If a calculation is performed, it should take two numbers
# and be able to use +, -, * or /
# The answer should be printed, and the entire equation recorded in the text file
#
# Use defensive programming to protect the app from crashing.
#
# When asking to print previous calcs this should just output the contents of the file.

## Note: i made a design choice to only do my calculations in fuctions, but i could
## further expand this to also do data validation via function also.

# Function to make the calculation, then return the results.
def calculation(num1, operator, num2):
    print()
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        answer = num1 / num2
    
    equation = f"{num1} {operator} {num2} = {answer}"    
    store_equation(equation)
    
    return answer


# Function to store all valid equations
def store_equation(equation):
    with open('./stored_equations.txt', 'a+') as f:
        f.write(f"{equation}\n")
    
# Function to list all previous equations
def view_history():
    try:
        with open('./stored_equations.txt', 'r') as f:
            for line in f:
                line = line.strip('\n')
                print(line)
    except FileNotFoundError as e:
        print("The file you are trying to open does not exist. This might be because you are not in the correct directory, or that no equations have been made to store.")
        print(e)
        
# Print our welcome message and display our function options

print('''Welcome to the calculator app
      
Please select one of the following options
1 - Make a calculation
2 - Show all previous calculations performed
      ''')


# Main loop block to drive the application
while True:
    # Used try except here so i use at least one for validation.
    try:
        option = int(input("Option: "))
        if option > 0 and option < 3:
            break
        else:
            print(f"{option} is not a valid selection, please select one of the predefined options.")
    except ValueError:
        print("That is not a valid input, please input an integer.")

if option == 1:
    while True:
        try:
            num1 = float(input("Please input your first number: "))
            break
        except ValueError:
            print("The number entered is not a valid number.")
    
    # Check to see what operator they have entered and validate its valid with the four operations, +, -, * and /
    operator = ""
    while not operator == '+' or not operator == '-' or not operator == '*' or not operator == '/]':
        operator = input("Please input if you want to add (+), subtract (-), multiply (*) or divide (/): ")
        
        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            break
        else:
            print("Please input a valid mathematical operand.")
    
    #Check to see if num2 is 0, if operator was /, then request num2 again
    num2 = 0
    
    #Oops - forgot to validate num2 :rofl: - Updated to do both in the same block
    while True and num2 == 0:
        try:
            num2 = float(input("Please input your second number: "))
            if operator == '/':
                if num2 == 0:
                    print("Dividing by zero is not valid, please enter your second number again")
                else:
                    break
        except ValueError:
            print("The number entered is not a valid number.")
        
    answer = calculation(num1, operator, num2)
    
    print(f"{num1} {operator} {num2} = {answer}")
elif option == 2:
    view_history()