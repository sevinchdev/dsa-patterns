# Count how many matching pairs exist while comparing from both ends.

# Time: O(n)
# Space: O(1)

def count_matching_end_pairs(word):
  left = 0
  right = len(word) - 1
  count = 0

  while left < right:

    if word[left] != word[right]:
      break

    left += 1
    right -= 1
    count += 1

  return count

word = 'abcdba'
print(count_matching_end_pairs(word))
