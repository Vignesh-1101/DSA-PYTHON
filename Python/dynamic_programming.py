from collections import Counter
def deletePoints(nums):
      #Write your code here
      freq = Counter(nums)
      max_val = max(nums)
      
      # Step 2: Create a DP array for all possible gem values
      dp = [0] * (max_val + 1)
      
      # Step 3: Fill the DP table
      for i in range(max_val + 1):
          dp[i] = max(dp[i - 1], dp[i - 2] + freq[i] * i) if i > 1 else freq[i] * i
      
      return dp[max_val]


# 969 845 279 806 906 679 34 651 767 971
# points = [3, 4, 2]
# print(deletePoints(points))

def special_arr(nums):
      MOD = 10**9 + 7
      n = len(nums)
      full_mask = (1 << n) - 1  # All elements included
      print(1 << n)
      dp = [[0] * n for _ in range(1 << n)]
      
      # Initialization: single-element subsets
      for i in range(n):
          dp[1 << i][i] = 1
      
      # Fill DP table
      for mask in range(1 << n):  # Iterate over all subsets
          for last in range(n):  # Iterate over all possible last elements
              if not (mask & (1 << last)):  # If `last` is not in the subset, skip
                  continue
              for next_elem in range(n):  # Try adding a new element to the subset
                  if mask & (1 << next_elem):  # If `next_elem` is already in the subset, skip
                      continue
                  if nums[last] % nums[next_elem] == 0 or nums[next_elem] % nums[last] == 0:
                      dp[mask | (1 << next_elem)][next_elem] += dp[mask][last]
                      dp[mask | (1 << next_elem)][next_elem] %= MOD
      
      # Sum up all valid arrangements
      result = 0
      for last in range(n):
          result += dp[full_mask][last]
          result %= MOD
      
      return result


print(special_arr([2,3,6]))

