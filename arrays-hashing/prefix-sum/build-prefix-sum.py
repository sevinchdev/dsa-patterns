def build_prefix(nums):
  prefix_array = [0] * len(nums)
  prefix_array[0] = nums[0]

  for i in range(1,len(nums)):
    prefix_array[i] = prefix_array[i-1] + nums[i]

  return prefix_array

nums1 = [3, 5, 2, 7]
print(build_prefix(nums1))