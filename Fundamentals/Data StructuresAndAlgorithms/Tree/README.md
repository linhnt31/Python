#TREE

- Concept: The difference between a tree in nature and a tree in computer science is that a tree data structure has its root at the top and its leaves on the bottom.

![Image](http://interactivepython.org/runestone/static/pythonds/_images/biology.png)

- All of the children of one node are independent of the children of another node. 
- Each leaf node is unique

![Image](http://interactivepython.org/runestone/static/pythonds/_images/directory.png)


- Vocabulary and definitions: 
    1. ***Node***
        - __key__: __payload__
    
    2. ***Edge***
        - An __edge connects two nodes to show that there is a relationship between them__. Every node (except the root) is connected by exactly one incoming edge from another node. Each node may have several outgoing edges.

    3. ***Root***
        - The root of the tree is the only node in the tree that has no incoming edges.

    4. ***Path***
        - A path is an ordered list of nodes that are connected by edges.

    5. ***Children***
        - The set of nodes c that have incoming edges from the same node to are said to be the children of that node.

    6. ***Sibling***
        - Nodes in the tree that are children of the same parent are said to be siblings.

    7. ***Subtree***
        - A subtree is a set of nodes and edges comprised of a parent and all the descendants of that parent.

    8. ***Leaf Node***
        - A leaf node is a node that has no children. 

    9. ***Level***
        - The level of a node n is the number of edges on the path from the root node to n. 
        - The level of the root node is zero.

    10. ***Height***
        - The height of a tree is equal to the maximum level of any node in the tree.

    11. Definitions: 
        - If each node in the tree has a __maximum of two children__, we say that the tree is a __binary tree__.
        - One node of the tree is designated as the root node.

    ![Image](http://interactivepython.org/runestone/static/pythonds/_images/treedef1.png)


- __Base case for recursive algorithms are checking for a leaf node__