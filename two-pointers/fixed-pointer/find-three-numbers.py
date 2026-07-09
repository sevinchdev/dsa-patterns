# Without worrying about duplicates,

# return **one** triplet whose sum equals the target.

def find_three_numbers(nums, target):

  nums.sort()

  for i in range(len(nums) - 2):

    left = i + 1
    right = len(nums) - 1

    while left < right:

      current_sum = nums[i] + nums[left] + nums[right]

      if current_sum == target:
        return [nums[i], nums[left], nums[right]]
      
      elif current_sum < target:
        left += 1

      else:
        right -= 1

  return None

nums = [-4,-1,-1,0,1,2]
target = 0
print(find_three_numbers(nums, target))