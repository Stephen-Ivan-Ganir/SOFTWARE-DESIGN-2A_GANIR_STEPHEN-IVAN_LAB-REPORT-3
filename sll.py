class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def iterate_item(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def append_item(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

items = singly_linked_list()
items.append_item('Software')
items.append_item('Design')
items.append_item('COE-2A')

for val in items.iterate_item():
    print(val)

print("\nhead.data: ",items.head.data)
print("tail.data: ",items.tail.data)