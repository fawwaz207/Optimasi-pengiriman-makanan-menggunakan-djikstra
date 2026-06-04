import heapq  #Mengimpor heapq untuk membuat priority queue, yaitu antrean yang otomatis mengambil jarak terkecil dulu
import matplotlib.pyplot as plt  #Mengimpor matplotlib untuk menggambar peta graph/rute


class Graph:  #Membuat class Graph sebagai wadah untuk menyimpan graph dan algoritma Dijkstra

    def __init__(self):  #Fungsi constructor, otomatis dipanggil saat objek Graph dibuat
        self.graph = {}  #Membuat dictionary kosong untuk menyimpan node dan tetangganya

    def add_edge(self, u, v, w):  #Fungsi untuk menambahkan jalan/edge dari node u ke node v dengan bobot w
        if u not in self.graph:  #Mengecek apakah node u belum ada di graph
            self.graph[u] = []  #Kalau belum ada, buat list kosong untuk menyimpan tetangga node u

        if v not in self.graph:  #Mengecek apakah node v belum ada di graph
            self.graph[v] = []  #Kalau belum ada, buat list kosong untuk menyimpan tetangga node v

        self.graph[u].append((v, w))  #Menambahkan v sebagai tetangga u dengan jarak/bobot w
        self.graph[v].append((u, w))  #Menambahkan u sebagai tetangga v karena graph ini dua arah

    def dijkstra(self, start):  #Fungsi untuk menjalankan algoritma Dijkstra dari titik awal start
        dist = {node: float("inf") for node in self.graph}  #Membuat jarak semua node menjadi tak hingga dulu
        parent = {node: None for node in self.graph}  #Membuat parent semua node kosong untuk menyimpan jalur sebelumnya
        dist[start] = 0  #Jarak dari titik awal ke dirinya sendiri adalah 0
        pq = [(0, start)]  #Membuat priority queue berisi titik awal dengan jarak 0

        while pq:  #Selama priority queue masih ada isinya, proses terus berjalan
            current_dist, current_node = heapq.heappop(pq)  #Mengambil node dengan jarak paling kecil dari priority queue

            if current_dist > dist[current_node]:  #Kalau jarak yang keluar ternyata lebih besar dari jarak terbaik terbaru
                continue  #Lewati node ini karena datanya sudah basi/tidak dipakai lagi

            for neighbor, weight in self.graph[current_node]:  #Mengecek semua tetangga dari node yang sedang diproses
                new_dist = current_dist + weight  #Menghitung jarak baru jika lewat current_node ke neighbor

                if new_dist < dist[neighbor]:  #Kalau jarak baru lebih pendek daripada jarak lama
                    dist[neighbor] = new_dist  #Update jarak neighbor menjadi jarak baru yang lebih pendek
                    parent[neighbor] = current_node  #Simpan current_node sebagai parent agar jalurnya bisa dilacak
                    heapq.heappush(pq, (new_dist, neighbor))  #Masukkan neighbor ke priority queue dengan jarak terbarunya

        return dist, parent  #Mengembalikan semua jarak terpendek dan parent untuk membentuk jalur

    def get_path(self, parent, target):  #Fungsi untuk menyusun jalur dari start ke target berdasarkan parent
        path = []  #Membuat list kosong untuk menyimpan urutan jalur
        current = target  #Mulai melacak jalur dari node tujuan

        while current is not None:  #Selama node saat ini masih ada parent-nya
            path.append(current)  #Masukkan node saat ini ke dalam list path
            current = parent[current]  #Pindah ke parent dari node saat ini

        path.reverse()  #Balik urutan path agar dari start ke target, bukan dari target ke start
        return path  #Mengembalikan jalur yang sudah tersusun


# --- KOORDINAT MANUAL AGAR PETA LEBIH REALISTIS ---

POSISI = {  #Dictionary untuk menyimpan posisi koordinat setiap node pada gambar peta
    'A': (0, 10),  #Koordinat node A di posisi x=0 dan y=10
    'B': (5, 12),  #Koordinat node B di posisi x=5 dan y=12
    'C': (2, 8),  #Koordinat node C di posisi x=2 dan y=8
    'D': (0, 6),  #Koordinat node D di posisi x=0 dan y=6
    'E': (3, 4),  #Koordinat node E di posisi x=3 dan y=4
    'F': (6, 7),  #Koordinat node F di posisi x=6 dan y=7
    'G': (5, 2),  #Koordinat node G di posisi x=5 dan y=2
    'H': (8, 3),  #Koordinat node H di posisi x=8 dan y=3
    'I': (12, 2),  #Koordinat node I di posisi x=12 dan y=2
    'J': (9, 6),  #Koordinat node J di posisi x=9 dan y=6
    'K': (10, 10),  #Koordinat node K di posisi x=10 dan y=10
    'L': (6, 9),  #Koordinat node L di posisi x=6 dan y=9
    'M': (11, 7),  #Koordinat node M di posisi x=11 dan y=7
    'N': (13, 5),  #Koordinat node N di posisi x=13 dan y=5
    'O': (8, 12),  #Koordinat node O di posisi x=8 dan y=12
    'P': (12, 11),  #Koordinat node P di posisi x=12 dan y=11
    'Q': (15, 10),  #Koordinat node Q di posisi x=15 dan y=10
    'R': (15, 6)  #Koordinat node R di posisi x=15 dan y=6
}


