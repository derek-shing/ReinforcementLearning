from GridWorld import GridWorld
import random


g = GridWorld(3,4)

'''
policy={
    (0, 0):{'R':1},
    (0, 1):{'R':1},
    (0, 2):{'R':1},
    (1, 0):{'U':1},
    (1, 1):{'U':1},
    (1, 2):{'U':1},
    (1, 3):{'U':1},
    (2, 0):{'R':0.5, 'U':0.5},
    (2, 1):{'R':1},
    (2, 2):{'U':1},
    (2, 3):{'L':1}
}
'''

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


def eval_policy(g,policy):
    V={}
    for s in g.state:
        V[s]=0
    grama = 0.9
    n=0
    while n<10:
        n+=1
        print("No of iteration :",n)
        print_value(V,g)
        different = 0
        for s in g.state:
            if not g.is_terminated_state(s):
                old_v = V[s]
                new_v= 0
                a = policy[s]
                #for a in g.action[s]:
                    #action_prob = policy[s].get(a,0)
                action_prob =1
                transition_probs = g.probs[(s,a)]
                possible_next_state=list(transition_probs.keys())

                for next_state in possible_next_state:
                    new_v += action_prob*transition_probs.get(next_state,0)*(g.reward.get(next_state,0) + (grama * V[next_state]))
                V[s] = new_v
                different = max(different, abs(new_v-old_v))

        if different<0.0003:
            break
    return V


def init_policy(g):
    policy ={}
    for s in g.state:
        if not g.is_terminated_state(s):
            policy[s]=random.choice(g.action[s])
    return policy


V={}



policy = init_policy(g)
V = eval_policy(g,policy)
print_policy(policy,g)
print_value(V,g)

grama = 0.9

while True:
    V = eval_policy(g,policy)
    policy_changed = False
    for s in g.state:
        if not g.is_terminated_state(s):
            max_v = V[s]
            for a in g.action[s]:
                v=0
                transition_probs = g.probs[(s,a)]
                possible_next_state=list(transition_probs.keys())
                for next_state in possible_next_state:
                    v += transition_probs.get(next_state,0)*(g.reward.get(next_state,0) + (grama * V[next_state]))
                if v > max_v:
                    policy_changed=True
                    policy[s] = a


    if policy_changed==False:
        break

print_policy(policy,g)
print_value(V,g)

#g.print_state()

"""
while not g.is_terminated_state(g.current_state):
    print("Possible move: ", g.action[g.current_state])
    i=input()
    g.move(i)
    g.print_current_state()

"""
