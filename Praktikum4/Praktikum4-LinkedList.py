#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

#=======================================================================================
#Implementai Dasar : Node pada Linked List
#=======================================================================================

class Node:
    #konsuktor yang dijalankan secara otomatis ketika Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1) membuat node dengan instantiasi clas node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4) Tranversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

#=======================================================================================
#Implementai Dasar : Stack
#=======================================================================================

