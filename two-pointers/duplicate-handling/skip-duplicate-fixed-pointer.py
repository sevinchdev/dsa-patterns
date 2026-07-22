# Write code that skips duplicate fixed values.

def skip_duplicates(nums):
  nums.sort()

  for i in range(len(nums)):

    if i > 0 and nums[i] == nums[i-1]:
      continue

    print(nums[i])

skip_duplicates([-4,-1,-1,0,1,2])