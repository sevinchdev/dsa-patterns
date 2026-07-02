def number_occuring_twice(nums):
  nums_count = {}

  for num in nums:
    nums_count[num] = nums_count.get(num, 0) + 1

  result = []
  for num, count in nums_count.items():
    if count == 2:
      result.append(num)

  return result

nums1 = [1,2,2,3,4,5,5,6,7,7]
print(number_occuring_twice(nums1))
