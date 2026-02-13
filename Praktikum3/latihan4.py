class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def print_list(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


def merge_linked_list(ll1, ll2):
    merged = LinkedList()

    # salin Linked List 1
    temp = ll1.head
    while temp:
        merged.append(temp.data)
        temp = temp.next

    # salin Linked List 2
    temp = ll2.head
    while temp:
        merged.append(temp.data)
        temp = temp.next

    return merged


# ================= MAIN PROGRAM ================= #

ll1 = LinkedList()
ll2 = LinkedList()

# input Linked List 1
data1 = input("Masukkan elemen untuk Linked List 1: ")

if data1.strip() != "":
    for x in data1.split(","):
        ll1.append(int(x.strip()))

# input Linked List 2
data2 = input("Masukkan elemen untuk Linked List 2: ")

if data2.strip() != "":
    for x in data2.split(","):
        ll2.append(int(x.strip()))

# tampilkan Linked List 1
print("Linked List 1:", end=" ")
ll1.print_list()

# tampilkan Linked List 2
print("Linked List 2:", end=" ")
ll2.print_list()

# gabungkan
merged = merge_linked_list(ll1, ll2)

print("Linked List setelah digabungkan:", end=" ")
merged.print_list()
