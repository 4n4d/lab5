import numpy as np
import random
from collections import deque

class adjGraf:
    def __init__(self, adjlist = None):
        self.__graph = adjlist
        self.__elements = None
        if adjlist != None:
            self.__elements = len(adjlist)-1

            
    @classmethod
    def random(cls, n, p):
        # returns a random graph
        # n : number of vertices in the graph
        # p : probability of creating an edge between two vertices
        cls.__graph = [[] for x in range(n)]

        # add random edges
        for i in range(n-1):
            for j in range(i+1, n):
                if random.uniform(0,1)<=p:
                    cls.__graph[i].append(j)
                    cls.__graph[j].append(i)

        return adjGraf(cls.__graph)

    def distance(self, start):
        # time complexity is O(|v|+|e|) when implemented with
        # an adjacency list. for each vertex we loop through
        # all edges that belong to this edge (i.e. each edge is checked twice)

        # the class interface hides the implementation details...
        
        # no graph
        if self.__graph == None:
            raise KeyError

        # start is out of range
        if start < 0 or start > self.__elements:
            raise KeyError

        # list of elements to be searched
        # [color, distance, parent]
        # color: 0 = white, 1 = gray, 2 = black
        searchspace = [[0,self.__elements**2,None] for i in range(self.__elements+1)]
        searchspace[start][0]=1
        searchspace[start][1]=0

        # fix dictionary
        resultdict = {key: None for key in range(self.__elements+1)}
        resultdict[start] = 0
        
        # queue object
        Q = deque([start])

        # white queue not empty
        while len(Q)>0:
            # u is the current element to be checked
            u = Q.popleft()
            # l is the adjacancy-list for element u
            l = self.__graph[u]
            for i in range(len(l)): # element i is adjacent to u
                if searchspace[l[i]][0]==0: # if element i is WHITE
                    searchspace[l[i]][0]=1 # set it to GRAY
                    searchspace[l[i]][1]=searchspace[u][1]+1 # increase distance
                    searchspace[l[i]][2]=u # set parent to u

                    # update dictionary
                    resultdict[l[i]]= searchspace[l[i]][1]
                    Q.append(l[i]) # add it to search
            searchspace[u][0]=2 # set element u to black!

        return resultdict

    def addNode(self):
        # adds a node to the adjacency list
        # returns the node ID
        if self.__graph != None:
            self.__graph.append([])
            self.__elements = self.__elements + 1
        else:
            self.__graph = [[]]
            self.__elements = 0
        return self.__elements

    def addEdge(self, node1, node2):
        if node1 == node2: #we dont allow edges to and from the same node
            raise KeyError

        if (node1 < 0) or (node1 > self.__elements) or (node2 < 0) or (node2 > self.__elements): #check that the nodes are good
            raise KeyError

        # this is not a multigraph, hence we check if the edge already exists
        # if it does not exist, we add it!

        for i in range(len(self.__graph[node1])):
            if self.__graph[node1][i] == node2:
                # edge already exists, return 0 (edge already exists)
                return 0

        # edge did not exist for one of the elements (and thus not for the other either, add the new edge!

        self.__graph[node1].append(node2)
        self.__graph[node2].append(node1)

        return 1 # return 1 (edge added)
        
    def __str__(self):
        return str(self.__graph)
        
class Graf:
    def __init__(self, graphmatrix = None):
        self.__graph = graphmatrix
        if graphmatrix != None:
            self.__elements = graphmatrix.shape[0]-1
        else:
            self.__elements = None
            
    @classmethod
    def random(cls, n, p):
        # returns a random graph
        # n : number of vertices in the graph
        # p : probability of creating an edge between two vertices

        # generates an n by n  matrix with all elements 0
        cls.__graph = np.matrix([[0 for y in range(n)] for x in range(n) ])

        # add edges randomly
        for i in range(n):
            for j in range(i):
                if random.uniform(0,1)<=p:
                    cls.__graph[n-1-i,n-1-j] = 1
                    cls.__graph[n-1-j,n-1-i] = 1

        return Graf(cls.__graph)
    
    def distance(self, start):
        # check that this graph has elements
        if self.__elements == None:
            raise KeyError

        # check that "start" is a proper element in the graph
        if (start < 0) or (start > self.__elements):
            raise KeyError

        # Breadth first search (BFS)
        # given a start vertex s, BFS explores all edges such that it discovers
        # every vertex that is reachable from s.
        # it computes the distance from s to each reachable vertex
        # it also produces a "breadth-first tree" with root s that contains
        # all reachable vertices.
        # For any vertex v that is reachable from s, the simple path in the
        # breadth first tree correspons to the shortest path from s to v in the graph.

        # it discovers all vertices that are k steps from s before any vertex that is
        # k+1 steps from s.

        # to keep track: it colors all vertices WHITE, GRAY or BLACK
        # all vertices are WHITE in the beginning
        # the first time a vertex is discovered it becomes non-white.
        # GRAY or BLACK?
        # If (u,v) is an edge in E, and u is BLACK, then v is either GRAY or BLACK
        # (i.e. all vertices adjacent to a black vertex have all been discovered)
        # GRAY vertices may have some white vertex adjacent, they are the
        # frontier between discovered and undiscovered.


        # this implementation is O(v^2) as
        # for each vertex we check all other vertices
        # an adjacency-list would only check those which are adjacent (i.e "e")
        
        # list of elements to be searched
        # [color, distance, parent]
        # color: 0 = white, 1 = gray, 2 = black
        searchspace = [[0,self.__elements**2,None] for i in range(self.__elements+1)]
        searchspace[start][0]=1
        searchspace[start][1]=0

        # queue object
        Q = deque([start])

        # white queue not empty
        while len(Q)>0:
            # u is the current element to be checked
            u = Q.popleft()
            # l is the adjacancy-list for element u, access elements by l[0,i]
            l = self.__graph[u,]
            for i in range(self.__elements+1):
                if l[0,i] != 0:
                    # element i is adjacent to l
                    if searchspace[i][0]==0:
                        # if element i is WHITE
                        searchspace[i][0]=1 # set it to GRAY
                        searchspace[i][1]=searchspace[u][1]+1 # increase distance
                        searchspace[i][2]=u # set parent to u
                        Q.append(i) # add it to search
            searchspace[u][0]=2 # set element u to black!
        #print searchspace
        resultdict = dict()
        for i in range(self.__elements+1):
            if searchspace[i][1] == self.__elements**2:
                resultdict[i]=None
            else:
                resultdict[i]=searchspace[i][1]

        return resultdict
        
    def __str__(self):
        return str(self.__graph)
    
def main():
    #g = Graf()
    #g = Graf.random(10,0.3)
    #t = Graf.random(5,0.5)
    
    #print g
    #print t
    #print t.distance(3)

    adjG = adjGraf.random(5,0.3)
    print adjG
    print adjG.distance(0)
    t = adjG.addNode()
    adjG.addEdge(0,t)
    print adjG
    print adjG.distance(0)
if __name__ == '__main__':
    main()
