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
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

  def peek (self):
    return (self.queue[0])

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

    # get the index from the vertex label
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex object with a given label to the graph
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

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        from_ = self.get_index(fromVertexLabel)
        to_ = self.get_index(toVertexLabel)
        weight = self.adjMat[from_][to_]
        if (weight != 0):
            return weight
        else:
            return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors (self, vertexLabel):
        idx = self.get_index(vertexLabel)
        ln = len(self.Vertices[vertexLabel])
        n = []
        for x in range (ln):
            if (self.Vertices[vertexLabel][x] != 0):
                n.append(self.Vertices[vertexLabel][x])
        return n
        
    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices (self):
        ln = len(self.Vertices)
        for x in range (ln):
            print(self.Vertices[x])

    # do a depth first search in a graph starting at vertex v (index)
    def dfs (self, v):
        # create the Stack
        theStack = Stack()

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

    # do a breadth first search in a graph starting at vertex v (index)
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

    # delete an edge from the adjacency matrix
    # delete the edge if the graph is going from start to finish
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        from_ = self.get_index(fromVertexLabel)
        to_ = self.get_index(toVertexLabel)
        self.adjMat[from_][to_] = 0
        self.adjMat[to_][from_] = 0
        # pass

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        ln = len(self.adjMat)
        idx = self.get_index(vertexLabel)
        self.adjMat.pop(idx)

        self.Vertices.pop(idx)
        for x in range (ln-1):
            self.adjMat[x].pop(idx)
        
        # pass

def main():
    #try to use only print() statements, if not uncomment the line below
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')


    # create the Graph object
    cities = Graph()

    # read the number of vertices
    num_vertices = int(input())

    # read all the Vertices and add them the Graph
    for i in range (num_vertices):
        city = input()
        cities.add_vertex(city)

    # read the number of edges
    num_edges = int(input())

    # read the edges and add them to the adjacency matrix
    for i in range (num_edges):
        edge = input()
        edge = edge.split()
        start = int (edge[0])
        finish = int (edge[1])
        weight = int (edge[2])
        cities.add_directed_edge(start, finish  , weight)

    

    # read the starting vertex fro dfs and bfs
    start_vertex = input()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # test depth first search
    print("Depth First Search")
    cities.dfs(start_index)

    # test breadth first search
    print("\nBreadth First Search")
    cities.bfs(start_index)

    # test deletion of an edge
    print("\nDeletion of an edge")
    delete_edge = [z for z in input().split()]
    cities.delete_edge(delete_edge[0], delete_edge[1])

    # print the adjacency matrix
    print ("\nAdjacency Matrix")
    for i in range (num_vertices):
        for j in range (num_vertices):
            print (cities.adjMat[i][j], end = " ")
        print()

    # test deletion of a vertex12
    print("\nDeletion of a vertex")
    delete = input()
    cities.delete_vertex(delete)
    
    print("\nList of Vertices")
    cities.get_vertices()

    print("\nAdjacency Matrix")
    for i in range (num_vertices-1):
        for j in range (num_vertices-1):
            print (cities.adjMat[i][j], end = " ")
        print()
main()