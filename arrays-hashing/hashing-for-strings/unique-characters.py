# Return **True** if every character appears exactly once.

# Otherwise return **False**.

# Time: O(n)
# Space: O(n)
def unique_characters(text):
  seen = set()

  for char in text:
    if char in seen:
      return False
    
    seen.add(char)

  return True

text = 'abcd'
print(unique_characters(text))

text1 = 'abca'
print(unique_characters(text1))