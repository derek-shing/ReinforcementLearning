from GridWorld import GridWorld
import random
g = GridWorld(3,4)

policy={
    (0, 0):'R',
    (0, 1):'R',
    (0, 2):'R',
    (1, 0):'U',
    (1, 1):'U',
    (1, 2):'U',
    (1, 3):'U',
    (2, 0):'R',
    (2, 1):'R',
    (2, 2):'U',
    (2, 3):'L'
}

def print_policy(p,g):
    for r in range(g.row):
        print('------------------')
        for c in range(g.col):
            a = p.get((r,c),' ')
            print(' %s |'%a, end="")
        print("")

def print_value(V,g):
    for r in range(g.row):
        print('------------------')
        for c in range(g.col):
            v = V.get((r,c), 0)
            print(' %f |'%v, end="")
        print("")



def play_game(policy, g):
    g.current_state = random.choice(g.state)
    state_reward = []
    grama =0.9

    while not g.is_terminated_state(g.current_state):
        a = policy[g.current_state]
        next_state = g.get_next_state(a,g.current_state)
        r = g.reward.get(next_state,0)
        state_reward.append((g.current_state,r))
        g.move(a)

    state_reward.append((g.current_state,0))

    G=0
    state_value=[]

    for s,r in state_reward[-2::-1]:
        G = r + grama * G
        state_value.append((s,G))
    return state_value

V={}
for s in g.state:
    V[s]=0



def calSampleMean(mean_list,new_sample):
    if mean_list.get(new_sample[0])==None:
        mean_list[new_sample[0]]=(new_sample[1],1)
    else:
        prev_sample_mean = mean_list[new_sample[0]][0]
        n = mean_list[new_sample[0]][1]
        new_sample_mean = (prev_sample_mean * n + new_sample[1])/(n+1)
        mean_list[new_sample[0]] =(new_sample_mean,n+1)

    return mean_list

n=10000
sample_mean={}




for i in range(n):
    state_value = play_game(policy,g)
    for new_sample in state_value:
        sample_mean = calSampleMean(sample_mean,new_sample)

print(sample_mean)
for v in sample_mean:
    V[v] = sample_mean[v][0]

print_value(V,g)
