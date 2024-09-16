# pseudo:
# Get user inputs for:
# - name
# - age
# - hair colour
# - eye colour
#
# Create Adult class with the same attributes above
# Add a method for can_drive() which prints the name
# and that they are old enough to drive
#
# Create a subclass of adult called Child, which method
# overrides can_drive() to say they cant drive
#
# Create logic to determine on user input if the Adult
# or Child class should be created

# Once the object has been created call the can_drive() method

class Adult():
    '''Adult class that takes the following attributes:\n
        Name\n
        Age\n
        Hair Colour\n
        Eye Colour'''
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")


class Child(Adult):
    '''A sublass of Adult, with a method override for can_drive()'''
    def can_drive(self):
        print(f"{self.name} is NOT old enough to drive.")


name = ""
while name == "":
    name = input("Please input your name: ")

# Validate entry of a valid integer, as upcoming logic
# reguires an integer value for calculation of age
while True:
    try:
        age = int(input("Please input your age: "))
        if isinstance(age, int):
            break
    except ValueError as error:
        print("Invalid integer value")
        print(error)

hair_colour = ""
while hair_colour == "":
    hair_colour = input("Please input your hair colour: ")

eye_colour = ""
while eye_colour == "":
    eye_colour = input("Please input your eye colour: ")

if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)

person.can_drive()
