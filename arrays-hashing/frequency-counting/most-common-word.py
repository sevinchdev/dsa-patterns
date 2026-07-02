# Find the most common word.

def common_word(words):
  words_count = {}

  for word in words:
    if word in words_count:
      words_count[word] += 1
    else:
      words_count[word] = 1

  max_count = max(words_count.values())

  result = [word for word, count in words_count.items() if count == max_count]

  return result

words1 = ['and', 'or', 'and','with','with','with','and']
print(common_word(words1))