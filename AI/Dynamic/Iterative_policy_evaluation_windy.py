from GridWorld import GridWorld


g = GridWorld(3,4)
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
            for a in g.action[s]:
                action_prob = policy[s].get(a,0)
                transition_probs = g.probs[(s,a)]
                possible_next_state=list(transition_probs.keys())
                for next_state in possible_next_state:
                    new_v += action_prob*transition_probs.get(next_state,0)*(g.reward.get(next_state,0) + (grama * V[next_state]))
            V[s] = new_v
            different = max(different, abs(new_v-old_v))

    if different<0.0003:
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
