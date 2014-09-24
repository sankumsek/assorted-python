#Chapter 8 Part 2

#Implementation of __sub__() and __truediv__() to the Point class
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __truediv__(self, scalar):
        return (self.x / scalar, self.y / scalar)

    
#Implementation of SEGMENT class

class Segment:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get(self):
        return (self.x1, self.x2, self.y1, self.y2)

    def length(self):
        return "Length is:" (math.sqrt(self.y2 - self.y1)-(self.x2 - self.x1))

    def slope(self):
        if self.x1 == self.x2:
            return None
        else:
            return "Slope is:"((self.y2 - self.y1)/(self.x2 - self.x1))

    def __eq__(self):
        return (self.x1 == other.x1 and self.x2 == other.x2 and self.y1 == other.y1 and self.y2 == other.y2)

    def __repr__(self):
        return "Segment((" +str(self.x1) + "," + str(self.y1) + ")(" + str(self.x2) + "," + str(self.y2) + "))"



#Implementation of PSEUDORANDOM class

class Pseudorandom:
    def __init__(self, a=1, x=1, c=0, m=1):
        self.a = a
        self.x = x
        self.c = c
        self.m = m

    def next(self):
        self.x = ((self.a*self.x) + self.c) % self.m
        return self.x

    def __eq__(self, a=1, x=1, c=0, m=1):
        return (self.a == other.a and self.x == other.x and self.c == other.c and self.m == other.m)

    def __repr__(self):
        return "The Values are:" + str(self.a) + "," + str(self.x) + "," + str(self.c) + "," + str(self.m) + "."
    


  
    
