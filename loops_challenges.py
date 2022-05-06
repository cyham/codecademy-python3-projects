# ----------------------------------------
# Challenge 1 - Divisible by Ten
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count
# Test
print(divisible_by_ten([20, 25, 30, 35, 40]))
# should return 3
# ----------------------------------------
# Challenge 2 - Greetings
def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append(f"Hello, {name}")
  return greetings
# Test
print(add_greetings(["Owen", "Max", "Sophie"]))
# should return ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']
# ----------------------------------------
# Challenge 3 - Delete Starting Even Numbers
def delete_starting_evens(lst):
  len_lst = len(lst)
  first_odd_num_index = len_lst 
  for i in range(len_lst):
    if lst[i] % 2 != 0:
      first_odd_num_index = i 
      break
  return lst[first_odd_num_index:]
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# should return [11, 12, 15]
print(delete_starting_evens([4, 8, 10]))
# should return []
# ----------------------------------------
# Challenge 4 - Odd Indices
def odd_indices(lst):
  return lst[1::2]
# Test
print(odd_indices([4, 3, 7, 10, 11, -2]))
# should return [3, 10, -2]
# ----------------------------------------
# Challenge 5 - Exponents
def exponents(bases, powers):
  answers = []
  for base in bases:
    for power in powers:
      answers.append(base ** power)
  return answers
# Test
print(exponents([2, 3, 4], [1, 2, 3]))
# should return [2, 4, 8, 3, 9, 27, 4, 16, 64]
# ----------------------------------------