def tampilkan_peta(edges, path, start, target, total_dist):  #Fungsi untuk menggambar peta dan rute terpendek
    plt.clf()  #Membersihkan gambar sebelumnya agar peta baru tidak menumpuk

    #1. Gambar semua jalur dasar
    for u, v, w in edges:  #Mengulang semua edge/jalan yang ada di graph
        p1, p2 = POSISI[u], POSISI[v]  #Mengambil koordinat titik awal u dan titik akhir v
        plt.plot(  #Menggambar garis untuk jalan antara u dan v
            [p1[0], p2[0]],  #Mengambil koordinat x dari u dan v
            [p1[1], p2[1]],  #Mengambil koordinat y dari u dan v
            color='lightgray',  #Memberi warna abu-abu muda untuk jalur biasa
            linestyle='--',  #Membuat garis putus-putus
            alpha=0.5,  #Membuat garis agak transparan
            zorder=1  #Meletakkan garis di layer belakang
        )
        plt.text(  #Menampilkan angka bobot/jarak di tengah edge
            (p1[0] + p2[0]) / 2,  #Menentukan posisi x teks di tengah garis
            (p1[1] + p2[1]) / 2,  #Menentukan posisi y teks di tengah garis
            str(w),  #Mengubah bobot menjadi teks agar bisa ditampilkan
            fontsize=7,  #Mengatur ukuran tulisan bobot
            color='gray'  #Memberi warna abu-abu pada tulisan bobot
        )

    #2. Gambar rute terpendek yang terpilih
    path_edges = list(zip(path, path[1:]))  #Membuat pasangan node yang berurutan dalam rute terpendek

    for u, v in path_edges:  #Mengulang setiap pasangan node dalam rute terpendek
        p1, p2 = POSISI[u], POSISI[v]  #Mengambil koordinat node u dan node v
        plt.plot(  #Menggambar garis rute terpendek
            [p1[0], p2[0]],  #Mengambil koordinat x dari u dan v
            [p1[1], p2[1]],  #Mengambil koordinat y dari u dan v
            color='red',  #Memberi warna merah untuk rute terpendek
            linewidth=3,  #Membuat garis rute lebih tebal
            zorder=2  #Meletakkan rute di atas jalur biasa
        )

    #3. Gambar semua titik kota/lokasi
    for node, (x, y) in POSISI.items():  #Mengulang semua node dan koordinatnya
        if node == start:  #Mengecek apakah node ini adalah titik awal
            color = 'lime'  #Jika titik awal, warnanya hijau terang
        elif node == target:  #Mengecek apakah node ini adalah titik tujuan
            color = 'red'  #Jika titik tujuan, warnanya merah
        elif node in path:  #Mengecek apakah node ini dilewati oleh rute terpendek
            color = 'orange'  #Jika dilewati rute, warnanya oranye
        else:  #Jika node bukan awal, bukan tujuan, dan bukan jalur
            color = 'skyblue'  #Node biasa diberi warna biru muda

        plt.scatter(  #Menggambar titik node pada peta
            x,  #Koordinat x node
            y,  #Koordinat y node
            s=600,  #Ukuran lingkaran node
            color=color,  #Warna node sesuai statusnya
            edgecolors='black',  #Memberi garis tepi hitam pada node
            zorder=3  #Meletakkan node di layer paling depan
        )
        plt.text(  #Menampilkan huruf nama node di tengah lingkaran
            x,  #Posisi x tulisan sama dengan posisi x node
            y,  #Posisi y tulisan sama dengan posisi y node
            node,  #Teks yang ditampilkan adalah nama node
            ha='center',  #Membuat teks rata tengah secara horizontal
            va='center',  #Membuat teks rata tengah secara vertikal
            fontweight='bold'  #Membuat huruf node menjadi tebal
        )

    plt.title(  #Membuat judul pada gambar peta
        f"Navigasi: {start} ke {target} | Jarak: {total_dist} km",  #Isi judul berupa start, target, dan total jarak
        fontsize=12  #Ukuran font judul
    )
    plt.axis('off')  #Menghilangkan sumbu x dan y agar tampilan seperti peta
    plt.draw()  #Menggambar/update tampilan plot
    plt.pause(0.1)  #Memberi jeda singkat agar gambar muncul saat program berjalan


#--- MAIN PROGRAM ---

gr = Graph()  #Membuat objek graph dari class Graph

