from collections import Counter
from functools import reduce


def frequencySort(s: str) -> str:
    # ssgysyqa
    final = ""
    words = Counter(s)
    print(list(words.keys()))
    for word in words:
        print(word)
        final += word * words[word]
    print(words)
    print(final)


def bfrequencySort(cars: str) -> str:
    frequency = Counter(cars)

    # Step 2: Sort cars by frequency (descending) and lexicographically
    sorted_cars = sorted(frequency.keys(), key=lambda x: (-frequency[x], x))

    # Step 3: Build the result string based on sorted order and frequencies
    result = "".join(car * frequency[car] for car in sorted_cars)

    print(result)


# bfrequencySort("ssgysyqa")


# [(3, 2), (1, 5), (4, 1)]
def sample_prblm(numbers):
    sorted_tuples = list(filter(lambda x: x % 2 == 0, numbers))
    print(sorted_tuples)


def sample2(numbers):
    sorted_tuples = reduce(lambda x, y: x * y, numbers)
    print(sorted_tuples)


def arrange(n, balls):
    final_map = Counter(balls)

    # Define the order and build the result string based on the count
    result = "".join(char * final_map[char] for char in "SWG" if char in final_map)

    print(" ".join(result))


def print_array(n, arr):
    for i in range(0, n - 1, 2):
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
    print(" ".join(str(a) for a in arr))


def maxelemetnfromarray(n, arr):
    max_element = Counter(arr)
    print(max_element)
    max_element = max(max_element.values())
    print(max_element)


def solve(n, x, y):
    friends = list(zip(x, y))

    friends.sort()

    visited = [False] * n  # Keep track of used friends
    days = 0  # Counter for the number of valid days

    while True:
        total_food = 0
        total_budget = 0
        group = []

        # Try to form a group
        for i in range(n):
            if not visited[i]:  # Friend not used yet
                total_food += friends[i][0]
                total_budget += friends[i][1]
                group.append(i)

                if len(group) >= 2 and total_food <= total_budget:
                    break  # Group is valid

        # If a valid group was formed
        if len(group) >= 2 and total_food <= total_budget:
            days += 1  # Increment days
            for idx in group:
                visited[idx] = True  # Mark these friends as used
        else:
            break  # No more valid groups can be formed

    print(days)


# print(solve(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))

# def MaximumPile(piles):
#       result = []
#       for i in range(len(piles)):
#         j = i + 3 -1
#         Vivek = piles[i]
#         while i < j and j < len(piles):
#           if piles[i]>piles[j]:
#             Vivek = min(Vivek, piles[j])
#           j-=1
#         result.append(Vivek)
#       return result


def max_stones_vivek(stones):
    # Sort the stones in descending order
    n = len(stones)
    stones.sort(reverse=True)
    print(stones, "stones")
    # Vivek gets the second maximum in each group of three
    vivek_stones = 0
    for i in range(1, n, 3):
        print(i, stones[i])
        vivek_stones += stones[i]

    return vivek_stones


# for i in range(1, 6, 3):
#     print(i)
# print(max_stones_vivek([2,4,9,8,11,2]))
def maxStones(piles):
    group1 = []
    group2 = []
    for i in range(len(piles)):
        if i % 2 == 0:
            group1.append(piles[i])
        else:
            group2.append(piles[i])

    group1.sort(reverse=True)
    group2.sort(reverse=True)
    return group1[1] + group2[1]
    # return vivek_stones, anurag_stones


# Test with given array
# piles = [2, 4, 9, 8, 11, 2]
# print(maxStones(piles))  # Should output 13


