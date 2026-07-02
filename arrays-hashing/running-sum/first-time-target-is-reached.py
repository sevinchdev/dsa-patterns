# A robot gains energy after each station.

# Return the **first index** where the running energy becomes **at least** the target.

# If it never happens, return `-1`.

def first_reached_target(energy, target):

  running_energy = 0

  for i in range(0,len(energy)):
    running_energy += energy[i]

    if running_energy >= target:
      return i
    
  return -1

energy =  [4, 2, 5, 1]
target = 10
print(first_reached_target(energy, target))
