# Instead of returning the first pivot,

# return **how many pivot indices exist**.
def count_balanced_indices(nums):
  total_sum = sum(nums)

  left_sum = 0
  count = 0
  for i in range(0, len(nums)):
    right_sum = total_sum - left_sum - nums[i]

    if left_sum == right_sum:
      count += 1

    left_sum += nums[i]

  return count

nums = [0, 0, 0]

print(count_balanced_indices(nums))

# Time complexity : O(n)
# Space complexity: O(1)