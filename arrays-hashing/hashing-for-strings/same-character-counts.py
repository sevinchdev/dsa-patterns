# Return True if two strings have identical character frequencies.

def same_character_counts(text1, text2):
  count1 = {}
  count2 = {}

  for char in text1:
    count1[char] = count1.get(char, 0) + 1

  for char in text2:
    count2[char] = count2.get(char,0) + 1

  if len(count1) != len(count2):
    return False
  
  return count1 == count2

text1 = 'aabbsc'
text2 = 'abcbca'
print(same_character_counts(text1, text2))
