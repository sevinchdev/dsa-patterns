# Return the character that appears the most.

def most_frequent_character(text):
  count = {}

  for char in text:
    count[char] = count.get(char, 0) + 1

  best_char = None
  best_count = 0

  for char, freq in count.items():
    if freq > best_count:
      best_count = freq
      best_char = char

  return best_char

text = "mississippi"
print(most_frequent_character(text))