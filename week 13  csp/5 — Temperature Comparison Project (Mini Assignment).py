# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.
temp = int(input("What is the temperature?"))
if temp >=-10 <=110:
    print("Normal temperature!")
else:
    print("Warning!!")

if temp >=-9 <=65:
    print("It's cold!")
if temp >=66 <=75:
    print("Its warm!")
elif temp >=76 <=109:
    print("Its hot!")
else:
    print("Extreme temperature warning!")
# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

