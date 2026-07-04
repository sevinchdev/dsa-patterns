# Return a dictionary containing the frequency of every character.

def count_charachters(text):
  count = {}

  for char in text:
    count[char] = count.get(char, 0) + 1

  return count

text = "banana"
print(count_charachters(text))