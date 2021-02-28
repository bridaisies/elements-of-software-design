# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 

import math

def encrypt(strng):

    message_table = []
    L = len(strng)
    M = math.ceil(math.sqrt(L))
 
    length_string = 0
    for row in range(M):
 	list_one = []
 	for col in range(M):
 	    try:
 		list_one.append(strng[length_string])
 	    except IndexError:
 		list_one.append("*")
 	    length_string += 1
 	message_table.append(list_one)

    rotate_string = zip(*message_table[::-1])
 
    list_two = []
    for x in (rotate_string):
    	for y in (x):
 	    if y == "*":
 		continue
 	    else:
 		list_two.append(y)
 
    return ''.join(list_two)

def decrypt(strng):

    message_table = []
    L = len(strng)
    M = math.ceil(math.sqrt(L))
 
    length_string = 0
    for row in range(M):
 	list_one = []
 	for col in range(M):
 	    try:
 		list_one.append(strng[length_string])
 	    except IndexError:
 		list_one.append("*")
 	    length_string += 1
 	message_table.append(list_one)
 
    rotate_string = zip(*message_table[::-1])

    length_string = 0
    table_list2 = []
    for x in (rotate_string):
 	list_one = []
 	for y in (x):
 	    if y == "*":
 		list_one.append("*")
 	    else:
 		list_one.append(strng[length_string])
 		length_string += 1
 	table_list2.append(list_one)
 
    reverse_string = zip(*[i[::-1] for i in table_list2])
 
    list_two = []
    for x in (reverse_string):
 	for y in (x):
 	    if y == "*":
 		continue
 	    else:
 		list_two.append(y)
    return ''.join(list_two)

def main(strng):

# ensure strng is between 1 and 100 characters (inclusive)
    length = len(strng)
    if 1 <= length <= 100:
# return encrypted strng
	return encrypt(strng)

# make sure strng is between 1 and 100 characters
    length = len(strng)
    if 1 <= length <= 100:
# return the decrypted strng
        return decrypt(strng)


