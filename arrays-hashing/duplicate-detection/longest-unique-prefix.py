# Return the length of the longest prefix containing no repeated values

def longest_unique_prefix(nums):
  seen = set()

  for num in nums:
    if num in seen:
      return len(seen)
    
    seen.add(num)

  return seen

num1 = longest_unique_prefix([1,2,3,4,5,6,1])
print(num1)