# Return the **ending index** of the first subarray whose sum equals the target.

# Return `-1` if none exists.

def first_target_subarray_ends_at(nums, target):
  prefix_counting = {0:1}

  current_prefix = 0

  for i in range(0, len(nums)):
    current_prefix += nums[i]

    needed = current_prefix - target

    if needed in prefix_counting:
      return i
    
    prefix_counting[current_prefix] =( prefix_counting.get(current_prefix, 0) +1)

  return -1

nums = [1, 2, 3, -2, 2]
target = 3

print(first_target_subarray_ends_at(nums, target))

  
    

