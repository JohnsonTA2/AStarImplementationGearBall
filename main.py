import tkinter as tk
from tkinter import *
import GearBallClass
import AStarImplementation as Astar
import matplotlib.pyplot as plt
our_gear_ball = GearBallClass.GearBall()


#Assign Face for Perspective: Orange is Front (Face 0)
face = 0

#Randomize our Gear Ball
num_turns = input("How many turns would you like: ")
our_gear_ball.randomize_ball(face, int(num_turns))
our_gear_ball.print_gear_ball()
#Run the AStar Algorithm, which outputs the turns you need to take
our_solution, expanded_nodes = Astar.AStar(our_gear_ball)
#Uses the moves from earlier on our gearball
our_gear_ball.solve_ball(our_solution)
#Prints solved gearball
our_gear_ball.print_gear_ball()



#Plotting Gear Ball
# dictionary to store values to plot
Iterations = {}

# Assign Face for Perspective: Orange is Front (Face 0)
face = 0

i = 3
 #iterate 3-k times
while i < 21:
    Iterations[i] = []
    for q in range(5):
        #var to store node count
        our_gear_ball = GearBallClass.GearBall()
        our_gear_ball.randomize_ball(face, i)
        our_solution, node_count = Astar.AStar(our_gear_ball)
        our_gear_ball.solve_ball(our_solution)
        #our_gear_ball.print_gear_ball()
        Iterations[i].append(node_count)
    i += 1

#print(Iterations)

Averages = {}
for key in Iterations:
    average = 0
    temp_list = Iterations[key]
    for val in temp_list:
        average += val
    average = average / 5
    Averages[key] = average


# create  figue and axis object
fig, ax, = plt.subplots(1, 2)
key_values = Iterations.keys()
new_key_vals = []
for val in key_values:
    for i in range(5):
        new_key_vals.append(val)

fig.tight_layout(rect=(0,0,1.5,1.5))
fig.subplots_adjust(wspace=.35)

ax[0].bar(Averages.keys(), Averages.values())
ax[1].scatter(new_key_vals, Iterations.values())
# sex axis labels for both graphs
ax[0].set_ylabel('Average Number of Nodes Expanded')
ax[1].set_ylabel('Nodes Expanded')
ax[0].set_xlabel('K Value')
ax[1].set_xlabel('K Value')

ax[0].set_title('Analysis of A*')
ax[1].set_title('Analysis of A*')

plt.show()