def frequencySort(s: str) -> str:
    # counts = {}
    # for i in s:
    #     if i in counts:
    #         counts[i] += 1
    #     else:
    #         counts[i] = 1
    #   sort = list(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    #   return "".join(s[0] * counts[s[0]] for s in sort)
    char = {}
    for i in s:
        char[i] = char.get(i, 0) + 1
    print(char)

    freq_list = [(key, count) for key, count in char.items()]
    # print(freq_list)
    # for i in range(len(freq_list)):
    #     for j in range(i + 1, len(freq_list)):
    #         if freq_list[i][1] < freq_list[j][1] or (freq_list[i][1] == freq_list[j][1] and freq_list[i][0] > freq_list[j][0]):
    #             freq_list[i], freq_list[j] = freq_list[j], freq_list[i]
    # print(freq_list)
    # return "".join(char * count for char, count in freq_list)

    for i in range(len(freq_list)):
        for j in range(i + 1, len(freq_list)):
            if freq_list[i][1] < freq_list[j][1] or (
                freq_list[i][1] == freq_list[j][1] and freq_list[i][0] > freq_list[j][0]
            ):
                # Swap if the frequency is smaller or if the character is lexicographically larger
                freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

    # Step 4: Build the result string based on sorted frequencies
    result = ""
    for char, freq in freq_list:
        result += char * freq
    return result
    # counts = Counter(s)
    # return ''.join(char * freq for char, freq in counts.most_common())


# print(frequencySort("tree"))


# arr = [2, 3, 4, 5, 6, 7, 8, 9]
# print(arr[0], arr[1], arr[2], arr[-2], arr[-1])
def count_anagrams(s, c):
    k = len(c)
    c_count = Counter(c)  # Frequency count of string `c`
    window_count = Counter(s[:k])  # Initial window of size `k`
    count = 0

    # Check the first window
    if window_count == c_count:
        count += 1

    # Slide the window
    for i in range(k, len(s)):
        # Add the next character to the window
        window_count[s[i]] += 1
        # Remove the first character of the previous window
        window_count[s[i - k]] -= 1
        # If count becomes zero, remove the key for comparison efficiency
        if window_count[s[i - k]] == 0:
            del window_count[s[i - k]]

        # Compare the current window count with `c` count
        if window_count == c_count:
            count += 1

    return count


# print(count_anagrams("aabaabaa", "aaba"))


def calculate_and_display_property(land_values):
    # To store the bounds
    n = len(land_values)
    left_bounds = [-1] * n
    right_bounds = [n] * n

    # Calculate left bounds using a monotonic decreasing stack
    stack = []
    for i in range(n):
        while stack and land_values[stack[-1]] <= land_values[i]:
            stack.pop()
        left_bounds[i] = stack[-1] if stack else -1
        stack.append(i)

    # Calculate right bounds using a monotonic decreasing stack
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and land_values[stack[-1]] <= land_values[i]:
            stack.pop()
        right_bounds[i] = stack[-1] if stack else n
        stack.append(i)

    # Calculate the total value for each king
    result = []
    for i in range(n):
        total_value = sum(land_values[left_bounds[i] + 1 : right_bounds[i]])
        result.append(total_value)

    return result


# print(calculate_and_display_property([1,8,6,10,15]))


def asteroid_collision(n, arr):
    stack = []

    for asteroid in arr:
        # If the asteroid is moving to the right, add it to the stack
        if asteroid > 0:
            stack.append(asteroid)
        else:
            # Process collision
            while stack and stack[-1] > 0:
                # There is a potential collision between a right-moving asteroid and the current left-moving asteroid
                print(abs(asteroid))
                if stack[-1] < abs(asteroid):
                    stack.pop()  # The right-moving asteroid explodes
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()  # Both arr explode
                    break
                else:
                    break
            else:
                # If no collision happens or the stack is empty, the current asteroid survives
                stack.append(asteroid)
      
    return stack


# print(asteroid_collision(3, [3, 5, -3]))

def maxPartition(n, arr):
        #Write your code here
      max_so_far = 0
      partions = 0
      for i in range(n):
        max_so_far = max(max_so_far, arr[i])
        if max_so_far == i:
            partions += 1
      return partions

# print(maxPartition(5, [1,0,2,3,4]))

def maxBreadthRamp(n, nums):
        #Write your code here
      # 6 0 8 2 1 5
      pairs = [(nums[i], i) for i in range(n)]
      pairs.sort()
      min_index = float('inf')
      max_breadth = 0
      for value, index in pairs:
        min_index = min(min_index, index)
        max_breadth = max(max_breadth, index - min_index)
      return max_breadth
# print(maxBreadthRamp(6, [6,0,8,2,1,5]))

def find132pattern(nums):
        stack = []
        third = float('-inf')
        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False
print(find132pattern([-1, 3, 2, 0]))