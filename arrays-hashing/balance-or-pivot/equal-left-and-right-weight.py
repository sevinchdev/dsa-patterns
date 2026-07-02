# A bridge has weights placed along it.

# Return the **first index** where the total weight on the left equals the total weight on the right.

# If no such index exists, return `-1`.

def equalize_left_and_right(weights):

  total_weight = sum(weights)

  left_sum = 0

  for i in range(0,len(weights)):
    right_sum = total_weight - left_sum - weights[i]

    if left_sum == right_sum:
      return i
    
    left_sum += weights[i]
  
  return -1

weights = [1, 7, 3, 6, 5, 6]
print(equalize_left_and_right(weights))

weights1 = [1,2,6,3]
print(equalize_left_and_right(weights1))