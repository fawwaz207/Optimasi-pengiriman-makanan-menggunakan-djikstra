🚀 Sistem Navigasi Katering Menggunakan Algoritma Dijkstra

Program ini merupakan implementasi Algoritma Dijkstra menggunakan bahasa pemrograman Python untuk mencari jalur tercepat (shortest path) antar lokasi pada sistem navigasi katering.
Program juga dilengkapi dengan visualisasi graf/peta interaktif menggunakan library matplotlib. 

📌 Deskripsi Project
Dalam sistem pengantaran katering, menentukan jalur tercepat sangat penting agar pengiriman lebih efisien dan hemat waktu.

Program ini dibuat untuk:

mencari rute tercepat, menghitung total jarak minimum, memvisualisasikan jalur pada peta

menggunakan metode:

- Graph
- Priority Queue
- Algoritma Dijkstra

🎯 Tujuan Program

1.Mengimplementasikan algoritma Dijkstra
2.Memahami konsep graph pada Struktur Data & Algoritma
3. Menampilkan visualisasi jalur terpendek
4. Membantu simulasi sistem navigasi pengantaran katering

✨ Fitur Program
✅ Mencari jalur tercepat
✅ Menghitung total jarak minimum
✅ Visualisasi peta otomatis
✅ Tampilan node dan edge
✅ Input lokasi interaktif
✅ Jalur tercepat ditandai warna merah
✅ Titik awal & tujuan diberi warna berbeda

🛠️ Teknologi yang Digunakan

- Teknologi	Fungsi
- Python	Bahasa pemrograman utama
- heapq	Priority Queue
- matplotlib	Visualisasi graf/peta

📂 Struktur Folder
SDA-TUGAS/
│
├── SDA TUGAS.py
├── README.md
└── assets/
    └── screenshot.png

⚙️ Cara Kerja Program
Program bekerja dengan langkah berikut:

1.User memasukkan lokasi awal
2.User memasukkan lokasi tujuan
3.Program menghitung jalur tercepat menggunakan algoritma Dijkstra

Program menampilkan:
- rute tercepat
- total jarak
- visualisasi jalur pada peta

📖 Penjelasan Algoritma Dijkstra
Algoritma Dijkstra digunakan untuk mencari jarak terpendek dari satu titik ke titik lainnya pada graph berbobot positif.

Cara Kerja:

1. Tentukan node awal
2. Set semua jarak node lain = infinity
3. Pilih node dengan jarak terkecil
4. Update jarak tetangga node
5. Ulangi sampai semua node dikunjungi

🧠 Konsep yang Digunakan
1. Graph
Graph terdiri dari:

- Node (titik/lokasi)
- Edge (jalur antar lokasi)
- Weight (jarak)

Contoh:

A ----- B
 \     /
   \ /
    C

2. Priority Queue
Digunakan untuk mengambil node dengan jarak terkecil secara efisien menggunakan heapq.

▶️ Cara Menjalankan Program
1. Install Python
Pastikan Python sudah terinstall.

2. Download Repository
Clone GitHub
git clone https://github.com/fawwaz207/optimasi-pengiriman-makanan-menggunakan-djikstra-repository.git

3. Install Library
Program membutuhkan library:

matplotlib

Install dengan command:

pip install matplotlib

4. Jalankan Program
Masuk ke folder project lalu jalankan:

python "SDA TUGAS.py"
🖥️ Contoh Input
Lokasi saat ini  : A
Lokasi tujuan    : R
📤 Contoh Output
✅ Rute Ditemukan: A -> B -> K -> R
✅ Jarak Terpendek: 6.0 km
Program juga akan menampilkan visualisasi peta seperti berikut:

🟢 Titik awal

🔴 Titik tujuan

🟠 Jalur yang dilewati

🔵 Node biasa

📍 Daftar Node Lokasi
Node	Keterangan
A	Lokasi A
B	Lokasi B
C	Lokasi C
D	Lokasi D
E	Lokasi E
F	Lokasi F
G	Lokasi G
H	Lokasi H
I	Lokasi I
J	Lokasi J
K	Lokasi K
L	Lokasi L
M	Lokasi M
N	Lokasi N
O	Lokasi O
P	Lokasi P
Q	Lokasi Q
R	Lokasi Tujuan

Kompleksitas Algoritma
Operasi	Kompleksitas
Dijkstra dengan Heap	O((V + E) log V)
Keterangan:

V = jumlah vertex/node

E = jumlah edge/jalur

Validasi Input
Program memiliki validasi:

lokasi harus tersedia di peta

lokasi awal ≠ lokasi tujuan

ketik EXIT untuk keluar program

📚 Materi yang Digunakan
Graph

Weighted Graph

Priority Queue

Shortest Path

Dijkstra Algorithm

Author:

Dalilah Putri Rahma (25031554239)

Aulia Mayza Widianto (25031554131)

Mochammad Fawwaz Muslih (25031554126)

Mata Kuliah
Struktur Data & Algoritma

Universitas
Universitas Negeri Surabaya

Pengembangan Selanjutnya
Project ini masih dapat dikembangkan menjadi:

GUI menggunakan Tkinter

Sistem navigasi real-time

Integrasi Google Maps API

Penyimpanan database lokasi

Visualisasi animasi jalur

Kesimpulan
Program ini berhasil mengimplementasikan algoritma Dijkstra untuk mencari jalur tercepat pada sistem navigasi katering dengan visualisasi graf menggunakan Python dan matplotlib.

Lisensi
Project ini dibuat untuk kebutuhan pembelajaran dan tugas kuliah.


Terima kasih telah mengunjungi repository ini 😄
