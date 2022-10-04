# Question : 1 => Given an integer array nums of length n and an integer target,
#  find three integers in nums such that the sum is closest to the target.

# For example:arr = [-1, 2, 1, -4],
# target = 1 Output: 2


# APPROACH - 1 => BRUTEFORCE APPROACH

# Defining a function that accepts array and target
def findTarget1(arr,target):
    # making closest sum as infinity
  closest = float('inf')
    # initial output is 0
  output = 0
    # applying 3 loops to find the sum
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      for k in range(j+1,len(arr)):
        x = arr[i]+arr[j]+arr[k]
        # if the current sum is less then closest values then update the closest
        if(x<closest and x>=0 ):
          closest = target-x
          output = x
   
  return output


# Driver code
array1 = [-1,2,1,-4]
target = 1
result = findTarget1(array1,target)
print("Closest sum to target is : ",result)

#  Time complexity of this approach is O(n^3)


# APPROACH - 1 => THREE POINTER APPROACH


# Defining a function that accepts array and target
def findTarget2(arr,target):
    # sort the array first
  arr.sort()
    # making closest sum as infinity
  closest = float('inf')
    # initial output is 0
  output = 0
    # first loop to travese till last element of array
  for i in range(len(arr)-1):
    # initializing three pointers 
    first = i
    second = i+1
    last = len(arr)-1
    # while loop till second and last pointer crosses each other
    while(second<last):
      x = arr[first] + arr[second]+arr[last]
      # if the current sum is less then closest values then update the closest
      if abs(target - x) < closest:
        closest = abs(target - x)
        output = x


        # if sum is less then the target then move second pointer to next index
      if x < target:
          second +=1  

        # if sum is greater then the target then move last pointer to previous index     
      elif x > target:
          last -=1
      else: return target
     
      

  return output


# Driver code
array1 = [-1,2,1,-4]
target = 1
result = findTarget2(array1,target)
print("Closest sum to target is : ",result)

#  Time complexity of this approach is O(n^2)







# Question : 2 => Given three points, check whether they lie on a straight (collinear) or not.
# For example: Input- [(1,1), (1,6), (0,9)] Output- No
# Input- [(1,1), (1,4), (1,5)] Output- Yes

# APPROACH - 1 => POINTS ARE COLLINEAR IF CREATED AREA BY THESE POINTS ARE 0
# FORMULA - 1/2 * [x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)]

# Defining function taking points as arguments

def isCollinear(x1, y1, x2, y2, x3, y3):
    # calculating area of triangle made by these points
    area =  x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    # if area is 0 then these points are collinear
    if (area == 0):
        print("Yes")
    else:
        print("No")

# Driver code
input = [(1,1), (1,6), (0,9)]
x1 = input[0][0]
y1 = input[0][1]
x2 = input[1][0]
y2 = input[1][1]
x3 = input[2][0]
y3 = input[2][1]
isCollinear(x1, y1, x2, y2, x3, y3)

# Time complexity of this approach is O(1)



# APPROACH - 2 => DISTANCE BETWEEN FIRST AND LAST POINT IS EQUAL TO SUM OF DISTANCE OF FIRST TO MIDDLE AND
# MIDDLE TO LAST POINT

# DISTANCE FORMULA = ROOT(SQUARE(X2-X1)+SQUARE(Y2-Y1))
# SUPPOSE FIRST POINT IS P , SECOND IS Q AND LAST IS R
# IF PR = PQ+QR , THEN GIVEN POINTS ARE COLLINEAR

# Defining function
import math
def isCollinear(x1, y1, x2, y2, x3, y3):
    PQ = math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
    QR = math.sqrt(((x3-x2)*(x3-x2))+((y3-y2)*(y3-y2)))
    PR = math.sqrt(((x3-x1)*(x3-x1))+((y3-y1)*(y3-y1)))
    if(PQ+QR == PR):
        print("Yes")
    else:
        print("No")

# Driver code
input = [(1,1), (1,6), (0,9)]
x1 = input[0][0]
y1 = input[0][1]
x2 = input[1][0]
y2 = input[1][1]
x3 = input[2][0]
y3 = input[2][1]
isCollinear(x1, y1, x2, y2, x3, y3)

# Time complexity of this approach is O(1)



# APPROACH - 3 => SLOPE OF ANY PAIR OF POINTS MUST BE SAME AS OTHER PAIR
# FORMULA - (y3 - y2)/(x3 - x2) = (y2 - y1)/(x2 - x1)
# (y3 - y2)(x2 - x1) = (y2 - y1)(x3 - x2) 
def isCollinear(x1, y1, x2, y2, x3, y3):
    if ((y3 - y2)*(x2 - x1) == (y2 - y1)*(x3 - x2)):
        print ("Yes")
    else:
        print ("No")

# Driver code
input = [(1,1), (1,6), (0,9)]
x1 = input[0][0]
y1 = input[0][1]
x2 = input[1][0]
y2 = input[1][1]
x3 = input[2][0]
y3 = input[2][1]
isCollinear(x1, y1, x2, y2, x3, y3)

# Time complexity of this approach is O(1)










# Question : 3 => An e-commerce site tracks the purchases made each day. The product that is purchased
# the most one day is the featured product for the following day. If there is a tie for the product
# purchased most frequently, those product names are ordered alphabetically ascending and
# the last name in the list is chosen

# ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
# 'greenPants', 'greenPants', 'greenPants']

# 'yellowShirt' - 2
# 'redHat' - 2
# 'blackShirt' - 2
# 'bluePants' - 1
# 'greenPants' - 3
# 'pinkHat' - 1
# Output - greenPants


# APPROACH - 1 => BRUTEFORCE        

# importing collection module to count products
from collections import Counter
# Defining the function
def mostFrequentProduct(productArr):
  # sorting array

  productArr.sort()
  # making dictionary of product counts

  productDictWithNumbers=dict(Counter(productArr))
  # initializing maximum value with 0
  maximum=0
  # final Product list
  product_list=[]
  # iterating through all the product list
  for i in productDictWithNumbers:
    # taking maximum with first element of dictionary (elements already sorted)
    if maximum < productDictWithNumbers[i]:
      maximum=productDictWithNumbers[i]

  # if maximum value is equal to dictionary items then add into product list.
  for key, value in productDictWithNumbers.items():
    if maximum == value:
      product_list.append(key)
  
  # return last value of this product list.
  return product_list[-1]


# Driver code
array = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt', 'greenPants', 'greenPants', 'greenPants']
result = mostFrequentProduct(array)
print(result)













# Question : 4 => An almost sorted array is given to us and the task is to sort that array completely. 
# Then, which sorting algorithm would you prefer and why?



# Answer : We can use Insertion Sort in almost already sorted array. 
# Because we have to do less swaps between elements. That will reduce time complexity.
# Time complexity = no. of comparisions + no. of swaps