def is_range_sum_even(nums, queries):

  parity = [0] * len(nums)

  running_sum = 0

  for i in range(1, len(nums)):
    running_sum += nums[i]
    parity[i] = running_sum % 2

  result = []

  for left, right in queries:
    if left == 0:
      is_even = (parity[right] == 0)
    else:
      is_even = (parity[right] == parity[left - 1])
    
    result.append(is_even)

  return result

nums = [5,7,2,4,8]
queries = [(0,3),

(2,4),

(1,2)]

print(is_range_sum_even(nums, queries))