# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''Import Statements'''
import matplotlib
matplotlib.use('TkAgg')
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import csv # to read files
import drunkFrameworkadvance
import time #for testing
import pandas as pd #for dataframes
import seaborn as sns #for heatmaps, looks better than plt
import sys
import argparse #used for commandline interface.
import tkinter as tk

    #Commandline interface
# parser = argparse.ArgumentParser(description=
# 'Run a Random Walk Agent Based Model where drunk people are simulated.')

# parser.add_argument('-s', '--seed', type=int, metavar = '', help='Assign a seed to the model')
# parser.add_argument('-e', '--exportName', type=str, metavar = '', help='Assign a name for the txt export file')
#args = parser.parse_args()

print('Step 1: Initialisaing Model')
'''Step 1: Initialisation'''
xAxis = 300
print('X Axis:', xAxis)
yAxis = 300
print('Y Axis:', yAxis)
environment = []
pubList = []
houseList = []
drunks = []
new_list = []
random.seed(10)
print('Random Seed:', random.random())
is_running=False



print('Step 2: Defining Functions')
'''Step 2: Define Functions'''
def open_file(input_file, output_file, var_type):
    '''
    
    Parameters
    ----------
    input_file : String
        DESCRIPTION.
    output_file : variable
        DESCRIPTION.
    var_type : TYPE
        DESCRIPTION.

    Returns
    -------
    Returns the input file as a List

    '''
    
    file = open(input_file, newline='') 
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:				# A list of rows
        rowlist = []                # An empty list
        for value in row:			# A list of value
            rowlist.append(var_type(value))   # Append values to rowlist
        output_file.append(rowlist) # Append rowlist to environment 
    file.close()
    
def write_file(input_file, output_file):
    '''
    
    Parameters
    ----------
    input_file : TYPE
        DESCRIPTION.
    output_file : TYPE
        DESCRIPTION.
  
    Returns
    -------
    None.

    '''
    file_finished = open(output_file, 'w', newline='') 
    writer = csv.writer(file_finished, delimiter=',')
    for row in input_file:		
    	writer.writerow(row)		# List of values.
    file_finished.close()

def main():
    '''
    

    Returns
    -------
    None.

    '''
    print('Step 3: Creating Base Environment')
    '''Step 3: Create Environment'''
    '''creates a 300 by 300 grid'''
    #for i in range(xAxis):				# A list of rows
    #    rowlist = []      
    #    for j in range(yAxis):	
    #        i = 0		# A list of value
    #        rowlist.append(i)   # Append values to rowlist
    #    environment.append(rowlist) # Append rowlist to environment 
    
    #print(environment)
    
    '''Opens the environment file to read where pubs house are located
    Inserts each row of file into a list of lists'''
    
    open_file('environment.txt', environment, int) 
    
    print('Step 4: Locating Pubs and Houses')
    '''Step 4: Get coordinates of all pubs in environment'''
    
    y = 0 #starting value
    for row in (environment): #goes over each row of list at a time
        y += 1 #finds position on y axis.
        x = 0 #starting value
        for i in row: #goes over each value in row
            x +=1 #finds position on y axis.
            if i == 1: #Pub values are equal to 1.
                pubList.append([i, x, y])# adds x and y values of each pub to a list.
    
    print('Pub List')           
    print(pubList) # A list of lists containing pub x-coordinate and y-coordinate.
     
    
    '''Step 4: Get coordinates of all house in environment'''
    
    y = 0 #starting value
    for row in (environment): #goes over each row of list at a time
        y += 1 #finds position on y axis.
        x = 0 #starting value
        for i in row: #goes over each value in row
            x +=1 #finds position on x axis. 
            if i != 1 and i != 0:
                houseList.append([i, x, y])
                
    print('House List')             
    print(houseList) # A list of lists containing pub x-coordinate and y-coordinate.
    
    
