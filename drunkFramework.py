# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:05:38 2021

@author: b3nle
"""

import random
import pandas as pd
random.seed(10)

class drunk():
    def __init__(self, pubX, pubY, houseX, houseY):
        self.x = pubX #initial starting location
        self.y = pubY
        self.start = (pubX, pubY)
        self.startX = pubX
        self.startY = pubY
        self.end = (houseX, houseY)#house
        self.route = []
        self.stuck = []
        self.distance = 0
        self.position = []
        self.j = 0
        
    def starting_location(self):
        print(self.start)
        return(self.start)
    
    def ending_location(self):
        print(self.end)
        return(self.end)
    
    def move(self):
        (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) # N, E, S, W
        x = dx + self.x
        y = dy + self.y
        if ([(x, y)]) not in self.stuck:
            i = 0
            while i <= 3:
                if ([(x, y)]) not in self.route:
                    #print([(x, y)])
                    self.x = (self.x + dx) % 300
                    self.y = (self.y + dy) % 300
                    self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
                    self.distance = self.distance + 1
                    i += 1
                else:
                    self.x = self.startX
                    self.y = self.startY
                    self.stuck = self.route[-1]
                    self.route = []
            
            
        
        
            # moves = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W
            # updated_moves = random.sample(moves, 4)
            # #print(updated_moves)
            # x = self.x
            # y = self.y
            # i = 0
            # for i in range(0, 4, 1):
            #     #print("loop", i)
            #     (dx, dy) = updated_moves[i] 
            #     x = (x + dx) % 300
            #     y = (y + dx) % 300
            #     i += 1
            #     if ([(x, y)]) not in self.route:
            #         self.x = (x + dx) % 300
            #         self.y = (y + dx) % 300
            #         self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
            #         self.distance = self.distance + 1
            #         #self.j += 1
            #         #print("2")
            #         #print("loop", i)
            #         return
            #     else:
            #         pass
            # else:
            #     (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) # N, E, S, W
            #     self.x = (self.x + dx) % 300
            #     self.y = (self.y + dy) % 300
            #     self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
            #     self.distance = self.distance + 1
            #     #self.j += 1
            #     #print("3")
            # #print(self.j)
                
                    
    def is_home(self):
        if (self.x, self.y) != self.end:
            #print("False")
            return(False)# will continue moving
        else:
            print("Walk completed")
            return(True)
            
    def get_route(self):
        df = pd.DataFrame(self.route)
        return(df)
              
        
    
    
    
    
    
    
    
    
    
    
    
    # def check_cell(self):
    #     check = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    #     position = [self.x, self.y]
    #     if position not in self.route:
    #         #print("3")
    #         return False
    #     else:
    #         for i in range(4):
    #             position = [sum(i) for i in zip(position, check[i])]
    #             if position not in self.route:
    #                 self.position = position
    #                 self.route.append([position])
    #                 #print("1")
    #                 return self.position
    #             else:
    #                 val = random.choice(check)
    #                 position = [sum(i) for i in zip(position, val)]
    #                 self.position = position
    #                 self.route.append([position])
    #                 #print("2")
    #                 return self.position
            
            
            
            
            
            
            # x = 0
            # while x < 5:
            #     randVal = random.choice(check)                                  
            #     try_pos = [sum(i) for i in zip(position, randVal)]
            #     if try_pos in self.route:
            #         x += 1
            #         print("moved")
            #         self.try_pos = try_pos
            #         return self.try_pos
            #     else:
            #         return False #if no spaces available force a move.
            # else:
            #     randVal = random.choice(check)
            #     try_pos = [sum(i) for i in zip(position, randVal)]
            #     self.try_pos = try_pos
            #     return self.try_pos                          