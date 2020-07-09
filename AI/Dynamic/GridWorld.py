class GridWorld:
    #Contruct the Grid world by row and col

    def create_state(self,row,col):
        state=[]
        for i in range(row):
            for j in range(col):
                state.append((i,j))

        return state


    def __init__(self,row, col):
        self.state= self.create_state(row,col)
        self.standard_grid()
        self.define_action()

    def print_state(self):
        print(self.state)

    def standard_grid(self):
        self.current_state =(2,0)
        self.reward = {}
        for s in self.state:
            self.reward[s]=-1
        self.reward[(0,3)] = 1

    #define Action
    def define_action(self):
        self.A = ['U','D','L','R']

    def move(self,a):
        if a == self.A[0]: #Up
            s = (self.current_state[0]-1,self.current_state[1])
            if s in self.state:
                self.current_state = s
        elif a == self.A[1]: #down
            s = (self.current_state[0]+1,self.current_state[1])
            if s in self.state:
                self.current_state = s
        elif a == self.A[2]: #Left
            s = (self.current_state[0],self.current_state[1] -1)
            if s in self.state:
                self.current_state = s
        elif a == self.A[3]: #Right
            s = (self.current_state[0],self.current_state[1] + 1)
            if s in self.state:
                self.current_state = s

    def print_current_state(self):
        print("The current state is ",self.current_state)

    def is_terminated_state(self,s):
        if s == (0,3):
            return True
        else:
            return False







g = GridWorld(3,4)
g.print_current_state()
while not g.is_terminated_state(g.current_state):
    i=input()
    g.move(i)
    g.print_current_state()

#g.print_state()
#print(g.reward)
