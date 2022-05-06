weight = 4.8

# Ground shipping
ground_flat_charge = 20.00
if weight <= 2:
  ground_price_per_pound = 1.5
elif weight <= 6:
  ground_price_per_pound = 3.0
elif weight <= 10:
  ground_price_per_pound = 4.0
else:
  ground_price_per_pound = 4.75

ground_cost = f"Ground Shipping Cost: ${ground_flat_charge + ground_price_per_pound * weight:.2f}"
print(ground_cost)

# Premium ground shipping
premium_flat_charge = 125.00
premium_cost = f"Premium Ground Shipping Cost: ${premium_flat_charge:.2f}"
print(premium_cost)

# Drone shipping
if weight <= 2:
  drone_price_per_pound = 4.5
elif weight <= 6:
  drone_price_per_pound = 9.0
elif weight <= 10:
  drone_price_per_pound = 12.0
else:
  drone_price_per_pound = 14.25

drone_cost = f"Drone Shipping Cost: ${weight * drone_price_per_pound:.2f}"
print(drone_cost)
