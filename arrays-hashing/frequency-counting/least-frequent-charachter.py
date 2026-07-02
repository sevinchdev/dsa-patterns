# Return the least frequent character.
def least_frequent_charachter(word):
  char_count = {}

  for char in word:
    char_count[char] = char_count.get(char, 0) + 1

  min_count = min(char_count.values())

  min_char = [char for char, count in char_count.items() if count == min_count]

  return min_char

word1 = 'Aziza'
print(least_frequent_charachter(word1))