# Sal's Shipping

#Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

#In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

#Sal’s Shippers has several different options for a customer to ship their package:



#Ground Shipping
weight = 41.5
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20
  
cost_ground_premium = 125.00
print(cost_ground)
print("Ground Shipping Premium $", cost_ground_premium)

#Drone Shipping

weight = 41.5

if weight <= 2:
  drone_shipping = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_shipping = weight * 9.0
elif weight > 6 and weight <= 10:
  drone_shipping = weight * 12.0
else:
  drone_shipping = weight * 14.25

print(drone_shipping)
