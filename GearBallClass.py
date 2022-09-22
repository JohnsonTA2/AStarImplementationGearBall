import numpy as np
import random
class GearBallSide:
    def __init__(self, color):

        #initialize values of pieces (aka color)
        self.left_edge = "LE: " + color
        self.left_edge_value = 0
        self.right_edge = "RE: " + color
        self.right_edge_value = 0
        self.top_edge = "TE: " + color
        self.top_edge_value = 0
        self.bottom_edge = "BE: " + color
        self.bottom_edge_value = 0
        self.center = color
        self.top_left_corner = "TLC: " + color
        self.top_right_corner = "TRC: " + color
        self.bottom_left_corner = "BLC: " + color
        self.bottom_right_corner = "BRC: " + color
        self.left_middle = "LM: " + color
        self.right_middle = "RM: " + color
        self.top_middle = "TM: " + color
        self.bottom_middle = "BM: " + color
        #initialize side neighbors
    def assign_neighbors(self, left_n, right_n,top_n, bottom_n):

        self.left_neighbor = left_n
        self.right_neighbor = right_n
        self.top_neighbor = top_n
        self.bottom_neighbor = bottom_n

    def print_face(self):


        #if self.right_edge_value == 3:
        print("====================", self.center, " face =======================================")
        print("       ", self.top_left_corner, "   ", self.top_edge_value, "/6", self.top_edge, "   ", self.top_right_corner)
        print("                    ", self.top_middle)
        print(self.left_edge_value, "/6", self.left_edge, "   ", self.left_middle, "   ", self.center, "   ", self.right_middle, "   ",self.right_edge_value, "/6", self.right_edge )
        print("                    ", self.bottom_middle)
        print("       ", self.bottom_left_corner, "   ",self.bottom_edge_value, "/6", self.bottom_edge, "   ", self.bottom_right_corner)
        print("=======================================================================")

    def find_neighbor(self, color):

        if self.center == color:
            return 0
        if self.left_neighbor.center == color:
            return 1
        if self.right_neighbor.center == color:
            return 1
        if self.top_neighbor.center == color:
            return 1
        if self.bottom_neighbor.center == color:
            return 1
        else:
            return 2


    def find_distance(self, piece):

        distance = 0
        #first check how far piece is from correct face
        if 'orange' in piece:
            distance += self.find_neighbor('orange')
        if 'purple' in piece:
            distance += self.find_neighbor('purple')
        if 'yellow' in piece:
            distance += self.find_neighbor('yellow')
        if 'red' in piece:
            distance += self.find_neighbor('red')
        if 'green' in piece:
            distance += self.find_neighbor('green')
        if 'blue' in piece:
            distance += self.find_neighbor('blue')

        return distance

