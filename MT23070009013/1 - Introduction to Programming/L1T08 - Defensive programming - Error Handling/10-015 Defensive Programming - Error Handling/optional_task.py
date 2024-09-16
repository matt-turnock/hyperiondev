# pseudo:
# write a program with two compilation errors (syntax), and runtime error and a logical error
# comment and explain what type of error occurs and why

# request integer input from user
## Compilation error: Missing end bracket on parentheses pair for int cast
num = int(input("Please input an integer: ")
## Logical error: in following if else, this < condition should be >
if num < 5:
    ## Complication error: missing parentheses on print statement
    print f"My number ({num}) is greater than 5"
else:
    ## Runtime error: unable to add an integer to a string
    print(f"My number " + num + " is less than 5")