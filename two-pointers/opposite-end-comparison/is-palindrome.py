#Return True if a string is a palindrome.

# Time: O(n)
#Space: O(1)

def is_palindrome(word):

  left = 0
  right = len(word) - 1

  while left < right:

    if word[left] != word[right]:
      return False

    left += 1
    right -= 1
  
  return True

word = 'racecar'
print(is_palindrome(word))

word1 = 'apple'
print(is_palindrome(word1))