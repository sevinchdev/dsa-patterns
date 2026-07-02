def one_range_sum(nums):
  prefix = [0] * len(nums)

  prefix[0] = nums[0]

  for i in range(1,len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

  result = prefix[5] - prefix[1]

  return result

nums = [4, 2, 7, 1, 5, 3]
print(one_range_sum(nums))