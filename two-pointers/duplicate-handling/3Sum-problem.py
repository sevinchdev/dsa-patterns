# Return all unique triplets whose sum equals zero.

def return_triplets(nums, target):
  nums.sort()

  result = []
  for i in range(len(nums) - 2):

    if i > 0 and nums[i] == nums[i-1]:
      continue

    left = i + 1
    right = len(nums) - 1

    while left < right:

      current_sum = nums[i] + nums[left] + nums[right]

      if current_sum == target:
        result.append([nums[i], nums[left], nums[right]])

        while left < right and nums[left] == nums[left + 1]:
          left += 1

        while left < right and nums[right] == nums[right - 1]:
          right -= 1

        left +=  1
        right -= 1

      elif current_sum < target:
        left += 1

      else:
        right -= 1

  return result

nums = [-1,0,1,2,-1,-4]
target = 1

print(return_triplets(nums, target))
