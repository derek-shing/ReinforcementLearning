import gym
import numpy as np
env = gym.make('CartPole-v0')
env.reset()




def get_action(s, params):
    if s.dot(params)>1:
        return 1
    else:
        return 0



def playgame(env,params):
    observation = env.reset()
    #params = np.random.random(4)*2-1
    done = False
    step=0
    while not done:
        #env.render()
        a = get_action(observation, params)
        #a = env.action_space.sample()
        observation, reward, done, info = env.step(a)
        step+=1
    return step

best=0

for i in range(2000):
    params = np.random.random(4)*2 -1
    step = playgame(env,params)
    if step > best:
        best = step
        best_params = params

env.close()
print(step)

'''
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
'''
