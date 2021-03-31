def merge_tuples (tuples_list):
    
    intervals = tuples_list
    # sort interval list by smallest lower end
    intervals.sort(key = lambda x: x[0])
    # create list for merged intervals
    merged_list = []
    
    for i in intervals:
        # add intervals into list
        if not merged_list:
            merged_list.append(i)
        else:
            # begin with smallest lower end of first interval, 
            # and compare with next interval
            # merging intervals if overlapping, moving onto the next if not
            j = merged_list.pop()
            if  i[0] <= j[1]:
                add_tuple_list = (j[0], max(j[1], i[1]))
                merged_list.append(add_tuple_list)
            else:
                merged_list.append(j)
                merged_list.append(i)

    return merged_list

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

def swap_elements(list, first, second):
    a = list[first]
    b = list[second]
    list[first] = b
    list[second] = a
    return

def sort_by_interval_size (tuples_list):

    interval_list = []
    for i in range(len(tuples_list)):
        size = tuples_list[i][1] - tuples_list[i][0]
        interval_list.append(size)
    j = 0
    while j < len(interval_list) + 1:
        i = 0
        while i + 1 < len(interval_list):
            if interval_list[i] > interval_list[i + 1]:
                swap_elements(interval_list, i, i + 1)
                swap_elements(tuples_list, i, i + 1)
            elif interval_list[i] == interval_list[i + 1]:
                if tuples_list[i][0] > tuples_list[i + 1][0]:
                    swap_elements(tuples_list, i, i + 1)
            i += 1
        j += 1
    return tuples_list

def main(tuples_list):
    #return smallest set of non-intersecting intervals sorted by interval size 
    merged = sort_by_interval_size(merge_tuples(tuples_list))
    
    return merged