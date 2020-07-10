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



V={}

for s in g.state:
    V[s]=0

grama = 0.9

while True:
    for s in g.state:
        old_v = V[s]
        new_v= 0
        for a in g.action[s]:
            next_s = g.get_next_state(a,s)
            print ('next state : ',next_s)
            new_v += g.reward.get(next_s,0) + (grama * V[next_s])
            print_value(V,g)
        V[s] = new_v
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
