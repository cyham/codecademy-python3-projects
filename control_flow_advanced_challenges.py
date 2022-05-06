# ----------------------------------------
# Challenge 1 - In Range
def in_range(num, lower, upper):
  return num >= lower and num <= upper
# Tests
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False
# ----------------------------------------
# Challenge 2 - Same Name
def same_name(your_name, my_name):
  return your_name == my_name
# Tests
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False
# ----------------------------------------
# Challenge 3 - Always False
def always_false(num):
  return num < 0 and num > 0 
# Tests
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
# ----------------------------------------
# Challenge 4 - Movie Review
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"
# Tests
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."
# ----------------------------------------
# Challenge 5 - Max Number
def max_num(num1, num2, num3):
  num_lst = [num1, num2, num3]
  max_num = max(num_lst)
  dupes = num_lst.count(max_num) > 1
  if dupes:
    return "It's a tie!"
  else:
    return max_num
# Tests
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
# ----------------------------------------