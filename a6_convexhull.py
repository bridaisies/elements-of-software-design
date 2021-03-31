import os
import re
import sys
import math

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det (p, q, r):

    return ((q.x * r.y) - (r.x * q.y)) - ((p.x * r.y) - (r.x * p.y)) + ((p.x * q.y) - (q.x * p.y))
# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull (sorted_points):

    s = sorted_points
    l = len(s)

    up_list, low_list = [], []

    up_list.append(s[0])
    up_list.append(s[1])

    for next_index in range(2, l):
        up_list.append(s[next_index])
        while((len(up_list) > 2) and (det(up_list[-1], up_list[-2], up_list[-3]) < 0)):
            up_list.remove(up_list[-2])

    low_list.append(s[-1])
    low_list.append(s[-2])

    for next_index in range(l - 3, -1, -1):
        low_list.append(s[next_index])
        while((len(low_list) > 2) and (det(low_list[-1], low_list[-2], low_list[-3]) < 0)):
            low_list.remove(low_list[-2])
        
    low_list.remove(low_list[0])
    low_list.remove(low_list[-1])
    
    return up_list + low_list

# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly (convex_poly):

    con = convex_poly
    area = 0.0
    length = len(convex_poly)

    j = length - 1
    for i in range(0, length):
        area += (con[i].x + con[j].x) * (con[j].y - con[i].y)
        j = i

    a = abs(area / 2.0)

    return a

def main(coords):

    point_list = []
    s = sorted(coords)
    for i in s:
        point_list.append(Point(i[0], i[1]))
    hull = convex_hull(point_list)
    area = area_poly(hull)
    rounded = round(area, 7)

    return rounded