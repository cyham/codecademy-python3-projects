# ----------------------------------------
# Challenge 1 - Larger Sum
def larger_sum(lst1, lst2):
  if sum(lst1) >= sum(lst2):
    return lst1
  else:
    return lst2
# Test
print(larger_sum([1, 9, 5], [2, 3, 7]))
# should return [1, 9, 5]
# ----------------------------------------
# Challenge 2 - Over 9000
def over_nine_thousand(lst):
  total = 0
  for num in lst:
    total += num
    if total > 9000:
      break
  return total
# Test
print(over_nine_thousand([8000, 900, 120, 5000]))
# should return 9020
# ----------------------------------------
# Challenge 3 - Max Sum
def max_num(nums):
  max_val = nums[0]
  for num in nums:
    if num > max_val:
      max_val = num
  return max_val
# Test
print(max_num([50, -10, 0, 75, 20]))
# should return 75
# ----------------------------------------
# Challenge 4 - Same Values
def same_values(lst1, lst2):
  indices = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      indices.append(i)
  return indices
# Test
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# should return [0, 2, 3]
# ----------------------------------------
# Challenge 5 - Reversed List
def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    if lst1[i] != lst2[-(i+1)]:
      return False
  return True
# Tests
print(reversed_list([1, 2, 3], [3, 2, 1]))
# should return True
print(reversed_list([1, 5, 3], [3, 2, 1]))
# should return False
# ----------------------------------------