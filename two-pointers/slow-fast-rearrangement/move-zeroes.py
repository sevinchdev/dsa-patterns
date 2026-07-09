# Move all zeroes to the end.

# Maintain order.

# len(nums) = n -> Time: O(2n) = O(n)
# Space: O(1) - no extra arrays

def move_zeroes(nums):
  slow = 0

  for fast in range(len(nums)):

    if nums[fast] != 0:
      nums[slow] = nums[fast]
      slow += 1

  while slow < len(nums):
    nums[slow] = 0
    slow += 1

  return nums

print(move_zeroes([0,1,0,3,12]))