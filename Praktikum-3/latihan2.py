class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # tambah node di akhir
    def append(self, data):
        new_node = Node(data)

        # jika list kosong
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # fungsi pencarian
    def search(self, key):
        # jika kosong
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return

            temp = temp.next

            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")


# ================= MAIN PROGRAM ================= #

cll = CircularLinkedList()

# input elemen
data_input = input("Masukkan elemen ke dalam Circular Linked List: ")

if data_input.strip() != "":
    elements = data_input.split(",")
    for item in elements:
        cll.append(int(item.strip()))

# input pencarian
key = int(input("Masukkan elemen yang ingin dicari: "))

# lakukan pencarian
cll.search(key)
