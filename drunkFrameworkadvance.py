# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:05:38 2021

@author: b3nle
"""

import random
import pandas as pd
random.seed()

class drunk():
    def __init__(self, pubX, pubY, houseX, houseY):
        self.x = pubX #initial starting location
        self.y = pubY
        self.start = (pubX, pubY)
        self.end = (houseX, houseY)#house
        self.route = []
        self.distance = 0
        self.position = []
        
    def starting_location(self):
        print(self.start)
        return(self.start)
    
    def ending_location(self):
        print(self.end)
        return(self.end)
    
    def move(self):
        
        #if self.check_cell() == False:
        (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) # N, E, S, W
        self.x = (self.x + dx) % 300
        self.y = (self.y + dy) % 300
        self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
        self.distance = self.distance + 1
        # else:
        #     self.x = self.position[0]
        #     self.y = self.position[1]
        #     self.distance = self.distance + 1

            
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
                    
                