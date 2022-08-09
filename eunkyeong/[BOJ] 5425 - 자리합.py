# Given two integers a and b. The task is to
# print sum of all the digits appearing in the
# integers between a and b
 
# Memoization for the state results
dp = [[[-1 for i in range(2)] for j in range(180)]for k in range(20)]
 
# Stores the digits in x in a list digit
def getDigits(x, digit):
    while x:
        digit.append(x % 10)
        x //= 10
         
# Return sum of digits from 1 to integer in digit list
def digitSum(index, sumof, tight, digit):
   
    # Base case
    if index == -1:
        return sumof
       
        # Checking if already calculated this state
    if dp[index][sumof][tight] != -1 and tight != 1:
        return dp[index][sumof][tight]
    ret = 0
     
    # Calculating range value
    k = digit[index] if tight else 9
    for i in range(0, k+1):
       
        # Calculating newTight value for nextstate
        newTight = tight if digit[index] == i else 0
         
        # Fetching answer from next state
        ret += digitSum(index-1, sumof+i, newTight, digit)
    if not tight:
        dp[index][sumof][tight] = ret
    return ret
   
# Returns sum of digits in numbers from a to b
def rangeDigitSum(a, b):
    digitA = []
     
    # Storing digits of a-1 in digitA
    getDigits(a-1, digitA)
     
    # Finding sum of digits from 1 to "a-1" which is passed as digitA
    ans1 = digitSum(len(digitA)-1, 0, 1, digitA)
    digitB = []
     
    # Storing digits of b in digitB
    getDigits(b, digitB)
     
    # Finding sum of digits from 1 to "b" which is passed as digitB
    ans2 = digitSum(len(digitB)-1, 0, 1, digitB)
    return ans2-ans1
 
 
a, b = 123, 1024
print("digit sum for given range: ", rangeDigitSum(a, b))
 
# This code is contributed by rupasriachanta421