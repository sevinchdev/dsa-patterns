# Ignore uppercase/lowercase.

# Time: O(n) - Calling .lower() on a single character is O(1). So it does not change overall time.
# Space: O(1)

def ignore_case_palindrome(word):
  left = 0
  right = len(word) - 1

  while left < right:

    if word[left].lower() != word[right].lower():
      return False
    
    left += 1
    right -= 1

  return True

print(ignore_case_palindrome('RaceCar'))