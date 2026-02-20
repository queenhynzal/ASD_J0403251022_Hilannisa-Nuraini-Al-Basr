#=======================================================================================
#Nama   : Hilannisa Nuraini Al'Basr
#NIM    : J0403251022
#Kelas  : A1
#=======================================================================================

#=======================================================================================
#Implementai Dasar : Stack
#=======================================================================================

class Node:
    #konsuktor yang dijalankan secara otomatis ketika Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#Stack ada operasi push (memasukkan head baru) dan pop (penghapus head)

class stack:
    def __init__(self): 
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
        
    def is_empty(self):
        return self.top is None #stack kosong jika top = None
        
    def push(self,data): #memasukkan data baru pada stack
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node
        
        #2 node baru menunjuk ke top yang Lama (head lama)
        nodeBaru.next = self.top
        
        #3 geser top pindah ke node baru
        self.top = nodeBaru
        
        
    def pop(self): #mengambil / menghapus node paling atas
        
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        # B -> A -> None
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
        
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data
        
    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print ("Top ->" , end=" ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print ("None")
        
#Instantiasi Class Stack
s = stack ()
s.push('A')
s.push('B')
s.push('C')
s.tampilkan()
print("Peak (Lihat Top) : ", s.peek())
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()