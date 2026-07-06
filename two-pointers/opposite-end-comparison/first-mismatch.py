#Return the first pair of indices where the characters differ.

# Time: O(n)
# Space: O(1)
def first_mismatch(word):
  left = 0
  right = len(word) - 1

  while left < right:

    if word[left] != word[right]:
      return left, right
    
    left += 1
    right -= 1

  return (-1,-1)

word = 'abca'
print(first_mismatch(word))

word1 = 'racecar'
print(first_mismatch(word1))