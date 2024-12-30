from collections import Counter, defaultdict


def matrix(matrixs):
    row, cols = len(matrixs), len(matrixs[0])
    row_Set = set()
    col_Set = set()
    for i in range(row):
        for j in range(cols):
            if matrixs[i][j] == 0:
                row_Set.add(i)
                col_Set.add(j)
    for i in range(row):
        for j in range(cols):
            if i in row_Set or j in col_Set:
                matrixs[i][j] = 0
    return matrixs

#inplace
def set_zeroes(matrix):
    """
    Sets entire rows and columns to 0 if any element in the row or column is 0.

    Args:
        matrix: A 2D matrix.

    Returns:
        The modified matrix with rows and columns set to 0 as needed.
    """

    rows, cols = len(matrix), len(matrix[0])
    is_col = False

    # Check if the first column needs to be set to 0
    for i in range(rows):
        if matrix[i][0] == 0:
            is_col = True
            break

    # Mark rows and columns with 0s using the first row and column as markers
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set rows and columns to 0 based on the markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Set the first column to 0 if necessary
    if is_col:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix

def count_subarrays(arr, target):
    prefix_sum = 0
    count = 0
    freq = {0: 1}

    for num in arr:
        prefix_sum += num
        required_sum = prefix_sum - target
        if required_sum in freq:
            count += freq[required_sum]
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count

# arr = [2, 7, 5, 6, 3, 4]
# target = 10
# result = count_subarrays(arr, target)
# print(result)

def longest_unique_substring(s):
    char_index = {}
    start = 0
    max_length = 0
    longest_substring = ""

    for index, char in enumerate(s):
        # If the character is already in the dictionary and is in the current substring
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = index
        current_length = index - start + 1

        if current_length > max_length:
            max_length = current_length
            longest_substring = s[start:index + 1]

    return longest_substring

input_string = "nothingdfsfa"
result = longest_unique_substring(input_string)
# print(f"The longest substring with unique characters is: '{result}'")


def subString(arr):
    i=0
    j=1 
    final = ''
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
                final = arr[i:j]
                print(final)

# print(subString("nothingdfsfa"), "aa")

def canDivideChocolate(n):
    print("YES" if n % 3 == 0 else "NO")

def word_correction(self, s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        else:
            lower += 1
    if upper > lower:
        return s.upper()
    else:
        return s.lower()
    
def calculate(s: str) -> int:
      #Write your code here
      stack = []
      num = 0
      sign = 1
      result = 0
      for i in s:
        if i.isdigit():
          num = num * 10 + int(i)
        elif i in "+-":
            result += sign * num  # Apply the previous sign and number
            num = 0
            sign = 1 if i == '+' else -1
        elif i == '(':
            # Push the result and sign onto the stack
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif i == ')':
            result += sign * num  # Apply the last number before the parenthesis
            num = 0
            result *= stack.pop()  # Multiply with the sign before the parenthesis
            result += stack.pop()  # Add the result before the parenthesis
      result += sign * num  # Add the last number
      return result

# print(calculate("(1+(4+5+2)-3)+(6+8)"))
    

def frequencySort(s: str) -> str:
    freq = Counter(s)
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    result = ''.join(char * count for char, count in sorted_chars)
    return result

# print(frequencySort("Aa"))

def groupAnagrams(strs):
    # Dictionary to group anagrams
    anagrams = defaultdict(list)
    
    # Group strings by their sorted tuple as the key
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    print(anagrams)
    # Prepare the output
    result = []
    for group in anagrams.values():
        result.append(" ".join(sorted(group)))  # Sort each group lexicographically
    # print(result)
    # Sort groups lexicographically by their first element
    result.sort()
    final = ""
    for group in result:
        final += group + "\n"
    result = "\n".join(result)
    return final

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))