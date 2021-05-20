# -*- coding: utf-8 -*-
"""
This python script allows you to simulate drunk peoples movements from
leaving a pub to their house. There is an advanced and simple option to chose.
The advanced option stops drunk agents backtracking whereas the simple version
allows backtracking. The advanced version has significantly better performance.

"""

'''Import Statements'''
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #for GUI
import matplotlib.pyplot as plt
from matplotlib.figure import Figure #for GUI
import random
import csv # to read files
import drunkFramework #drunk class
import time #for testing
import pandas as pd #for dataframes
import argparse #used for commandline interface.
from tkinter import *
import tkinter as tk
from tkinter import ttk# for additional frames and progress bar

'''Step 1: Initialisation'''
print('Step 1: Initialisaing Model')

xAxis = 300
#print('X Axis:', xAxis)
yAxis = 300
#print('Y Axis:', yAxis)
environment = []
pubList = []
houseList = []
drunks = []
list_to_export = []
exportDataName = "" # used to name the exported data.
exportMapName = "" #used to name the exported map



'''Step 2: Define Functions'''
print('Step 2: Defining Functions')

def open_file(input_file, output_file, var_type):
    '''
    Opens a file and saves it as a list of lists. Can change what variable
    type parameters are saved as. e.g. string, int, float.
    
    Parameters:
    
        input_file : file
            A raw txt file.
        output_file : variable
            A list of list containing input file data.
        var_type : TYPE
            Assigns input data a variabale type.

    Returns:
    
        Returns the input file as a List of Lists.

    '''
    
    file = open(input_file, newline='') 
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:				# A list of rows
        rowlist = []                # An empty list
        for value in row:			# A list of value
            rowlist.append(var_type(value))   # Append values to rowlist
        output_file.append(rowlist) # Append rowlist to environment 
    file.close()
    
def write_file(input_file, output_file, mode):
    '''
    Writes a file out from a local file with a given file name.
    
    Parameters:
    
        input_file : variable
            A list of list containing data
        output_file : file
            A txt file containing that data from input file with rows equal to the length of a list.
        Mode : string
            String which decides if output rewrites('w') or appends ('a') data.
  
    Returns:
    
        A file with the output data written in it.

    '''
    file_finished = open(output_file, mode, newline='') 
    writer = csv.writer(file_finished, delimiter=',')
    for row in input_file:		
    	writer.writerow(row)		# List of values.
    file_finished.close()
    

def main():
    '''
    Performs first steps of the script when run. Assigns command line variables
    to args and locates all pubs and houses in environment. Additional code to
    create environment is also included but not used.
    
    Parameters:
    
        environment: file
            A txt file which contains locations of houses and pubs.

    Returns:
        
        pubList: List
            A list of pub locations with x and y coordinates.
        houseList: List
            A list of house locations with x and y coordinates

    '''
    
    '''Commandline interface'''

    parser = argparse.ArgumentParser(description=
    'Run a Random Walk Agent Based Model where drunk people are simulated moving from pubs to houses.')
    
    parser.add_argument('-s', '--seed', type=int, metavar = '', help='Assign a seed to the model')
    parser.add_argument('-m', '--exportMapName', type=str, metavar = '', help='Assign a name for the Map export')
    parser.add_argument('-d', '--exportDataName', type=str, metavar = '', help='Assign a name for the txt export file')
    parser.add_argument('-f', '--drunkFramework', type=str, metavar = '', help='Default is advanced, simple includes backtracking')
    args = parser.parse_args()
    
    #Assigning arg values to variables.
    
    global exportMapName
    global exportDataName
    global framework
    
    # Assigning random seed
    if args.seed == None:
        random.seed(5) #set to five to measure consitency
    else:
        random.seed(args.seed)
    print('Random Seed:', random.random())
    
    #Assigning name for export map
    if args.exportMapName == None:
        exportMapName = 'exportMap'
    else:
        exportMapName = args.exportMapName
    print("Map Name: ", exportMapName)
    
    #Assigning name for data export
    if args.exportDataName == None:
        exportDataName = 'exportData.txt'#makes sure file is saved as txt file
    else:
        exportDataName = args.exportDataName + '.txt'
    print("Data Name: ", exportDataName)
    
    #Assining method type
    if args.drunkFramework == 'simple':
        framework = 'simple'
    else:
        framework = 'advance'
    
    '''Step 3: Create Environment'''
    print('Step 3: Creating Base Environment')
    
    #creates a 300 by 300 grid for the pubs and houses to be located in
    #Not needed for model to run just to create data.
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
    
    '''Step 4: Get coordinates of all pubs and house in environment'''
    print('Step 4: Locating Pubs and Houses')
    
    '''Pubs'''
    
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
    
    # #testing
    # pubLength = len(pubList)
    # if pubLength != 9:
    #     print("Pub length Failed")
    # else:
    #     print("Pub length Pass")
    
    '''Houses'''
    
    y = 0 #starting value
    for row in (environment): #goes over each row of list at a time
        y += 1 #finds position on y axis.
        x = 0 #starting value
        for cell in row: #goes over each value in row
            x +=1 #finds position on x axis. 
            if cell != 1 and cell != 0:
                houseList.append([cell, x, y])
                
    print('House List')             
    print(houseList) # A list of lists containing pub x-coordinate and y-coordinate.
    
    #testing
    # houseLength = len(houseList)
    # if houseLength != 25:
    #     print("House length Failed")
    # else:
    #     print("House length Pass")
    
