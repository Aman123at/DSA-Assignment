# Question 1 => Given a singly linked list, give me the reversal of the linked list.
# For example 
# Input - 1 -> 2 -> 3 -> 4 -> 5
# Output - 5 -> 4 -> 3 -> 2 -> 1

# Defining node class
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


# Defining linkedlist class
class LinkedList:
  def __init__(self):
    self.head = None

    # Defining reverse Linked List function
  def reverseLL(self):
    # initialized previous pointer to none
    previous = None

    # current pointer is head
    current = self.head

    # traversing till node is not none
    while (current is not None):
        # taking next pointer is current data's next, initially its next element of head
      next = current.next
      # reversing the pointer, pointing to previous element
      current.next = previous
      # now previous becomes current value and ready for next iteration
      previous = current
      # current pointer becomes next from where we have reversed LL
      current = next

    # out off the loop updating head pointer to previous value
    self.head = previous



    # Defining function to add nodes in LL
  def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    # Defining function to print the LL
  def printLinkedList(self):
      temp = self.head
      while(temp):
          print (temp.data,end=" ")
          temp = temp.next


# initializing LL class creating object of class
llist = LinkedList()
llist.push(10)
llist.push(50)
llist.push(25)
llist.push(75)
llist.push(35)
llist.push(27)

print ("Linked List Before Reverse")
llist.printLinkedList()
llist.reverseLL()
print ("\nLinked List After Reverse")
llist.printLinkedList()



# Time complexity is O(n) , using one while loop for iteration and same for print LL















# Question 2 => Convert a singly linked list into a circular linked list

# Defining node class
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


# Defining linkedlist class
class LinkedList:
  def __init__(self):
    self.head = None

    # Defining circular function
  def circular(self):
    # taking pointer head which is head
    head = self.head
    # taking pointer start which is head
    start = self.head
    # traversing till start pointer is not null
    while (start.next is not None):
      start = start.next
    
    # start pointer is null then we will point its next value to head to form a loop
    start.next = head


  def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

  def printLinkedList(self):
    temp = self.head
   
    while(temp):
        print (temp.data,end=" ")
        temp = temp.next

  def printLinkedListCircular(self):
    head = self.head
    start = self.head
    while(head.next is not start):
        print (head.data,end=" ")
        head = head.next

    print(head.data)

llist = LinkedList()
llist.push(10)
llist.push(50)
llist.push(25)
llist.push(75)
llist.push(35)
llist.push(27)

print ("Linked List Before Circular")
llist.printLinkedList()
llist.circular()
print ("\nLinked List After Circular")
llist.printLinkedListCircular()


# Time complexity is O(n) , using one while loop for iteration and same for print LL













# Question 3 => Write a function to check whether a given linked list is palindrome or not

# Defining node class
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


# Defining linkedlist class
class LinkedList:
  def __init__(self):
    self.head = None

    # Defining ispalindrome function that returns true of false
  def ispalindrome(self):
    # initializing temporary pointer with head value
    temp = self.head

    # creating stack to store all elements of LL
    stack = []

    # initializing isPalindrome variable with true value
    isPalindrome = True


    # travesing LL till None value
    while (temp is not None):
        # pushing each values to stack
      stack.append(temp.data)
      temp = temp.next

    while (self.head is not None):

        # getting topmost element of stack
       topElemOfStack = stack.pop()


        # if topmost element is equal to head data then its palindrome
       if(self.head.data == topElemOfStack):
         isPalindrome = True

       else:
         isPalindrome = False
         break


       self.head = self.head.next

    return isPalindrome



  def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

  def printLinkedList(self):
    temp = self.head
   
    while(temp):
        print (temp.data,end=" ")
        temp = temp.next

  

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print ("Linked List")
llist.printLinkedList()
llist.ispalindrome()

# Time complexity is O(n) , using one while loop for iteration and same for print LL.








# Question 4 => Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to the head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s. 

# Defining node class
class Node:

	
	def __init__(self, data):
		self.data = data
		self.next = None

# Defining linkedlist class
class LinkedList:

	
    def __init__(self):
		self.head = None

	
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	
	def printLinkedList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next


    # Defining sortList function
	def sortList(self):

        # initializing 0s,1s,2s count with 0
        count = [0, 0, 0]
 
        temp = self.head

        # counting total number of 0s, 1s and 2s
        # count[0] will store total number of 0s
        # count[1] will store total number of 1s
        # count[2] will store total number of 2s
        while temp != None:
            count[temp.data]+=1
            temp = temp.next
 
        i = 0
        temp = self.head



        # if count[0] = n1, count[1] = n2 and count[2] = n3
        # start traversing list from head ,
        # fill the list with 0, till n1 > 0
        # fill the list with 1, till n2 > 0
        # fill the list with 2, till n3 > 0 
        while temp != None:
            if count[i] == 0:
                i+=1
            else:
                temp.data = i
                count[i]-=1
                temp = temp.next
        

        


# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
print ("Linked List Before Delete")
llist.printLinkedList()
llist.deleteNode(2)
print ("Linked List After Delete")
llist.printLinkedList()

# Time complexity is O(n) , using while loop for iteration and same for print LL.








# Question 5 => Given a linked list, detect the loop inside the linked list.


# Defining node class
class Node:

	
	def __init__(self, data):
		self.data = data
		self.next = None

# Defining linkedlist class
class LinkedList:

	
	def __init__(self):
		self.head = None

	
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	
	def printLinkedList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next


    # Defining detectLoop function which returns true or false
	def detectLoop(self):
		myset = set()
		temp = self.head
		while (temp):

			# if this node is already in the set then we have a loop
			if (temp in myset):
				return True

			# adding node to the set (hashmap)
			myset.add(temp)

			temp = temp.next

		return False


# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
print ("Linked List")
llist.printLinkedList()
llist.detectLoop()


# Time complexity is O(n) , using one while loop for iteration and same for print LL.







# Question 6 => Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Defining node class
class Node:

	
	def __init__(self, data):
		self.data = data
		self.next = None

# Defining linkedlist class
class LinkedList:

	
    def __init__(self):
		self.head = None

	
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	
	def printLinkedList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next


    # Defining deletenode function
	def deleteNode(self, n):
        # taking first pointer with head value
        first = self.head
        # taking second pointer with head value
        second = self.head

        # travesing till the nth node
        for i in range(n):
             
            # If count of nodes in the list is less than n
            if(second.next == None):
                 
                # if index is same as nth node then deleting the value
                if(i == n - 1):
                    self.head = self.head.next
                return self.head
            second = second.next
         
        while(second.next != None):
            second = second.next
            first = first.next
         
        first.next = first.next.next


# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
print ("Linked List Before Delete")
llist.printLinkedList()
llist.deleteNode(2)
print ("Linked List After Delete")
llist.printLinkedList()

# Time complexity is O(n) , using one while loop for iteration and same for print LL.







