# Merge characters until the two strings differ.
# len(str1) = n and len(str2) = m -> Time: O(min(n,m))
# k = length of a common prefix -> Space: O(k)

def common_prefix_merge(str1, str2):
  i = 0
  j = 0
  result = []
  while i < len(str1) and j < len(str2):

    if str1[i] != str2[j]:
      break
    
    result.append(str1[i])

    i += 1
    j += 1

  return "".join(result)

print(common_prefix_merge('flower', 'flowing'))
print(common_prefix_merge('phone', 'phonetic'))