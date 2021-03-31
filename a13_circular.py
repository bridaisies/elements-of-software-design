import sys
import os
class Link(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class CircularList(object):
    # Constructor
    def __init__ ( self ):
        self.first = None

    # # Insert an element (value) in the list

    def insert (self, data):
        x = Link(data)
        if self.first is None:
            self.first = x
            x.next = x

        else:
            c = self.first
            temp = c.next
            while temp.next != c:
                temp = temp.next
            x.next = temp.next
            temp.next = x

    
    def find (self, data):
        c = self.first
        while (data != c.data):
            # print(data,c.data)
            c = c.next
        return c

    # Delete a link with a given data (value)
    def delete (self, data):
        if self.first.next == self.first:
            self.first = None
        else:
            c = self.first
            while c.next.data != data:
                c = c.next
            c.next = c.next.next
            if self.first.data == data:
                self.first = c.next



    # Delete the nth link starting from the Link start 
    # Return the next link from the deleted Link
    def delete_after (self, start, n,num_soldiers):
        x = self.find(start)
        # print(x.data,x.next.data,"here1")
        ans = []
        for j in range(num_soldiers - 1):
            for i in range(n - 1):
                x = x.next
                
            # print(str(x.data), end = ' ')
            ans.append(x.data)
            self.delete(x.data)
            x = x.next

        return ans
        
    # Return a string representation of a Circular List
    def __str__ (self):
        s = ''
        x = self.first

        while (self.first != x.next):
            s = s + str(x.data) + ' '
            x = x.next
        
        return s
def main(num_soldiers, starting_soldier, elim_num):
    #return a list with the order in which the soldiers were removed in
    ls = CircularList()
    for x in range(1, num_soldiers + 1):
        ls.insert(x)
    
    ans = ls.delete_after(starting_soldier, elim_num, num_soldiers)
    # print(ans)
    return ans
    
if __name__ == "__main__":
    fptr = open('out.txt', 'w+')
    inpt=[]
    inpt.append(input())
    inpt.append(input())
    inpt.append(input())
    result = main(int(inpt[0]), int(inpt[1]), int(inpt[2]))
    for num in result:
        fptr.write(str(num) + ' ')
    fptr.close()