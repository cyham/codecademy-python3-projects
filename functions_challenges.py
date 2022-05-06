# ----------------------------------------
# Challenge 1 - Tenth Power
def tenth_power(num):
  return num ** 10
# Tests
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024
# ----------------------------------------
# Challenge 2 - Square Root
def square_root(num):
  return num ** 0.5
# Tests
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10
# ----------------------------------------
# Challenge 3 - Win Percentage
def win_percentage(wins, losses):
  return (wins / (wins + losses)) * 100
# Tests
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
# ----------------------------------------
# Challenge 4 - Average 
def average(num1, num2):
  return (num1 + num2) / 2
# Tests
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0
# ----------------------------------------
# Challenge 5 - Remainder
def remainder(num1, num2):
  return (num1 * 2) % (num2 / 2)
# Tests
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0
# ----------------------------------------