edges = [  #List semua jalan/edge beserta bobot jaraknya
    ("A", "B", 1.8),  #Jalan dari A ke B dengan jarak 1.8 km
    ("A", "C", 1.4),  #Jalan dari A ke C dengan jarak 1.4 km
    ("A", "D", 1.6),  #Jalan dari A ke D dengan jarak 1.6 km
    ("B", "L", 1.3),  #Jalan dari B ke L dengan jarak 1.3 km
    ("B", "K", 1.9),  #Jalan dari B ke K dengan jarak 1.9 km
    ("C", "L", 1.4),  #Jalan dari C ke L dengan jarak 1.4 km
    ("D", "E", 1.1),  #Jalan dari D ke E dengan jarak 1.1 km
    ("E", "F", 1.3),  #Jalan dari E ke F dengan jarak 1.3 km
    ("E", "G", 1.4),  #Jalan dari E ke G dengan jarak 1.4 km
    ("F", "B", 0.8),  #Jalan dari F ke B dengan jarak 0.8 km
    ("F", "J", 1.8),  #Jalan dari F ke J dengan jarak 1.8 km
    ("G", "H", 0.8),  #Jalan dari G ke H dengan jarak 0.8 km
    ("H", "I", 2.1),  #Jalan dari H ke I dengan jarak 2.1 km
    ("H", "J", 0.6),  #Jalan dari H ke J dengan jarak 0.6 km
    ("I", "N", 1.1),  #Jalan dari I ke N dengan jarak 1.1 km
    ("J", "M", 0.5),  #Jalan dari J ke M dengan jarak 0.5 km
    ("K", "P", 0.7),  #Jalan dari K ke P dengan jarak 0.7 km
    ("K", "R", 2.3),  #Jalan dari K ke R dengan jarak 2.3 km
    ("L", "K", 1.6),  #Jalan dari L ke K dengan jarak 1.6 km
    ("L", "O", 0.7),  #Jalan dari L ke O dengan jarak 0.7 km
    ("M", "K", 0.9),  #Jalan dari M ke K dengan jarak 0.9 km
    ("M", "N", 2.0),  #Jalan dari M ke N dengan jarak 2.0 km
    ("N", "R", 0.9),  #Jalan dari N ke R dengan jarak 0.9 km
    ("O", "P", 1.8),  #Jalan dari O ke P dengan jarak 1.8 km
    ("P", "Q", 2.0),  #Jalan dari P ke Q dengan jarak 2.0 km
    ("Q", "R", 0.6),  #Jalan dari Q ke R dengan jarak 0.6 km
]

for u, v, w in edges:  #Mengulang semua data edge yang ada di list edges
    gr.add_edge(u, v, w)  #Memasukkan setiap edge ke dalam graph

plt.ion()  #Mengaktifkan mode interaktif matplotlib agar gambar bisa diperbarui berkali-kali

print("=== SISTEM NAVIGASI KATERING (DIJKSTRA) ===")  #Menampilkan judul program di terminal
print("Ketik 'EXIT' untuk keluar.\n")  #Memberi instruksi bahwa user bisa mengetik EXIT untuk keluar

while True:  #Loop utama agar program bisa dipakai berkali-kali
    start = input("\nLokasi saat ini  : ").upper()  #Meminta input lokasi awal lalu mengubahnya menjadi huruf besar

    if start == 'EXIT':  #Mengecek apakah user ingin keluar setelah input lokasi awal
        break  #Menghentikan loop jika user mengetik EXIT

    target = input("Lokasi tujuan    : ").upper()  #Meminta input lokasi tujuan lalu mengubahnya menjadi huruf besar

    if target == 'EXIT':  #Mengecek apakah user ingin keluar setelah input lokasi tujuan
        break  #Menghentikan loop jika user mengetik EXIT

    #Validasi input
    if start not in POSISI or target not in POSISI:  #Mengecek apakah start atau target tidak ada di daftar node
        print("Error: Lokasi tidak terdaftar di peta!")  #Menampilkan pesan error jika lokasi tidak valid
        continue  #Kembali ke awal loop untuk meminta input lagi

    if start == target:  #Mengecek apakah lokasi awal dan tujuan sama
        print("Anda sudah berada di lokasi tujuan.")  #Memberi tahu user bahwa tidak perlu mencari rute
        continue  #Kembali ke awal loop untuk meminta input lagi

    dist, parent = gr.dijkstra(start)  #Menjalankan Dijkstra dari lokasi awal untuk mencari jarak terpendek
    path = gr.get_path(parent, target)  #Mengambil jalur dari start ke target berdasarkan parent

    print(f"✅ Rute Ditemukan: {' -> '.join(path)}")  #Menampilkan rute terpendek dalam bentuk A -> B -> C
    print(f"✅ Jarak Terpendek: {dist[target]} km")  #Menampilkan total jarak terpendek ke tujuan

    tampilkan_peta(edges, path, start, target, dist[target])  #Menampilkan gambar peta dan menyorot rute terpendek

print("\nProgram ditutup.")  #Menampilkan pesan bahwa program sudah selesai
plt.ioff()  #Mematikan mode interaktif matplotlib
plt.show()  #Menampilkan plot terakhir agar tidak langsung tertutup
