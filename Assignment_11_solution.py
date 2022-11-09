# Question 1 => Implement a LIFO stack using only two queues. The implemented stack should support all the
# functions of a usual stack (push, pop, top, empty)



# importing deque from collections module
from collections import deque

# defining MyStack class
class MyStack:

    # initializing stack using deque
    def __init__(self):
        self.container = deque()


    # pushing elements in stack
    def push(self, x):
       return self.container.append(x)
        

    # returning and deleting topmost element from stack
    def pop(self):
        return self.container.pop()


    # returning topmost element from stack
    def top(self):
        return self.container[-1]
        


    # checking if stack empty
    def empty(self):
        return len(self.container) == 0



# Driver code


# initializing object of class to access functions of stack
myStack = MyStack()

# pushing the values into stack
myStack.push(1)
myStack.push(2)


# peeking the topmost value from stack
myStack.top() # return 2

# deleting topmost value from stack
myStack.pop() # return 2


# checking stack is empty or not
myStack.empty() # return False


# Time complexity -> For each operations time complexity is O(1) , using deque
# if we use list then TC will be O(n)








# Question 2 => Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should
# support a normal queue's functions (push, peek, pop, and empty).




# importing deque from collections module
from collections import deque

# defining MyStack class
class MyQueue:

    # initializing queue using deque
    def __init__(self):
        self.container = deque()


    # pushing elements in queue
    def push(self, x):
       return self.container.appendleft(x)
        

    # returning and deleting very first element from queue
    def pop(self):
        return self.container.pop()


    # returning first element from queue
    def peek(self):
        return self.container[-1]
        


    # checking if queue empty
    def empty(self):
        return len(self.container) == 0



# Driver code


myQueue = MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2] (leftmost in front of the queue)
myQueue.peek() # return 1
myQueue.pop() # return 1, the queue is [2]
myQueue.empty() # return false


# Time complexity -> For each operations time complexity is O(1) , using deque
# if we use list then TC will be O(n)

