# def powerOfNumber(base, exp):
#     assert int(exp) == exp, 'must be positive integer'
#     if exp == 0:
#         return 1
#     elif n < 0:
#         return 1/base * powerOfNumber(base, exp+1)
#     else:
#         return base * powerOfNumber(base, exp-1)

from collections import Counter


def ispalindrome(n: int):
    return "palindrome" if n == n[::-1] else "not palindrome"

# print(ispalindrome(121))    

def findDenominations(votes):
    n = len(votes)
    freq = [0] * (n + 1)  # Frequency array to track votes for denominations [1, N]
    
    # Count votes for each denomination
    for vote in votes:
        freq[vote] += 1

    # Collect denominations with more than one vote
    result = [i for i in range(1, n + 1) if freq[i] > 1]

    return result
# mine  
# def longestUniqueSubsttr(s):
#       result = 0
#       j = 0
#       while j <= len(s):
#         final = {}
#         for i in range(j, len(s)):
#           if s[i] not in final:
#             final[s[i]] = i
#           else:
#             j=final[s[i]]
#             break
#         result = max(len(final), result)
#         if result <= (len(s) / 2) + 1: 
#             j += 1 
#         else: 
#            break
#       return result    

def longestUniqueSubsttr(s):
    n = len(s)
    if n == 0:
        return 0

    start = 0
    max_length = 0
    char_index = {}

    for end in range(n):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

        char_index[s[end]] = end

        max_length = max(max_length, end - start + 1)

    return max_length

print(longestUniqueSubsttr("abcabcbb"))


def nextgreater(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] > arr[i]:
                result.append(arr[j])
                break
            else:
                print(-1)

    
