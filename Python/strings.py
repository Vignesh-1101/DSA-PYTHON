def findPatternIndices(text, pattern):
    # Write your code here
    plen = len(pattern)
    result = []
    for i in range(0, len(text)):
        print(text[i : (plen + i)])
        if text[i : (plen + i)] == pattern:
            result.append(i)
    return result


# print(findPatternIndices("abababab", "aba"))

# t=["A", "B", "C", "Z"]
# for i in t:
#     if i in s:
#         print("true")
#     else:
#         print("false")
# s="ADOBECODEBANC"
def minWindow(s: str, t: str) -> str:
    result =""
    wside = ["A", "B", "C"]
    i=0
    j = 1
    while i < len(s):
        while j < len(s):
            if s[i:j] in t[wside-1]:
                result += s[i]
                j += 1
                wside -= 1
            else:
                j += 1
        i+=1
    result = result[::-1]
    return result

# print(minWindow("ADOBECODEBANC", "ABC"))

def solve(n, s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    i = 0
    start = 0
    
    while i < n:
        # Check for two-character syllable (CV)
        if i + 1 < n and s[i] not in vowels and s[i + 1] in vowels:
            result.append(s[i:i + 2])
            i += 2
        # Check for three-character syllable (CVC)
        elif i + 2 < n and s[i] not in vowels and s[i + 1] in vowels and s[i + 2] not in vowels:
            result.append(s[i:i + 3])
            i += 3
        else:
            i += 1
            continue

    return result
# print(solve(5,"badef"))

from collections import Counter, defaultdict

def min_window_substring(s: str, t: str) -> str:
    if not s or not t:
        return ""
    
    # Count characters in t
    t_count = Counter(t)
    required = len(t_count)  # Number of unique characters in t
    
    # Initialize sliding window pointers and variables
    l, r = 0, 0  # Left and right pointers
    window_count = defaultdict(int)  # Tracks counts of characters in the window
    formed = 0  # Number of characters that meet the required frequency in window
    
    # To track the smallest window
    min_len = float("inf")
    min_window = (0, 0)
    
    while r < len(s):
        # Add character from the right to the window
        char = s[r]
        window_count[char] += 1
        
        # Check if this character satisfies the required frequency
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # Try shrinking the window until it becomes invalid
        while l <= r and formed == required:
            char = s[l]
            
            # Update the result if the current window is smaller
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_window = (l, r)
            
            # Remove the character at l from the window
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            
            # Move the left pointer
            l += 1
        
        # Expand the window by moving the right pointer
        r += 1
    
    # Return the smallest window substring or an empty string if not found
    start, end = min_window
    return s[start:end + 1] if min_len != float("inf") else ""

# # Example usage
# s = "ADOBECODEBANC"
# t = "ABC"
# print(min_window_substring(s, t))  # Output: "BANC"

def longestKSubstr(s, k):
    # Initialize variables
    char_count = {}
    max_length = -1
    start = 0  # Sliding window's start index

    # Iterate over the string with the end pointer
    for end in range(len(s)):
        # Add the current character to the hash map
        char_count[s[end]] = char_count.get(s[end], 0) + 1

        # While the number of unique characters exceeds k, shrink the window
        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        # If the number of unique characters equals k, calculate the length
        if len(char_count) == k:
            max_length = max(max_length, end - start + 1)

    return max_length

print(longestKSubstr("aabacbebebe", 3))
