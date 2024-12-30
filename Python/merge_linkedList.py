from heapq import heappush, heappop

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __lt__(self, other):
        # Define comparison for the priority queue based on node value
        return self.value < other.value

def merge_and_sort_linkedlists(lists):
    if not lists:
        return None

    # Min-Heap (Priority Queue)
    min_heap = []

    # Add the head of each list to the priority queue
    for l in lists:
        while l:  # Push all elements into the heap
            heappush(min_heap, l.value)
            l = l.next

    # Dummy head for the resulting merged sorted list
    dummy = ListNode()
    current = dummy

    # Extract from heap and build the sorted merged list
    while min_heap:
        smallest_value = heappop(min_heap)
        current.next = ListNode(smallest_value)
        current = current.next
    print(dummy.value)
    return dummy.next
# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(" -> ".join(map(str, values)))

# Input: Array of unsorted linked lists
# list1 = create_linked_list([3, 1, 4])
# list2 = create_linked_list([2, 7, 5])
# list3 = create_linked_list([9, 7, 8])

# # Merge and sort the lists
# sorted_merged_list = merge_and_sort_linkedlists([list1, list2, list3])

# # Print the merged sorted linked list
# print_linked_list(sorted_merged_list)

from collections import Counter
from heapq import heappush, heappop

def k_most_frequent_elements(nums, k):
    frequency = {}
    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1
    
    min_heap = []
    for num, freq in frequency.items():
        heappush(min_heap, (freq, num)) 
        if len(min_heap) > k:
            heappop(min_heap)
    
    result = [num for freq, num in min_heap]
    return result

nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
k = 2

result = k_most_frequent_elements(nums, k)
print("The", k, "most frequent elements are:", result)


