from numpy import *
import environment
import heapq

class Agent:

    def search_pos(env):
        for i in range (0, env.chart.shape[0]):
            for j in range (0, env.chart.shape[1]):
                if (env.chart[i][j] == 2) or (env.chart[i][j] == 3):
                    return (i,j)
    
    def __init__(self, env):
        self.environment = env
        self.pos = Agent.search_pos(env)

    def idle(self):
        return True
    
    def move(self,xDisp,yDisp):
        x = self.pos[0]
        y = self.pos[1]
        
        self.environment.chart[x + xDisp][y + yDisp] += 2
        self.environment.chart[x][y] -= 2
        self.pos = (x + xDisp,y + yDisp)

    def up(self):
        try:
            self.move(-1,0)
        except:
            self.right()

    def right(self):
        try:
            self.move(0,1)
        except:
            self.down()

    def down(self):
        try:
            self.move(1,0)
        except:
            self.left()

    def left(self):
        try:
            self.move(0,-1)
        except:
            self.up()

    def suck(self):
        x = self.pos[0]
        y = self.pos[1]
        self.environment.accept_action('suck',x,y)

    def idle(self):
        return
    
    # def find_nearest_one(self, matrix, target_row, target_column):
    #     nearest_distance = float('inf')  # Inicializamos la distancia con infinito para encontrar la más pequeña
    #     nearest_row = -1
    #     nearest_column = -1
        
    #     for row in range(len(matrix)):
    #         for column in range(len(matrix[0])):
    #             if matrix[row][column] == 1:
    #                 distance = abs(row - target_row) + abs(column - target_column)  # Calculamos la distancia Manhattan
    #                 if distance < nearest_distance:
    #                     nearest_distance = distance
    #                     nearest_row = row
    #                     nearest_column = column
    
    #     return (nearest_row, nearest_column, nearest_distance) 
    
    def find_nearest_one(self, matrix, target_row, target_column):

        nearest_distance = float('inf')
        nearest_row = -1
        nearest_column = -1

        for row in range(max(0, target_row - nearest_distance), min(len(matrix), target_row + nearest_distance + 1)):
            for column in range(max(0, target_column - nearest_distance), min(len(matrix[0]), target_column + nearest_distance + 1)):
                if matrix[row][column] == 1:
                    distance = abs(row - target_row) + abs(column - target_column)
                    if distance < nearest_distance:
                        nearest_distance = distance
                        nearest_row = row
                        nearest_column = column

        return (nearest_row, nearest_column, nearest_distance)
    
    def perspective(self):
        x = self.pos[0]
        y = self.pos[1]

        res = self.find_nearest_one(self.environment.chart, x, y)

        if res == None:
            return False
        
        xn = res[0]
        yn = res[1]

        return (xn,yn)
        

    
    def think(self):
        moves = 0
        is_clean = False

        while (not self.environment.check_clean()) and moves < 1000:
            x = self.pos[0]
            y = self.pos[1]

            rn = self.perspective()

            if rn == False:
                break

            if self.environment.is_dirty(x,y):
                self.suck()
            else:
                if x < rn[0]:
                    if rn[1] > y:
                        for i in range (0, abs(y - rn[1])):
                            moves += 1
                            self.right()
                    elif rn[1] < y:
                        for i in range (0, abs(y - rn[1])):
                            moves += 1
                            self.left()

                    for i in range (0,abs(x - rn[0])):
                        moves += 1
                        self.down()
                elif x > rn[0]:
                    if rn[1] > y:
                        for i in range (0, abs(y - rn[1])):
                            moves += 1
                            self.right()
                    elif rn[1] < y:
                        for i in range (0, abs(y - rn[1])):
                            moves += 1
                            self.left()

                    for i in range (0,abs(x - rn[0])):
                        moves += 1
                        self.up()
                else:
                    if rn[1] > y:
                        for i in range (0, abs(y - rn[1])):
                            moves += 1
                            self.right()
                    elif rn[1] < y:
                        for i in range (0, abs(y - rn[1])):
                            moves += 1
                            self.left()

        if moves < 1000:
            is_clean = True

        return (moves,self.environment.performance)
    
    def random_think(self):

        moves = 0
        is_clean = False

        while (not self.environment.check_clean()) and moves < 1000:
            num = random.randint(0,6)

            if num < 4:
                moves += 1
                if num == 0:
                    self.up()
                elif num == 1:
                    self.right()
                elif num == 2:
                    self.down()
                else:
                    self.left()
            elif num == 4:
                self.idle()
            else:
                self.suck()

        if moves < 1000:
            is_clean = True

        return (moves,self.environment.performance)

