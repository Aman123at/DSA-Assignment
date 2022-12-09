# Question 1 => 0-1 Kanpsack Problem: Display the names of the objects which are contributing to the maximum profit.

# Solution =>

# Task - To print the string of longest common subsequence
def lcs(X , Y):
  

	# find the length of the strings
	# m - number of rows
	# n - number of columns
  m = len(X)
  n = len(Y)
  
  

	# declaring the array for storing the dp values
  LCS_table = [[None]*(n+1) for i in range(m+1)]

  for i in range(m+1):
    for j in range(n+1):
      ## base condition
      if i == 0 or j == 0 :
        LCS_table[i][j] = 0
      ## if there is a match of characters in string1 and string2
      elif X[i-1] == Y[j-1]:
        
        LCS_table[i][j] = 1 + LCS_table[i-1][j-1]
        

      else:
      ## if there is no match of characters in string1 and string2
        LCS_table[i][j] = max(LCS_table[i-1][j] , LCS_table[i][j-1])

  # initializing final string
  lcstr = ""
  # taking pointers of string1 and string2
  ps_1 = m
  ps_2 = n
  # iterating till string1 and string2 pointers are greater than 0
  while ps_1>0 and ps_2>0:
    # if we found a match of characters then concat in lcstr variable and decrease both pointers to move further
    if X[ps_1-1]==Y[ps_2-1]:
      lcstr+=str(X[ps_1-1])
      ps_1-=1
      ps_2-=1

    # if there is no match then take maximum of previous two values and move upwords
    elif LCS_table[ps_1-1][ps_2]>LCS_table[ps_1][ps_2-1]:
      ps_1-=1

    # moving to left in matrix to search for source of the current value
    else:
      ps_2-=1

  # return final string length and final string, reverse final string because we are iterating backward but we have to show values from start of the string
  return LCS_table[m][n],lcstr[::-1]


# Driver code
# string1 = "bd"
# string2 = "abcd"
string2 = "AGGTAB"
string1 = "GXTXAYB"
## output string - "GTAB"
## function calling
length,string = lcs(string1,string2)
print ("Length of LCS is ", length )  # Output - 4
print("LCS final string is ->",string)  # Output - GTAB










# Question 2 => Sum of subset problem : input : {3,34,4,15,5,2}, sum = 9
# output : True


# Solution => I will go with all these below approaches one by one
# approach 1 - Bruteforce approach
# approach 2 - Memoization approach
# approach 3 - Tabulation approach




# approach 1 - Bruteforce approach
def isSubSet(sets,n,sum):
  # base case conditions
  # if given sum is 0 then return True
  if sum==0:
    return True

  # if set is empty then return false
  if n==0:
    return False

  # if value from set is greater then sum value, then we skip that value and move to next element
  if (sets[n-1] >sum):
    return isSubSet(sets,n-1,sum)

  # we are including or excluding the value according to recursive tree
  return isSubSet(sets,n-1,sum) or isSubSet(sets,n-1,sum-sets[n-1])


# Driver code
# arr = [3,4,5,2]
arr = [3,34,4,12,5,2]
n = len(arr)
# sum = 6
sum = 9
isSubSet(arr,n,sum)


# approach 2 - Memoization approach
def isSubSet(sets,n,sum,memo):
  # base case conditions
  # if given sum is 0 then return True
  if sum==0:
    return True

  # if set is empty then return false
  if n==0:
    return False

  # if value is already there in this position at memoized table, then return that value
  if memo[n-1][sum]!=-1:
    return memo[n-1][sum]

  # if value from set is greater then sum value, then we skip that value and move to next element and store the result in memoized table
  if (sets[n-1] >sum):
    memo[n-1][sum] = isSubSet(sets,n-1,sum,memo)
    return memo[n-1][sum]
  else:
    # we are including or excluding the value according to recursive tree and storing result in memoized table
    memo[n-1][sum] = isSubSet(sets,n-1,sum,memo)
    return memo[n-1][sum] or isSubSet(sets,n-1,sum-sets[n-1],memo)


# Driver code
# arr = [3,4,5,2]
arr = [3,34,4,12,5,2]
n = len(arr)
# sum = 6
sum = 9
memo = [[-1 for i in range(sum+1)] for j in range(n+1)]
print(isSubSet(arr,n,sum,memo))





# approach 3 - Tabulation approach
def isSumSub(arr,n,sum):
  # initializing subset table with false value
  subset = ([[False for i in range(sum+1)] for i in range(n+1)])

  # for sum 0 all values from set to be true
  for i in range(n+1):
    subset[i][0] = True

  # for all other sum rather than 0 will be false in starting
  for i in range(1,sum+1):
    subset[0][i] = False


  for i in range(1,n+1):
    for j in range(1,sum+1):

      # if sum is less than actual value in table, copy the previous row value
      if j<arr[i-1]:
        subset[i][j] = subset[i-1][j]

      # if actual value and sum value matches or sum is greater than actual value, take either above row value or first value when sum becomes 0 and so on
      if j>=arr[i-1]:
        subset[i][j] = (subset[i-1][j] or subset[i-1][j-arr[i-1]])

  # return the last value from table that will be final answer
  return subset[n][sum]

# Driver code

# arr = [3,4,5,2]
arr = [3,34,4,12,5,2]
n = len(arr)
# sum = 6
sum = 9
isSumSub(arr,n,sum)












