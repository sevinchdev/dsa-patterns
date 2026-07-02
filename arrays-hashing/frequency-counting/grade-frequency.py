# Count how many times each grade appears.

def grade_frequency(grades):
  grades_count = {}

  for grade in grades:
    if grade in grades_count:
      grades_count[grade] += 1
    else:
      grades_count[grade] = 1

  return grades_count

grades1 = grade_frequency([60,80,80,70,70,75,90])
print(grades1)

  
