def sortboxes(boxes):
    for i in range(len(boxes)):
        mid = sum(boxes[i]) - min(boxes[i]) - max(boxes[i])
        low = min(boxes[i])
        high = max(boxes[i])
        boxes[i][0] = low
        boxes[i][1] = mid
        boxes[i][2] = high
        
# Input: box_list is a list of boxes that have already been sorted
#        sub_set is a list that is the current subset of boxes
#        idx is an index in the list box_list
#        all_box_subsets is a 3-D list that has all the subset of boxes
# Output: generates all subsets of boxes and stores them in all_box_subsets
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
    ln = len(box_list)
    if idx == ln:
        all_box_subsets.append(sub_set)
        return
    else:
        sub_set2 = sub_set[:]
        sub_set.append(box_list[idx])
        sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
        sub_sets_boxes(box_list, sub_set2, idx + 1, all_box_subsets)
    
def clean(lst):
    i = 1
    while i < len(lst):
        if lst[i][0] == lst[i - 1][0]:
            if lst[i][1] < lst[i - 1][1]:
                a = lst[i]
                lst[i] = lst[i - 1]
                lst[i - 1] = a
            elif lst[i][1] == lst[i - 1][1]:
                if lst[i][2] < lst[i - 1][2]:
                    a = lst[i]
                    lst[i] = lst[i - 1]
                    lst[i - 1] = a
        i += 1
# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets(all_box_subsets,largest_size, all_nesting_boxes):
    anb = all_nesting_boxes
    largest_size = 0
    for i in all_box_subsets:
        length = len(i)
        if (largest_size > length):
            continue
        x = 1
        for j in range(length - 1):
            if not does_fit(i[j], i[j + 1]):
                x = 0
        if (x == 1):
            if (largest_size < length):
                largest_size = length
                anb.clear()
                anb.append(i)
            elif (largest_size == length):
                anb.append(i)
              
# Input: box1 and box2 are the dimensions of two boxes
# Output: returns True if box1 fits inside box2
def does_fit (box1, box2):
    return ((box1[0] < box2[0]) and (box1[1] < box2[1]) and( box1[2] < box2[2]))

    #Sort each box by dimension, then sort boxes by the first dimension
    #return all largest nesting subsets
def main(boxes):
    sortboxes(boxes)
    boxes.sort(key = lambda x: x[0])
    clean(boxes)
    clean(boxes)
    box_list = []
    sub_set = []
    sub_sets_boxes (boxes, sub_set, 0, box_list)
    largest_size = 0
    all_nesting_boxes = []
    largest_nesting_subsets(box_list, 0, all_nesting_boxes)
    return all_nesting_boxes