import gym
import numpy as np
import seaborn as sns


env = gym.make('CartPole-v0')
env.reset()

def playgame(env,record):
    env.reset()
    done=False
    while not done:
        o,r,done,info = env.step(env.action_space.sample())
    record['CPosition'].append(o[0])
    record['CVelocity'].append(o[1])
    record['PoleAngle'].append(o[2])
    record['PoleVelcity'].append(o[3])
    return record


record ={
    'CPosition':[],
    'CVelocity':[],
    'PoleAngle':[],
    'PoleVelcity':[]
}
for i in range(10000):
    record = playgame(env,record)


sns.distplot(record['CPosition'])
