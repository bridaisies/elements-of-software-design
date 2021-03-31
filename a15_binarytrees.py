import sys

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    def __init__ (self):
        self.root = None

  # insert data into the tree
    def insert (self, data):
        new_node = Node (data)

        if (self.root == None):
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            
            while (current != None):
                parent = current
                if (data < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            # found location now insert node
            if (data < parent.data):
                parent.lchild = new_node
            else:
                parent.rchild = new_node
                
    # Returns true if two binary trees are similar

    def is_similar (self, pNode):
        def sim_help ( n1, n2):
            if (n1 == None) and (n2 == None):
                return True

            if (n1 != None) and (n2 != None):
                return (n1.data == n2.data) and (sim_help(n1.lchild, n2.lchild)) and (sim_help(n1.rchild, n2.rchild))
            else:
                return False
        
        return sim_help(self.root, pNode.root)

    # Prints out all nodes at the given level
    def print_level (self, level):
        n_list = []
        def print_help ( n, l, num):
            if(n == None):
                return
            if(l == 1):
                num.append(n.data)
            elif(l > 1):
                print_help(n.lchild, l - 1, num)
                print_help(n.rchild, l - 1, num)
            return num
        print_help(self.root, level, n_list )
        return n_list

    # Returns the height of the tree
    def get_height (self): 
        def height_help (n):
            if (n == None):
                return 0
            else:
                return max(height_help(n.lchild), height_help(n.rchild)) + 1
        return height_help(self.root)

    # Returns the number of nodes in tree which is 
    # equivalent to 1 + number of nodes in the left 
    # subtree + number of nodes in the right subtree
    def num_nodes (self):
        def num_help (n):
            if (n != None):
                return (1 + num_help(n.lchild) + num_help(n.rchild))
            else:
                return 0
        return num_help(self.root)

def main():

    t1 = Tree()
    t2 = Tree()

    #in1 = "14 17 1" # input()
    #in2 =  "1 2 3"# input()
    #in2 = "14 17 1"

    in1 = input()
    in2 = input()

    for item in map(int,in1.split(" ")):
        t1.insert(item)

    for item in map(int,in2.split(" ")):
        t2.insert(item)

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout


    fptr.write("The Trees are similar: ")
    fptr.write(str(t1.is_similar(t2)))
    fptr.write("\n")
    fptr.write("\n")

    fptr.write("Levels of Tree 1: ")
    for i in range(t1.get_height()+1):
        for item in t1.print_level(i):
            fptr.write(str(item))
            fptr.write(" ")
        fptr.write("\n")

    fptr.write("\n")
    fptr.write("\n")

    fptr.write("Levels of Tree 2: ")
    for i in range(t2.get_height()+1):
        for item in t2.print_level(i):
            fptr.write(str(item))
            fptr.write(" ")
        fptr.write("\n")

    fptr.write("\n")
    fptr.write("\n")

    fptr.write("Height of Tree 1: "+str(t1.get_height()-1))
    fptr.write("\n")

    fptr.write("Nodes in Tree 1: "+str(t1.num_nodes()))
    fptr.write("\n")

    fptr.write("Height of Tree 2: "+str(t2.get_height()-1))
    fptr.write("\n")

    fptr.write("Nodes in Tree 2: "+str(t1.num_nodes()))
    fptr.write("\n")

if __name__ == "__main__":
    main()