import os
import re
import sys
import math

class Stack (object):
    def __init__ (self):
        self.stack = []
    
    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty (self):
        return len (self.stack) == 0

    # return the number of elements in the stack
    def size (self):
        return len (self.stack)


class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty (self):
        return len (self.queue) == 0

    # return the size of the queue
    def size (self):
        return len (self.queue)

class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
        return self.visited

    # determine the label of the vertex
    def get_label (self):
        return self.label

    # string representation of the vertex
    def __str__ (self):
        return str (self.label)

class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given the label get the index of a vertex
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        if (not self.has_vertex (label)):
            self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    def get_neighbors (self, vertexLabel):
        neighbors = []
        idx = self.get_index(vertexLabel)
        for i in range (len(self.adjMat[idx])):
            if (self.adjMat[idx][i] > 0):
                neighbors.append(self.Vertices[i])
        return neighbors

    # do a depth first search in a graph
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs (self, v):
        the_q = Queue()

        self.Vertices[v].visited = True
        the_q.enqueue(v)
        print(self.Vertices[v])

        while (not the_q.is_empty()):
            u = self.get_adj_unvisited_vertex(the_q.peek())
            if (u == -1):
                u = the_q.dequeue()
            else:
                self.Vertices[u].visited = True
                print(self.Vertices[u])
                the_q.enqueue(u)
        
        ln = len(self.Vertices)
        for x in range(ln):
            self.Vertices[x].visited = False

     # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def cycle_help (self, vert):
        # print(vert,"\n\n\n\n\n\n")
        vert.visited = True
        # stack.push(self.Vertices[v])
    
        for x in self.get_neighbors(vert):
            if(x.visited == False):
                if(self.cycle_help(x)):
                    return True
            elif(x.visited):
                return True
      
        # reset the flags
        ln = len(self.Vertices)
        for i in range (ln):
            (self.Vertices[i]).visited = False
      
        # pop the top element from the stack
        # stack.pop()
        return False
    
    def has_cycle (self):
        # s = Stack()
        # print("here")
        ln = len(self.Vertices)
        # print("length ",ln)
        for x in self.Vertices:
            if ((x.visited == False)):
                # print(x)
                if (self.cycle_help(x)):
                    # print(x)
                    return True
        return False
    
    def delete_vertex (self, vertexLabel):
        ln = len(self.adjMat)
        idx = self.get_index(vertexLabel)
        self.Vertices.pop(idx)
        for x in range (ln - 1):
            self.adjMat[x].pop(idx)
        self.adjMat.pop(idx)

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort (self):
        if not self.has_cycle():
            vert = []
            while (len(self.Vertices) > 0):
                c = 0
                for x in self.adjMat:
                    if (sum(self.adjMat[c]) == 0):
                        vert.insert(0, (self.Vertices[c]).label)
                        self.delete_vertex((self.Vertices[c]).label)
                    else:
                        c = c + 1
            return vert

def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # create a Graph object (add vertices and edges)
    theGraph = Graph()
    
    # Get num vertices
    num_vertices = int(input().strip())
    for vert in range(num_vertices):
        theGraph.add_vertex(input().strip())
     
    # Get num edges
    num_edges = int(input().strip())
    for edge in range(num_edges):
        edge_to_edge = input().strip()
        start = theGraph.get_index(edge_to_edge[0])
        finish = theGraph.get_index(edge_to_edge[-1])
        theGraph.add_directed_edge(start, finish)


    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if (not theGraph.has_cycle()):
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort\n")
        for i in range(len(vertex_list)): 
            print(str(vertex_list[i]))
            if i < len(vertex_list) - 1:
                print('\n')
    
    # fptr.close()

main()