# Write a function that returns the running temperature total after each hour.

def running_temperature(changes):
  running_sum = 0
  result = []
  for change in changes:
    running_sum += change
    result.append(running_sum)

  return result

changes =  [2, -1, 3, -2]
print(running_temperature(changes))


