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
    step =0
    seen_states = set()
    seen_states.add(g.current_state)

    while not g.is_terminated_state(g.current_state):
        a = policy[g.current_state]
        next_state = g.get_next_state(a,g.current_state)
        if next_state in seen_states:
            r = -0.5
            state_reward.append((g.current_state,a,r))
            break
        else:
            r = g.reward.get(next_state,0)
        state_reward.append((g.current_state,a,r))
        g.move(a)
        seen_states.add(g.current_state)
        step+=1

    state_reward.append((g.current_state,0))

    G=0
    state_value=[]

    for s,a,r in state_reward[-2::-1]:
        G = r + grama * G
        state_value.append((s,a,G))
    return state_value

V={}
for s in g.state:
    V[s]=0



def calSampleMean(mean_list,new_sample):
    if mean_list.get((new_sample[0], new_sample[1]))==None:
        mean_list[(new_sample[0],new_sample[1])]=(new_sample[2],1)
    else:
        prev_sample_mean = mean_list[(new_sample[0],new_sample[1])][0]
        n = mean_list[(new_sample[0],new_sample[1])][1]
        new_sample_mean = (prev_sample_mean * n + new_sample[2])/(n+1)
        mean_list[(new_sample[0],new_sample[1])] =(new_sample_mean,n+1)

    return mean_list

n=1000
sample_mean={}

def init_policy(g):
    policy ={}
    for s in g.state:
        if not g.is_terminated_state(s):
            policy[s]=random.choice(g.action[s])
    return policy

policy = init_policy(g)
Q = {}

for s in g.state:
    if not g.is_terminated_state(s):
        for a in g.action[s]:
            Q[(s,a)] = 0


def argmax(Q,s,g):
    a = g.action[s][0]
    max = Q[(s,a)]
    key = a
    for a in g.action[s]:
        if Q[(s,a)]>max:
            max = Q[(s,a)]
            key = a
    return key

for i in range(n):
    #policy = init_policy(g)
    state_value = play_game(policy,g)
    for new_sample in state_value:
        sample_mean = calSampleMean(sample_mean,new_sample)

    for new_mean in sample_mean:
        Q[(new_mean[0],new_mean[1])] = sample_mean[new_mean][0]

    for s in g.state:
        if not g.is_terminated_state(s):
            policy[s] = argmax(Q,s,g)



#print(sample_mean)
print_policy(policy,g)
for s in g.state:
    if not g.is_terminated_state(s):
        V[s] = Q[(s,policy[s])]

print_value(V,g)



#for v in sample_mean:
#    V[v] = sample_mean[v][0]

#print_value(V,g)
