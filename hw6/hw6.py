"""
      Name: Ruiqing Qiu
      PID: A98022702
      Userid: rqiu
      filename: hw6.py
"""
import math
reward = []
Lambda = 0.985
valueList = []
west = []
north = []
east = []
south = []
with open ('rewards.txt') as rewardFile:
  for line in rewardFile:
    tmp = line.split()
    num = (float)(tmp[0])
    reward.append(num)
# print reward
with open ('prob_a1.txt') as westFile: 
  for line in westFile:
    tmp = line.split()
    west.append(tmp)
#print west
with open ('prob_a2.txt') as northFile: 
  for line in northFile:
    tmp = line.split()
    north.append(tmp)
with open ('prob_a3.txt') as eastFile: 
  for line in eastFile:
    tmp = line.split()
    east.append(tmp)
with open ('prob_a4.txt') as southFile: 
  for line in southFile:
    tmp = line.split()
    south.append(tmp)


for i in range(0, 81):
  valueList.append(0.0)
# print valueList
valueList1 = []
#Copy of valueList
for i in valueList:
  valueList1.append(i)

for i in range (1, 1000):
  for s in range (0, 81):
    Rs = reward[s]
    maxValue = 0.0
    for action in range(1, 5):
      if(action == 1):
        total = 0.0
        for smallList in west:

          if (int)(smallList[0]) == (s+1):
            sprime = (int)(smallList[1])
            prob = (float)(smallList[2])
            total += prob * valueList[sprime-1]
        maxValue = total
      elif(action == 2):
        total = 0.0
        for smallList in north:
          if (int)(smallList[0]) == (s+1):
            sprime = (int)(smallList[1])
            prob = (float)(smallList[2])
            total += prob * valueList[sprime-1]
        if maxValue < total:
          maxValue = total
      elif(action == 3):
        total = 0.0
        for smallList in east:
          if (int)(smallList[0]) == (s+1):
            sprime = (int)(smallList[1])
            prob = (float)(smallList[2])
            total += prob * valueList[sprime-1]
        if maxValue < total:
          maxValue = total
      elif(action == 4):
        total = 0.0
        for smallList in south:
          if (int)(smallList[0]) == (s+1):
            sprime = (int)(smallList[1])
            prob = (float)(smallList[2])
            total += prob * valueList[sprime-1]
        if maxValue < total:
          maxValue = total
    valueList1[s] = Rs + Lambda * maxValue
    difference = 0.0
  for x in range (0, 81):
    difference += abs(valueList[x] - valueList1[x])
  if difference < 0.0001:
    break
  for x in range (0, 81):
    valueList[x] = valueList1[x]
for i in range(0, 81):
  print "state %d: %.14f" %(i+1, valueList[i])

PI = []
for s in range(0, 81):
  maxValue = 0.0
  direction = 0
  if valueList[s] == 0.0:
    PI.append(0)
    continue
  for action in range(1, 5):
    if action == 1:
      direction = action
      total = 0.0
      for smallList in west:
          if (int)(smallList[0]) == (s+1):
            sprime = (int)(smallList[1])
            prob = (float)(smallList[2])
            total += prob * valueList[sprime-1]
      maxValue = total
    elif(action == 2):
      total = 0.0
      for smallList in north:
        if (int)(smallList[0]) == (s+1):
          sprime = (int)(smallList[1])
          prob = (float)(smallList[2])
          total += prob * valueList[sprime-1]
      if maxValue < total:
        maxValue = total
        direction = action
    elif(action == 3):
      total = 0.0
      for smallList in east:
        if (int)(smallList[0]) == (s+1):
          sprime = (int)(smallList[1])
          prob = (float)(smallList[2])
          total += prob * valueList[sprime-1]
      if maxValue < total:
        maxValue = total
        direction = action
    elif(action == 4):
      total = 0.0
      for smallList in south:
        if (int)(smallList[0]) == (s+1):
          sprime = (int)(smallList[1])
          prob = (float)(smallList[2])
          total += prob * valueList[sprime-1]
      if maxValue < total:
        maxValue = total
        direction = action
  PI.append(direction)
for i in range(0, 81):
  print "State %d: action: %d" % (i+1, PI[i])