def displayData():
    '''
    A function which creates a scatter plot of houses and pubs which overlays
    an environment map of the area. Figure is added to GUI frame 2.

    Parameters:
    
        environment: List
            A list containing base, pub and house values.
        pubList: List
            A list of pub locations with x and y coordinates
        houseList: List
        A list of house locations with x and y coordinates
    
    
    Returns:
    
        Figure for GUI.
    

    '''
    
    '''Step 5: Show pubs houses and environment'''
    print('Step 5: Displaying Environment, Pubs and Houses')
    
    #creating figure
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    a.imshow(environment)
    #comment out for loops to see base environment without scatter points.
    for i in range(25): #Number of houses
         a.scatter(houseList[i][1], houseList[i][2], c='Red')
    for j in range(9): #Number of pubs
         a.scatter(pubList[j][1], pubList[j][2], c='Green', label='Pubs')
    a.set_title('Pub and House Location', fontsize=18)
      
    #adding figure to GUI
    canvas = FigureCanvasTkAgg(f, frame2)#adds to frame 2
    canvas.draw()
    canvas.get_tk_widget().pack(side= BOTTOM, fill= BOTH, expand=True)
    my_notebook.select(1)#automatically takes user to frame 2
    my_notebook.add(frame2, text="Environment")#adds frame 2 tab to GUI
    
    
