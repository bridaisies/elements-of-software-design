def sortboxes(boxes):
    for i in range(len(boxes)):
        mid=sum(boxes[i])-min(boxes[i])-max(boxes[i])
        low=min(boxes[i])
        high=max(boxes[i])
        boxes[i][0]=low
        boxes[i][1]=mid
        boxes[i][2]=high
# Input: box_list is a list of boxes that have already been sorted
#        sub_set is a list that is the current subset of boxes
#        idx is an index in the list box_list
#        all_box_subsets is a 3-D list that has all the subset of boxes
# Output: generates all subsets of boxes and stores them in all_box_subsets
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
    ln=len(box_list)
    if idx==ln:
        all_box_subsets.append(sub_set)
        return
    else:
        sub_set2=sub_set[:]
        sub_set.append(box_list[idx])
        sub_sets_boxes(box_list, sub_set, idx+1, all_box_subsets)
        sub_sets_boxes(box_list, sub_set2, idx+1, all_box_subsets)
    
def clean(lst):
    i=1
    while i<len(lst):
        if lst[i][0]==lst[i-1][0]:
            if lst[i][1]<lst[i-1][1]:
                a=lst[i]
                lst[i]=lst[i-1]
                lst[i-1]=a
            elif lst[i][1]==lst[i-1][1]:
                if lst[i][2]<lst[i-1][2]:
                    a=lst[i]
                    lst[i]=lst[i-1]
                    lst[i-1]=a
        i+=1

def main(boxes):
    sortboxes(boxes)
    boxes.sort(key = lambda x: x[0])
    j=0
    clean(boxes)
    clean(boxes)
    box_list=[]
    empty_list=[]
    sub_sets_boxes(boxes,empty_list,0,box_list)
    return box_list