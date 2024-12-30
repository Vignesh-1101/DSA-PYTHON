def monotonicStack(arr):
    stack = []
    ans = []
    ans2 = []
    for i in range(len(arr) - 1, -1, -1):
        while len(stack) != 0 and stack[-1] < arr[i]:
            stack.pop()
        ans.append(stack[-1] if stack else -1)
        stack.append(arr[i])
    return ans


# print(monotonicStack([2,1,7,9,3,11,4,19]))

# def maxirightStack(arr):
#     stack = []
#     ans = []
#     for i in range(len(arr)):
#         while stack and stack[-1]


def maxArea(arr):
    n = len(arr)
    area = 0
    for i in range(n):
        for j in range(i + 1, n):
          
            # Calculating the max area
            area = max(area, min(arr[j], arr[i]) * (j - i))
    return area


# print(maxArea([12,6,1,8,9]))

def largest_histogram_area(heights):
    stack = []  # To store indices of histogram bars
    max_area = 0
    index = 0

    while index < len(heights):
        # Push the current index onto the stack if it's empty or the current bar is taller
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # Pop the top of the stack
            top = stack.pop()
            # Calculate the area with heights[top] as the smallest (or minimum height)
            height = heights[top]
            # If the stack is empty, the width is the entire length up to `index`
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)

    # Handle remaining bars in the stack
    while stack:
        top = stack.pop()
        height = heights[top]
        width = index if not stack else index - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

# # Example usage:
# histogram = [2, 1, 5, 6, 2, 3]
# print("Largest area:", largest_histogram_area(histogram))

def largest_histogram_area_bruteforce(heights):
    max_area = 0
    n = len(heights)
    for i in range(n):
        min_height = heights[i] 
        for j in range(i, n):
            min_height = min(min_height, heights[j])  
            width = j - i + 1
            max_area = max(max_area, min_height * width) 

    return max_area

# Example usage:
# histogram = [2, 1, 5, 7, 11, 6, 5, 4]
# print("Largest area (brute force):", largest_histogram_area_bruteforce(histogram))

def getMaxArea(arr, n):
    stack = []
    max_area = 0
    
    for i in range(n):
        # Maintain increasing order in the stack
        while stack and arr[stack[-1]] > arr[i]:
            h = arr[stack.pop()]
            # Width is the distance between current index and the index in stack after popping
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    # Process remaining bars in stack
    while stack:
        h = arr[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    return max_area

print(getMaxArea([2,1,5,6,2,3], 6))