def runModel():
    '''
    Assigns drunks to starting locations and finishing locations.
    Moves each drunk until it has reached its finishing location.
    Can either move with simple model or advance model.
    A dictionary is created which counts how often individual cells appear.
    The dictionary is converted into a list of lists so it can be exported.
    Step function is used to update progress bar.
    
    Parameters:
    
        pubList: List
            A list of pub locations with x and y coordinates
        houseList: List
            A list of house locations with x and y coordinates
        step: Function
            Updates the progress bar everytime it is called
        stop: Function
            Stops and clears progress bar
        Framework: Variable
            Contains text to decide which method is being used.
        

    Returns:
        
        list_to_export: List
            A list of lists of occurences for each cell
        timing.txt: List
            A txt file which contains run times for the function
        heatmap: figure
            A figure which shows cell occurences and is added to figure 3

    '''
    runTimeStart = time.process_time()
    '''Step 6: Assigning drunks to start and end locations'''
    print('Step 6: Assigning Start and End Locations')    

    '''Assigning drunks to a pub (starting location) and a house (ending location).'''
    
    global houseList
    global pubList
    global step
    global stop
    global framework
    
    
    step()#Moves progress bar forward.
    
    random.shuffle(pubList)#randomises where drunks start
    random.shuffle(houseList)#randomises where drunks finish
    for i in range(25): #number of drunks
        n = random.randint(0,8)
        pubX, pubY = pubList[n][0], pubList[n][1]
        houseX, houseY = houseList[i][1], houseList[i][2]
        drunks.append(drunkFramework.drunk(pubX, pubY, houseX, houseY))
        
    step()#Moves progress bar forward.
        
    #Testing                  
    #print(drunks)
    for i in(drunks):
        print("Drunk ", i)
        i.starting_location()
        i.ending_location()    
        
    #Memory usage    
    del pubList    
    del houseList
    del n
    #print("Deleted House and Pub list from Memory")
        
    
    '''Step 7: Moving Drunks decides which method to use'''
    print('Step 7: Moving Drunks')
    if framework != 'simple':
        print('Advance Model')
        drunk_num = 0
        for i in (drunks):
            start = time.process_time()
            drunk_num += 1
            while i.is_home() == False:
                i.moveAdvance()
            else:
                end = time.process_time()
                #print("Drunk", drunk_num,"finished in", i.distance, "steps and", end - start, "seconds.")
                #print(i.is_home())
                step() #Moves progress bar forward everytime loop is completed.
    else:
        print('Simple Model')
        #drunk_num = 0
        for i in (drunks):
            #start = time.process_time()
            #drunk_num += 1
            while i.is_home() == False:
                i.move()
            else:
                #end = time.process_time()
                #print("Drunk", drunk_num,"finished in", i.distance, "steps and", end - start, "seconds.")
                #print(i.is_home())
                step() #Moves progress bar forward everytime loop is completed.
    
        
    
    '''Step 8: Storing and sorting drunk movements'''
    print('Step 8: Storing and Sorting Drunk Results')
    
    '''Creating table to store cell counts'''
    #print('Starting Table')
    data = []
    for x in range(0,300):
        for y in range(0, 300):
            data.append([x, y])
    data = pd.DataFrame(data)
    data.columns = ['x', 'y']
    #print(data)
    #print('Finished Tables')
    
    step()#Moves progress bar forward

    
    '''Creating a dictionary which counts the number of occurences of
    a cell for all drunks'''
    # modified from Datacamp. https://campus.datacamp.com/courses/python-data-science-toolbox-part-2/using-iterators-in-pythonland?ex=12
    count = {}#dictionary to store cell occurances
    for i in drunks:
        df_route = i.get_route()
        #print(df_route)
        column = df_route[0]
        for value in column:
            if value in count.keys():#sees if value if already in dictionary 
                count[value] += 1#if it is adds one to count
            else:
                count[value] = 1#if not adds value to dictionary
                
    #Testing        
    # countTest = len(count)
    # if countTest > yAxis * xAxis:
    #     print("Count Test Failed")
    # else:
    #     print("Count Test Pass")
    
    step()#Moves progress bar forward
    #print(count)
   
    
    
    '''converts dictionary into a dataframe'''    
    cell_count = pd.DataFrame(list(count.items()), columns = ['Coords', 'Amount'])#creates new dataframe to hold results
    cell_count['x'], cell_count['y'] = zip(*cell_count.Coords)#divides one column into two.
    cell_count.pop('Coords') #removes coords column
    
    #print(cell_count)
    
    '''merges dataframe of all cells with cell occurences'''            
    merge_data = pd.merge(data, cell_count)# merges two dfs together so that every cell has a value.
    
    # #Testing        
    # countTest = len(merge_data)
    # if countTest != 90000: #if there are not 90,000 cells something has failed
    #     print("Count Test Failed")
    # else:
    #     print("Count Test Pass")
    
    step()#Moves progress bar forward
    
    #memory usage
    del data
    del cell_count
    
    '''Sort df into rows'''
    sorted_data = merge_data.sort_values(['y', 'x'], ascending=[True, True])
    #print(sorted_data.columns)
    #print(sorted_data)
    
    step()#Moves progress bar forward
    
    '''converts into a list'''
    list_of_amount = sorted_data['Amount'].values.tolist()#converts df into list.
    #print(list_of_amount)
    
    step()#Moves progress bar forward
    
    '''converts into list of list'''
    global list_to_export
    # writes list into a list of lists which can be used to create heatmap.
    i = 0
    list_to_export = []
    while i <len(list_of_amount):
        list_to_export.append(list_of_amount[i : i + 300])#so it knows when to start a new line
        i += 300 #300 values per row.
     
    #print(list_to_export)
    step()#Moves progress bar forward
        
    #memory usage
    del list_of_amount
    
    #timing
    runTimeEnd = time.process_time()
    tTime = runTimeEnd-runTimeStart
    print("Model Run Time:", tTime )
    
    #export Timing for comparison
    file = open('timing.txt', 'a')#appends data to txt file
    file.write(str(tTime) +'\n')
    file.close
    
    '''Step 9: Creating a Map'''
    print('Step 9: Creating a Map of Cell Densities')
    
    step()#Moves progress bar forward
    
    #Create graph
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    a.imshow(list_to_export, cmap='inferno')
    a.set_title("Random Walk Density Map", fontsize=18)
        
    #Add graph to canvas
    canvas = FigureCanvasTkAgg(f, frame3)
    canvas.draw()
    canvas.get_tk_widget().pack(side= BOTTOM, fill= BOTH, expand=True)#fills entire page with graph
    my_notebook.select(2)#opens third tab on GUI
    my_notebook.add(frame3, text="Drunk Hotspot") #adds figure to thrid frame.
    
    stop()#Ends and resets progress bar

