# Count how many triplets have a sum equal to the target.

# Ignore duplicate handling for now.

def count_triplets(nums, target):
  count = 0

  for i in range(len(nums) - 2):
    left = i + 1
    right = len(nums) - 1
    
    while left < right:
      current_sum = nums[i] + nums[left] + nums[right]

      if current_sum == target:
        count += 1
        left += 1
        right -= 1

      elif current_sum < target:
        left += 1

      else:
        right -= 1

  return count

nums = [-4,-1,-1,0,1,2]
target = 0
print(count_triplets(nums, target))