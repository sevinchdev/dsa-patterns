def subarray_sum(nums, k):
  prefix_count = {0:1}

  current_prefix = 0
  count = 0

  for num in nums:

    current_prefix += num

    needed = current_prefix - k

    if needed in prefix_count:
      count += prefix_count[needed]

    
    prefix_count[current_prefix] = (prefix_count.get(current_prefix, 0) + 1)

  return count

nums = [1, 2]
k = 3
print(subarray_sum(nums, k))