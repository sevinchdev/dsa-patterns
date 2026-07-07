# len(nums1) = n and len(nums2) = m -> Every element is visited only once -> Time: O(n+m)
# Space : O(n+m)

def merge_two_sorted_arrays(nums1, nums2):
  i = 0
  j = 0

  result = []

  while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
      result.append(nums1[i])
      i += 1
    else:
      result.append(nums2[j])
      j += 1

  while i < len(nums1):
    result.append(nums1[i])
    i += 1

  while j < len(nums2):
    result.append(nums2[j])
    j += 1

  return result

print(merge_two_sorted_arrays([1,3,5], [2,4,6]))