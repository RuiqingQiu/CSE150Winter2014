'''
	Name: Ruiqing Qiu
	PID: A98022702
	Userid: rqiu
	filename: hw4.py
'''
import matplotlib.pyplot as plt
import math
xList = []
yList = []
T = 267
n = 23
with open ('y.txt') as yFile:
  for line in yFile:
    tmp = line.split()
    yList.append(tmp[0])
with open ('x.txt') as xFile:
  for line in xFile:
    tmp = line.split()
    tmpList = []
    for i in range(0, 23):
    	tmpList.append(tmp[i])
    xList.append(tmpList)

#Passing in the position of the Y, the number of its sample
def noisy_OR_CPT (Y, Yt, Pi):
  if Y == 0:
    total = 1.0
    for i in range(0, 23):
      total *= ((1.0 - Pi[i]) ** int(xList[Yt][i]))
    return total
  else:
    total = 1.0
    for i in range(0, 23):
      total *= ((1.0 - Pi[i]) ** int(xList[Yt][i]))
    return 1.0 - total

def LogLike(Pi):
  LogLikelihood = 0.0
  mistake = 0
  for i in range (0, T):
    if int(yList[i]) == 0: 
      num = noisy_OR_CPT(0, i, Pi)
      mis = noisy_OR_CPT(1, i, Pi)
      if mis >= 0.5:
	mistake += 1
    else:
      num = noisy_OR_CPT(1, i, Pi)
      mis = noisy_OR_CPT(1, i, Pi)
      if mis <= 0.5:
	mistake += 1
    LogLikelihood += math.log(num)
  print 'mistake %d' %mistake 
  return LogLikelihood

#count Ti, the number of example in which Xi = 1
def findTi(i):
  total = 0.0
  for index in range(0, T):
    if(int(xList[index][i]) == 1):
      total = total + 1.0
  return total

def PI_update(Pi):
  newPi = []
  for i in range(0, 23):
    Ti = findTi(i)
    total = 0.0
    for j in range(0, T):
      Yt = int(yList[j])
      Xit = int(xList[j][i])
      oldPi = Pi[i]
      denominator = noisy_OR_CPT(1, j, Pi)
      total += Yt*Xit*oldPi / denominator 
    newPi.append(1/Ti * total)
  return newPi

Pi = []
for i in range (0,23):
  Pi.append(1.0/n)
LogList = []
for i in range (0, 513):
  value = (1.0/T * LogLike(Pi))
  print "%d log %f\n" % (i, value)
  LogList.append(value)
  Pi = PI_update(Pi)
print Pi
plt.plot(Pi)
plt.ylabel('pi')
plt.show()
