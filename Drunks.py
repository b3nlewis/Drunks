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
import seaborn as sns

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
            pubList.append([j, y, x])
            
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
            houseList.append([i, y, x])
            
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
    #num_of_steps = 0
    drunk_num += 1
    while i.is_home() == False:
        i.move()
       # num_of_steps += 1
    else:
        end = time.process_time()
        print("Drunk", drunk_num,"finished in", i.distance, "steps and", end - start, "seconds.")
        #print(i.is_home())

##################################
 
'''Creating table to store cell counts'''
print('Starting Table')
data = []
for row in range(0,300):
    for col in range(0, 300):
        data.append([row,col])
data = pd.DataFrame(data)
data.columns = ['x', 'y']
print(data)
print('Finished Tables')
##################################

'''creating a dictionary which counts the number of occurences of
a cell for all drunks'''

count = {}
for i in drunks:
    df_route = i.get_route()
    print(df_route)
    column = df_route[0]
    for entry in column:
        if entry in count.keys():
            count[entry] += 1
        else:
            count[entry] = 1
#print(count)


'''converts dictrionary into a dataframe'''    
cell_count = pd.DataFrame(list(count.items()), columns = ['Coords', 'Amount'])
cell_count['x'], cell_count['y'] = zip(*cell_count.Coords)
cell_count.pop('Coords')

print(cell_count)

'''merges dataframe of all cells with cell occurences'''            
merge_data = pd.merge(data, cell_count)

'''Sort df into rows'''
sorted_data = merge_data.sort_values(['y', 'x'], ascending=[True, True])
print(sorted_data.columns)
print(sorted_data)
 
'''converts into a list'''
list_of_amount = sorted_data['Amount'].values.tolist()
print(list_of_amount)

'''converts into list of list'''
i = 0
new_list = []
while i <len(list_of_amount):
    new_list.append(list_of_amount[i : i + 300])
    i += 300
    
print(new_list)

'''creates map'''
ax = sns.heatmap(new_list)

'''export data'''
file_finished = open('export_walks.txt', 'w', newline='') 
writer = csv.writer(file_finished, delimiter=',')
for row in new_list:		
	writer.writerow(row)		# List of values.
file.close()

# #################################
    

# # for i in range(25): #Number of houses
# #      plt.scatter(houseList[i][1], houseList[i][2], c='Red')
# # for j in range(9): #Number of pubs
# #      plt.scatter(pubList[j][1], pubList[j][2], c='Green')
# # plt.show()

