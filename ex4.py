#number of cars available
cars = 100
#number of people we can fit in one car
space_in_car = 4.0
#number of available drivers
drivers = 30
#number of people we need to transport
passengers = 90
#leftover cars after each driver gets one
cars_not_driven = cars - drivers
#number of cars in use
cars_driven = drivers
#number of people we can transport
carpool_capacity = cars_driven * space_in_car
#average passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
