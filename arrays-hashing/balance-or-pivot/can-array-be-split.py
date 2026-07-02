# Return **True** if the array can be divided into two parts with equal sums.

# Otherwise return **False**.

def split_array(nums):
  total_sum = sum(nums)

  left_sum = 0

  for num in nums:
    left_sum += num

    right_sum = total_sum - left_sum 

    if left_sum == right_sum:
      return True
    

  return False

nums = [2, 3, 5]
print(split_array(nums))

nums1 = [1,2,3,5]
print(split_array(nums1))