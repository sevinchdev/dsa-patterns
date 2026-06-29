def first_repeated(nums):
  seen = set()

  for num in nums:
    if num in seen:
      return num
    seen.add(num)

  return num

num1 = first_repeated([1,1,2,3,3,4,4])
print(num1)