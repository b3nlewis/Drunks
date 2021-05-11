# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:05:38 2021

@author: b3nle
"""

import random
random.seed()

class drunk():
    def __init__(self, pubX, pubY, houseX, houseY):
        self.x = pubX #initial starting location
        self.y = pubY
        self.start = (pubX, pubY)
        #self.number = number
        #self.drunks = drunks
        self.end = (houseX, houseY)#house
        self.route = []
        self.distance = 0
        
    def starting_location(self):
        print(self.start)
        return(self.start)
    
    def ending_location(self):
        print(self.end)
        return(self.end)
    
    def move(self):
        #if ([self.x, self.y]) == #that coord in route list:
            #find coords before and after
            #move to closest coord which hasnt been seen
        (dx, dy) = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)]) # N, E, S, W
        self.x = (self.x + dx) % 300
        self.y = (self.y + dy) % 300
        self.route.append([[self.x, self.y]]) #So agent can see if they have been here before.
        #self.pushX = self.x
        #self.pushY = self.y
        self.distance = self.distance + 1
        
    def is_home(self):
        if (self.x, self.y) != self.end:
            #print("False")
            return(False)# will continue moving
        else:
            print("Walk completed")
            return(True)
            


     
'''gets drunk to move until it reaches home'''
#for i in range(25):
     
#    j = drunk(i)
#    x = 0
#    while drunk.is_home(j) == False:
#        drunk.move(j)
#        x += 1
        #plt.figure(figsize=(8,8))
        #plt.scatter(a.pushX, a.pushY)
        #plt.show()
#    else:
#        print("Drunk:",i,"finished in", x, "steps")
#        print(j.is_home())
           