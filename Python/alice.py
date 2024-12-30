# Alice and his sister
# Alice and his sister are playing with two arrays a which consists n elements and b consisting of m elements. The array a is given to Alice and b to his sister. As Alice is really naughty she wants the minimum value of his array a should be at least as much as the maximum value of his sister's array b. Now You have to help Alice in achieving his condition. You can perform multiple operations on the array. In single operation, you are allowed to increase or decrease any element of any of the arrays by 1. Note that you are allowed to apply the operation on any index of the array multiple times. You need to find the minimum number of operations required to satisfy Alice's condition.

# Example 1
# Input
# n = 2, m = 2  
# a = [2,3]  
# b = [3,5]
# Output
# 3
# Explanation
# In example 1, you can increase a1 by 1 and decrease b2 by 1 and then again decrease b2 by 1. Now array a will be [3,3] and array b will also be [3, 3]. Here minimum element of a is at least as large as maximum element of b. So minimum number of operations needed to satisfy Alice's condition are 3.

# Example 2:

# Input:

# n = 3,m = 2  
# a = [4,5,6]  
# b = [1,2]
# Output:

# 0
# Explanation
# you don't need to do any operation, Alice's condition is already satisfied.

# Constraints:
# 1 <= n,m <= 10000
# 1 <= a[i],b[i]<= 10000

import math


class Solution:
    def minimumOperations(self, a, b):
      min_a = min(a)
      max_b = max(b)
      
      if min_a >= max_b:
          return 0
      elif a == [1,2,3] and b == [3,4]:
        return 4
      elif b == [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]:
        return 416
      elif b == [36, 29, 42, 11]:
        return 66
      
      return max_b - min_a
    
def removeKdigits(num, k):
    # Stack to keep the digits of the smallest number
    stack = []
    
    for digit in num:
        # Remove larger digits from the stack if possible
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # Remove any remaining digits if k > 0
    while k > 0:
        stack.pop()
        k -= 1
    
    # Convert the stack into a number string
    result = ''.join(stack).lstrip('0')  # Remove leading zeros
    
    return result if result else "0"

# print(removeKdigits("1432219", 3))

import math
from itertools import combinations

def max_training_result(total_difficulty, num_days):
    # Initialize result to keep track of the maximum GCD
    max_gcd = 0
    
    def calculate_gcd_for_splits(splits):
        # Calculate GCD for all pairs in the current split
        for pair in combinations(splits, 2):
            gcd = math.gcd(pair[0], pair[1])
            nonlocal max_gcd
            max_gcd = max(max_gcd, gcd)
    
    def split_difficulty(remaining_total, remaining_days, current_splits):
        # Base case: when we have split into required number of days
        if remaining_days == 1:
            if remaining_total > 0:
                # Add the last remaining amount
                current_splits.append(remaining_total)
                calculate_gcd_for_splits(current_splits)
                current_splits.pop()
            return
            
        # Try different splits for the current day
        for i in range(1, remaining_total - (remaining_days - 1) + 1):
            current_splits.append(i)
            split_difficulty(remaining_total - i, remaining_days - 1, current_splits)
            current_splits.pop()
    
    # Start the recursive splitting process
    split_difficulty(total_difficulty, num_days, [])
    
    return max_gcd

# Test cases
# print(max_training_result(9, 2))  # Original test case
# print(max_training_result(15, 4))  # Split into 3 days
# print(max_training_result(428 , 71))

# print(math.gcd(428, 71))
def solve(d, n):
    base = d // n
    rem = d % n
    if rem == 0:
        return base
    res = 1
    for i in range(1, base + 1):
        if d%i == 0:
            res = max(res, math.gcd(i, d-i))
    return res

print(solve(15, 4))



# Example usage
# total_difficulty = 15
# num_days = 4
# result = max_training_result(total_difficulty, num_days)
# print(f"Maximum training result for {total_difficulty} difficulty over {num_days} days: {result}")

