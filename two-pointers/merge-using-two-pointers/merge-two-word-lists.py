# len(list1) = n and len(list2) = m -> Time: O(n+m)
# Space: O(n+m)
def merge_two_word_lists(list1, list2):

  i = 0
  j = 0

  result = []

  while i < len(list1) and j < len(list2):
    result.append(list1[i])
    result.append(list2[j])
    i += 1
    j += 1


  while i < len(list1):
    result.append(list1[i])
    i += 1

  while j < len(list2):
    result.append(list2[j])
    j += 1

  return result

print(merge_two_word_lists(["apple","banana"],["cat","dog","fish"]))