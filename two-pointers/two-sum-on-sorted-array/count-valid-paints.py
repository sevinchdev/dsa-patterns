#Count how many pairs have a sum equal to the target.

# Time: O(n)
# Space: O(1)
def count_valid_paint(nums, target):
  left = 0
  right = len(nums) - 1
  count = 0

  while left < right:
    current_sum = nums[left] + nums[right]

    if current_sum == target:
      count += 1
      left += 1
      right -= 1
    elif current_sum < target:
      left += 1
    else:
      right -= 1
    
  return count

print(count_valid_paint([1,2,3,4,5,6], 7))