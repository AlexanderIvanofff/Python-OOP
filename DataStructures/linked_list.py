class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'GET' Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'GET' Erase out of range!")
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1


my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()
my_list.erase(1)
my_list.display()
print(my_list.get(1))
