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
    

class Rectangle2:

    def __init__(self, posn , w, h):
        self.corner = posn
        self.width = w
        self.height = h
    
    def __str__(self):
        return  "({0}, {1}, {2})" \
                  .format(self.corner, self.width, self.height)       

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height
    
    def move(self, dx, dy):
        self.corner.x = dx
        self.corner.y = dy
    
    def area(self):
        ''' return the area of the any instance '''
        return self.width * self.height

    def swapValues(self):
        '''  swaps the width and the height '''

        self.width, self.height = self.height, self.width
        return "(width: {0},height: {1})".format(self.width, self.height)

    def contains(self):
        if self.corner.x >= 0 and self.corner.x < self.width:
            if self.corner.y >= 0 and self.corner.y < self.height:
                return True 
        return False

    def get_vertices(self):
        """Finds the corners of rectangle"""
        a = Point(self.corner.x, self.corner.y + self.height)
        b = self.corner
        c = Point(self.corner.x + self.width,
                self.corner.y + self.height)
        d = Point(self.corner.x + self.width, self.corner.y)

        return a, b, c, d


p1 = Rectangle2(Point(0, 0), 1, 2)
p2 = Rectangle2(Point(1, 2), 3, 4)
# print('The area of this instance: {}'.format(p1.height * p1.width))
# res = p1.swapValues()
# print('Before swaping: width= {}, height= {}'.format(p1.width, p1.height))
# print('After swaping: {}'.format(res))


# print(p1.contains())
# print((p1.get_vertices()))
