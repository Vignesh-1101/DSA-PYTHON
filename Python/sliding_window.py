def sliding_window(arr, k):
    for i in range(len(arr)):
        if len(arr[i : i + k]) >= 3:
            print(max(arr[i : i + k]))


# sliding_window([2,7,3,1,5,11,8,9], 3)


from collections import deque

def sliding_windows(arr, k):
    if k > len(arr):
        return  # Edge case: window size larger than array

    dq = deque()  # Store indices of array elements
    result = []  # Store the max values for each window

    for i in range(len(arr)):
        # Remove elements not within the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove elements smaller than the current element
        # They will not be the maximum for the current window
        # 2 < 7
        # 7 < 5
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        # Add the current element's index
        dq.append(i)

        # Append the max value for the window to the result
        if i >= k - 1:
            result.append(arr[dq[0]])

    for val in result:
        print(val)

sliding_windows([2, 7, 3, 1, 5, 11, 8, 9], 3)
