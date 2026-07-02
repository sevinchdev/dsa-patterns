# Return the index where the **difference** between the left sum and the right sum is the smallest.

# If there are multiple answers, return the first one.
def closest_balance_point(nums):

  total_sum = sum(nums)

  left_sum = 0

  difference = float('inf')
  best_index = -1
  for i in range(0, len(nums)):
    left_sum += nums[i]

    right_sum = total_sum - left_sum

    if abs(right_sum - left_sum) < difference:
      difference = abs(right_sum - left_sum)
      best_index = i

  return best_index


nums =  [4, 1, 6, 3]

print(closest_balance_point(nums))

nums1 = [1, 2, 3, 5]
print(closest_balance_point(nums1))

# Time complexity :O(n)
# Space complexity: O(1)