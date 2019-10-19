class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None    

    def asc_ordered_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if temp.data > data:
            new_node.next = temp
            self.head = new_node
            return

        while temp.next:
            if temp.next.data > data:
                break
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def desc_ordered_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if data > temp.data:
            new_node.next = temp
            self.head = new_node
            return

        while temp.next:
             if temp.data > data and temp.next.data <= data:
                 break
             temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def display_list(self):
        temp = self.head
        while temp is not None:
            print("data = {0}".format(temp.data))
            temp = temp.next
    
    def peek(self, index):
        curr = self.head
        while curr is not None and index > 1:
            curr = curr.next
            index-=1
        print(curr.data)

if __name__ == "__main__":
    llist = LinkedList()
    n = int(input())
    li = list(map(int, input().split()))
    for e in li:
        llist.desc_ordered_list(e)
    i = int(input())
    llist.peek(i)

