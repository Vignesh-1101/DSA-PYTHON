from collections import Counter, defaultdict, deque
from datetime import datetime
from decimal import Decimal
from fractions import Fraction
import math
import heapq


def palindrome_recursion(name):
    print(name)
    if len(name) == 0:
        return True
    else:
        if name[0] == name[-1]:
            return palindrome_recursion(name[1:-1])
        else:
            return False


def palindrome_stack(names):
    stack = deque(names)

    print(names, "names")

    while len(stack) > 1:
        print(stack)
        last = stack.popleft()
        first = stack.pop()
        print(first, "first")

        print(last, "last")

        if first != last:
            return False
    return True


# print(palindrome_stack("madam"))
# print(palindrome_stack("madana"))


def sum_of_digits(N):
    N = str(N)
    sum = 0
    for i in N:
        sum += int(i)
    return sum


def reverseString(s):
    # stack = deque(s)
    # print(stack)
    word = ""
    print(s[1:])
    print(s[0])
    for i in s:
        word = i + word
    print(word)


# reverseString("asdfdsfsadf")


def checked(n, m):
    # for i in range(n, m):
    #     print(i)
    sum = n
    while sum < m:
        sum += 1
        print(sum)


def count_divisible(start, end, divisor):
    count = 0
    for i in range(start, end + 1):
        if i % divisor == 0:
            count += 1
    return count


def analyze_string(input_string):
    has_letter = 0
    has_number = 0
    has_whitespace = 0
    has_special_character = 0
    total = ""

    for char in input_string:
        if char.isalpha():
            has_letter += 1
        elif char.isdigit():
            has_number += 1
        elif char.isspace():
            has_whitespace += 1
        else:
            has_special_character += 1

    total = (
        str(has_letter)
        + " "
        + str(has_whitespace)
        + " "
        + str(has_number)
        + " "
        + str(has_special_character)
    )

    return total


from typing import List


def mostWordsFound(sentences: List[str]) -> int:
    cnt = 1
    for sentence in sentences:
        print(sentence)
        icnt = 1
        for i in sentence:
            print(i)
            if i == " ":
                icnt += 1
        cnt = max(cnt, icnt)
    return cnt


def restoreString(s: str, indices: List[int]) -> str:
    v = ""
    for j in range(len(indices)):
        print(indices.index(0))
        # print(indices.index(j))
        v = v + s[indices.index(j)]
        # print(v)
    return v


def numJewelsInStones(jewels: str, stones: str) -> int:
    aux = set(jewels)
    return sum((1 for x in stones if x in aux))


def countPoints(rings: str) -> int:
    rods = [set() for _ in range(10)]
    for i in range(0, len(rings), 2):
        rods[int(rings[i + 1])].add(rings[i])
    return sum(len(rod) == 3 for rod in rods)


def checkIfPangram(sentence: str) -> bool:
    return len(set(sentence)) == 26


def sortString(s: str) -> str:
    # Create an array to count occurrences of each character (26 lowercase letters)
    counts = [0] * 26
    # Count each character's occurrence
    for char in s:
        counts[ord(char) - ord("a")] += 1
    print(counts)

    result = []
    length = len(s)

    while len(result) < length:
        # Add characters in increasing order (a -> z)
        for i in range(26):
            if counts[i] > 0:
                result.append(chr(i + ord("a")))
                counts[i] -= 1

        # Add characters in decreasing order (z -> a)
        for i in range(25, -1, -1):
            if counts[i] > 0:
                result.append(chr(i + ord("a")))
                counts[i] -= 1

    return "".join(result)


def convert_seconds(seconds):
    # Calculate hours, minutes, and remaining seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    print(seconds % 3600)
    remaining_seconds = seconds % 60
    # Format the result as a string
    result = f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"
    return result


def sortSentence(s: str) -> str:
    # result = {}
    # final = ""
    # words = s.split()
    # for word in words:
    #     position = word[len(word) - 1]
    #     result[position] = word[:len(word) - 1]
    # for i in range(1, len(result) + 1):
    #     final += result[str(i)] + " "
    # return final[:len(final) - 1]

    s = s.split(" ")
    print(s)
    odict = {n[-1]: n[:-1] for n in s}
    odict = sorted(odict.items())
    print(odict)
    return " ".join([x[1] for x in odict])


