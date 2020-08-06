import gym
env = gym.make('CartPole-v0')
env.reset()

done = False
step=0
while not done:
    observation, reward, done, info = env.step(env.action_space.sample())
    step+=1

print (step)
