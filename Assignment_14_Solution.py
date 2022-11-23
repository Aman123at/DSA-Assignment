# Question 1 => Recover binary search tree
# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the
# tree were swapped by mistake. Recover the tree without changing its structure.

# Definition for a binary tree node.
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# defining function that takes root and 4 pointers as argument
def correctBstUtil(root,first,middle,last,prev):
    if root:
        # heading to very left of bst using recursion
        correctBstUtil(root.left,first,middle,last,prev)

        # after reaching to very left of BST checking if prev pointer's value is present and current root value is smaller then prev pointer value
        if (prev[0] and root.data < prev[0].data):
            # if first pointer's value is none
            if (not first[0]):
                # assigning prev pointer value to first pointer and middle pointer with root
                first[0] = prev[0]
                middle[0] = root

            # if first pointer value is present
            else:
                # assigning last pointer to current root
                last[0] = root
        # if prev pointer is none then assigning prev to root
        prev[0] = root

        # using recursion to move right side of tree and nodes
        correctBstUtil(root.right,first,middle,last,prev)

# Definin Correct BST function that accepts root as an argument
def correctBst(root):

    # starting with 4 pointers , all initialized with list of None values
    first = [None]
    middle = [None]
    last = [None]
    prev = [None]


    # calling correctbstutil function with all pointers and root itself
    correctBstUtil(root,first,middle,last,prev)

    # if there is any changes in actual binary tree then we will get pointer values filled with nodes
    # start swapping the nodes to get correct BST
    if (first[0] and last[0]):
        first[0].data,last[0].data = last[0].data,first[0].data

    elif (first[0] and middle[0]):
        first[0].data,middle[0].data = middle[0].data,first[0].data

    

# printing in order to show BST is correct if all the values is ascending sorted
def printInorder(root):
    if root:
        printInorder(root.left)
        
        print(str(root.data)+" ",end=' ')
        printInorder(root.right)


            

# root = Node(1)
# root.left = Node(3)
# root.left.right = Node(2)

root = Node(3)
root.left = Node(1)
root.right = Node(4)
root.right.left = Node(2)

print("inorder traversal of normal tree")
printInorder(root)
print("")


correctBst(root)

print("")
print("inorder for corrected BST")
printInorder(root)







# Question 2 => Lowest Common Ancestor of a Binary Search Tree


# defining function
def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Base case
        if root is None:
            return None

        # if both the node values are less than current root value , then LCA will be present at left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)

        # if both the node values are greater than current root value , then LCA will be present at right subtree
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)

        # if above condition fails then root is LCA
        return root

        