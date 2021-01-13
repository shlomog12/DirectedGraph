This project represents a data structure of a undirectional weighted graph.
Which supports a large number of nodes (above 10 ^ 6, with an average rank of 10).

A. WGraph_DS:

  A class that represents the graph
  So that the realization is done by using one hashMap of nodes that represents the collection of vertices of the graph,
   And another hashMap for each key contains a hashMap that represents the neighbors' keys and the side weight.
  The use of a hashMap for data retention results in low and efficient complexity operations.
  The class implements functions for 
  1. adding vertices
  2. deleting vertices, 
  3. adding  sides
  4. deleting sides, 
  5.checking if a side between two nodes exists,
  6. and checking if a vertex exists in the graph.

B. WGraph_Algo:


  A class that initializes a graph and executes algorithms of
  1. copying,
  2. Check if the graph is linked,
  3. A function that returns the weight of the lowest trajectory between two nodes in a graph,
  4. A function that returns a linked list of the nodes of the trajectory with the lowest weight between two nodes in the graph,
  5. A function that saves the graph as a text file on your computer
  6. function that loads from the computer a text file that represents a graph and initializes the graph
