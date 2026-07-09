# Remove every occurrence of target in-place.

# Return the new length.

def remove_target(nums, target):
  result = []
  for i in range(len(nums)):
    if nums[i] != target:
      result.append(nums[i])

  return len(result)

print(remove_target([2,3,3,2], 3))
