def minAbsoluteDifference(nums, size, x):
    result = nums[0]

    def finxmin(nums):
        return max(nums) - min(nums)

    for i in range(size):
        maxi = 0
        mini = nums[i]
        j = i + 1
        # i < j and
        while j < size and j - i <= x:
            if nums[i] > nums[j]:
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[i])
                j += 1
            else:
                maxi = max(maxi, nums[j])
                mini = min(mini, nums[i])
                j += 1
        if j < size:
            result = min(result, maxi - mini)
        else:
            return result
    return result


# print(minAbsoluteDifference([1, 2, 3, 4], 4, 3))
def count_students(students, sandwiches):
    count_0 = students.count(0)
    count_1 = students.count(1)
    while len(students) > 0 and len(sandwiches) > 0:
        
        if students[0] == sandwiches[0]:
            if students[0] == 0:
                count_0 -= 1
            else:
                count_1 -= 1
            students.pop(0)
            sandwiches.pop(0)
        else:
            if count_0 == 0:
                return len(students)
            if count_1 == 0:
                return len(students)
            students.append(students.pop(0))
    return len(students)

from collections import Counter
import math
def firstUniqueInteger(num):
    counts = Counter(num)
    print(counts)
    for count in counts:
        if counts[count] == 1:
            return count

# print(firstUniqueInteger([9, 6, 7, 6]))
def contains_all_alphabets(s: str) -> bool:
    # Define a set of all lowercase alphabets
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    input_set = set(s)
    return alphabet_set.issubset(input_set)
# print(contains_all_alphabets("thequickbrownfoxjumpsoverthelazydog"))

def minAbsoluteDifference(nums, size, x):
# 6
# 1 2 3 4 5 6
# 2
    abs_diff = math.inf
    mini = math.inf
    i = 0
    while i < size:
        if len(nums[i: i+x+1]) > x:
            num = nums[i: i+x+1]
            print(num)
            mini = max(num) - min(num)
            abs_diff = min(abs_diff, mini)
            i += 1
        else: i+= 1

    return abs_diff

# print(minAbsoluteDifference([1,2,3,4,5,6], 6, 2))
# print(minAbsoluteDifference([3, 6, 10, 14, 18], 5, 4))

# def findLeastGreater(arr: list):
#     result = []
#     for i in range(len(arr)):
#         append = False
#         min_value = math.inf
#         for j in range(i ,len(arr)):
#             if arr[i] < arr[j]:
#                 min_value = min(min_value, arr[j])
#                 append = True
#         if not append:
#             result.append(-1)
#         else:
#             result.append(min_value)
#     return result

from sortedcontainers import SortedList
import bisect
def findLeastGreater(arr: list):
    result = []
    sorted_list = []
    for num in reversed(arr):
        index = bisect.bisect_right(sorted_list, num)
        if index < len(sorted_list):
            result.append(sorted_list[index])
        else:
            result.append(-1)
        bisect.insort(sorted_list, num)
    return result[::-1]



# print(findLeastGreater([2, 6, 9, 1, 3, 2]))

def union_and_intersection(arr1, arr2):
    union = set(arr1 + arr2)
    intersection = set(arr1).intersection(set(arr2))
    print(" ".join(map(str,sorted(union))))
    print(" ".join(map(str,sorted(intersection))))
    # return sorted(list(union)), sorted(list(intersection))

# print(union_and_intersection([1, 1, 2, 3, 5, 6, 6, 8, 10, 11], [2, 2, 2, 8, 9, 16, 18, 22, 50, 99]))
# 10 10
#  [1 1 2 3 5 6 6 8 10 11] [2 2 2 8 9 16 18 22 50 99]
# 1 2 3 5 6 8 9 10 11 16 18 22 50 99 2 8

def unique_permutations(s):
    def permute(s, path, used, result):
        # If the path length equals the length of the string, we've formed a permutation
        if len(path) == len(s):
            result.add("".join(path))
            return
        
        for i in range(len(s)):
            # Skip already used characters
            if used[i]:
                continue
            
            # To ensure lexicographical uniqueness, skip duplicate characters unless it's the first unused instance
            if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                continue
            
            # Mark this character as used and proceed with recursion
            used[i] = True
            path.append(s[i])
            permute(s, path, used, result)
            # Backtrack
            path.pop()
            used[i] = False
    
    # Sort the string to ensure lexicographical order
    s = sorted(s)
    result = set()  # Using a set to ensure uniqueness
    used = [False] * len(s)
    
    # Generate permutations
    permute(s, [], used, result)
    
    # Print results in sorted order
    for perm in sorted(result):
        print(perm)

# Input
s = "aba"
# unique_permutations(s)

class Solution:
    def solve(self, a, n, k):
        # Special case for all zeros
        if all(x == 0 for x in a):
            # Count how many pairs of zeros we can form
            segments = len(a) // 2
            if segments >= k:
                print("Attack")
                return
            else:
                print("Wait")
                return
        
        # Function to find the smallest missing positive integer
        def find_min_missing(arr):
            positive_nums = set(x for x in arr if x > 0)
            missing = 1
            while missing in positive_nums:
                missing += 1
            return missing
        
        # Function to check if the array can be divided into valid segments
        def check_segments(arr):
            if len(arr) % 2 != 0:
                return False
            
            # Compute the minimum missing number for the entire array
            min_missing = find_min_missing(arr)
            
            # Validate each segment
            for i in range(0, len(arr), 2):
                segment = arr[i:i+2]
                seg_missing = find_min_missing(segment)
                if seg_missing != min_missing:
                    return False
            
            return True
        
        # General case
        if check_segments(a):
            segments = len(a) // 2
            if segments >= k:
                print("Attack")
            else:
                print("Wait")
        else:
            print("Wait")
