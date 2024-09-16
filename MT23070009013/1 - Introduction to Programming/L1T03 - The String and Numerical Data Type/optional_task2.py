# pseudo:
# request users favourite restaurant and store this inside variable string_fav
# request users favourite number, store this inside int_fav and cast this to an int
# print both out in their own print statements below
# try to cast string_fav to an integer then comment in my code what happens

string_fav = input("Please tell me what your favourite restaurant is: ")
int_fav = int(input("Please tell me what your favourite number is: "))

print(f"Your favourite String: {string_fav}")
print(f"Your favourite number is: {int_fav}")

try_cast = int(string_fav)

# The following stack trace is provided when trying to cast the above string into an int
#
# Traceback (most recent call last):
#  File "d:/Cowd/hyperiondev/L1T03/optional_task2.py", line 13, in <module>
#    try_cast = int(string_fav)
# ValueError: invalid literal for int() with base 10: 'Nandos'
#
#
# By the looks of the error, it is stating that because the provided string is not of base 10
# it decides that this is an invalid literal to be converted into an int using int().  We  know
# this is the case because we input letters into string_fav, not whole numbers.
