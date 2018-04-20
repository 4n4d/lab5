# Lab 5: Graphs
# Lab 6: Graphs and BFS
In this assignment, you will implement your own graph datastructure and method for breadth-first search (BFS). This code will then be utilised in a small investigation of the diameter of some random graphs.

## 1. A graph class
Implement the class Graf in a module graf.py using the established graph representation you prefer.
The Graf class should have a reasonable interface hiding the implementation details. Two higher level methods are required:

* Graf.random(n,p) is a classmethod that takes two arguments and returns a random graph. The arguments are the number of vertices in the graph and the probability of creating an edge between any two vertices. A method like this is sometimes called a named constructor. 
* Graf.distance(start) takes one argument, a start vertex, and computes the distance to all other vertices, returned in a dictionary. The distance to v∈V is computed as the minimum number of edges in a path from start to v. If there is no path to  v, then that distance is reported as None. The distances must be computed using BFS.

### Requirements for Graf
The higher level methods in Graf should use the class interface as well as possible to make it easy to change the graph representation.

### Hints
You can use Python datastructures like lists and dictionaries, or Numpy matrices, for your graph representation.

### For grading
1. You should be able to discuss the time complexity of your BFS implementation. Is it O(|V|+|E|) as it should be?
2. Is your class interface hiding the implementation details?

## 2. A module for reading graphs in DOT format.

An old format for sharing graph data is called DOT (Wikipedia) and there are several Unix tools for visualising such graph files.
You will write a module called dotio.py that has a public function read_dot that understands a subset of the DOT format. Although DOT is fairly simple, there are several details that we do not need in this lab. The list of example files below defines the subset of DOT. In words: your code must parse undirected graphs without weights and labels. For example:
```Python
graph Small {
   a -- b;
   b -- c;
}  
```
is the graph with vertex set V={a, b, c} and edge set E={(a, b), (b, c)}.

### Requirements for read_dot
* The function read_dot will take a file handle as parameter and return a graph object. Note that by reading from a filehandle, you function will be able to parse data from stdin as well as from files.
* The exception Error should be raised if there is a problem with the input.
* You must construct at least three additional test files and argue for why they are meaningful to work with when testing your graph class and the dotio module.

### For grading
3. Show your testfiles and argue why they are useful.
4. Demonstrate that read_dot works on your testfiles and the example files (below).

## 3. Diameter investigation on random graphs
Write a Python program that investigates the mean diameter on connected random graphs, as implemented in Graf.random(). This class of random graphs is not guaranteed to be connected, but we can get around that by simply rejecting disconnected graphs when they are found. (Note: you do not need to explicitly implement such a test -- it is sufficient to discover this when computing the diameter.)

Your random graphs must have at least 100 vertices. The edge probability p should be varied between 0.1 and 0.9 in steps of 0.1. For each p, the mean diameter must be computed over at least 100 connected graphs. 

The program should produce a simple table to stdout and a plot (using Matplotlib) saved in a PDF file.

### For grading
5. What is the time complexity of your algorithm for computing the diameter of a graph?
6. You must be able to explain what your code and how it works.
7. Show a PDF plotting the mean diameter for different values of p.

## Example data
You can download sample data from here:
line.dot
circular.dot

