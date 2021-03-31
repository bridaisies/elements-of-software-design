#Drew Hardie, DHH636
#Brionna Huynh, BPH637
def grid_init(w,h):
    grid = [[0 for i in range(w+1)] for j in range(h+1)]
    return grid

def increment_grid(l,r,b,t,grid):
    h=l
    k=t
    while k<=b:
        h=l
        while h<=r:
            grid[k][h]+=1
            h+=1
        k+=1
    return grid

def count_grid(val,grid):
    count=0
    left=0
    right=0
    top=0
    bottom=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==val:
                if count==0:
                    left=j
                    bottom=i
                count+=1
                right=j
                top=i
    rectup=(left,bottom,right,top)
    for i in range(len(grid)):
        print(grid[i])
    return rectup
# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    a=(rect[0]-rect[2])*(rect[1]-rect[3])
    if a<0:
        a*=-1
    return a

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectanlge.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    if rect1[0]<rect2[0]:
        left=rect1[0]
    else:
        left=rect2[0]
    if rect1[1]<rect2[1]:
        bottom=rect1[1]
    else:
        bottom=rect2[1]
    if rect1[2]>rect2[2]:
        right=rect1[2]
    else:
        right=rect2[2]
    if rect1[3]>rect2[3]:
        top=rect1[3]
    else:
        top=rect2[3]
#    print('bottom',bottom)
#    print('left', left)
    top2=top
    top+=bottom*-1
    bottom2=bottom
    bottom=0
    right2=right
    right+=left*-1
    left2=left
    left=0
    box=grid_init(right,top)
    rect1[0]+=left2*-1
    rect1[2]+=left2*-1
    rect2[0]+=left2*-1
    rect2[2]+=left2*-1
    rect1[1]+=bottom2*-1
    rect1[3]+=bottom2*-1
    rect2[1]+=bottom2*-1
    rect2[3]+=bottom2*-1
    box=increment_grid(rect1[0],rect1[2],rect1[3],rect1[1],box)
    box=increment_grid(rect2[0],rect2[2],rect2[3],rect2[1],box)
    count=count_grid(2,box)
    print('bottom2', bottom2)
    print('left2',left2)
    if count[0]!=0 and count[1]!=0 and count[2]!=0 and count[3]!=0:
        left3=count[0]+left2
        right3=count[2]+left2
        bottom3=count[1]+bottom2
        top3=count[3]+bottom2
        otuple=(left3,bottom3,right3,top3)
    else:
        otuple=count

    return otuple

def main (inpt, fptr):
    #Read in both corners of Cubicle 1 and 2
    print(inpt)
    tups=inpt.split('\n')
    rect1=tups[0]
    rect1=rect1.split(' ')
    rect2=tups[1]
    rect2=rect2.split(' ')
    for i in range(len(rect1)):
        if rect1[i]=='':
            rect1.pop(i)
        if rect2[i]=='':
            rect2.pop(i)
            break
        rect1[i]=int(rect1[i])
        rect2[i]=int(rect2[i])
    #Write Cubicle 1's Area
    c1area=area(rect1)
    c2area=area(rect2)
    olap=overlap(rect1,rect2)
    fptr.write('Cubicle 1 Area: ')
    fptr.write(str(c1area))
    fptr.write('\nCubicle 2 Area: ')
    fptr.write(str(c2area))
    fptr.write('\nOverlap: ')
    fptr.write(str(olap))
    #Write Cubicle 2's Area
    
    #Write the overlapped rectangle's corners