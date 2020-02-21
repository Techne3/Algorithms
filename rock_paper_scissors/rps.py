#!/usr/bin/python

import sys
"""
     v
[r,p,s]
recursive call n -1
[["rock", rock],["rock", paper],[rock]]


"""
def rock_paper_scissors(n):
    plays = []
    rps = [['rock'], ['paper'], ['scissors']]
    
    #base cases
    if n == 0:
        return [plays]
    if n == 1:
        return rps

    for newlist in rock_paper_scissors(n - 1):
        # for loop -> action in the plays, set new action equal to the sub
        # list + the action, then append to plays the new action
        for eachPlay in rps:
            plays.append(newlist + eachPlay)

    return plays
print(rock_paper_scissors(3))




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')