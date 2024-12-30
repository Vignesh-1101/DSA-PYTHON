class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.tail.next = new_node
        self.length += 1
    
    def pop_last(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


def permutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i] 
    nums[i + 1:] = reversed(nums[i + 1:])
nums = [1, 2, 3]
permutation(nums)
print(nums)
# obj = LinkedList()
# obj.append(10)
# obj.append(20)
# print(obj.pop_last)
# print(obj.head.value, obj.tail.value, obj.length)

