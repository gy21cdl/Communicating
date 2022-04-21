# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:08:33 2022

@author: clambert

model7 relateds to the "Communication" practical and should be used with 
the agentframework7 and the csvreader7 files.

in.txt is the input data for the csvreader7 file and should be stored in the same directory

Directions:
1. Save model7, agentframework7, in.txt and csvreader7 in the same directory location
2. Run model7

Expected outputs:
1. Scatter chart of agents, coloured individually and displayed on environment
background in a seperate window. The moved and eaten "paths" will be displayed
2. print shared neighberhood values between agents (sharing)
3. "Finished" printed on closing the seperate window.
"""

#Imported modules
import random
import operator
import matplotlib.pyplot
import agentframework7
import csvreader7

# Set the seed for reducability
#random.seed(0) #testing reducability of model - when set, output should be the same each time
#random.seed(1)

#bring enviroment data in from csvreader7
environment = csvreader7.get_data()

#List of Agents created
agents = []


a = agentframework7.Agent(environment, agents)
#a. __init__()
a. move ()
#print(a.y, a.x) #test agentframework


'''
#distance_between method - calcualtion used for distance at bottom of code
def distance_between(a, b):
    """
    Calculates and returns the 2D coordinate distance between a and b.

    Parameters
    ----------
    a : Agent
        Located in 2D space with an x and y cordinate values.
    b : Agent
        Located in 2D space with an x and y cordinate values.

    Returns
    -------
    Number
        The 2D coordinate distance bertween a and b.
    """
    return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5
'''


num_of_agents = 10 #changable value
num_of_iterations = 100 #changable value
neighbourhood = 25 #changable value

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework7.Agent(environment, agents))
        

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move() #moving the agents
        agents[i].eat() #eating into the environment
        agents[i].share_with_neighbours(neighbourhood) #sharing locations between agents

#returns graphical results
matplotlib.pyplot.xlim(0, 99) #x axis
matplotlib.pyplot.ylim(0, 99) #y axis
matplotlib.pyplot.imshow(environment) #plots enviroment data from csvreader7
for i in range(num_of_agents): #created and moved agents based on number of agents
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y) #plot scatter of agents
matplotlib.pyplot.show() #show window


'''     
# defining min and max dstance variables
maxd = distance_between(agents[0], agents[1])
mind = distance_between(agents[0], agents[1])


# Calculating the distance
for i in range(num_of_agents):
    for j in range(i + 1, num_of_agents, 1):
            #print(i, j)
            distance = distance_between(agents[i], agents[j])
            #print(distance)
            maxd = max(maxd, distance)
            mind = min(mind, distance)
print("maxd", maxd)
print("mind", mind)
'''

# done marker
print ("finished")
