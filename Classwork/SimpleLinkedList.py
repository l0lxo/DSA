class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data}", end=' ')
            temp = temp.next
        print()

if __name__=="__main__":
    llist = LinkedList()
    llist.insertAtBeginning("New")
    llist.insertAtBeginning("Data")
    llist.insertAtBeginning("Is")
    llist.insertAtBeginning("New")
    llist.insertAtBeginning("Data")

    llist.print_list()