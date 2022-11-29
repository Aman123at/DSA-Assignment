# Question 1 => Implementation of Job Sequencing with Deadline using the heap-based data structure.

# Solution => There are few steps to solve this problem - 
# 1. sort the given array on the basis of deadline
# 2. create a blank list for max_heap and result
# 3. calculte available slot by comparing previous element deadline from current on every iteration, going with reverse iteration
# 4. push the current element in heap
# 5. if slot is available , pop element from heap (we will get max profit element), append this in result
# 6. After coming out of loop, sort the result array with least deadline element, that is final sequence of jobs with least deadline and max profit.


from heapq import heappush,heappop

# defining job scheduling function
def printJobScheduling(arr):
  n = len(arr)
  # sorting array on the basis of deadline, less comes first
  arr.sort(key = lambda x:x[1])

  result = []
  maxHeap = []

  # iterating in reverse order
  for i in range(n-1,-1,-1):
    # calculating avaliable slot
    if i==0:
      slot_available = arr[i][1]
    else:
      # taking difference between current elem deadline with prev
      slot_available = arr[i][1]-arr[i-1][1]

    # pushing current elem in heap , to create maxHeap , multiplying with -1 in profit
    heappush(maxHeap,(-1*arr[i][2],arr[i][1],arr[i][0]))

    # iterating till slot available and elem present in maxHeap
    while slot_available and maxHeap:
      # popping from heap to get max profit element
      profit,deadline,job_name = heappop(maxHeap)
      # decreasing value of slot available
      slot_available -= 1
      # adding this job name and deadline into result array
      result.append([job_name,deadline])

  # after adding relavent jobs in result array, sorting result in basis of deadline, lesser comes first
  result.sort(key = lambda x:x[1])

  # iterating throught the result to print the jobs in order
  for job in result:
    print(job[0],end=' ')


# Driver code 

arr = [['J1', 5, 55],
    ['J2', 2, 65],
    ['J3', 7, 75],
    ['J4', 3, 60],
    ['J5', 2, 70],
    ['J6', 1, 50],
    ['J7', 4, 85],
    ['J8', 5, 68],
    ['J9', 3, 45]]

printJobScheduling(arr) # output - J5 J2 J4 J7 J8 J3 







# Question 2 => Do the implementation of Huffman code according to the approach and pseudocode
# discussed in the live session. Consider the same example discussed in the live session
# only so that you can verify the results as well.
# a = 45, b = 15, c = 2, d = 30, e = 5, f = 3

# Solution => There are few steps to solve this problem - 
# 1. Create Node class to store data of individual node. That have frequency, character, huffcode,left and right properties
# 2. Push the tree node into heap with frequency and character value.( We have override "<" operator using __lt__ method in python. It helps the heap to decide which value need to fit in the property of minheap.We are going with frequency.)
# 3. Pop two elements from min heap called left and right, assign left to huff value 0 and right to 1. According to algo.
# 4. Push the new node into heap again that contains sum of these two (left and right) nodes frequency.
# 5. Define function printNodes that takes node object as argument.
# 6. Then add the huff value into newValue and keep on adding for left and right node of the current node.
# 7. If left or right node is not present for current node then print the character with newval value.

from heapq import heappush,heappop
# Define class node that contains frequency , character, left, right and huff properites.
class Node:
  def __init__(self,freq,char,left=None,right=None):
    self.freq = freq
    self.char = char
    self.left = left
    self.right = right
    self.huff = ''

  # overriding "<" operator helping heap to identify which value should be taken as fit for minheap.
  def __lt__(self,nxt):
    return self.freq<nxt.freq

# defining printNodes function
def printNodes(node,val=''):
  # adding previous huff code with new
  newVal = val + str(node.huff)
  # using recursion to traverse left and right of the current node
  if node.left:
    printNodes(node.left,newVal)

  if node.right:
    printNodes(node.right,newVal)

  # print the character with value if there is no left or child child of current node
  if (not node.left and not node.right):
    print(f"{node.char} -> {newVal}")
# Driver code
# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']


 
# frequency of characters
freq = [ 45, 15, 2, 30, 5, 3]

# initializing mean heap
nodes = []


# pushing all the characters and their frequencies into heap with node class
for x in range(len(chars)):
  heappush(nodes,Node(freq[x],chars[x]))


# iterating till heap is not empty or remains with one value
while len(nodes)>1:
   # popping out two minimum values from heap to make tree, according to algorithm.
  left = heappop(nodes)
  right = heappop(nodes)

  # assigning left huff code to 0 and right to 1
  left.huff = 0
  right.huff = 1

  # calculating and storing newNode value or taking sum of left and right frequencies and pushing into heap again
  newNode = Node(left.freq+right.freq,left.char+right.char,left,right)
  heappush(nodes,newNode)

printNodes(nodes[0]) 

# output :-
# a -> 0
# e -> 1000
# c -> 10010
# f -> 10011
# b -> 101
# d -> 11






















