class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

class CreateList:
    def __init__(self):
        self.head = Node(None);
        self.tail = Node(None);
        self.head.next = self.tail;
        self.tail.next = self.head;

    def add(self, data):
        newNode = Node(data);
        if self.head.data is None:
            self.head = newNode;
            self.tail = newNode;
            newNode.next = self.head;
        else:
            self.tail.next = newNode;
            self.tail = newNode;
            self.tail.next = self.head;

    def show(self):
        current = self.head;
        if self.head is None:
            print("List is empty");
            return;
        else:
            print("Nodes of the circular linked list: ");
            print(current.data),
            while (current.next != self.head):
                current = current.next;
                print(current.data),


class CircularLinkedList:
    cll = CreateList();
    cll.add(1);
    cll.add(2);
    cll.add(3);
    cll.add(4);
    cll.show();