def meeting_planner(slotsA, slotsB, dur):
  pointerB = pointerA = 0
  
  while pointerA < len(slotsA) and pointerB < len(slotsB):
    start = max(slotsA[pointerA][0], slotsB[pointerB][0])
    end = min(slotsA[pointerA][1], slotsB[pointerB][1])
     
    if end - start >= dur:
      return [start, start+dur]

    else:
      if slotsB[pointerB][1] == slotsA[pointerA][1]:
        pointerA += 1
        pointerB += 1
      elif slotsB[pointerB][1] < slotsA[pointerA][1]:
        pointerB += 1
      else:
        pointerA += 1

  return []



slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8


print meeting_planner(slotsA, slotsB, dur)