def displayData():
    '''
    

    Returns
    -------
    None.

    '''
    print('Step 5: Displaying Environment, Pubs and Houses')
    '''show pubs and house'''
  
    # the figure that will contain the plot
    fig = plt.figure(figsize=(8,8))
  

    plot1 = fig.add_subplot(111)
    plot1 = plt.imshow(environment)
    for i in range(25): #Number of houses
        plot1 = plt.scatter(houseList[i][1], houseList[i][2], c='Red')
    for j in range(9): #Number of pubs
        plot1 = plt.scatter(pubList[j][1], pubList[j][2], c='Green', label='Pubs')
    canvas =   matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)  
    
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    plt.close()  
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    
    
def runModel():
    '''
    

    Returns
    -------
    None.

    '''
    print('Step 6: Assigning Start and End Locations')    
    '''Step 6: Assigning drunks to start and end locations'''
    '''Assigning drunks to a pub (starting location) and a house (ending location).'''
    random.shuffle(pubList)#randomises where drunks start
    random.shuffle(houseList)#randomises where drunks finish
    for i in range(25): #number of drunks
        n = random.randint(0,8)
        pubX, pubY = pubList[n][0], pubList[n][1]
        houseX, houseY = houseList[i][1], houseList[i][2]
        drunks.append(drunkFrameworkadvance.drunk(pubX, pubY, houseX, houseY))
    
    #Testing                  
    print(drunks)
    for i in(drunks):
        print("Drunk ", i)
        i.starting_location()
        i.ending_location()
        
    #################################
    
    print('Step 7: Moving Drunks')
    '''Step 7: Moving Drunks'''
    drunk_num = 0
    for i in (drunks):
        start = time.process_time()
        drunk_num += 1
        while i.is_home() == False:
            i.move()
        else:
            end = time.process_time()
            print("Drunk", drunk_num,"finished in", i.distance, "steps and", end - start, "seconds.")
            #print(i.is_home())
    
    print('Step 8: Storing and Sorting Drunk Results')
    '''Step 8: Storing and sorting drunk movements'''
    
    '''Creating table to store cell counts'''
    print('Starting Table')
    data = []
    for x in range(0,300):
        for y in range(0, 300):
            data.append([x, y])
    data = pd.DataFrame(data)
    data.columns = ['x', 'y']
    print(data)
    print('Finished Tables')

    
    '''Creating a dictionary which counts the number of occurences of
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
    global new_list
    i = 0
    new_list = []
    while i <len(list_of_amount):
        new_list.append(list_of_amount[i : i + 300])
        i += 300
        
    print(new_list)
    
    print('Step 9: Creating a Map of Cell Densities')
    '''Step 9: Creating a Map'''
    
    fig = plt.figure(figsize=(8,8))
    
  

    plot1 = fig.add_subplot(111)
    plot1 = sns.heatmap(new_list)
    plot1.set_title("Random Walk Density Map", fontsize=18)
    plt.close()
    canvas =  matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root)  
    
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
    
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

  
    
def exportMap():
    '''
    

    Returns
    -------
    None.

    '''
    plt.savefig('walk_heatmap.png')
    plt.close()
    print('Map Exported')
    

def exportData():
    '''
    

    Returns
    -------
    None.

    '''
    '''Step 10: Exporting Data'''
    write_file(new_list, 'walk_data_export.txt')

    print('Data Exported')

    
def exiting():
    '''
    

    Returns
    -------
    None.

    '''
    #need to clear map
    root.quit()
    root.destroy()
    print('Model Closed')
    
      


'''Creating GUI'''
root = tk.Tk()
root.wm_title("Model")
root.geometry('800x800')
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
model_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Display Pubs and Houses", command=displayData)
model_menu.add_command(label="Run model", command=runModel)
model_menu.add_command(label="Export Data", command=exportData)
model_menu.add_command(label="Export Map", command=exportMap)
model_menu.add_command(label="Exit model", command=exiting) 

if __name__ == '__main__':
    main()
root.protocol('WM_DELETE_WINDOW', exiting)#When the GUI window is closed the exiting function is run.
tk.mainloop()#GUI is constantly checking if it has been clicked.
