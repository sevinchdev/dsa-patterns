# Return the number of contiguous subarrays whose sum is 0.

def count_zero_sum_subarrays(nums):
  prefix_count = {0:1}

  current_prefix = 0
  count = 0

  for num in nums:
    current_prefix += num

    needed = current_prefix

    if needed in prefix_count:
      count += prefix_count[needed]

    prefix_count[current_prefix] = (prefix_count.get(current_prefix, 0) + 1)

  return count

nums = [3, -3, 2, -2]
print(count_zero_sum_subarrays(nums))

    
