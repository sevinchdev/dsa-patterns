# You may remove **at most one character**.

# Return whether it can become a palindrome.

def almost_palindrome(word):
  left = 0
  right = len(word) - 1
  count = 0

  while left < right:
    if word[left] == word[right]:
      left += 1
      right -= 1


    if word[left - 1] == word[right] or word[left] == word[right + 1]:
      count += 1
      left += 1
      right -= 1

  if count == 1:
    return True
  else:
    return False

print(almost_palindrome('abca'))