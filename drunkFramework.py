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
        self.end = (houseX, houseY)#house
        self.route = []
        self.distance = 0
        self.lastPos = []
        
    def starting_location(self):
        print(self.start)
        return(self.start)
    
    def ending_location(self):
        print(self.end)
        return(self.end)
    
    def move(self):#simple method which includes backtracking
        
        #if self.check_cell() == False:
        (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) # N, E, S, W
        self.x = (self.x + dx) % 300
        self.y = (self.y + dy) % 300
        self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
        self.distance = self.distance + 1
    
    def moveAdvance(self): #advance method which stops drunk backtracking
        if self.lastPos != None:
            if self.lastPos == [0, 1]: #check if last pos is north
                (dx, dy) = random.choice([(0, 1), (1, 0), (-1, 0)]) #Cannot go south
                self.x = (self.x + dx) % 300
                self.y = (self.y + dy) % 300
                self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
                self.lastPos = [dx, dy]
                self.distance = self.distance + 1
            #check if last pos is east
            elif self.lastPos == [1, 0]: #check if last pos is east
                (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1)]) #Cannot go west
                self.x = (self.x + dx) % 300
                self.y = (self.y + dy) % 300
                self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
                self.lastPos = [dx, dy]
                self.distance = self.distance + 1
            #check if last pos is south
            elif self.lastPos == [0, -1]: #check if last pos is south
                (dx, dy) = random.choice([(1, 0), (0, -1), (-1, 0)]) #Cannot go north
                self.x = (self.x + dx) % 300
                self.y = (self.y + dy) % 300
                self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
                self.lastPos = [dx, dy]
                self.distance = self.distance + 1
            #check if last pos is west
            else:  #check if last pos is west
                (dx, dy) = random.choice([(0, 1), (0, -1), (-1, 0)]) #Cannot go east
                self.x = (self.x + dx) % 300
                self.y = (self.y + dy) % 300
                self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
                self.lastPos = [dx, dy]
                self.distance = self.distance + 1
        else:
            (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) # N, E, S, W
            self.x = (self.x + dx) % 300
            self.y = (self.y + dy) % 300
            self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
            self.lastPos = [dx, dy]
            self.distance = self.distance + 1              
                    
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
              
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
    
    
    
    
    
                      