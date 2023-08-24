from numpy import *
import random

class Environment:


    def __init__(self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
        self.chart = zeros((sizeX,sizeY))
        self.chart[init_posX][init_posY] = 2

        values = [0,1]
        probs = [1 - dirt_rate,dirt_rate]

        for i in range (0,sizeX):
            for j in range (0,sizeY):
                self.chart[i][j] = random.choices(values,probs) + self.chart[i][j]

        self.performance = 0

    def print_environment(self):
        chart_list = self.chart.tolist()

        for list in chart_list:
            print(list)

    def accept_action(self,action,x,y):
        if action == 'suck':
            self.chart[x][y] -= 1
            self.performance += 1

    def is_dirty(self,x,y):
        if (self.chart[x][y] % 2) == 0:
            return False
        else:
            return True
        
    def get_performance(self):
        return self.performance
    
    def check_clean(self):
        x = self.chart.shape[0]
        y = self.chart.shape[1]

        for i in range(0,x):
            for j in range(0,y):
                if (self.chart[i][j] % 2) != 0:
                    return False
                
        return True
                
