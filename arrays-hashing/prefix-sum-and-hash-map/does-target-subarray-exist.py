# Given an integer array and a target, return True if any contiguous subarray 
# sums to the target. Otherwise return False.

def target_subarray_exist(nums, target):

  prefix_count = {0:1}

  current_prefix = 0
  count = 0

  for num in nums:
    current_prefix += num

    needed = current_prefix - target

    if needed in prefix_count:
      return True
    
    prefix_count[current_prefix] = (prefix_count.get(current_prefix, 0) + 1)

  return False

nums = [3, 4, -2, 5]
target = 5

print(target_subarray_exist(nums, target))

# Time complexity: O(n)
# Space complexity: O(n)
