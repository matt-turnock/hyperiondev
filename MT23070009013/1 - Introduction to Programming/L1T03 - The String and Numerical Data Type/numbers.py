# pseudo:
# request num1, num2, and num3 from the user as integers
# print out the sum of all three numbers
# print out the first number minus the second number
# print out the third number multiplied by the first number
# print out the sum of all numbers divided by the third number

num1 = input("Please input num1 as an integer: ")
num2 = input("Please input num2 as an integer: ")
num3 = input("Please input num3 as an integer: ")

# I recast these as ints here once, instead of doing them in the
# seperate operations below for both total, and the num1 - num2 equation
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

total = num1 + num2 + num3
print(f"Total: {total}")

print(f"num1({num1}) - num2({num2}) = {num1 - num2}")
print(f"num3({num3}) * num1({num1}) = {num3 * num1}")
print(f"Sum of all three({total}) divided by num3({num3}) = {total / num3}")