Find Euler Tour
===
Given an edge list representation of a proper non-directional graph
which either has all nodes of even degrees greater than zero or two
nodes of odd degree, this program finds an Euler tour (defined as
traversing every edge only once) for the graph.

This implementation uses a recursive version of Hierholzer's algorithm of 
cycle finding followed by edge removal. By using recursion and a persistant 
stack, the need for inserting into doubly-linked list can be eliminated.

There is currently no precondition checking implemented: a proper edge
list for input is assumed.

Feynman Liang   
<feynman.liang@gmail.com>

Licensed under the MIT License
