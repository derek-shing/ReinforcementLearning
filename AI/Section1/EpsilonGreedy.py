#Problem:
#1. Create Bandit with different wining rate
#2. Experiment code to explore and exploit

#EpsilonGreedy :
# Gerenate random number x from 0-1
# if x is less the epsilon:
#     select a random bandit (index = random....)
# else:
#     select the Bandit with maximun reward index = max(bandit)
# exploit the bandit[index]
# update the reward rate of bandit[index]


import random

winingRate = [0.2 , 0.3 , 0.5, 0.8];
numberOfTrail = 1000;

class Bandit:
    def __init__(this,winingRate):
        this.winingRate = winingRate;
        this.numberOfBandit = len(winingRate)

    def pull(this,i):
        x = random.random()
        if x <= this.winingRate[i]:
            return 1
        else:
            return 0

bandit = Bandit(winingRate)
reward = 0

sampleRate = [0]*bandit.numberOfBandit
noOfSample = [0]*bandit.numberOfBandit
epsilon = 0.1

def calSampleMean(i, sample):
    n = noOfSample[i]
    prevMean = sampleRate[i]
    newMean = (prevMean * n + sample)/(n+1)
    return newMean




for i in range(numberOfTrail):
    x=random.random()
    if x<epsilon:
        j = random.choice(range(bandit.numberOfBandit))
    else:
        j =sampleRate.index(max(sampleRate))
    result = bandit.pull(j)
    reward = reward + result
    sampleRate[j] = calSampleMean(j,result)
    noOfSample[j] = noOfSample[j] +1

print("reward  is :",reward)
print("estimated wining rate: ", sampleRate)