def exportMap():
    '''
    Exports the heatmap with the given name, run from GUI
    
    Parameters:
    
        exportMapName: variable
            name assigned during main.

    Returns:
    
        Image file of heatmap.

    '''
    global exportMapName
    plt.imshow(list_to_export, cmap='inferno')
    plt.savefig(exportMapName)
    plt.close()#so that blank plt figure does not appear.
    print('Map Exported as', exportMapName)
    

def exportData():
    
    '''
    Exports a list into a txt file, run from GUI
    
    Parameters:
    
        exportDataName: variable
            name assigned during main

    Returns:
    
        txt file of list_to_export

    '''
    global exportDataName
    write_file(list_to_export, exportDataName, 'w')

    print('Data Exported as', exportDataName)
    
def step():
    '''
    Every time step is called the progress bar moves 3%
    
    Parameters:
        
        progress_bar['value']: variable
            position of the progress bar
            
    Returns:
       Updated progress_bar value    
    
    '''
    
    
    progress_bar['value'] += 3
    root.update_idletasks()#Updates the GUI to show pregression.
    
def stop():
    '''
    Stops the progress bar
    
    Parameters:
        
        progress_bar: variable
            position of the progress bar
            
    Returns:
       A stopping function for the progress bar.   
    
    '''
    progress_bar.stop()

    
def exitModel():
    '''
    Deletes all remaining variables
    
    Parameters:
        
        list_to_export: list
            list of cell occurences.
        environment: list
            values of cells displays pubs and houses
        drunks: list
            list of drunks
        xAxis: int
            size of x axis
        yAxis: int
            size of y axis
        exportMapName: string
            name of export
        exportDataName: string
            name of export
            
    Returns:
       None   
    
    '''
    global list_to_export
    global environment
    global drunks
    global xAxis
    global yAxis
    global exportMapName
    global exportDataName
    
    #memory usage
    del list_to_export
    del environment
    del drunks
    del xAxis
    del yAxis
    del exportMapName
    del exportDataName
    
    #delete GUI.
    root.quit()
    root.destroy()
    
    print('Model Closed')
    
    
'''Creating GUI'''
'''GUI code was edited from https://www.youtube.com/watch?v=kqbkUKIc1Gk
and https://www.youtube.com/watch?v=Grbx15jRjQA'''
 
#GUI page
root = tk.Tk()
root.title('Drunk Agents')
root.geometry('500x500')

#Sets up multiple tabs for GUI page
my_notebook = ttk.Notebook(root)
my_notebook.pack()

#The tabs used for GUI page
frame1 = Frame(my_notebook, width=500, height=500, bg='grey')
frame2 = Frame(my_notebook, width=500, height=500)
frame3 = Frame(my_notebook, width=500, height=500)

#Displays each tab on GUI
frame1.pack(fill='both', expand=1)
frame2.pack(fill='both', expand=1)
frame3.pack(fill='both', expand=1)

#Adds a tab link to top of GUI to each page
my_notebook.add(frame1, text="Home Page")
my_notebook.add(frame2, text="Environment")
my_notebook.add(frame3, text="Drunk Hotspot")

#Hides the extra frames until they are needed
my_notebook.hide(1)
my_notebook.hide(2)

#Progress bar for runModel function
progress_bar = ttk.Progressbar(frame1, orient=HORIZONTAL, length=220, mode='determinate')

#Buttons and progress bar for home page on GUI
button1 = Button(frame1, text='Display Pubs and Houses', height=3, width=30, command=displayData).pack(pady=15)
button2 = Button(frame1, text='Run Model', height=3, width=30, command=runModel).pack(pady=15)
progress_bar.pack()#puts progress bar under run model button so that users know it is working
button3 = Button(frame1, text='Export Data', height=3, width=30, command=exportData).pack(pady=15)
button4 = Button(frame1, text='Export Graph', heigh=3, width=30, command=exportMap).pack(pady=15)
button5 = Button(frame1, text='Exit Model', height=3, width=30, command=exitModel).pack(pady=15)

#runs program until first function
if __name__ == '__main__':
    main()
    
root.protocol('WM_DELETE_WINDOW', exitModel)#When the GUI window is closed the exiting function is run.
tk.mainloop()#GUI is constantly checking if it has been clicked.