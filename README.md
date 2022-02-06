# Dijkstra Alghorithm

## Alghorithm description:

Dijkstra's algorithm is an algorithm that searches for the shortest path in the graph, from the start vertex to all other vertices. It works well in the case of problems with positive edge weighting (in the case of graphs with negative weight edges, we can use the Ford Bellman algorithm). The Dijkstra algorithm is used in computer networks for so-called routing. It consists in determining the best possible route and sending it a data packet in the computer network. Another application of the Dijkstra algorithm is to use it to determine the shortest possible route to a given town from the starting point. In such a situation, we treat roads as edges with different weights, and we treat intersections as graph nodes.

![How Dijkstra Alghorithm works](http://cstwiki.wtb.tue.nl/images/Dijkstra_EMC3_2019.gif)
---

## How to use it:
In order to use the above algorithm, input should be entered in the json file as the adjacency matrix, in which instead of entering "1" in a situation where the vertices are connected by an edge, enter the weight of this edge. For example, in a situation where vertex 0 is connected to vertex 2 with a directed edge weighing 5, then in the adjacency matrix "5" should be placed at position "[0] [2]". If there is no connection, enter "0".
