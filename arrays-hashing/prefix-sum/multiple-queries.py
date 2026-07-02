def multiple_queries(nums, queries):
  prefix = [0] * len(nums)

  prefix[0] = nums[0]

  for i in range(1, len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

  result = []

  for left, right in queries:
    if left == 0:
      result.append(prefix[right])
    else:
      result.append(prefix[right] - prefix[left - 1])

  return result


nums = [2, 4, 6, 8, 10, 12]

queries = [
    (0, 2),
    (2, 5),
    (1, 4)
]

print(multiple_queries(nums, queries))