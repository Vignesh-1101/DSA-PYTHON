def print_first_negative_integer(arr, k):
    #Write your code here
    # 12 -1 -7 8 -15 30 16 28
    start = 0
    result = []
    for i in range(len(arr)):
      if i - start + 1 == k:
        is_negative = False
        for i in arr[start: i+1]:
          if i < 0:
            is_negative = True
            result.append(i)
            break
        if is_negative == False:
          result.append(0)
        start += 1
    print(result)


from collections import deque

def first_negative_in_every_window(arr, k):
    # Initialize deque to store indices of negative numbers
    negatives = deque()
    result = []

    # Iterate through the array
    for i in range(len(arr)):
        # Remove elements out of the current window
        if negatives and negatives[0] < i - k + 1:
            negatives.popleft()

        # Add current element's index if it is negative
        if arr[i] < 0:
            negatives.append(i)

        # If we've processed at least k elements, record the result
        if i >= k - 1:
            # Append the first negative in the deque, or 0 if deque is empty
            result.append(arr[negatives[0]] if negatives else 0)

    return result
print(first_negative_in_every_window([12, -1, -7, 8, -15, 30, 16, 28], 3))