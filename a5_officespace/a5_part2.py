#Drew Hardie, DHH636
#Brionna Huynh, BPH637
# Input: bldg is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing
#        all the requested cubicles
# Output: a single integer denoting the area of the unallocated 
#         space in the office
global office
office=[]
def unallocated_space (bldg, cubicles):
    global office
    a=(bldg[2]-bldg[0])*(bldg[3]-bldg[1])
    UOA=count_grid2(office)
    unallocated=a-UOA[1]-UOA[2]
    return unallocated

# Input: bldg is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing
#        all the requested cubicles
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg, cubicles):
    global office
    UOA=count_grid2(office)
    contested=UOA[1]
    return contested

# Input: rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
#        cubicles is a list of tuples of 4 integers representing
#        all the requested cubicles
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (rect, cubicles):
    pass


def grid_init(w,h):
    grid = [[0 for i in range(w*2)] for j in range(h*2)]
    return grid

def increment_grid(name,l,r,b,t,grid):
    h=l
    k=t
    while k<b:
        h=l
        while h<r:
            if grid[k][h]==0:
                grid[k][h]=name
            else:
                grid[k][h]=1
            h+=1
        k+=1
    return grid

def count_grid(val,grid):
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==val:
                count+=1
    return count

def count_grid2(grid):
    count=0
    count2=0
    count3=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                count2+=1
            elif grid[i][j]==1:
                count3+=1
            else:
                count+=1
    UOA=[count2,count3,count]
    print('count',count)
    return UOA
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
    global office
    print(inpt)
    cubicles=[]
    vals=inpt.split('\n')
    vals[0]=vals[0].split(' ')
    i=2
    office=grid_init(int(vals[0][1]),int(vals[0][0]))
    while i<2+int(vals[1]):
        vals[i]=vals[i].split(' ')
        j=1
        while j<5:
            vals[i][j]=int(vals[i][j])
            j+=1
        cubicles.append(vals[i])
        office=increment_grid(vals[i][0],vals[i][1],vals[i][3],vals[i][4],vals[i][2],office)
        i+=1
    print(vals)
    print('cubicles:\n',cubicles)
    rect=(0,0,int(vals[0][1]),int(vals[0][0]))
    for i in range(len(office)):
        print(office[i])
    UOA=count_grid2(office)
    fptr.write('Total: ')
    fptr.write(str(int(vals[0][1])*int(vals[0][0])))
    fptr.write('\nUnallocated: ')
    fptr.write(str(unallocated_space(rect,cubicles)))
    fptr.write('\nContested: ')
    fptr.write(str(contested_space(rect,cubicles)))
    for i in range(len(cubicles)):
        cspace=count_grid(cubicles[i][0],office)
        fptr.write('\n')
        fptr.write(cubicles[i][0])
        fptr.write(': ')
        fptr.write(str(cspace))