def isAnagram(s: str, t: str) -> bool:
    s = Counter(s)
    t = Counter(t)
    print(t)
    print(s)
    return Counter(s) == Counter(t)


def findTheDifference(s: str, t: str) -> str:
    s = Counter(s)
    t = Counter(t)
    print(t, "\n", s)
    difference = Counter(t) - Counter(s)
    return list(difference.keys())[0]


def frequencySort(s: str) -> str:
    s = Counter(s)
    print(s)
    s = sorted(s.items(), key=lambda x: x[1], reverse=True)
    print(s)
    result = ""
    for i in s:
        result += i[0] * i[1]
    return result


def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    def encode(word):
        mapping = {}
        return [mapping.setdefault(ch, len(mapping)) for ch in word]

    pattern_encoded = encode(pattern)
    return [word for word in words if encode(word) == pattern_encoded]


def firstPalindrome(words: List[str]) -> str:
    def ispalindrome(word):
        print(word[::-1])
        return word == word[::-1]

    for word in words:
        if ispalindrome(word):
            return word


def reverseWords(s: str) -> str:
    return " ".join([word[::-1] for word in s.split(" ")])


def reversePrefix(word: str, ch: str) -> str:
    string = ""
    complete = False
    for char in word:
        if char == ch and not complete:
            string += char
            string = string[::-1]
            complete = True
        else:
            string += char
    return string


def diStringMatch(s: str) -> List[int]:
    n = len(s)
    perm = []
    low, high = 0, n
    for i in s:
        if i == "I":
            perm.append(low)
            low += 1
        else:
            perm.append(high)
            high -= 1
    perm.append(low)
    return perm


def balancedStringSplit(s: str) -> int:
    count = 0
    balance = 0
    for i in s:
        if i == "R":
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            count += 1
    return count


def halvesAreAlike(s: str) -> bool:
    vowles = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]
    if sum(1 for i in first_half if i in vowles) == sum(
        1 for i in second_half if i in vowles
    ):
        return True


def areOccurrencesEqual(s: str) -> bool:
    s = Counter(s)
    return len(set(s.values())) == 1


def kthDistinct(arr: List[str], k: int) -> str:
    s = Counter(arr)
    print(s)
    for i in s:
        print(s[i])
        if s[i] == 1:
            k -= 1
        if k == 0:
            return i
    return ""


def find_penultimate_word(sentence):
    # Write your code here
    word = sentence.split(" ")
    return word[-2]


def countGoodSubstrings(s: str) -> int:
    pairs = []
    count = 0
    for i in range(len(s) - 1):
        x = s[i : i + 3]
        pairs.append(x)
    print(pairs)
    for pair in pairs:
        if len(set(pair)) == 3:
            count += 1
    return count


def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""

    char_set = set(s)

    for i, c in enumerate(s):
        if c.swapcase() not in char_set:
            left = longestNiceSubstring(s[:i])
            right = longestNiceSubstring(s[i + 1 :])
            return max(left, right, key=len)

    return s


def check_common_digits(num1, num2):
    # Convert numbers to strings
    num1_str = str(num1)
    num2_str = str(num2)
    print(num1_str)
    print(num2_str)
    result = set(num2_str)
    print(result)
    # Create sets of unique digits for each number
    for n in num1_str:
        print(n)
        if n in result:
            return True


# def numberOfSubstrings(s: str) -> int:
#         result = 0
#         left = 0
#         right = 0
#         if len(set(s)) < 3:
#             return 0
#         while left < len(s):
#             while right < len(s):
#                 if len(s[left:right+1]) > 2 and set(s).issubset(s[left:right+1]):
#                     result += result
#                 right += 1
#             left += 1
#             right = left
#         return result


def numberOfSubstrings(s: str) -> int:
    count = {"a": 0, "b": 0, "c": 0}
    left = 0
    result = 0

    for right in range(len(s)):
        # Update the count for the current character
        count[s[right]] += 1

        # Check if the window contains all three characters
        while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
            # All substrings from `left` to `right` are valid, add them to the result
            result += len(s) - right
            # Shrink the window by moving the left pointer
            count[s[left]] -= 1
            left += 1

    return result


