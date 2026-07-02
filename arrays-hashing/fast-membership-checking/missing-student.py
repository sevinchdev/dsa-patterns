def missing_students(registered, attended):

  missing_students_list = [student for student in attended if student not in registered]

  return missing_students_list

print(missing_students(registered = [101, 102, 103, 104],attended = [102, 105, 104, 108]))