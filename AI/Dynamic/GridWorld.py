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

    def print_state(self):
        print(self.state)


g = GridWorld(3,4)
g.print_state()
