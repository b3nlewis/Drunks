# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''Import Statements'''
import random
import numpy
import matplotlib.pyplot as plt
import csv
import drunkFramework
import time
import pandas as pd

'''Step 1'''
xAxis = 300
yAxis = 300
environment = []
pubList = []
houseList = []
drunks = []
random.seed()


'''Step 2'''
#environment = []
#for i in range(xAxis):				# A list of rows
#    rowlist = []      
#    for j in range(yAxis):	
#        i = 0		# A list of value
#        rowlist.append(i)   # Append values to rowlist
#    environment.append(rowlist) # Append rowlist to environment 

#print(environment)

file = open('environment.txt', newline='') 
reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    rowlist = []                # An empty list
    for value in row:			# A list of value
        rowlist.append(int(value))   # Append values to rowlist
    environment.append(rowlist) # Append rowlist to environment 
file.close()

plt.imshow(environment)
plt.show

#file = open('environment.txt', 'w', newline='') 
#writer = csv.writer(file, delimiter=',')
#for row in environment:		
#	writer.writerow(row)		# List of values.
#file.close()

'''Step 3: Get coordinates of all pubs in environment'''

x = 0
for row in (environment):
    rowlist = []
    x += 1
    y = 0
    for j in row:
        y +=1
        if j == 1:
            pubList.append([j, x, y])
            
print(pubList) # A list of lists containing pub x-coordinate and y-coordinate.
    
'''Step 4: Get coordinates of all house in environment'''

x = 0
for row in (environment):
    rowlist = []
    x += 1
    y = 0
    for i in row:
        y +=1
        if i != 1 and i != 0:
            houseList.append([i, x, y])
            
print(houseList) # A list of lists containing pub x-coordinate and y-coordinate.

'''Assigning drunks to a pub (starting location) and a house (ending location).'''
random.shuffle(pubList)#randomises where drunks start
random.shuffle(houseList)#randomises where drunks finish
for i in range(25): #number of drunks
    n = random.randint(0,8)
    pubX, pubY = pubList[n][1], pubList[n][2]
    houseX, houseY = houseList[i][1], houseList[i][2]
    drunks.append(drunkFramework.drunk(pubX, pubY, houseX, houseY))

#Testing                  
print(drunks)
for drunk in(drunks):
    drunk.starting_location()
    drunk.ending_location()
#################################

'''Moving drunks'''
drunk_num = 0
for i in (drunks):
    start = time.process_time()
    num_of_steps = 0
    drunk_num += 1
    while i.is_home() == False:
        i.move()
        num_of_steps += 1
    else:
        end = time.process_time()
        print("Drunk", drunk_num,"finished in", num_of_steps, "steps and", end - start, "seconds.")
        #print(i.is_home())

  
'''Creating table to store cell counts'''
print('Starting Table')
#Creates a dataframe with all cells from environment in it.
data = []
for row in range(0,301):
    for col in range(0, 301):
        data.append([row, col])
#print(data)

data1 = pd.Series(data)#converts matrix into series so only one column
df = pd.DataFrame(data1)#converts series into dataframe to add column
df.insert(1, 'Count', 0, False)#creates an additional column called Count.
print(df)
print('Finished Tables')

# #go through every drunk route list
# for i in (drunks):
#     drunk_route = pd.DataFrame(drunk.route)
#     drunk_route.columns
#     #print(drunk_route)
#     drunk_route[0].value_counts()
#     print(drunkdrunk_route)
# #for every point add a value of 1 to count column



#################################
    

for i in range(25): #Number of houses
     plt.scatter(houseList[i][1], houseList[i][2], c='Red')
for j in range(9): #Number of pubs
     plt.scatter(pubList[j][1], pubList[j][2], c='Green')
plt.show()

