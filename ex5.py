name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
height_mm = height * 25.4
weight = 180 #lbs
weight_Kg = round(weight * 0.453592)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"In metric units that would be.... {height_mm/100} m.")
print(f"He's {weight} pounds heavy, but only {weight_Kg}Kg light!")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes nad {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
