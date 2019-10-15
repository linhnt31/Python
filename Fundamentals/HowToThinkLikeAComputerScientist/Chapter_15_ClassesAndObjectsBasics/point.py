class Point:
    """ Point class represents and manipulates x,y coords. """

    def Point(self):
        """constructor """
        pass

    def __init__(self, x = 0, y = 0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def to_string(self):
        return "({}, {})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def mid_point(self, p1, p2): 
        return (p1.x + p2.x + p1.y + p2.y) / 2

p = Point(1, 2) # Instantiate an object of type Point
q = Point(3, 4) # Make a second point
r = Point()
# p.x = 3
# p.y = 4
# print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y
print(p.x, p.y, r.x)
print(p.distance_from_origin())
print(r.distance_from_origin())
print(p.to_string())
# print(str(p))
print(p.mid_point(p, q))
