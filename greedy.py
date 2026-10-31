from scedule import *

def find_earliest_end(last_end):
    earliest = float("inf")
    pick = None
    for activity in scedule:
        if scedule[activity]["start"] >= last_end and scedule[activity]["end"] < earliest:
            earliest = scedule[activity]["end"]
            pick = activity
    return pick

chosen = []
last_end = 0
pick = find_earliest_end(last_end)
while pick is not None:
    chosen.append(pick)
    last_end = scedule[pick]["end"]
    pick = find_earliest_end(last_end)