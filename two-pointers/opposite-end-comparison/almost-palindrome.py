# You may remove **at most one character**.

# Return whether it can become a palindrome.
# Time: O(n)
# Space: O(1)

def is_palindrome(word, left, right):

  left = 0
  right = len(word) - 1

  while left < right:

    if word[left] != word[right]:
      return False
    
    left += 1
    right -= 1

  return True

def almost_palindrome(word):
  left = 0
  right = len(word) - 1

  while left < right:
    if word[left] != word[right]:
      return (is_palindrome(word, left + 1, right)
              or
              is_palindrome(word, left, right - 1))

    left += 1
    right -= 1

  return True

print(almost_palindrome('abca'))

    
