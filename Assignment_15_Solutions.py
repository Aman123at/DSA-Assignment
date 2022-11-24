# Question 1 => Find if path exits
# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as 2D integer array edges, where each edge[i] = [ui, vi]
# denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at
# most one edge, and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from the vertex source to the vertex
# destination.
# Given edges and the integers n, source, and destination, return true if there is a valid path from source
# to destination, or false otherwise.



# Solution => There are few steps from which we can solve this problem.

# 1. Convert edges (matrix) to adjcency list
# 2. Use DFT/BFT to traverse to find path, I am going with DFT. Starting node is source node.
# 3. Got traversal list from DFT/BFT that started from source. 
# 4. If destination is present in traversal list then path exists otherwise no path exists.

from collections import defaultdict
class Solution(object):

    # function to convert matrix to adjcency list
    def convertToAdjList(self,matrix):
        G = defaultdict(list)

        for u,v in matrix:
            G[u].append(v)
            G[v].append(u)

        return G

    # function for depth first traversal
    def DFT(self,graph,visited,node,ans):
        
        if node not in visited:
            visited.add(node)
            ans.append(node)

            for item in graph[node]:
                if item not in visited:
                    
                    self.DFT(graph,visited,item,ans)



    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        # base case condition - if there is 0 or 1 node in edges then return True
        if n <= 1:
            return True

        # create visited set to track nodes while DFT
        visited = set()

        # initialize empty list to store traversal of DFT
        answer = []
        mygraph = self.convertToAdjList(edges)

        # calling DFT with source as starting node
        self.DFT(mygraph,visited,source,answer)

        # if destination is present in after DFT list then path exists
        if destination in answer:
            return True
        else:
            return False




# Question 2 => Invert Binary Tree

# Solution => Traverse through every node and swap left and right children.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # Base case condition
        if root is None:
            return

        # swap childrens of node
        if root :
            root.left,root.right = root.right,root.left

        # traverse left of root node
        self.invertTree(root.left)
        # traverse right of root node
        self.invertTree(root.right)

        return root





# TASK => Level Order Traversal of tree

# Solution => using BFT to print level order traversal of a tree.

# Level order traversal
from collections import deque

# defining Node class of a tree
class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None


# defining level order traversal function
def printLevelOrderTraversal(root):
    
    # base case condition
    if root is None:
        return

    # initializing queue
    q = deque()
    # append root value in queue
    q.append(root)
    # looping till queue is not empty
    while len(q)>0:
        # print the data
        print(str(q[0].data)+" ",end=' ')
        p = q.popleft()

        # append nodes in queue till left is not none
        if p.left is not None:
            q.append(p.left)
        # append nodes in queue till right is not none
        if p.right is not None:
            q.append(p.right)

      

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
printLevelOrderTraversal(root) # OUTPUT => 1 2 3 4 5 6 7 
        
        


