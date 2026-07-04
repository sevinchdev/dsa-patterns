# Return a dictionary showing which characters are missing from the second string.

# n = len(source) and m = len(target) => Time: O(n+m)
# k = distinct characters in source => Space: O(k)

def missing_letters(source, target):
  source_count = {}
  target_count = {}

  for char in source:
    source_count[char] = source_count.get(char, 0) + 1

  for char in target:
    target_count[char] = target_count.get(char, 0) + 1

  missing = {}

  for char in source_count:
    missing_count = source_count[char] - target_count.get(char, 0)

    if missing_count > 0:
      missing[char] = missing_count

  return missing

source = "banana"
target = "band"
print(missing_letters(source, target))