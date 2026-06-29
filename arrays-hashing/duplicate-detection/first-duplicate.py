# Given an array of integers, determine whether any number appears more than once.

def first_duplicate(nums):
  seen = set()

  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False

num1 = first_duplicate([4, 8, 2, 5, 8])
print(num1)
num2 = first_duplicate([1,2,3,4,5])
print(num2)