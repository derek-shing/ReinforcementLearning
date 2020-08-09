import gym
import numpy as np
import seaborn as sns
import random


env = gym.make('CartPole-v0')
env.reset()



def to_state(observation):
    s=[]
    cart_position_bins = np.linspace(-2.4, 2.4, 9)
    cart_velocity_bins = np.linspace(-2, 2, 9) # (-inf, inf) (I did not check that these were good values)
    pole_angle_bins = np.linspace(-0.4, 0.4, 9)
    pole_velocity_bins = np.linspace(-3.5, 3.5, 9) # (-inf, inf) (I did not check that these were good values)
    r = str(np.digitize(observation[0], cart_position_bins))+\
    str(np.digitize(observation[1], cart_velocity_bins))+\
    str(np.digitize(observation[2], pole_angle_bins))+\
    str(np.digitize(observation[3], pole_velocity_bins))
    return int(r)



def get_action(Q,observation):
    e = random.random()
    if e<0.05:
        return env.action_space.sample()
    else:
        s = to_state(observation)
        return np.argmax(Q[s])


def playgame(env,Q):
    o = env.reset()
    done=False
    reward =0
    while not done:
        a = get_action(Q,o)
        previous_o = o
        o,r,done,info = env.step(a)
        if done:
            r=-300
        Q = update(Q,previous_o,a,r,o)
        reward+=1
    return reward

def predict(Q,s):
    return np.max(Q[s])


def update(Q,previous_o,a,r,o):
    state = to_state(previous_o)
    next_state = to_state(o)
    G = r + 0.9 *predict(Q, next_state)
    Q[state][a]+= Q[state][a] + 0.02*(G - Q[state][a])
    return Q




num_states = 10**4
num_actions =2

Q = np.random.uniform(low=-1, high=1, size=(num_states, num_actions))

num_esp = 10000

for i in range(num_esp):
    reward = playgame(env,Q)
    print(i," Iteration: ", reward)


#ns.distplot(record['CPosition'])
