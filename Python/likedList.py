class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    # def __init__(self, value) -> None:
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 0

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += ' -> '
            temp = temp.next
        return result
    
    def add_first(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def getnode(self, value):
        if value == -1:
            return self.tail
        if value < -1 or value >= self.length:
            return None
        current_node = self.head
        for _ in range(value-1):
            current_node = current_node
        return current_node
    
    def set_value(self, index, value):
        temp = self.getnode(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def pop_last(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()
        pre = self.getnode(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index < 0:
            return False
        elif index == 0:
            self.add_first(value)
        # elif index >= self.length:
        #     self.add_last(value)
        else:
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True



v = LinkedList()
v.append(10)
v.append(20)
v.append(30)
v.append(40)
v.append(50)
# v.add_first(100)
# v.add_last(200)
v.insert(2, 1000)
print(v.head.value)
print(v.tail.value)
print(v)
print(v.getnode(2).value)


