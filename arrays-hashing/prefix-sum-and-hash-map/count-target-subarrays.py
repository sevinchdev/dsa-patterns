def count_target_subarrays(nums, target):
  
  prefix_count = {0:1}

  current_prefix = 0
  count = 0

  for num in nums:
    current_prefix += num

    needed = current_prefix - target

    if needed in prefix_count:
      count += prefix_count[needed]

    prefix_count[current_prefix] = (prefix_count.get(current_prefix, 0) + 1) 

  return count

nums = [1, 2, 3, -2, 2]
target = 3

print(count_target_subarrays(nums, target))