def insert_word_middle(sentence, word):
    words = sentence.split(" ")
    middle = len(words) // 2
    words.insert(middle, word)
    return " ".join(words)


def calculate_digit_sums(n):
    even = 0
    odd = 0
    for i in str(n):
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    print(str(even) + " " + str(odd))


def print_factors(n):
    result = ""
    for i in range(2, n):
        if n % i == 0:
            if i == n:
                result += str(i)
            else:
                result += str(i) + " "
    print(result if result != "" else -1)


class Solution:
    def power(x, n):
        if n == 0:
            return 1
        print(x * Solution.power(x, n - 1))


def populate():
    j = []
    total = 0
    for i in range(0, 4):
        json = {}
        json[i] = i
        j.append(json)
    return j


a = populate()


def addjson():
    j = populate()
    total = 0
    for i in range(len(j)):
        total += j[i][i]
    print(total)


def find_longest_words(word_list):
    if not word_list:
        return []

    # Find the maximum word length in the list
    max_length = max(len(word) for word in word_list)

    # Get all words that have the maximum length
    longest_words = [word for word in word_list if len(word) == max_length]

    return longest_words


def check_precedence(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stack = []
    output = []
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()  # Remove the '(' from the stack
        else:
            while (
                stack and stack[-1] != "(" and precedence[char] <= precedence[stack[-1]]
            ):
                output.append(stack.pop())
            stack.append(char)
            while stack:
                output.append(stack.pop())
            return output
        return output
    while stack:
        output.append(stack.pop())
    return output


def print_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):

            print(num, int(num**0.5) + 1, i)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def is_palindrome(s):
    s = str(s)
    return s == s[::-1]


def firstUniqChar(s: str):
    char_count = {}
    for i, char in enumerate(s):
        if char in char_count:
            return char_count.get(char)
        else:
            char_count[char] = i
    return -1


a = ("reverse")
b = a[::-1]

a = [1, 2, 3]
b = ['x', 'y']

# def maxVowels(s: str, k: int) -> int:
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     max_vowels = 0
#     current_vowels = 0
#     left = 0
#     for right in range(len(s)):
#         if s[right] in vowels:
#             current_vowels += 1
#         if right - left + 1 > k:
#             if s[left] in vowels:
#                 current_vowels -= 1
#             left += 1
#         max_vowels = max(max_vowels, current_vowels)
#     return max_vowels

def maxVowels(s: str, k: int) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_vowels = 0
    current_vowels = 0
    left = 0
    for right in range(len(s)):
        if s[right] in vowels:
            current_vowels += 1
        if right - left + 1 > k:
            if s[left] in vowels:
                current_vowels -= 1
            left += 1
        max_vowels = max(current_vowels, max_vowels)
    return max_vowels


