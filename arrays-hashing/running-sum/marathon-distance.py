# A runner completes several laps.

# Each lap has a different distance.

# Return the total distance completed after each lap.

def marathon_distance(laps):

  running_distance = 0

  result = []

  for lap in laps:
    running_distance += lap

    result.append(running_distance)

  return result

laps = [400, 400, 800, 200]
print(marathon_distance(laps))