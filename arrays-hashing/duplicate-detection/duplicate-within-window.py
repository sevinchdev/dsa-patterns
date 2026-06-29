# Return True if a duplicate exists within distance k.

def duplicate_exists(nums, k):
  seen = set()

  for num in nums[:k]:
    if num in seen:
      return True
    seen.add(num)

  return False

  
num1 = duplicate_exists([1,1,5,3,4], 5)
print(num1)