# Without using a frequency dictionary,

# return **True** if two words are anagrams.
# n = length of each word => Time: O(nlogn)
# Space: O(n)
def are_words_anagram(word1, word2):
  return "".join(sorted(word1)) == "".join(sorted(word2))
  

word1 = 'listen'
word2 = 'silent'
print(are_words_anagram(word1, word2))