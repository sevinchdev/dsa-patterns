# Given a sorted array and a target, return True if there exist two numbers 
# whose sum equals the target.

def two_sum_exists(nums, target):

  left = 0
  right = len(nums) - 1

  while left < right:
      current_sum = nums[left] + nums[right]

      if current_sum == target:
        return  True
      
      elif current_sum < target:
        left += 1

      else:
        right -= 1

  return False

nums = [1,2,4,6,8]
target = 10
print(two_sum_exists(nums, target))

