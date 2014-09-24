#November 6, 2013 Notes
#Adding additional features to the point class


class Point:
    def __init__(self, x=0, y= 0):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)


#redefines how two points are equal
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

#concept that represents string such that if you were to do eval, you would get object back
#repr stands for representation
    def __repr__(self):
        return "Point(" +str(self.x) + "," + str(self.y) + ")"


#adds two points together to do some arithmetic
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    

#performs multiplication
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    
