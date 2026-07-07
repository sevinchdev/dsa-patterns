# len(first) = n and len(second) = m => Time: O(n+m)
# Space : O(n+m)

def merge_strings(first, second):
  i = 0
  j = 0

  result = []

  while i < len(first) and j < len(second):
    result.append(first[i])
    result.append(second[j])

    i += 1
    j += 1

  while i < len(first):
    result.append(first[i])
    i += 1

  while j < len(second):
    result.append(second[j])
    j += 1

  return "".join(result)

print(merge_strings('abc', '123'))
print(merge_strings('abc', '12345'))