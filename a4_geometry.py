import os
import re
import sys
import math

def compareDist(x1,y1,z1,x2,z2,y2,d):
    d2=((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2)**.5
    if d2 < d:
        return True
    else:
        return False
def getDist(x1,y1,z1,x2,z2,y2):
    d2=((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2)**.5
    return d2

class Point (object):
  # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
    def __str__ (self):
        sx = str(self.x)
        sy = str(self.y)
        sz = str(self.z)
        sxyz = '({}, {}, {})'.format(sx,sy,sz)
        return sxyz
  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
    def distance (self, other):
        d=(((self.x-other.x)**2)+((self.y-other.y)**2)+((self.z-other.z)**2))**.5
        return d
  # test for equality between two points
  # other is a Point object
  # returns a Boolean
    def __eq__ (self, other):
        if (self.x==other.x) and (self.y==other.y) and (self.z==other.z):
            return True
        else:
            return False
class Sphere (object):
  # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
    def __str__ (self):
        sx = str(self.x)
        sy = str(self.y)
        sz = str(self.z)
        sr = str(self.radius)
        sxyzsphere = 'Center: ({}, {}, {}), Radius: {}'.format(sx,sy,sz,sr)
        return sxyzsphere
  # compute surface area of Sphere
  # returns a floating point number
    def area (self):
        areas = 4*math.pi*(self.radius**2)
        return areas
  # compute volume of a Sphere
  # returns a floating point number
    def volume (self):
        volumes = (4/3)*math.pi*(self.radius**3)
        return volumes
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
    def is_inside_point (self, p):
        d=(((self.x-p.x)**2)+((self.y-p.y)**2)+((self.z-p.z)**2))**.5
        if d < self.radius:
            return True
        else:
            return False

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
    def is_inside_sphere (self, other):
        if ((self.x+self.radius)>(other.x+other.radius)) and ((self.x-self.radius)<(other.x-other.radius)):
            if ((self.y+self.radius)>(other.y+other.radius)) and ((self.y-self.radius)<(other.y-other.radius)):
                if ((self.z+self.radius)>(other.z+other.radius)) and ((self.z-self.radius)<(other.z-other.radius)):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are inside 
  # the Sphere
  # a_cube is a Cube object
  # returns a Boolean
    def is_inside_cube (self, a_cube):
        cubearr=[0,0,0,0,0,0,0,0]
        x=a_cube.x
        y=a_cube.y
        z=a_cube.z
        s=a_cube.side
        hs=s/2
        cubearr[0]=[x-hs,y-hs,z-hs]
        cubearr[1]=[x+hs,y-hs,z-hs]
        cubearr[2]=[x-hs,y+hs,z-hs]
        cubearr[3]=[x-hs,y-hs,z+hs]
        cubearr[4]=[x+hs,y+hs,z-hs]
        cubearr[5]=[x+hs,y-hs,z+hs]
        cubearr[6]=[x-hs,y+hs,z+hs]
        cubearr[7]=[x-hs,y+hs,z+hs]
        flag=0
        for i in range(len(cubearr)):
            if compareDist(cubearr[i][0],cubearr[i][1],cubearr[i][2],self.x,self.y,self.z,self.radius)==True:
                flag=flag*1
            else:
                flag=0
        if flag==1:
            return True
        else:
            return False

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        cylarr=[0,0,0,0,0,0,0,0,0]
        x=a_cyl.x
        y=a_cyl.y
        z=a_cyl.z
        h=a_cyl.height
        hh=h/2
        r=a_cyl.radius
        cylarr[0]=[x,y,z]
        cylarr[1]=[x+r,y,z+hh]
        cylarr[2]=[x-r,y,z+hh]
        cylarr[3]=[x,y+r,z+hh]
        cylarr[4]=[x,y-r,z+hh]
        cylarr[5]=[x+r,y,z-hh]
        cylarr[6]=[x-r,y,z-hh]
        cylarr[7]=[x,y+r,z-hh]
        cylarr[8]=[x,y-r,z-hh]
        flag=0
        for i in range(len(cylarr)):
            if compareDist(cylarr[i][0],cylarr[i][1],cylarr[i][2],self.x,self.y,self.z,self.radius)==True:
                flag=flag*1
            else:
                flag=0
        if flag==1:
            return True
        else:
            return False
  # determine if another Sphere intersects this Sphere
  # there is a non-zero volume of intersection
  # other is a Sphere object
  # returns a Boolean
    def does_intersect_sphere (self, other):
        d1 = self.radius+other.radius
        d2 = getDist(self.x,self.y,self.z,other.x,other.y,other.z)
        if d1 <= d2:
            return True
        else:
            return False

  # determine if a Cube intersects this Sphere
  # there is a non-zero volume of intersection
  # there is at least one corner of the Cube in 
  # the Sphere
  # a_cube is a Cube object
  # returns a Boolean
    def does_intersect_cube (self, a_cube):
        cubearr=[0,0,0,0,0,0,0,0]
        x=a_cube.x
        y=a_cube.y
        z=a_cube.z
        s=a_cube.side
        hs=s/2
        cubearr[0]=[x-hs,y-hs,z-hs]
        cubearr[1]=[x+hs,y-hs,z-hs]
        cubearr[2]=[x-hs,y+hs,z-hs]
        cubearr[3]=[x-hs,y-hs,z+hs]
        cubearr[4]=[x+hs,y+hs,z-hs]
        cubearr[5]=[x+hs,y-hs,z+hs]
        cubearr[6]=[x-hs,y+hs,z+hs]
        cubearr[7]=[x-hs,y+hs,z+hs]
        flag=0
        for i in range(len(cubearr)):
            if compareDist(cubearr[i][0],cubearr[i][1],cubearr[i][2],self.x,self.y,self.z,self.radius)==False:
                flag=1
            else:
                flag*=1
        if flag==1:
            return True
        else:
            return False
  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
    def circumscribe_cube (self):
        cside=(2*self.radius)/(3**.5)
        cside=f"{cside:.4f}"
        ccube=Cube(x=self.x,y=self.y,z=self.z,side=cside)
        return ccube
class Cube (object):

  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.x = x
        self.y = y
        self.z = z
        self.side = side
  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
    def __str__ (self):
        sx = str(self.x)
        sy = str(self.y)
        sz = str(self.z)
        sside = str(self.side)
        sxyzcube = 'Center: ({}, {}, {}), Side: {}'.format(sx,sy,sz,sside)
        return sxyzcube
  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
    def area (self):
        u=0
  # compute volume of a Cube
  # returns a floating point number
    def volume (self):
        u=0
  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
    def is_inside_point (self, p):
        u=0
  # determine if a Sphere is strictly inside this Cube or
  # a_sphere is a Sphere object
  # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        u=0
  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
    def is_inside_cube (self, other):
        u=0
  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        u=0
  # determine if another Cube intersects this Cube
  # there is a non-zero volume of intersection
  # there is at least one vertex of the other Cube
  # in this Cube
  # other is a Cube object
  # returns a Boolean
    def does_intersect_cube (self, other):
        u=0
  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
    def intersection_volume (self, other):
        u=0
  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
    def inscribe_sphere (self):
        u=0
class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height
  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        sx = str(self.x)
        sy = str(self.y)
        sz = str(self.z)
        sr = str(self.radius)
        sh = str(self.height)
        sxyzcylinder = 'Center: ({}, {}, {}), Radius: {}, Height: {}'.format(sx,sy,sz,sr,sh)
        return sxyzcylinder
  # compute surface area of Cylinder
  # returns a floating point number
    def area (self):
        u=0
  # compute volume of a Cylinder
  # returns a floating point number
    def volume (self):
        u=0
  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
    def is_inside_point (self, p):
        u=0
  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        u=0
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are in
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
    def is_inside_cube (self, a_cube):
        u=0
  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
    def is_inside_cylinder (self, other):
        u=0
  # determine if another Cylinder intersects this Cylinder
  # there is a non-zero volume of intersection
  # other is a Cylinder object
  # returns a Boolean
    def does_intersect_cylinder (self, other):
        u=0
def main(inpt, fptr):
    inpt = inpt.split('\n')
    for i in range(len(inpt)):
        temparr = inpt[i]
        temparr = temparr.split(' ')
        for j in range(len(temparr)):
            temparr[j]=float(temparr[j])
        if i == 0:
            pointp=Point(x=temparr[0],y=temparr[1],z=temparr[2])
        elif i == 1:
            pointq=Point(x=temparr[0],y=temparr[1],z=temparr[2])
        elif i == 2:
            sphereA=Sphere(x=temparr[0],y=temparr[1],z=temparr[2],radius=temparr[3])
        elif i == 3:
            sphereB=Sphere(x=temparr[0],y=temparr[1],z=temparr[2],radius=temparr[3])
        elif i == 4:
            cubeA=Cube(x=temparr[0],y=temparr[1],z=temparr[2],side=temparr[3])
        elif i == 5:
            cubeB=Cube(x=temparr[0],y=temparr[1],z=temparr[2],side=temparr[3])
        elif i == 6:
            cylA=Cylinder(x=temparr[0],y=temparr[1],z=temparr[2],radius=temparr[3],height=temparr[4])
        elif i == 7:
            cylB=Cylinder(x=temparr[0],y=temparr[1],z=temparr[2],radius=temparr[3],height=temparr[4])
    temp=sphereA.area()
    temp=f"{temp:.5f}"
    temp=str(temp)
    fptr.write('Area of sphereA: ')
    fptr.write(temp)
    fptr.write('\n')
    temp=sphereA.volume()
    temp=f"{temp:.5f}"
    temp=str(temp)
    fptr.write('Volume of sphereA: ')
    fptr.write(temp)
    fptr.write('\n')
    temp=sphereA.is_inside_point(pointp)
    if temp==True:
        fptr.write('Point p is inside sphereA\n')
    else:
        fptr.write('Point p is not inside sphereA\n')
    temp=sphereA.is_inside_sphere(sphereB)
    if temp==True:
        fptr.write('sphereB is inside sphereA\n')
    else:
        fptr.write('sphereB is not inside sphereA\n')
    temp=sphereA.is_inside_cube(cubeA)
    if temp==True:
        fptr.write('cubeA is inside sphereA\n')
    else:
        fptr.write('cubeA is not inside sphereA\n')
    temp=sphereA.is_inside_cyl(cylA)
    if temp==True:
        fptr.write('cylA is inside sphereA\n')
    else:
        fptr.write('cylA is not inside sphereA\n')
    temp=sphereA.does_intersect_sphere(sphereB)
    if temp==True:
        fptr.write('sphereA does intersect sphereB\n')
    else:
        fptr.write('sphereA does not intersect sphereB\n')
    temp=sphereB.does_intersect_cube(cubeB)
    if temp==True:
        fptr.write('cubeB does intersect sphereB\n')
    else:
        fptr.write('cubeB does not intersect sphereB\n')  
    temp=sphereA.circumscribe_cube()
    temp=str(temp)
    fptr.write('Largest Cube circumscribed by sphereA: ')
    fptr.write(temp)