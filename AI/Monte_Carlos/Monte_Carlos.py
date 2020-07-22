from GridWorld import GridWorld
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

n=100
g.current_state = (2,0)
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

print(state_value)
