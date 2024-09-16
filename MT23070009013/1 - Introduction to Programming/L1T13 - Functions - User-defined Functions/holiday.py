# pseudo:
# first, obtain city_flight, num_nights and rental_days as user inputs
# create four functions as follows
# hotel_cost, which takes num_nights as an argument and return the total cost
# plane_cost, which takes city_flight as an argument and returns the cost of the flight
# car_rental, which takes rental_days as an argument and returns total cost of rental
# holiday_cost, which takes three arguments from the three above functions
# and calculates the total holiday cost.
# print out all the details in a readable fashion

def plane_cost(city):
    # Just grab the value for the city key from the dict.
    return dest_options[city]
    
def hotel_cost(nights):
    # Could make this more dynamic by having different prices depending on which city the hotel is in.
    total_cost = nights * night_cost
    return total_cost

def car_rental(days):
    # arbitrary figure
    total_cost = days * rental_cost
    return total_cost

# Take in the three functions above as arguements into the below function
# calling them from within this function.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_hotel = hotel_cost(num_nights)
    total_city = plane_cost(city_flight)
    total_rental = car_rental(rental_days)
    total = total_hotel + total_city + total_rental
    
    # As these variables are scoped and i am only returning total, print
    # this part of the output here.
    print(f"""Details for your trip\nYour flight to {city_flight.title()} cost £{total_city}.
The hotel stay cost £{total_hotel}, {num_nights} night(s) at £{night_cost} per night.
The car rental cost £{total_rental}, {rental_days} day(s) at £{rental_cost}""")
    return total

# define these so i can test against them when they are invalid data into their relevant data types
city_flight = ""
num_nights = ""
rental_days = ""

# define the following outside of the function scope so that i can use them in my final print message.
night_cost = 300
rental_cost = 70

# Dictionary for my destinations, allows me to set a price here, but also validate they enter a valid city by
# checking their input against valid dictionary keys.
dest_options = {'paris': 1000, 'new york': 2500, 'rome': 1150, 'london': 500}
print("Possible destinations")
for d in dest_options.keys():
    # using .title() here to uppercase the first letter of each word.
    print(d.title())

# I was using a while loop to check if my entry was a valid key of my dict before, but was
# encouraged to try using try:except instead.

while True:
    try:
        city_flight = input("Please enter one of the options above for your destination: ").lower()
        if city_flight in dest_options:
            break
    except:
        pass
    
    print(f"{city_flight} is not on the destination list, please provide one listed.")

while True:
    try:
        num_nights = int(input("Please input the number of nights for your visit: "))
        # Had to look up how to check if something was an integer
        if isinstance(num_nights, int):
            break
    except:
        pass
    
    print(f"Invalid entry: {num_nights}. Must be an integer value.")
    
while True:
    try:
        rental_days = int(input("Please input the number of rental days required for the car rental: "))
        if isinstance(rental_days, int):
            break
    except:
        pass
    
    print(f"Invalid entry: {rental_days}. Must be an integer value.")

# call my total function passing in the other three functions to obtain the holiday total cost.
total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

print(f"Holiday total: £{total_cost}")