def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
    max_length = 0
    left = 0
    count = {"T": 0, "F": 0}
    for right in range(len(answerKey)):
        count[answerKey[right]] += 1
        while count["T"] > k and count["F"] > k:
            count[answerKey[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

def addBinary(a: str, b: str) -> str:
    result = ""
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        result = str(total % 2) + result
        carry = total // 2
    return result

import math
def is_fibonacci(n):
    def is_perfect_square(m):
        sqr_num = int(math.sqrt(m))
        return sqr_num * sqr_num == m
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def pivotIndex(nums: list[int]) -> int:
    left = 0
    right = sum(nums)
    for i ,num in enumerate(nums):
        right -= num
        if right == left:
            return i
        left += num
    return -1

def findGCD(nums: List[int]) -> int:
        maxi = heapq.nlargest(1, nums)[0]
        mini = heapq.nsmallest(1, nums)[0]
        return math.gcd(maxi, mini)

class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        else:
            j = sum(int(digits) for digits in str(num))
            return Solution.addDigits(self, j)

def isPower(n: int) -> int:
    if n < 0: 
        return False
    print(n & (n - 1))
    return n & (n - 1) == 0

def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)  # Clears the least significant 1 bit
        print(n)
        count += 1
    return count

# def interchangeableRectangles(rectangles: List[List[int]]) -> int:
#         count = 0
#         for i, rectangle in enumerate(rectangles):
#             right = len(rectangles) - 1
#             while  right > i: 
#                 if rectangle[0] / rectangle[1] == rectangles[right][0] / rectangles[right][1]:
#                     print(rectangle[0] / rectangle[1])
#                     print(rectangles[right][0] / rectangles[right][1])
#                     count += 1
#                     right -= 1
#         return count
# print(interchangeableRectangles([[4,5],[7,8]]))

# def interchangeableRectangles(rectangles: List[List[int]]) -> int:
#     aspect_ratios = dict(int)
#     count = 0

#     for rectangle in rectangles:
#         # Calculate the aspect ratio using Fraction to avoid precision issues
#         aspect_ratio = Fraction(rectangle[0], rectangle[1])
        
#         # Add to count if aspect ratio was seen before
#         if aspect_ratio in aspect_ratios:
#             print(aspect_ratios[aspect_ratio])
#             count += aspect_ratios[aspect_ratio]
        
#         # Increment the count of this aspect ratio
#         aspect_ratios[aspect_ratio] += 1
#     print(aspect_ratios)
#     return count

def interchangeableRectangles(rectangles: List[List[int]]) ->int:
        ratios = {}
        count = 0
        for width, height in rectangles:
            ratio = width / height
            ratios[ratio] = ratios.get(ratio, 0) + 1
        for val in ratios.values():
            count += val * (val - 1) // 2
        return count

# Test the function
def ispalindrome():
    letter ="google"
    count = Counter(letter)
    for i, n in enumerate(letter):
        if count[n] == 1:
            return i
    return -1

def convert_fahrenheit_to_celsius():
    n = "0 100 20"
    n = n.split(" ")
    for i in range(int(n[0]), int(n[1])+1, int(n[2])):
        print(i, int((int(i) - 32) * 5/9))
def isSubsequence(s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        left = len(s)
        for i in range(len(t) - 1, -1, -1):
            if t[i] == s[left - 1]:
                left -= 1
            if left == 0:
                return True
        else: 
            return False
    
def generateParenthesis(n: int) -> List[str]:
    # Memoization dictionary to store intermediate results
    dp = {0: [""]}  # Base case: 0 pairs yield an empty string

    def dp_generate(pairs: int) -> List[str]:
        if pairs in dp:
            return dp[pairs]

        result = []
        for k in range(pairs):
            left = dp_generate(k)             # Well-formed parentheses for k pairs
            right = dp_generate(pairs - 1 - k)  # Well-formed parentheses for pairs - 1 - k pairs
            
            # Combine left and right parts wrapped in a new pair ()
            for l in left:
                for r in right:
                    result.append(f"({l}){r}")
        
        dp[pairs] = result
        return result

    # Generate for n pairs
    return dp_generate(n)

# Example usage

# def reverseString(s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         result = []
#         for i in range(len(s)-1, -1, -1):
#             result.append(s[i])
#         return result

def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        # Move pointers
        left += 1
        right -= 1
s = ["h", "e", "l", "l", "o"]
def chec(s):
    left = 0
    right = len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        # s[right], s[left] = s[left], s[right]
        left += 1
        right +=1
    return s


def calculate_premium_percentage(
        pet_to_be_used ,
        final_price: Decimal,
        premium_percentage: Decimal = Decimal(0.00),
       
    ) -> Decimal:
        """
        Calculate the final price including a premium based on the given final price and premium percentage.

        Parameters:
        - final_price (Decimal): The base price before applying the premium.
        - premium_percentage (Decimal, optional): The percentage value of the premium. Default is 0.00.

        Returns:
        - Decimal: The final price including the premium.
        """
        final_price_decimal = Decimal(str(final_price))
        premium_amount = final_price_decimal * (
            premium_percentage / Decimal("100.0")
        )
        premium_detail_amount = (round(premium_amount,2)) * pet_to_be_used
        # Calculate total amount
        final_price = Decimal(final_price) + premium_amount * pet_to_be_used
        return final_price

print(calculate_premium_percentage(1, 10, 10))