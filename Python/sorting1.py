from collections import deque


class Solution:
    def __init__(self):
        self.cnt = 0
    def print(self):
        self.cnt += 1
    def addnum(self, n):
        while n > 0:
            for i in range(n+1):
                self.print()
            n //= 2

n = 8
solution = Solution()
solution.addnum(n)

word = "neeabcdcbaww"
def checksubstringpali(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            if string[i:j] == string[i:j][::-1]:
                if len(longest) < len(string[i:j]):
                    longest = string[i:j]
    print(longest, "long")

def left_right_sum(nums):
    left_sum = 0
    right_sum = sum(nums)
    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1

def game(a, b, n):
      def count_swaps(arr):
          swaps = 0
          for i in range(len(arr)):
            for j in range(len(arr) -i -1):
                if(arr[j] > arr[j+1]):
                    arr[j] = arr[j+1]
                    arr[j+1] = arr[j]
                    swaps += 1
            return swaps
        #   for i in range(len(arr)):
        #       for j in range(len(arr) - i - 1):
        #         print(arr)
        #         #4,6,2,5,3
        #         if arr[j] > arr[j + 1]:
        #             arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap adjacent elements
        #             swaps += 1
        #   return swaps
  
      anish_swaps = count_swaps(a[:])  
      binish_swaps = count_swaps(b[:]) 
  
      if anish_swaps < binish_swaps:
          print("Anish")
      elif binish_swaps < anish_swaps:
          print("Binish")
      else:
          print("Tie")

def solve1(inventory1, inventory2):
    # Merge and sort the inventories using two-pointer approach
    n, m = len(inventory1), len(inventory2)
    merged = []
    
    # Two pointers for inventory1 and inventory2
    i, j = 0, 0
    
    while i < n and j < m:
        if inventory1[i] <= inventory2[j]:
            merged.append(inventory1[i])
            i += 1
        else:
            merged.append(inventory2[j])
            j += 1
    
    # Add remaining items from either inventory
    merged.extend(inventory1[i:])
    merged.extend(inventory2[j:])
    
    # Return the result as a space-separated string
    return " ".join(merged)

def left_right_sum(nums):
    total_sum = sum(nums)
    left_sum = 0
    arr = []
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        arr.append(left_sum + right_sum)
        left_sum += nums[i]

def movetwos(nums):
      stack = deque()
      for i in range(len(nums)):
          if nums[i] == 2:
              stack.append(nums[i])
          else:
              stack.appendleft(nums[i])
      return " ".join(str(i) for i in stack)


def solve(weather, n, k, t):
    count = 0
    start = 0       
    # 5 2 10
    # -5 0 5 10 15
    for end in range(n):
        if weather[end] > t:
            start = end + 1
        
        if end - start + 1 >= k:
            count += end - start + 1 - (k - 1)
    
    print(count)

def solve(s, n):
      # Count total mangoes and pineapples in the string
      total_mangoes = s.count('M')
      total_pineapples = s.count('P')
  
      # Initialize prefix and suffix counts
      mango_prefix = pineapple_prefix = 0
      mango_suffix = total_mangoes
      pineapple_suffix = total_pineapples
  
      for i in range(1, n):  # i = 1 to n-1 (both sides must have at least 1 fruit)
          # Update prefix counts
          if s[i - 1] == 'M':
              mango_prefix += 1
              mango_suffix -= 1
          else:  # s[i - 1] == 'P'
              pineapple_prefix += 1
              pineapple_suffix -= 1
  
          # Check the conditions
          if mango_prefix != mango_suffix and pineapple_prefix != pineapple_suffix:
              return i 
  
      return -1  

print(solve("PMP", 3))

