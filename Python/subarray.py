from typing import List


def printSubarray(n: List):
    for i in range(len(n)):
        for j in range(i, len(n)):
            print(n[i:j+1])
        
# print(printSubarray([2,3,4,5,6]))

s = [2,3,4,5,6]
# print(s[0:1])            

# def max_average_subarray(nums: List[int], k: int) -> float:
#     # Edge case: if k is greater than the array length
#     if k > len(nums):
#         return float('-inf')  # Invalid input

#     # Step 1: Compute the sum of the first window
#     current_sum = sum(nums[:k])
#     max_sum = current_sum

#     # Step 2: Slide the window across the array
#     for i in range(k, len(nums)):
#         # Add the next element and remove the first element of the window
#         current_sum += nums[i] - nums[i - k]
#         # Update the maximum sum
#         max_sum = max(max_sum, current_sum)

#     # Step 3: Compute and return the maximum average
#     return max_sum / k

def max_average_subarray(nums: List[int], k: int) -> float:
    left = 0
    max_sum = 0
    for i in range(len(nums)):
        for j in range(i, k+left):
            print(i, nums[j], k)
            max_sum = max(max_sum, sum(nums[i:j+1]))
        left += 1
                
print(max_average_subarray([1,2,3,4,5,6], 3))