from collections import Counter
import math
from typing import List
def map_implementation(arr):
        # Write your code here
      result = []
      counts = Counter(arr)
      for count in counts:
        result.append([count, counts[count]])
      return sorted(result)
# print(map_implementation([1, 2, 4, 1, 3, 3]))

def winner(input_list):
      result = {}
      stack = []
      for arr in input_list:
        if result.get(arr[0]) is None:
            result[arr[0]] = arr[1]
        else:
            result[arr[0]] += arr[1]
        if stack:
          if stack[0][1] < arr[1]:
            stack.pop()
            stack.append(arr)
        else:
          stack.append(arr)
      
      return stack[0][0]

# print(winner([["andrew", 3], ["andrew", 2], ["mike", 5]]))

def berlogging_winner(n, rounds):
    scores = {}  # To track the cumulative scores of players
    first_to_reach = {}  # To track when a player first reached a specific score
    max_score = float('-inf')  # To keep track of the highest score
    winner = None  # To store the winner's name

    for i in range(n):
        name, score = rounds[i]
        score = int(score)

        # Update the cumulative score
        if name not in scores:
            scores[name] = 0
        scores[name] += score

        # Check if the player reaches a new maximum score
        if scores[name] > max_score:
            max_score = scores[name]
            winner = name
            first_to_reach[name] = i
        elif scores[name] == max_score:
            if name not in first_to_reach:
                first_to_reach[name] = i

    # Return the player who reached the max_score first
    return winner
n = 3
rounds = [
    ("alice", 3),
    ("bob", 5),
    ("alice", 2),
]

# Function call
# print(berlogging_winner(n, rounds))

def count_subarrays_with_sum(nums, k):
    # Initialize the hash map to store prefix sums and their counts
    prefix_sums = {0: 1}
    cumulative_sum = 0
    count = 0

    # Traverse through the array
    for num in nums:
        cumulative_sum += num
        # Check if (cumulative_sum - k) exists in the hash map
        if cumulative_sum - k in prefix_sums:
            count += prefix_sums[cumulative_sum - k]
        # Update the hash map with the current cumulative sum
        prefix_sums[cumulative_sum] = prefix_sums.get(cumulative_sum, 0) + 1

    return count

# print(count_subarrays_with_sum([-4, 4, 3, 3, 8, -2], 6))

def findMaxLength( nums):
      #Write your code here
      # 0 1 1 0 1 1 0
      cumulative_sum = 0
      max_length = 0
      cumulative_index = {0: -1}  # Initialize with cumulative sum 0 at index -1
  
      for i, num in enumerate(nums):
          # Update cumulative sum
          cumulative_sum += 1 if num == 1 else -1
  
          # Check if cumulative sum has been seen before
          if cumulative_sum in cumulative_index:
              # Calculate the length of the subarray
              length = i - cumulative_index[cumulative_sum]
              max_length = max(max_length, length)
          else:
              # Store the first occurrence of the cumulative sum
              cumulative_index[cumulative_sum] = i
  
      return max_length
# print(findMaxLength([0, 1, 1, 0, 1, 1, 0]))

def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    for i in range(len(image)):
        print(image[i][::-1])
    for i in range(len(image)):
        for j in range(len(image)):
            image[i][j] = 1 - image[i][j]
    print(image)

# print(flipAndInvertImage([[1,1,0], [1,0,1], [1, 1, 0],]))

def minimum_operations(a: list[int], b: list[int]):
    # Write your code here
    # 1 2 3 4 5
    # 2 3 4 5 6
    # 3 4 5 6 7
    # 4 5 6 7 8
    # 5 6 7 8 9
    count = 0
    for i in range(len(a)):
        if a[i] and b[i]:
            count += abs(a[i] - b[i])
    return count

# print(minimum_operations([1,2,3], [3,4]))


def max_training_result(d, n):
    # Initialize maximum GCD
    max_gcd = 0

    # Iterate through all possible divisions of `d` into `n` days
    for i in range(1, n + 1):
        if d % i == 0:  # Check if `d` can be divided into `i` parts evenly
            # Divide the difficulty into `i` parts and calculate the GCD of the parts
            part_difficulty = d // i
            gcd = math.gcd(part_difficulty, i)
            max_gcd = max(max_gcd, gcd)

    return max_gcd

# Output the maximum GCD
print(max_training_result(15, 4))
