# Move all negative numbers to the end.

# Maintain order of positives.

def move_negatives(nums):
  slow = 0
  
  for fast in range(len(nums)):
    
    if nums[fast] >= 0:
      nums[slow] = nums[fast]
      slow += 1


  return nums

print(move_negatives([-1,4,-2,5,6]))