def range_average(nums):
  prefix = [0] * len(nums)

  prefix[0] = nums[0]

  for i in range(1,len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

  average = (prefix[4] - prefix[0])/len(prefix[1:5])

  return average

nums = [8,4,6,2,10,5]
print(range_average(nums))