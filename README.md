# Drunks
GEOG5990 Assessment 2

## Overview
This is an agent based model which simulates the routes drunk people will take after leaving a pub to get home.
There are tow methods to choose from simple and advanced.
Simple is a pure psuedo-random walking algorithm.
Advanced is a psuedo-random algorithm which stops drunks backtracking their steps.
Each agent is assigned one pub and one house. Multiple agents can start from one pub, but only one agent can finish at each house.
The program will show starting and ending locations and produce a heatmap of cells which the agents travel through the most.
The user has the ability to export the final map as an image and as a txt file.

## How to Use
The program is initiated from the command line.
The program has default options or the user can set there own in the command line.
To start type:
python drunks.py -h
-This brings up a help menu which shows the user what model parameters can be changed.
* -s: changes the seed. Default is 5.
* -m: sets the map export name. Default is mapExport.
* -d: sets the txt file export name. Default is dataExport.
* -f: decides which method to use, simple or advance. Default is advance.


![Commandline](https://github.com/b3nlewis/Drunks/blob/main/docs/commandline.png?raw=true)
	
Once the command line is entered a GUI will appear.
To run the model click each button until the process is completed.
To end the model, either click the cross on the GUI or click exit model.
The model must close before it can be run again.
![GUI](https://github.com/b3nlewis/Drunks/blob/main/docs/homepage.png?raw=true)

For more detailed documentation click [here](https://b3nlewis.github.io/Drunks/).

## Files included
drunks.py: This is the main script where the analysis and GUI code is located. 
drunkFramework: This is responsible for the drunk movement 
environment.txt: Contains location of pubs and houses.
timing.txt: Shows previous advance method timings.
docs: Where documentation html files are stored.
sphinx: Contains data used to build documentation.
