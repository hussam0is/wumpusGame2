ids = ["315881656", "111111111"]
from logic import *


class WumpusController:

    def __init__(self, initial_map, initial_observations):
        self.KB = PropKB()
        self.heroes_locations = {'11': None, '12': None, '13': None, '14': None}
        print(initial_map,initial_observations)
        self.dim_x = len(initial_map)
        self.dim_y = len(initial_map[0])
        for i in range(1,self.dim_x +1):
            for j in range(1,self.dim_y+1):
                B = "B" + str(i) + str(j) + ' <=> ('
                notB = "~B" + str(i) + str(j) + ' <=> ('
                Gold = "GOLD" + str(i) + str(j) + ' <=> ('
                notGold = "~GOLD" + str(i) + str(j) + ' <=> ('
                S = "S" + str(i) + str(j) + ' <=> ('
                notS = "~S" + str(i) + str(j) + ' <=> ('
                stench = self.Available_indecies_stench(i,j)
                breeze_glitter = self.Available_indecies_breeze_glitter(i,j)
                for e in stench:
                    S += " W" + str(e[0]) + str(e[1]) + " |"
                    notS += " ~W" + str(e[0]) + str(e[1]) + " &"
                S = S[:-1] + ")"
                notS = notS[:-1] + ")"
                self.KB.tell(expr(S))
                self.KB.tell(expr(notS))
                for e in breeze_glitter:
                    B += " P" + str(e[0]) + str(e[1]) + " |"
                    notB += " ~P" + str(e[0]) + str(e[1]) + " &"
                    Gold += " G" + str(e[0]) + str(e[1]) + " |"
                    notGold += " ~G" + str(e[0]) + str(e[1]) + " &"
                B = B[:-1] + ")"
                notB = notB[:-1] + ")"
                self.KB.tell(expr(B))
                self.KB.tell(expr(notB))
                Gold = Gold[:-1] + ")"
                notGold = notGold[:-1] + ")"
                self.KB.tell(expr(Gold))
                self.KB.tell(expr(notGold))

        for obs in initial_observations:
            index = str(obs[0][0]) + str(obs[0][1])
            if obs[1] == 'breeze':
                P = 'P' + index
                self.KB.tell(expr(P))
            else:
                P = '~P' + index
                self.KB.tell(expr(P))
            if obs[1] == 'stench':
                P = 'W' + index
                self.KB.tell(expr(P))
            else:
                P = '~W' + index
                self.KB.tell(expr(P))
            if obs[1] == 'glitter':
                P = 'G' + index
                self.KB.tell(expr(P))
            else:
                P = '~G' + index
                self.KB.tell(expr(P))
        print(self.KB.ask_if_true(expr('GOLD18')))
        return



    def Available_indecies_stench(self,i,j):
        indecies = []
        if i > 2:
            indecies.append([i-2,j])
            indecies.append([i-1, j])
        elif i == 2:
            indecies.append([i - 1, j])
        if j > 2:
            indecies.append([i, j-1])
            indecies.append([i, j-2])
        elif j == 2:
            indecies.append([i, j - 1])
        if i < self.dim_x -2:
            indecies.append([i + 2, j])
            indecies.append([i + 1, j])
        elif i == self.dim_x -2:
            indecies.append([i + 1, j])
        if j < self.dim_y -2:
            indecies.append([i , j+2])
            indecies.append([i, j+1])
        elif j == self.dim_y -2:
            indecies.append([i, j+1])
        if i > 1 and j > 1:
            indecies.append([i-1, j-1])
        if i < self.dim_x and j > 1:
            indecies.append([i + 1, j - 1])
        if i > 1 and j < self.dim_y:
            indecies.append([i - 1, j + 1])
        if i < self.dim_x and j < self.dim_y:
            indecies.append([i + 1, j + 1])

        return indecies


    def Available_indecies_breeze_glitter(self,i,j):
        indecies = []
        if i >  1:
            indecies.append([i-1, j])
        if j > 1:
            indecies.append([i, j - 1])
        if i < self.dim_x:
            indecies.append([i+1, j])
        if j < self.dim_y:
            indecies.append([i, j+1])

        return indecies



    def go(self, coordinates, direction1, direction2 = None):
        if direction2:
            return (coordinates[0] + direction1[0] + direction2[0], coordinates[1] + direction1[1] + direction2[1])
        return (coordinates[0] + direction1[0], coordinates[1] + direction1[1])

    def get_next_action(self, partial_map, observations):
        action = None
        direction = None
        up = (-1, 0)
        down = (1, 0)
        right = (0, 1)
        left = (0, -1)
        if observations:
            hero = 11
            return (action,int(hero), direction)
        else:
            print('Observations is empty: All heroes Died')

        #return (str(do_something), hero,str(direction))
        pass
        # TODO: fill in
        # Timeout: 5 seconds


