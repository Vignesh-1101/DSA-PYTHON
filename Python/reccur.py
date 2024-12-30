def max_k_occurrences(arr: list, n: int, k: int, arrs: list):
    if n == len(arr):
        return -1
    ans = max_k_occurrences(arr, n+1, k, arrs)
    if ans != -1 and ans != ans:
        return ans
    if arr[n] == k:
        ans = n
        arrs.append(ans)
    return arrs

# print(max_k_occurrences([1,2,3,2,3,6, 2, 2, 2], 1, 2, []))

def solve(arr: list, n: int) -> int:
    # arr = 
    if n == 0:
        return 0
    ans = solve(arr, n-1)
    if arr[n] == 0:
        return ans + 1
    return ans

def removeDuplicateLetters(s: str) -> str:
      # Write Your code here
      # Frequency count of each character
      frequency = {ch: 0 for ch in s}
      for ch in s:
          frequency[ch] += 1
  
      stack = []
      visited = set()
  
      for ch in s:
          # Decrease the frequency of the current character
          frequency[ch] -= 1
          
          # Skip the character if it's already in the result stack
          if ch in visited:
              continue
          
          # Maintain lexicographical order by removing larger characters
          # that occur later
          if stack:
            print(ch < stack[-1])
          while stack and ch < stack[-1] and frequency[stack[-1]] > 0:
              removed = stack.pop()
              visited.remove(removed)
          
          # Add the current character to the stack and mark it as visited
          stack.append(ch)
          visited.add(ch)
  
      # Convert stack to string for the result
      return ''.join(stack)

# Example Usage
# s1 = "bcabc"
# s1 = "cbacdcbc"

# print(removeDuplicateLetters(s1))  # Output: "abc"
# print(removeDuplicateLetters(s2))

def countCollisions(dirs: str) -> int:
    dirs = dirs.lstrip('L').rstrip('R')
    # Initialize collision count
    collisions = 0
    
    # Traverse through the string
    for ch in dirs:
        # If it's not a stopped car, it will cause collisions
        if ch != 'S':
            collisions += 1
    
    return collisions
directions1 = "LSRRSLLRLSR"
# directions1 = "LLRR"
# print(countCollisions(directions1))  # Output: 5
    # stack = []
    # collide = 0
    # continued = False
    # for i in range(len(dirs)):
    #     if continued:
    #         collide += 1
    #     elif dirs[i] == "S":
    #         continued = True
    #         collide += 1
    #     elif stack and dirs[i] == stack[-1]:
    #         while stack:
    #             stack.pop()
    #     elif stack and stack[-1] != dirs[i]:
    #         collide += 2
    #         while stack:
    #             stack.pop()
                
    #     else:
    #         stack.append(dirs[i])
    # return collide
    # Write your code here
    # stack = []
    # collisions = 0
    # for direction in dirs:
    #     if direction == 'L':
    #         if stack and stack[-1] == 'R':
    #             collisions += 1
    #         else:
    #             stack.append(direction)
    #     elif direction == 'S':
    #         if stack and stack[-1] == 'R':
    #             collisions += 1
    #         stack.append(direction)
    #     elif direction == 'R':
    #         stack.append(direction)
        
    # return collisions

# Example Usage


# def minimumOperations(nums):
#     # 2 1 3 2 1
#     count = 0
#     result = []
#     for num in nums:
#         if result and num < result[-1]:
#             count += 1
#             while result and num < result[-1]:
#                 result.pop()
#         result.append(num)
#     return count

# # Example Usage
# # nums = [2, 1, 3, 2, 1]

def minimumSwaps(nums):
    n = len(nums)
    swaps = 0
    
    # First, handle consecutive group reorganization
    for target_group in [1, 3]:
        # Find the first and last occurrences of the target group
        first_indices = [i for i in range(n) if nums[i] == target_group]
        if not first_indices:
            continue
        
        first = first_indices[0]
        last = first_indices[-1]
        
        # Count misplaced elements before first occurrence and after last occurrence
        swaps += min(first, n - last - 1)
    
    return swaps

# Test the specific input
input_arr = [1, 3, 3, 3, 1, 2, 3, 3, 2, 1]
print(minimumSwaps(input_arr))