# Given a sorted array and a target, return the pair of numbers whose sum equals the target.

# If none exists, return `None`.
# Time: O(n)
# Space: O(1)

def return_pair(nums, target):
  left = 0
  right = len(nums) - 1

  while left < right:

    current_sum = nums[left] + nums[right]

    if current_sum == target:
      return nums[left], nums[right]
    
    elif current_sum < target:
      left += 1

    else:
      right -= 1

  return None

print(return_pair([1,2,3,4,6], 7))