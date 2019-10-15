'''
- Link: http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_II.html
'''
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
# print(p.x, p.y, r.x)
# print(p.distance_from_origin())
# print(r.distance_from_origin())
# print(p.to_string())
# print(str(p))
# print(p.mid_point(p, q))



class Ractangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})" \
                  .format(self.corner, self.width, self.height)

    def modifySize(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy



box = Ractangle(Point(0, 0), 100, 200)
bomb = Ractangle(Point(100, 80), 5, 10) #In my video game

# print('Box: ', box)
# print('Bomb: ', bomb)
# print('Attributes: ', box.corner.x, bomb.corner.y)

#Objects are mutable
# box.modifySize(100, 50)
# print('After modify, width= {} + height= {}'.format(box.width, box.height))
# box.move(20, -30)
# print('After move, x= {} + y= {}'.format(box.corner.x, box.corner.y))

""" 16.3 Sameness """

# p1 = Point(1, 2)
# p2 = Point(1, 2)

''' shallow equality
- It compares only the referrences not the contents of the obj

'''
# p3 = p1 # they are aliases if the same object

# print(p1 is p2)
# print(p1 is p3)

'''deep equality
- In compares the contents of the obj
 '''
def same_coordinates(p1, p2):
    return p1.x == p2.x \
            and p1.y == p2.y


# p5 = Point(10, 11)
# p6 = Point(10, 11)

# print(same_coordinates(p5, p6))


"""16.4 Copying 
- Copying an object is often an alternative to aliasing. 
- To copy a simple obj which does not contain any embedded objs
"""

import copy

# p1 = Point(3, 4)
p1 = Ractangle(Point(1, 2), 100, 200)
#shallow copy
# p2 = copy.copy(p1)
#deep copy
p2 = copy.deepcopy(p1)


print('Before modify: px= {}, py= {} '.format(p1.corner.x, p2.corner.x))
p1.move(10, 0)
print('After modify: px= {}, py= {}'.format(p1.corner.x, p2.corner.x))
