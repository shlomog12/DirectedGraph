# OOP-EX3

## directed graph
![graph7](https://user-images.githubusercontent.com/73135976/104511874-09395480-55f6-11eb-810e-a4868cda55f9.jpg)


This project represents a data structure of a directed weighted graph. Which supports a large number of nodes.

### A. DiGraph:

A class that inherits from the GraphInterface class
And represents the weighted directed graph,
When data storage is done using
a. Dictionary of nodes
b. Dictionary of ribs
The use of a dictionary for data retention results in low and efficient complexity operations

The class implements functions for

1. Add vertices
2. Deleting vertices,
3. Adding edges
4. Delete edges
5. A function that receives a vertex and returns a dictionary of all its neighbors
6. A function that receives a vertex and returns a dictionary of all nodes that is their neighbor
7. In addition there are functions that return the
The number of vertices in the graph, the number of sides in the graph, the number of changes made to the graph


### B. GraphAlgo .:

A class inherited from GraphAlgoInterface
Which initializes the graph and executes algorithms of


1. Upload a graph from a json file.
2. Save a graph to a json file
3. A function that returns the weight of the lowest route between two nodes in the graph and a linked list of the nodes in the shortest route,
4. A function that receives a vertex and returns a list of all the vertices that are with it in the same Strongly Connected Component
5. A function that returns a list of all the Strongly Connected Components in the graph
6. A function that displays the graph in a graphical window using matplotlib
