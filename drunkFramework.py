# -*- coding: utf-8 -*-
"""
This is a framework to be used for the drunks.py model.
It is responsible for moving the agents around the environment.
There are two moving functions: move and moveAdvance.
Move is a pseudo random algorithm whereas moveAdvance, stops agents backtracking.

"""

import random
import pandas as pd
random.seed(10)

class drunk():
    
    def __init__(self, pubX, pubY, houseX, houseY):
        '''
        Initilisation of drunk agents.
        Variables are initialised from runModel function in drunks.py
        
        Parameters:
        
        pubX: variable
            x position of its assigned starting point
        pubY: variable
            y position of its assigned starting point
        houseX: variable
            x position of its assigned ending point
        houseY: variable
            y position of its assigned ending point

        Returns:
        
        self.x: variable
            current x position of drunk
        self.y: variable
            current y position of drunk
        self.start: variable
            starting location of drunk
        self.end: variable
            ending location of drunk
        self.route: list
            a list containing every cell drunk has visited
        self.distance: list
            a list containing the number of moves the drunk has made
        self.lastPos: list
            a list containing the last position the drunk was
            
        '''
        self.x = pubX #initial starting location
        self.y = pubY #initial starting location
        self.start = (pubX, pubY)
        self.end = (houseX, houseY)#house/ending position
        self.route = [] #exported to drunk.py
        #self.distance = 0 #used to see how far each agent has travelled.
        self.lastPos = []# only used in the module
        
    def starting_location(self):
        '''
        Returns:
        
        Drunk starting location

        '''
        print(self.start)
        return(self.start)
    
    def ending_location(self):
        '''
        Returns:
        
        Drunk ending location

        '''
        print(self.end)
        return(self.end)
    
    def move(self):#simple method which includes backtracking
        '''
        Simple method which creates a pseudo-random walking alogrithm

        Returns:
        
        self.x: variable
            current x position of drunk
        self.y: variable
        current y position of drunk
        self.route: list
            a list of cells drunks have visited
        self.distance: list
            a list of the number of moves

        '''
        #if self.check_cell() == False:
        (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) # N, E, S, W
        self.x = (self.x + dx) % 300
        self.y = (self.y + dy) % 300
        self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
        #self.distance = self.distance + 1
    
    def moveAdvance(self): #advance method which stops drunk backtracking previous step.
        '''
        Advanced method which stops backtracking of drunks.

        Returns:
        
        self.x: variable
            current x position of drunk
        self.y: variable
        current y position of drunk
        self.route: list
            a list of cells drunks have visited
        self.lastPos: list
            a list of the drunks last position
        self.distance: list
            a list of the number of moves

        '''
    
        #if self.lastPos != None:#any move apart from first move
            
        if self.lastPos == [0, 1]: #check if last pos is north
            (dx, dy) = random.choice([(0, 1), (1, 0), (-1, 0)]) #Cannot go south
            self.x = (self.x + dx) % 300
            self.y = (self.y + dy) % 300
            self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
            self.lastPos = [dx, dy]
            #self.distance = self.distance + 1
            
        #check if last pos is east
        elif self.lastPos == [1, 0]: 
            (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1)]) #Cannot go west
            self.x = (self.x + dx) % 300
            self.y = (self.y + dy) % 300
            self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
            self.lastPos = [dx, dy]
            #self.distance = self.distance + 1
            
        #check if last pos is south
        elif self.lastPos == [0, -1]:
            (dx, dy) = random.choice([(1, 0), (0, -1), (-1, 0)]) #Cannot go north
            self.x = (self.x + dx) % 300
            self.y = (self.y + dy) % 300
            self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
            self.lastPos = [dx, dy]
            #self.distance = self.distance + 1
            
        #check if last pos is west
        elif self.lastPos == [-1, 0]:
            (dx, dy) = random.choice([(0, 1), (0, -1), (-1, 0)]) #Cannot go east
            self.x = (self.x + dx) % 300
            self.y = (self.y + dy) % 300
            self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
            self.lastPos = [dx, dy]
            #self.distance = self.distance + 1
                
        else:
            #used for first move where no last position is available
            (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) # N, E, S, W
            self.x = (self.x + dx) % 300
            self.y = (self.y + dy) % 300
            self.route.append([(self.x, self.y)]) #So agent can see if they have been here before.
            self.lastPos = [dx, dy]
            #self.distance = self.distance + 1              
                    
    def is_home(self):#looks to see if drunk has reached its house
        '''
        Checks to see if drunk has reached its ending point

        Returns:
        
        False: Boolean
            Drunk has not finished
        True: Boolean
            Drunk has finished its walk.

        '''
        if (self.x, self.y) != self.end:
            #print("False")
            return(False)# will continue moving
        else:
            print("Walk completed")
            return(True)#tells drunks.py to move onto next agent
            
    def get_route(self):
        '''
        Converts self.route into a dataframe

        Returns:
        
        df: pandas dataframe
            A dataframe containing every cell the drunk has visited.

        '''
        df = pd.DataFrame(self.route)
        return(df)
              
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
    
    
    
    
    
                      