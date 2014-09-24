#November 24, 2013 Review Session


#declare class, constructor, methods, etc...

import math

class Circle:
    
    def __init__(self, r, x, y):
        self.radius = r
        self.x = x
        self.y = y

    def diameter(self):
        return self.radius*2

    def __eq__(self, other): #two radius are equal if they have same x and y coordinates
        if self.radius == other.radius and self.x == other.x and self.y == other.y:
            return True

    def circumference(self):
        return self.diameter * math.pi

    def __repr__ (self):
        return "Circle(" +str(self.radius)+ "," +str(self.x)+ "," +str(self.y)+ ")"




#GRADEBOOK

class GradeBook:

    def __init__(self):
        self.dict = {}

    def addgrade(self, n, g): #n is the name of the student
        if n not in self.dict:
            self.dict[n] = []
        self.dict[n] += [g]#or self.dict[n].append[g] (just pick one of these two)

    def hasgradesfor(self, n):
        if n in self.dict:
            return True
        else:
            return False

    def allgradesfor(self, n):
        return self.dict[n]

    def averagegradefor(self, n):
        return sum(self.dict[n])/len(self.dict[n]


#DIEROLLS
import random

class Dierolls:

    def __init__(self, n):
        self.n = n
        self.h = {}

    def roll(self):
        result = 0
        for in range (self.n):
            result += random.randrange(1,7)
        if result not in self.h:
            self.h = 0
            self.h[result] += 1
            return result

    def rollsOf(self, n):
        if n in self.h:
            return self.h[n]
        else:
            return 0    
        
