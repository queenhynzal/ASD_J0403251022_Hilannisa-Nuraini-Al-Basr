# ======================================================================================
# Nama   : Hilannisa Nuraini Al'Basr
# NIM    : J0403251022
# Kelas  : A1
# ======================================================================================

# ======================================================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# ======================================================================================

import heapq

# Representasi weighted graph antar kota
graph = {

    'Bogor': {
        'Jakarta': 5,
        'Depok': 2
    },

    'Depok': {
        'Jakarta': 2,
        'Bandung': 6
    },

    'Jakarta': {
        'Bandung': 7
    },

    'Bandung': {}
}

def dijkstra(graph, start):
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak awal = 0
    distances[start] = 0
    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak lebih besar dari data sebelumnya
        if current_distance > distances[current_node]:
            continue

        # Periksa tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Node awal
start_node = 'Bogor'

# Menjalankan algoritma Dijkstra
hasil = dijkstra(graph, start_node)

# Menampilkan hasil
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")

# ======================================================================================
# Jawaban Analisis:
#
# 1. Node awal yang digunakan apa?
#    Node awal yang digunakan adalah Bogor
#
# 2. Node mana yang memiliki jarak paling kecildari node awal?
#    Node dengan jarak paling kecil adalah Depok
#
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Node dengan jarak paling besar adalah Bandung
#
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Algoritma Dijkstra bekerja dengan memilih node dengan jarak terkecil terlebih 
#    dahulu, kemudian memperbarui jarak ke node tetangga hingga semua node mendapatkan
#    jarak minimum.
# ======================================================================================