class GearBall:

    def __init__(self):
        #generate sides
        side_one = GearBallSide('orange')
        side_two = GearBallSide('purple')
        side_three = GearBallSide('yellow')
        side_four = GearBallSide('red')
        side_five = GearBallSide('green')
        side_six = GearBallSide('blue')

        #connect sides
        side_one.assign_neighbors(side_four, side_two, side_five, side_six)
        side_two.assign_neighbors(side_one, side_three, side_five, side_six)
        side_three.assign_neighbors(side_two, side_four, side_six, side_five)
        side_four.assign_neighbors(side_three, side_one, side_five, side_six)
        side_five.assign_neighbors(side_four, side_two, side_three, side_one)
        side_six.assign_neighbors(side_four, side_two, side_one, side_three)

        #assign base color
        #side_one.center = 'orange'
        #side_two.center = 'purple'
        #side_three.center = 'yellow'
        #side_four.center = 'red'
        #side_five.center = 'green'
        #side_six.center = 'blue'

        #stack of sides
        self.gear_ball_sides = []
        self.gear_ball_sides.append(side_one)
        self.gear_ball_sides.append(side_two)
        self.gear_ball_sides.append(side_three)
        self.gear_ball_sides.append(side_four)
        self.gear_ball_sides.append(side_five)
        self.gear_ball_sides.append(side_six)

    def print_gear_ball(self):
        for i in range(len(self.gear_ball_sides)):
            self.gear_ball_sides[i].print_face()

        print("")
        print("")
        print("")
        print("")
        print("")
    #here we will define movements

    def center_third_still_left_up(self, face):

        #move edge pieces
        self.gear_ball_sides[face].top_edge_value = (self.gear_ball_sides[face].top_edge_value + 1) % 6
        self.gear_ball_sides[face].bottom_edge_value = (self.gear_ball_sides[face].bottom_edge_value + 1) % 6

        self.gear_ball_sides[face].top_neighbor.top_edge_value = (self.gear_ball_sides[face].top_neighbor.top_edge_value + 1) % 6
        self.gear_ball_sides[face].top_neighbor.bottom_edge_value = (self.gear_ball_sides[face].top_neighbor.bottom_edge_value + 1) % 6

        self.gear_ball_sides[face].top_neighbor.top_neighbor.top_edge_value = (self.gear_ball_sides[face].top_neighbor.top_neighbor.top_edge_value + 1) % 6
        self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_edge_value = (self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_edge_value + 1) % 6

        self.gear_ball_sides[face].bottom_neighbor.top_edge_value = (self.gear_ball_sides[face].bottom_neighbor.top_edge_value + 1) % 6
        self.gear_ball_sides[face].bottom_neighbor.bottom_edge_value = (self.gear_ball_sides[face].bottom_neighbor.bottom_edge_value + 1) % 6

        #left side comes up
        self.gear_ball_sides[face].top_left_corner , self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.top_left_corner = self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.top_left_corner, self.gear_ball_sides[face].top_left_corner , self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_left_corner
        self.gear_ball_sides[face].left_edge , self.gear_ball_sides[face].top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.left_edge = self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.left_edge, self.gear_ball_sides[face].left_edge , self.gear_ball_sides[face].top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge
        self.gear_ball_sides[face].left_middle , self.gear_ball_sides[face].top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.left_middle = self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.left_middle, self.gear_ball_sides[face].left_middle , self.gear_ball_sides[face].top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_middle
        self.gear_ball_sides[face].bottom_left_corner , self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.bottom_left_corner = self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_left_corner , self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_left_corner



        #right side comes down
        self.gear_ball_sides[face].top_right_corner, self.gear_ball_sides[face].top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.top_right_corner = self.gear_ball_sides[face].top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.top_right_corner, self.gear_ball_sides[face].top_right_corner
        self.gear_ball_sides[face].right_edge, self.gear_ball_sides[face].top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.right_edge = self.gear_ball_sides[face].top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.right_edge, self.gear_ball_sides[face].right_edge
        self.gear_ball_sides[face].right_middle, self.gear_ball_sides[face].top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.right_middle = self.gear_ball_sides[face].top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.right_middle, self.gear_ball_sides[face].right_middle
        self.gear_ball_sides[face].bottom_right_corner, self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.bottom_right_corner = self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_right_corner


        #rotate left face clockwise

        #swap side face corners
        self.gear_ball_sides[face].left_neighbor.top_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_right_corner, self.gear_ball_sides[face].left_neighbor.top_right_corner = self.gear_ball_sides[face].left_neighbor.top_right_corner, self.gear_ball_sides[face].left_neighbor.top_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_right_corner

        #swap side edges
        self.gear_ball_sides[face].left_neighbor.top_edge, self.gear_ball_sides[face].left_neighbor.left_edge, self.gear_ball_sides[face].left_neighbor.bottom_edge, self.gear_ball_sides[face].left_neighbor.right_edge = self.gear_ball_sides[face].left_neighbor.right_edge, self.gear_ball_sides[face].left_neighbor.top_edge, self.gear_ball_sides[face].left_neighbor.left_edge, self.gear_ball_sides[face].left_neighbor.bottom_edge

        #swap middle pieces
        self.gear_ball_sides[face].left_neighbor.top_middle, self.gear_ball_sides[face].left_neighbor.left_middle, self.gear_ball_sides[face].left_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.right_middle = self.gear_ball_sides[face].left_neighbor.right_middle, self.gear_ball_sides[face].left_neighbor.top_middle, self.gear_ball_sides[face].left_neighbor.left_middle, self.gear_ball_sides[face].left_neighbor.bottom_middle

        #rotate right face clockwise

        #swap side face corners
        self.gear_ball_sides[face].right_neighbor.top_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_right_corner, self.gear_ball_sides[face].right_neighbor.top_right_corner = self.gear_ball_sides[face].right_neighbor.top_right_corner, self.gear_ball_sides[face].right_neighbor.top_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_right_corner

        #swap side edges
        self.gear_ball_sides[face].right_neighbor.top_edge, self.gear_ball_sides[face].right_neighbor.left_edge, self.gear_ball_sides[face].right_neighbor.bottom_edge, self.gear_ball_sides[face].right_neighbor.right_edge = self.gear_ball_sides[face].right_neighbor.right_edge, self.gear_ball_sides[face].right_neighbor.top_edge, self.gear_ball_sides[face].right_neighbor.left_edge, self.gear_ball_sides[face].right_neighbor.bottom_edge

        #swap middle pieces
        self.gear_ball_sides[face].right_neighbor.top_middle, self.gear_ball_sides[face].right_neighbor.left_middle, self.gear_ball_sides[face].right_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_middle = self.gear_ball_sides[face].right_neighbor.right_middle, self.gear_ball_sides[face].right_neighbor.top_middle, self.gear_ball_sides[face].right_neighbor.left_middle, self.gear_ball_sides[face].right_neighbor.bottom_middle

    def center_third_still_right_up(self, face):
        # move edge pieces
        self.gear_ball_sides[face].top_edge_value = (self.gear_ball_sides[face].top_edge_value - 1) % 6
        self.gear_ball_sides[face].bottom_edge_value = (self.gear_ball_sides[face].bottom_edge_value - 1) % 6

        self.gear_ball_sides[face].top_neighbor.top_edge_value = (self.gear_ball_sides[face].top_neighbor.top_edge_value - 1) % 6
        self.gear_ball_sides[face].top_neighbor.bottom_edge_value = (self.gear_ball_sides[face].top_neighbor.bottom_edge_value - 1) % 6

        self.gear_ball_sides[face].top_neighbor.top_neighbor.top_edge_value = (self.gear_ball_sides[face].top_neighbor.top_neighbor.top_edge_value - 1) % 6
        self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_edge_value = (self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_edge_value - 1) % 6

        self.gear_ball_sides[face].bottom_neighbor.top_edge_value = (self.gear_ball_sides[face].bottom_neighbor.top_edge_value - 1) % 6
        self.gear_ball_sides[face].bottom_neighbor.bottom_edge_value = (self.gear_ball_sides[face].bottom_neighbor.bottom_edge_value - 1) % 6

        #right side comes up
        self.gear_ball_sides[face].top_right_corner , self.gear_ball_sides[face].top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.top_right_corner = self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.top_right_corner, self.gear_ball_sides[face].top_right_corner , self.gear_ball_sides[face].top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_right_corner
        self.gear_ball_sides[face].right_edge , self.gear_ball_sides[face].top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.right_edge = self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.right_edge, self.gear_ball_sides[face].right_edge , self.gear_ball_sides[face].top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge
        self.gear_ball_sides[face].right_middle , self.gear_ball_sides[face].top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.right_middle = self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.right_middle, self.gear_ball_sides[face].right_middle , self.gear_ball_sides[face].top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_middle
        self.gear_ball_sides[face].bottom_right_corner , self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.bottom_right_corner = self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_right_corner , self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_right_corner
        #left side comes down
        self.gear_ball_sides[face].top_left_corner, self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.top_left_corner = self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.top_left_corner, self.gear_ball_sides[face].top_left_corner
        self.gear_ball_sides[face].left_edge, self.gear_ball_sides[face].top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.left_edge = self.gear_ball_sides[face].top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.left_edge, self.gear_ball_sides[face].left_edge
        self.gear_ball_sides[face].left_middle, self.gear_ball_sides[face].top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.left_middle = self.gear_ball_sides[face].top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.left_middle, self.gear_ball_sides[face].left_middle
        self.gear_ball_sides[face].bottom_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.bottom_left_corner = self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_left_corner

        #rotate left face clockwise

        self.gear_ball_sides[face].left_neighbor.top_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_right_corner, self.gear_ball_sides[face].left_neighbor.top_right_corner = self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_right_corner, self.gear_ball_sides[face].left_neighbor.top_right_corner, self.gear_ball_sides[face].left_neighbor.top_left_corner

        self.gear_ball_sides[face].left_neighbor.top_middle, self.gear_ball_sides[face].left_neighbor.left_middle, self.gear_ball_sides[face].left_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.right_middle = self.gear_ball_sides[face].left_neighbor.left_middle, self.gear_ball_sides[face].left_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.right_middle, self.gear_ball_sides[face].left_neighbor.top_middle

        self.gear_ball_sides[face].left_neighbor.top_edge, self.gear_ball_sides[face].left_neighbor.left_edge, self.gear_ball_sides[face].left_neighbor.bottom_edge, self.gear_ball_sides[face].left_neighbor.right_edge = self.gear_ball_sides[face].left_neighbor.left_edge, self.gear_ball_sides[face].left_neighbor.bottom_edge, self.gear_ball_sides[face].left_neighbor.right_edge, self.gear_ball_sides[face].left_neighbor.top_edge

        #rotate right face clockwise
        self.gear_ball_sides[face].right_neighbor.top_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_right_corner, self.gear_ball_sides[face].right_neighbor.top_right_corner = self.gear_ball_sides[face].right_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_right_corner, self.gear_ball_sides[face].right_neighbor.top_right_corner, self.gear_ball_sides[face].right_neighbor.top_left_corner

        self.gear_ball_sides[face].right_neighbor.top_middle, self.gear_ball_sides[face].right_neighbor.left_middle, self.gear_ball_sides[face].right_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_middle = self.gear_ball_sides[face].right_neighbor.left_middle, self.gear_ball_sides[face].right_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_middle, self.gear_ball_sides[face].right_neighbor.top_middle

        self.gear_ball_sides[face].right_neighbor.top_edge, self.gear_ball_sides[face].right_neighbor.left_edge, self.gear_ball_sides[face].right_neighbor.bottom_edge, self.gear_ball_sides[face].right_neighbor.right_edge = self.gear_ball_sides[face].right_neighbor.left_edge, self.gear_ball_sides[face].right_neighbor.bottom_edge, self.gear_ball_sides[face].right_neighbor.right_edge, self.gear_ball_sides[face].right_neighbor.top_edge

    def center_third_still_top_left(self, face):
        # move edge pieces
        self.gear_ball_sides[face].left_edge_value = (self.gear_ball_sides[face].left_edge_value + 1) % 6
        self.gear_ball_sides[face].right_edge_value = (self.gear_ball_sides[face].right_edge_value + 1) % 6

        self.gear_ball_sides[face].left_neighbor.left_edge_value = (self.gear_ball_sides[face].left_neighbor.left_edge_value + 1) % 6
        self.gear_ball_sides[face].left_neighbor.right_edge_value = (self.gear_ball_sides[face].left_neighbor.right_edge_value + 1) % 6

        self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge_value = (self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge_value + 1) % 6
        self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge_value = (self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge_value + 1) % 6

        self.gear_ball_sides[face].right_neighbor.left_edge_value = (self.gear_ball_sides[face].right_neighbor.left_edge_value + 1) % 6
        self.gear_ball_sides[face].right_neighbor.right_edge_value = (self.gear_ball_sides[face].right_neighbor.right_edge_value + 1) % 6

        #rotate top third left
        self.gear_ball_sides[face].top_left_corner , self.gear_ball_sides[face].left_neighbor.top_left_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.top_left_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.top_left_corner = self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.top_left_corner, self.gear_ball_sides[face].top_left_corner , self.gear_ball_sides[face].left_neighbor.top_left_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.top_left_corner
        self.gear_ball_sides[face].top_edge , self.gear_ball_sides[face].left_neighbor.top_edge, self.gear_ball_sides[face].left_neighbor.left_neighbor.top_edge, self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.top_edge = self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.top_edge, self.gear_ball_sides[face].top_edge , self.gear_ball_sides[face].left_neighbor.top_edge, self.gear_ball_sides[face].left_neighbor.left_neighbor.top_edge
        self.gear_ball_sides[face].top_right_corner , self.gear_ball_sides[face].left_neighbor.top_right_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.top_right_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.top_right_corner = self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.top_right_corner, self.gear_ball_sides[face].top_right_corner , self.gear_ball_sides[face].left_neighbor.top_right_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.top_right_corner
        self.gear_ball_sides[face].top_middle , self.gear_ball_sides[face].left_neighbor.top_middle, self.gear_ball_sides[face].left_neighbor.left_neighbor.top_middle, self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.top_middle = self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.top_middle, self.gear_ball_sides[face].top_middle , self.gear_ball_sides[face].left_neighbor.top_middle, self.gear_ball_sides[face].left_neighbor.left_neighbor.top_middle

        #rotate bottom third right
        self.gear_ball_sides[face].bottom_left_corner , self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.bottom_left_corner = self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.bottom_left_corner , self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_left_corner
        self.gear_ball_sides[face].bottom_edge , self.gear_ball_sides[face].left_neighbor.bottom_edge, self.gear_ball_sides[face].left_neighbor.left_neighbor.bottom_edge, self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.bottom_edge = self.gear_ball_sides[face].left_neighbor.bottom_edge, self.gear_ball_sides[face].left_neighbor.left_neighbor.bottom_edge , self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.bottom_edge, self.gear_ball_sides[face].bottom_edge
        self.gear_ball_sides[face].bottom_right_corner , self.gear_ball_sides[face].left_neighbor.bottom_right_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.bottom_right_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.bottom_right_corner = self.gear_ball_sides[face].left_neighbor.bottom_right_corner, self.gear_ball_sides[face].left_neighbor.left_neighbor.bottom_right_corner , self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_right_corner
        self.gear_ball_sides[face].bottom_middle , self.gear_ball_sides[face].left_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.left_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.bottom_middle = self.gear_ball_sides[face].left_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.left_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.left_neighbor.left_neighbor.bottom_middle, self.gear_ball_sides[face].bottom_middle

        #rotate top face clockwise

        self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_right_corner = self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_left_corner

        #swap side edges
        self.gear_ball_sides[face].top_neighbor.top_edge, self.gear_ball_sides[face].top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.bottom_edge, self.gear_ball_sides[face].top_neighbor.right_edge = self.gear_ball_sides[face].top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.bottom_edge, self.gear_ball_sides[face].top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_edge

        #swap middle pieces
        self.gear_ball_sides[face].top_neighbor.top_middle, self.gear_ball_sides[face].top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.bottom_middle, self.gear_ball_sides[face].top_neighbor.right_middle = self.gear_ball_sides[face].top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.bottom_middle, self.gear_ball_sides[face].top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_middle

        #rotate bottom face clockwise

        self.gear_ball_sides[face].bottom_neighbor.top_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_right_corner = self.gear_ball_sides[face].bottom_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_left_corner

        #swap side edges
        self.gear_ball_sides[face].bottom_neighbor.top_edge, self.gear_ball_sides[face].bottom_neighbor.left_edge, self.gear_ball_sides[face].bottom_neighbor.bottom_edge, self.gear_ball_sides[face].bottom_neighbor.right_edge = self.gear_ball_sides[face].bottom_neighbor.left_edge, self.gear_ball_sides[face].bottom_neighbor.bottom_edge, self.gear_ball_sides[face].bottom_neighbor.right_edge, self.gear_ball_sides[face].bottom_neighbor.top_edge

        #swap middle pieces

        self.gear_ball_sides[face].bottom_neighbor.top_middle, self.gear_ball_sides[face].bottom_neighbor.left_middle, self.gear_ball_sides[face].bottom_neighbor.bottom_middle, self.gear_ball_sides[face].bottom_neighbor.right_middle = self.gear_ball_sides[face].bottom_neighbor.left_middle, self.gear_ball_sides[face].bottom_neighbor.bottom_middle, self.gear_ball_sides[face].bottom_neighbor.right_middle, self.gear_ball_sides[face].bottom_neighbor.top_middle

    def center_third_still_top_right(self, face):
        # move edge pieces
        self.gear_ball_sides[face].left_edge_value = (self.gear_ball_sides[face].left_edge_value - 1) % 6
        self.gear_ball_sides[face].right_edge_value = (self.gear_ball_sides[face].right_edge_value - 1) % 6

        self.gear_ball_sides[face].left_neighbor.left_edge_value = (self.gear_ball_sides[face].left_neighbor.left_edge_value - 1) % 6
        self.gear_ball_sides[face].left_neighbor.right_edge_value = (self.gear_ball_sides[face].left_neighbor.right_edge_value - 1) % 6

        self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge_value = (self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge_value - 1) % 6
        self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge_value = (self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge_value - 1) % 6

        self.gear_ball_sides[face].right_neighbor.left_edge_value = (self.gear_ball_sides[face].right_neighbor.left_edge_value - 1) % 6
        self.gear_ball_sides[face].right_neighbor.right_edge_value = (self.gear_ball_sides[face].right_neighbor.right_edge_value - 1) % 6


        self.gear_ball_sides[face].top_left_corner, self.gear_ball_sides[face].right_neighbor.top_left_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.top_left_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.top_left_corner = self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.top_left_corner,self.gear_ball_sides[face].top_left_corner, self.gear_ball_sides[face].right_neighbor.top_left_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.top_left_corner
        self.gear_ball_sides[face].top_edge, self.gear_ball_sides[face].right_neighbor.top_edge,self.gear_ball_sides[face].right_neighbor.right_neighbor.top_edge, self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.top_edge = self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.top_edge, self.gear_ball_sides[face].top_edge,self.gear_ball_sides[face].right_neighbor.top_edge, self.gear_ball_sides[face].right_neighbor.right_neighbor.top_edge
        self.gear_ball_sides[face].top_right_corner , self.gear_ball_sides[face].right_neighbor.top_right_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.top_right_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.top_right_corner = self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.top_right_corner, self.gear_ball_sides[face].top_right_corner , self.gear_ball_sides[face].right_neighbor.top_right_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.top_right_corner
        self.gear_ball_sides[face].top_middle , self.gear_ball_sides[face].right_neighbor.top_middle, self.gear_ball_sides[face].right_neighbor.right_neighbor.top_middle, self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.top_middle = self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.top_middle, self.gear_ball_sides[face].top_middle , self.gear_ball_sides[face].right_neighbor.top_middle, self.gear_ball_sides[face].right_neighbor.right_neighbor.top_middle

        self.gear_ball_sides[face].bottom_left_corner , self.gear_ball_sides[face].right_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.bottom_left_corner = self.gear_ball_sides[face].right_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.bottom_left_corner , self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_left_corner
        self.gear_ball_sides[face].bottom_edge , self.gear_ball_sides[face].right_neighbor.bottom_edge, self.gear_ball_sides[face].right_neighbor.right_neighbor.bottom_edge, self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.bottom_edge = self.gear_ball_sides[face].right_neighbor.bottom_edge, self.gear_ball_sides[face].right_neighbor.right_neighbor.bottom_edge , self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.bottom_edge, self.gear_ball_sides[face].bottom_edge
        self.gear_ball_sides[face].bottom_right_corner , self.gear_ball_sides[face].right_neighbor.bottom_right_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.bottom_right_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.bottom_right_corner = self.gear_ball_sides[face].right_neighbor.bottom_right_corner, self.gear_ball_sides[face].right_neighbor.right_neighbor.bottom_right_corner , self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_right_corner
        self.gear_ball_sides[face].bottom_middle , self.gear_ball_sides[face].right_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.bottom_middle = self.gear_ball_sides[face].right_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_neighbor.right_neighbor.bottom_middle, self.gear_ball_sides[face].bottom_middle

        #rotate top face counter_clockwise

        #swap side face corners
        self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_right_corner = self.gear_ball_sides[face].top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_right_corner

        #swap side edges
        self.gear_ball_sides[face].top_neighbor.top_edge, self.gear_ball_sides[face].top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.bottom_edge, self.gear_ball_sides[face].top_neighbor.right_edge = self.gear_ball_sides[face].top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_edge, self.gear_ball_sides[face].top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.bottom_edge

        #swap middle pieces
        self.gear_ball_sides[face].top_neighbor.top_middle, self.gear_ball_sides[face].top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.bottom_middle, self.gear_ball_sides[face].top_neighbor.right_middle = self.gear_ball_sides[face].top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_middle, self.gear_ball_sides[face].top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.bottom_middle

        #rotate right face counter_clockwise

        #swap side face corners
        self.gear_ball_sides[face].bottom_neighbor.top_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_right_corner = self.gear_ball_sides[face].bottom_neighbor.top_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_right_corner

        #swap side edges
        self.gear_ball_sides[face].bottom_neighbor.top_edge, self.gear_ball_sides[face].bottom_neighbor.left_edge, self.gear_ball_sides[face].bottom_neighbor.bottom_edge, self.gear_ball_sides[face].bottom_neighbor.right_edge = self.gear_ball_sides[face].bottom_neighbor.right_edge, self.gear_ball_sides[face].bottom_neighbor.top_edge, self.gear_ball_sides[face].bottom_neighbor.left_edge, self.gear_ball_sides[face].bottom_neighbor.bottom_edge

        #swap middle pieces
        self.gear_ball_sides[face].bottom_neighbor.top_middle, self.gear_ball_sides[face].bottom_neighbor.left_middle, self.gear_ball_sides[face].bottom_neighbor.bottom_middle, self.gear_ball_sides[face].bottom_neighbor.right_middle = self.gear_ball_sides[face].bottom_neighbor.right_middle, self.gear_ball_sides[face].bottom_neighbor.top_middle, self.gear_ball_sides[face].bottom_neighbor.left_middle, self.gear_ball_sides[face].bottom_neighbor.bottom_middle


    def front_move_counter_clockwise(self, face): #error here
        # move edge pieces
        self.gear_ball_sides[face].top_neighbor.left_edge_value = (self.gear_ball_sides[face].top_neighbor.left_edge_value + 1) % 6
        self.gear_ball_sides[face].top_neighbor.right_edge_value = (self.gear_ball_sides[face].top_neighbor.right_edge_value + 1) % 6

        self.gear_ball_sides[face].left_neighbor.top_edge_value = (self.gear_ball_sides[face].left_neighbor.top_edge_value + 1) % 6
        self.gear_ball_sides[face].left_neighbor.bottom_edge_value = (self.gear_ball_sides[face].left_neighbor.bottom_edge_value + 1) % 6

        self.gear_ball_sides[face].right_neighbor.top_edge_value = (self.gear_ball_sides[face].right_neighbor.top_edge_value + 1) % 6
        self.gear_ball_sides[face].right_neighbor.bottom_edge_value = (self.gear_ball_sides[face].right_neighbor.bottom_edge_value + 1) % 6

        self.gear_ball_sides[face].bottom_neighbor.left_edge_value = (self.gear_ball_sides[face].bottom_neighbor.left_edge_value + 1) % 6
        self.gear_ball_sides[face].bottom_neighbor.right_edge_value = (self.gear_ball_sides[face].bottom_neighbor.right_edge_value + 1) % 6



        #shift front face counter_clockwise

        #swap side face corners
        self.gear_ball_sides[face].top_left_corner, self.gear_ball_sides[face].bottom_left_corner, self.gear_ball_sides[face].bottom_right_corner, self.gear_ball_sides[face].top_right_corner = self.gear_ball_sides[face].top_right_corner, self.gear_ball_sides[face].top_left_corner, self.gear_ball_sides[face].bottom_left_corner, self.gear_ball_sides[face].bottom_right_corner

        #swap side edges
        self.gear_ball_sides[face].top_edge, self.gear_ball_sides[face].left_edge, self.gear_ball_sides[face].bottom_edge, self.gear_ball_sides[face].right_edge = self.gear_ball_sides[face].right_edge, self.gear_ball_sides[face].top_edge, self.gear_ball_sides[face].left_edge, self.gear_ball_sides[face].bottom_edge

        #swap middle pieces

        self.gear_ball_sides[face].top_middle, self.gear_ball_sides[face].left_middle, self.gear_ball_sides[face].bottom_middle, self.gear_ball_sides[face].right_middle = self.gear_ball_sides[face].right_middle, self.gear_ball_sides[face].top_middle, self.gear_ball_sides[face].left_middle, self.gear_ball_sides[face].bottom_middle

        #shift back face clockwise

        self.gear_ball_sides[face].top_neighbor.top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_right_corner = self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_left_corner

        #swap side edges
        self.gear_ball_sides[face].top_neighbor.top_neighbor.top_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge = self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_edge

        #swap middle pieces

        self.gear_ball_sides[face].top_neighbor.top_neighbor.top_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_middle = self.gear_ball_sides[face].top_neighbor.top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_middle

        #shift closest third left
        self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_right_corner, self.gear_ball_sides[face].right_neighbor.top_left_corner = self.gear_ball_sides[face].right_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_right_corner
        self.gear_ball_sides[face].top_neighbor.bottom_edge, self.gear_ball_sides[face].left_neighbor.right_edge, self.gear_ball_sides[face].bottom_neighbor.top_edge, self.gear_ball_sides[face].right_neighbor.left_edge = self.gear_ball_sides[face].right_neighbor.left_edge,self.gear_ball_sides[face].top_neighbor.bottom_edge, self.gear_ball_sides[face].left_neighbor.right_edge, self.gear_ball_sides[face].bottom_neighbor.top_edge
        self.gear_ball_sides[face].top_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.right_middle, self.gear_ball_sides[face].bottom_neighbor.top_middle, self.gear_ball_sides[face].right_neighbor.left_middle = self.gear_ball_sides[face].right_neighbor.left_middle,self.gear_ball_sides[face].top_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.right_middle, self.gear_ball_sides[face].bottom_neighbor.top_middle
        self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].left_neighbor.top_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_left_corner = self.gear_ball_sides[face].right_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].left_neighbor.top_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_left_corner

        #shift furthest third right
        self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_right_corner, self.gear_ball_sides[face].right_neighbor.top_right_corner = self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_right_corner, self.gear_ball_sides[face].right_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_left_corner
        self.gear_ball_sides[face].top_neighbor.top_edge, self.gear_ball_sides[face].left_neighbor.left_edge, self.gear_ball_sides[face].bottom_neighbor.bottom_edge, self.gear_ball_sides[face].right_neighbor.right_edge = self.gear_ball_sides[face].left_neighbor.left_edge,self.gear_ball_sides[face].bottom_neighbor.bottom_edge, self.gear_ball_sides[face].right_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_edge
        self.gear_ball_sides[face].top_neighbor.top_middle, self.gear_ball_sides[face].left_neighbor.left_middle, self.gear_ball_sides[face].bottom_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_middle = self.gear_ball_sides[face].left_neighbor.left_middle,self.gear_ball_sides[face].bottom_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_middle
        self.gear_ball_sides[face].top_neighbor.top_right_corner, self.gear_ball_sides[face].left_neighbor.top_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_right_corner = self.gear_ball_sides[face].left_neighbor.top_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_right_corner

    def front_move_clockwise(self, face):

        self.gear_ball_sides[face].top_neighbor.left_edge_value = (self.gear_ball_sides[face].top_neighbor.left_edge_value - 1) % 6
        self.gear_ball_sides[face].top_neighbor.right_edge_value = (self.gear_ball_sides[face].top_neighbor.right_edge_value - 1) % 6

        self.gear_ball_sides[face].left_neighbor.top_edge_value = (self.gear_ball_sides[face].left_neighbor.top_edge_value - 1) % 6
        self.gear_ball_sides[face].left_neighbor.bottom_edge_value = (self.gear_ball_sides[face].left_neighbor.bottom_edge_value - 1) % 6

        self.gear_ball_sides[face].right_neighbor.top_edge_value = (self.gear_ball_sides[face].right_neighbor.top_edge_value - 1) % 6
        self.gear_ball_sides[face].right_neighbor.bottom_edge_value = (self.gear_ball_sides[face].right_neighbor.bottom_edge_value - 1) % 6

        self.gear_ball_sides[face].bottom_neighbor.left_edge_value = (self.gear_ball_sides[face].bottom_neighbor.left_edge_value - 1) % 6
        self.gear_ball_sides[face].bottom_neighbor.right_edge_value = (self.gear_ball_sides[face].bottom_neighbor.right_edge_value - 1) % 6
        #shift front face clockwise

        #swap side face corners
        self.gear_ball_sides[face].top_left_corner, self.gear_ball_sides[face].bottom_left_corner, self.gear_ball_sides[face].bottom_right_corner, self.gear_ball_sides[face].top_right_corner = self.gear_ball_sides[face].bottom_left_corner, self.gear_ball_sides[face].bottom_right_corner, self.gear_ball_sides[face].top_right_corner, self.gear_ball_sides[face].top_left_corner

        #swap side edges
        self.gear_ball_sides[face].top_edge, self.gear_ball_sides[face].left_edge, self.gear_ball_sides[face].bottom_edge, self.gear_ball_sides[face].right_edge = self.gear_ball_sides[face].left_edge, self.gear_ball_sides[face].bottom_edge, self.gear_ball_sides[face].right_edge, self.gear_ball_sides[face].top_edge

        #swap middle pieces

        self.gear_ball_sides[face].top_middle, self.gear_ball_sides[face].left_middle, self.gear_ball_sides[face].bottom_middle, self.gear_ball_sides[face].right_middle = self.gear_ball_sides[face].left_middle, self.gear_ball_sides[face].bottom_middle, self.gear_ball_sides[face].right_middle, self.gear_ball_sides[face].top_middle

        #shift back face clockwise

        self.gear_ball_sides[face].top_neighbor.top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_right_corner = self.gear_ball_sides[face].top_neighbor.top_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_right_corner

        #swap side edges
        self.gear_ball_sides[face].top_neighbor.top_neighbor.top_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge = self.gear_ball_sides[face].top_neighbor.top_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_edge, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_edge

        #swap middle pieces

        self.gear_ball_sides[face].top_neighbor.top_neighbor.top_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.right_middle = self.gear_ball_sides[face].top_neighbor.top_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.top_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.top_neighbor.bottom_middle

        #shift closest third right
        self.gear_ball_sides[face].top_neighbor.bottom_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_right_corner, self.gear_ball_sides[face].right_neighbor.top_left_corner = self.gear_ball_sides[face].left_neighbor.bottom_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_right_corner, self.gear_ball_sides[face].right_neighbor.top_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_left_corner
        self.gear_ball_sides[face].top_neighbor.bottom_edge, self.gear_ball_sides[face].left_neighbor.right_edge, self.gear_ball_sides[face].bottom_neighbor.top_edge, self.gear_ball_sides[face].right_neighbor.left_edge = self.gear_ball_sides[face].left_neighbor.right_edge, self.gear_ball_sides[face].bottom_neighbor.top_edge, self.gear_ball_sides[face].right_neighbor.left_edge,  self.gear_ball_sides[face].top_neighbor.bottom_edge
        self.gear_ball_sides[face].top_neighbor.bottom_middle, self.gear_ball_sides[face].left_neighbor.right_middle, self.gear_ball_sides[face].bottom_neighbor.top_middle, self.gear_ball_sides[face].right_neighbor.left_middle = self.gear_ball_sides[face].left_neighbor.right_middle, self.gear_ball_sides[face].bottom_neighbor.top_middle, self.gear_ball_sides[face].right_neighbor.left_middle, self.gear_ball_sides[face].top_neighbor.bottom_middle
        self.gear_ball_sides[face].top_neighbor.bottom_right_corner, self.gear_ball_sides[face].left_neighbor.top_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_left_corner = self.gear_ball_sides[face].left_neighbor.top_right_corner, self.gear_ball_sides[face].bottom_neighbor.top_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_left_corner, self.gear_ball_sides[face].top_neighbor.bottom_right_corner

        #shift furthest third left
        self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_right_corner, self.gear_ball_sides[face].right_neighbor.top_right_corner = self.gear_ball_sides[face].right_neighbor.top_right_corner, self.gear_ball_sides[face].top_neighbor.top_left_corner, self.gear_ball_sides[face].left_neighbor.bottom_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_right_corner
        self.gear_ball_sides[face].top_neighbor.top_edge, self.gear_ball_sides[face].left_neighbor.left_edge, self.gear_ball_sides[face].bottom_neighbor.bottom_edge, self.gear_ball_sides[face].right_neighbor.right_edge = self.gear_ball_sides[face].right_neighbor.right_edge, self.gear_ball_sides[face].top_neighbor.top_edge, self.gear_ball_sides[face].left_neighbor.left_edge, self.gear_ball_sides[face].bottom_neighbor.bottom_edge
        self.gear_ball_sides[face].top_neighbor.top_middle, self.gear_ball_sides[face].left_neighbor.left_middle, self.gear_ball_sides[face].bottom_neighbor.bottom_middle, self.gear_ball_sides[face].right_neighbor.right_middle =  self.gear_ball_sides[face].right_neighbor.right_middle, self.gear_ball_sides[face].top_neighbor.top_middle, self.gear_ball_sides[face].left_neighbor.left_middle, self.gear_ball_sides[face].bottom_neighbor.bottom_middle
        self.gear_ball_sides[face].top_neighbor.top_right_corner, self.gear_ball_sides[face].left_neighbor.top_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_left_corner, self.gear_ball_sides[face].right_neighbor.bottom_right_corner = self.gear_ball_sides[face].right_neighbor.bottom_right_corner, self.gear_ball_sides[face].top_neighbor.top_right_corner, self.gear_ball_sides[face].left_neighbor.top_left_corner, self.gear_ball_sides[face].bottom_neighbor.bottom_left_corner


    def randomize_ball(self, face, k):
        #number of moves applied to ball
        num_turns = k
        for i in range(int(num_turns)):
            our_int = random.randint(0, 5)
            if our_int == 0:
                self.center_third_still_left_up(face)

            if our_int == 1:

                self.center_third_still_right_up(face)

            if our_int == 2:

                self.center_third_still_top_left(face)

            if our_int == 3:

                self.center_third_still_top_right(face)

            if our_int == 4:

                self.front_move_clockwise(face)

            if our_int == 5:

                self.front_move_counter_clockwise(face)
        heuristic = self.smarty_heuristic()


    def dummy_heuristic(self):
        solved = 1
        for face in self.gear_ball_sides:
            #gears in correct position
            #check edge in solved position
            if face.top_edge_value == 0 and face.bottom_edge_value == 0 and face.left_edge_value == 0 and face.right_edge_value == 0:
                #check edge color
                if (face.top_edge == "TE: " + face.center) and (face.left_edge == "LE: " + face.center) and (face.bottom_edge == "BE: " + face.center) and (face.right_edge_value == "RE: " + face.center):
                    #check corner color
                    if (face.top_left_corner == "TLC: " + face.center) and (face.top_right_corner == "TRC: " + face.center) and (face.bottom_left_corner == "BLC: " + face.center) and (face.bottom_right_corner == "BRC: " + face.center):
                        #check middle color
                        if (face.top_middle == "TM: " + face.center) and (face.left_middle == "LM: " + face.center) and (face.bottom_middle == "BM: " + face.center) and (face.right_middle == "RM: " + face.center):
                            solved = 0
                            return solved
            else:
                return solved

    #manhattan distance
    def smarty_heuristic(self):
        total_distance = 0
        gears_closed = 0
        for side in self.gear_ball_sides:

            #check how far piece is from correct side
            total_distance += side.find_distance(side.top_left_corner)
            total_distance += side.find_distance(side.top_right_corner)
            total_distance += side.find_distance(side.bottom_left_corner)
            total_distance += side.find_distance(side.bottom_right_corner)
            total_distance += side.find_distance(side.left_edge)
            total_distance += side.find_distance(side.right_edge)
            total_distance += side.find_distance(side.top_edge)
            total_distance += side.find_distance(side.bottom_edge)
            total_distance += side.find_distance(side.left_middle)
            total_distance += side.find_distance(side.right_middle)
            total_distance += side.find_distance(side.top_middle)
            total_distance += side.find_distance(side.bottom_middle)

            if side.top_edge_value != 0:
                total_distance += 1
            if side.left_edge_value != 0:
                total_distance += 1

        return ((total_distance / 32) + gears_closed)

    #check to see if puzzle is in solvable state
    def solve_ball(self, moves):
        face = 0
        print(moves)
        #reverse moves
        moves.reverse()
        for i in moves:

            if i == 0:
                print("0")
                self.center_third_still_left_up(face)

            if i == 1:
                print("1")
                self.center_third_still_right_up(face)

            if i == 2:
                print("2")
                self.center_third_still_top_left(face)

            if i == 3:
                print("3")
                self.center_third_still_top_right(face)

            if i == 4:
                print("4")
                self.front_move_clockwise(face)

            if i == 5:
                print("5")
                self.front_move_counter_clockwise(face)

