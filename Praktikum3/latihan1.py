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

    # ===== FUNGSI DELETE NODE ===== #
    def delete_node(self, key):
        temp = self.head

        # Jika node yang dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        # Cari node yang akan dihapus
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika data tidak ditemukan
        if temp is None:
            print("Data tidak ditemukan")
            return

        # Hapus node
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
