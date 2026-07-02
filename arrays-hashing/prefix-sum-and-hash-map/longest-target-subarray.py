# Return the **length** of the longest contiguous subarray whose sum equals the target.

# This introduces one new idea about what you store in the hash map.

def longest_target_subarray(nums, target):
  prefix_index = {0:-1}

  current_prefix = 0

  longest = 0

  for i, num in enumerate(nums):
    current_prefix += num

    needed = current_prefix - target

    if needed in prefix_index:
      length = i - prefix_index[needed]
      longest = max(longest, length)

    if current_prefix not in prefix_index:
      prefix_index[current_prefix] = i

  return longest

nums = [1, -1, 5, -2, 3]

target = 3

print(longest_target_subarray(nums, target))