
def duplicate_report(nums):
  frequency = {}
  
  for num in nums:
    if num in frequency:
      frequency[num] += 1
    else:
      frequency[num] = 1

  duplicates = {}

  for num, count in frequency.items():
    if count > 1:
      duplicates[num] = count

  return duplicates


num1 = duplicate_report([2,3,2,5,5,5])
print(num1)



  