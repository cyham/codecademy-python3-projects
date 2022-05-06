# ----------------------------------------
# Challenge 1 - Large Power
def large_power(base, exponent):
  return base**exponent > 5000
# Tests
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
# ----------------------------------------
# Challenge 2 - Over budget
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  return budget < food_bill + electricity_bill + internet_bill + rent
# Tests
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True
# ----------------------------------------
# Challenge 3 - Twice as Large
def twice_as_large(num1, num2):
  return num1 > num2 * 2
# Tests
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True
# ----------------------------------------
# Challenge 4 - Divisible by Ten
# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  return num % 10 == 0
# Tests
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False
# ----------------------------------------
# Challenge 5 - Not Sum to Ten
def not_sum_to_ten(num1, num2):
  return num1 + num2 != 10
# Tests
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False
# ----------------------------------------