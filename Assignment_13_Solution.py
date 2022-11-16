# Question 1 => Implement inOrder, preOrder, and postOrder traversal algorithms using iteration.

# Defining node class to create nodes of the trees

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

# Iterative approach of preorder traversal
def preOrder(root):

    # defining base case
    if root is None:
        return
    
    # creating an stack to push nodes
    nodeStack = []
    # pushing root first
    nodeStack.append(root)

    # iteration till stack is not empty
    while len(nodeStack)>0:
        # popping the topmost node from stack and print its value
        popped = nodeStack.pop()
        print(str(popped.data)+" ",end=' ')

        # pushing left and right children of popped node into stack

        # pushing right children first into stack because left children should print first while popping for top

        if popped.right is not None:
            nodeStack.append(popped.right)

        # after pushing right child , push left child node
        if popped.left is not None:
            nodeStack.append(popped.left)


# Iterative approach of inorder traversal
def inOrder(root):
    # setting current is root of tree
    current = root
    # initializing empty stack
    stack = []
    
    while True:
        # Traverse till left most node of the current node
        if current is not None:
            stack.append(current)
            current = current.left

        # Backtracking from the empty subtree and visiting node again which is topmost of the stack
        elif len(stack)>0:
            current = stack.pop()
            print(str(current.data)+" ",end=' ')


            # now traversing the right subtree
            current = current.right


        else:
            break

# Iterative approach of postorder traversal

def postOrder(root):
    # checking for empty tree
    if root is None:
        return

    # initializing stack
    stack = []

    while True:
        while root is not None:
            # pushing roots two times
            
            stack.append(root)
            stack.append(root)
            # setting root as left child of the node
            root = root.left

            # checking if stack is empty 
            if (len(stack)==0):
                return

            # popping item from stack and set it as root
            root = stack.pop()


            # if lenght of stack is greater than zero and topmost element of stack is root element, make root as right child of the root node
            if (len(stack)>0 and stack[-1] == root):
                root = root.right

            else:
                print(str(root.data)+" ",end=' ')
                root = None


        
        

       

# Driver code

myroot = Node(10)
myroot.left = Node(20)
myroot.right = Node(30)
myroot.left.left = Node(40)
myroot.left.right = Node(50)
myroot.right.left = Node(60)
myroot.right.right = Node(70)


# print("PreOrder is ")
preOrder(myroot)  # 10 20 40 50 30 60 70
print("\n")


print("InOrder is ")
inOrder(myroot) # 40 20 50 10 60 30 70
print("\n")


print("PostOrder is ")
postOrder(myroot) # 40 50 20 60 70 30 10
print("\n")


# Time Complexity - O(n)
# Space Complexity - O(n) -> pushing every node to stack




# Question 2 => Implement the function in which given the Binary Tree Inorder and Preorder traversal, the result will give the postorder traversal of the tree.
# Inorder: DIABCEGHF
# Preorder: CDBIAEFGH


# defining search function , which takes list of nodes , element to search and lenght of list and return the index
def search(arr,item,n):
    for i in range(n):
        if(arr[i]==item):
            return i

    return -1


def postOrderFromPreAndInOrder(inOrd,preOrd,n):
    # first element of preOrder list is always root
    # search this root element in inOrder to find left and right subtrees

    root = search(inOrd,preOrd[0],n)
    

    # if left subtree is not empty then print left

    if (root != 0):
        postOrderFromPreAndInOrder(inOrd,preOrd[1:n],root)

    # if right subtree is not empty then print right

    if (root != n-1):
        postOrderFromPreAndInOrder(inOrd[root+1:n],preOrd[root+1:n],n-root-1)

    # print root
    print(str(preOrd[0])+" ",end=' ')

inorder = [10,20,40,50,30,60,70]
inorder = ["D","I","A","B","C","E","G","H","F"]
preorder = ["C","D","B","I","A","E","F","G","H"]

postOrderFromPreAndInOrder(inorder,preorder,len(inorder))


# Overall Time Complexity is - O(n^2)



        
