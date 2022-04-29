# Graph

## Introduction


```python
```
The Graph is a package offering solutions to applied graph theory problems and visualizing tree graphs in an interactive way.
The package takes in two parameters: a list of edges and a list of corresponding edge lengths such as
    edges = ['AB', 'AC', 'BC', 'DE', 'EF', 'FG', 'DG']
    edge_lens = [2, 2, 2, 1, 1, 1, 1]
It can be used in daily application of graph theory topics such as finding the shortest path in a road or a network, checking if a network is connected or not and how reliable a local network is by checking how many cycles it contains.
It solves problems including: 
    1). Test user’s inputs. 
    2). Check connectivity of graph.  
    3). Find all unique cycles in a graph. 
    4). Find the shortest path between two input vertices. 
    5). Check if the input graph or any subgraph is a tree. 
If the graph is a tree. Problems that can be solved are: 
    1). Find optical roots that give the tree a minimum height. 
    2). Find given node’s parent, children, siblings, ascendents and descendants. 
    3). Find nodes at the same level. 
    4). Visualize the tree graph.
This is the structure of our package:
```
```

├── DS5010_Project
    ├── Graph
        ├── __init__.py
        ├── drivers.py
        ├── plot_drivers.py
        ├── graph.py
           ├── class Graph
              ├── __init__()
              ├── set_edges_and_lens()
              ├── set_vertices()
              ├── set_subgraphs() etc...
              ├── is_tree()
              ├── get_connected_subgraphs()
              ├── get_cycles() 
              ├── get_shortest_path()
           ├── class Tree(Graph)
              ├── __init__()
              ├── set_root() etc...
              ├── roots_with_min_height()
              ├── get_parent() etc...
              ├── get_same_level_nodes()
              ├── plot_tree()
    ├── README.md   
    ├── setup.py
    ├── test.py
    ├── LICENSE

## Install


```python
```
Use pip to install the package.
From source
```
```


```python
git clone https://github.com/HongyanYang825/DS5010_Project
cd DS5010_Project/
python setup.py install
```

## Usage


```python
```
1. Initialize Graph
```
```


```python
from Graph.graph import *

edges = ['AB', 'AC', 'BC', 'DE', 'EF', 'FG', 'DG']
edge_lens = [2, 2, 2, 1, 1, 1, 1]
graph = Graph(edges, edge_lens)
```


```python
```
2. Find all CONNECTED sub_graphs
```
```


```python
graph.get_connected_subgraphs()	# Should return two sets of sub_graphs
```


```python
```
3. Find all Cycles in a connected graph
```
```


```python
edges = ['AC', 'AD', 'BC', 'BD', 'BE', 'CE', 'EF', 'BF', 'AG']
edge_lens = [2, 2, 2, 2, 1, 2, 1, 1, 1]
graph.set_edges_and_lens(edges, edge_lens)
graph.get_cycles() # Should return a dictionary with key as the size of 
	       	   # cycle and value as a list of same-size cycles
```


```python
```
4. Find the Shortest Path between two nodes
```
```


```python
path_tuple = ("A", "F")
# Should return a list consisting all shortest paths, 
# and return the shortest length
graph.get_shortest_path(path_tuple)
```


```python
```
5. Check if a graph is a tree
```
```


```python
edges = ["AC", "CG", "CH", "AF", "BF", "DF", "DE"]
edge_lens = [1,2,3,4,5,6,7]
graph.set_edges_and_lens(edges, edge_lens)

graph.is_tree() # Should return True

tree = Tree(edges, edge_lens, "A") # Create a tree object
```


```python
```
6. Get a tree node's siblings
```
```


```python
tree.get_siblings("A") # Should return {'B', 'D'}
```


```python
```
7. Plot the tree graph
```
```


```python
tree.set_root("A")
tree.plot_tree()
![tree with root A](https://github.com/HongyanYang825/DS5010_Project/blob/main/Picture1.png)
```
