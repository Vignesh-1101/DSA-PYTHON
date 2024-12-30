def minimumCost(nums):
    n = len(nums)
    dp = [[float('inf')] * 4 for _ in range(n + 1)]  # dp[i][k]: min cost to divide first i elements into k subarrays
    
    dp[0][0] = 0  # Base case: 0 cost with 0 elements and 0 subarrays
    
    for i in range(1, n + 1):  # Iterate over first i elements
        for k in range(1, 4):  # Divide into k subarrays
            for j in range(k - 1, i):  # Check all valid split points
                dp[i][k] = min(dp[i][k], dp[j][k - 1] + nums[j])
    
    return dp[n][3]

n = 4
nums = [1, 2, 3, 12]
# print(minimumCost(nums))

# prev = None
# next_node = head.next
# current.next = prev
# prev = current
# current = next_node

def maximumGap(nums):
      if len(nums) < 2:
        return 0

      # Step 1: Find the min and max values
      min_val, max_val = min(nums), max(nums)
  
      # Step 2: Calculate bucket size and count
      n = len(nums)
      if max_val == min_val:  # All elements are the same
          return 0
      bucket_size = max(1, (max_val - min_val) // (n - 1))
      bucket_count = (max_val - min_val) // bucket_size + 1
  
      # Step 3: Initialize buckets
      buckets = [[None, None] for _ in range(bucket_count)]  # [min, max] for each bucket
  
      # Step 4: Assign elements to buckets
      for num in nums:
          idx = (num - min_val) // bucket_size
          if buckets[idx][0] is None:
              buckets[idx][0] = buckets[idx][1] = num
          else:
              buckets[idx][0] = min(buckets[idx][0], num)
              buckets[idx][1] = max(buckets[idx][1], num)
  
      # Step 5: Calculate maximum gap
      max_gap = 0
      prev_max = min_val
      for b in buckets:
          if b[0] is not None:  # Non-empty bucket
              max_gap = max(max_gap, b[0] - prev_max)
              prev_max = b[1]
  
      return max_gap

print(maximumGap([6,3,6,9,1,4,9]))