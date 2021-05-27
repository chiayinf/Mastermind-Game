'''
   CS5001
   Spring 2021
   Chiayin Fan
   Class of Point
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delta_x(self, other):
        return abs(self.x - other.x)

    def delta_y(self, other):
        return abs(self.y - other.y)
    def __str__(self):
        return str(self.x) + ' ' + str(self.y)
