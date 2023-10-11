class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next


    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next


    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


    def printlist(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = List()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.printlist()
my_list.delete(2)
my_list.printlist()
my_list.update(3, 4)
my_list.printlist()
print(my_list.search(4))
print(my_list.search(5))
