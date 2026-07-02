def maximum_in_two_ranges(nums, range_a, range_b):
  prefix = [0] * len(nums)

  prefix [0] = nums[0]

  for i in range(1, len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

  left, right = range_a

  for left, right in range_a:
    if left == 0:
      range_a = prefix[right]
    else:
      range_a = prefix[right] - prefix[left-1]

  left, right = range_b
  for left, right in range_b:
    if left == 0:
      range_b = prefix[right]
    else:
      range_b = prefix[right] - prefix[left-1]

  
  if range_a > range_b:
    return "Range A"
  elif range_a <range_b:
    return "Range B"
  else:
    return "Equal"
  
nums = [4, 6, 3, 8, 5, 7]

range_a = (0,2)

range_b = (3,5)

print(maximum_in_two_ranges(nums, range_a, range_b))