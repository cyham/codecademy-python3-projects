# ----------------------------------------
# Challenge 1 - Append Size
def append_size(lst):
  lst.append(len(lst))
  return lst
# Test
print(append_size([23, 42, 108]))
# should return [23, 42, 108, 3]
# ----------------------------------------
# Challenge 2 - Append Sum
def append_sum(lst):
  for i in range(3):
    lst.append(sum(lst[-2:]))
  return lst
# Test
print(append_sum([1, 1, 2]))
# should return [1, 1, 2, 3, 5, 8]
# ----------------------------------------
# Challenge 3 - Larger List
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]
# Test
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
# should return 5
print(larger_list([4, 10, 2, 5, 6], [-10, 2, 5, 10]))
# should return 6
print(larger_list([4, 10, 2], [-10, 2, 5, 10]))
# should return 10
# ----------------------------------------
# Challenge 4 - More Than N
def more_than_n(lst, item, n):
  return lst.count(item) > n
# Tests
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
# should return True
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 4))
# should return False
# ----------------------------------------
# Challenge 5 - Combine Sort
def combine_sort(lst1, lst2):
  return sorted(lst1 + lst2)
# Test
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
# should return [-10, 2, 2, 4, 5, 5, 10, 10]
# ----------------------------------------