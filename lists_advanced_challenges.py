# ----------------------------------------
# Challenge 1 - Every Three Numbers 
def every_three_nums(start):
  return list(range(start, 101, 3))
# Test
print(every_three_nums(91))
# should return [91, 94, 97, 100]
# ----------------------------------------
# Challenge 2 - Remove Middle
def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]
# Test
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
# should return [4, 23, 42]
# ----------------------------------------
# Challenge 3 - More Frequent Item
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
      return item1
  else:
      return item2
# Test
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
# should return 3
# ----------------------------------------
# Challenge 4 - Double Index
def double_index(lst, index):
    if index >= len(lst):
        return lst
    double_index_lst = lst[:] 
    double_index_lst[index] = double_index_lst[index] * 2
    return double_index_lst
# Test
print(double_index([1, 2, 3, 4], 2))
# should return [1, 2, 6, 4]
print(double_index([3, 8, -10, 12], 2))
# should return [3, 8, -20, 12]
# ----------------------------------------
# Challenge 5 - Middle Item
def middle_element(lst):
    len_lst = len(lst)
    middle_index = int(len_lst/2)
    if len_lst % 2 == 0:
        return (lst[middle_index] + lst[middle_index-1]) / 2
    else:
        return lst[middle_index]
# Test
print(middle_element([5, 2, -10, -4, 4, 5]))
# should return -7
print(middle_element([5, 2, -10, -4, 4, 5, 1]))
# should return -4
# ----------------------------------------