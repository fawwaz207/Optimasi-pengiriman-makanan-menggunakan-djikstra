import heapq
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph: self.graph[u] = []
        if v not in self.graph: self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, start):
        dist = {node: float("inf") for node in self.graph}
        parent = {node: None for node in self.graph}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            current_dist, current_node = heapq.heappop(pq)
            if current_dist > dist[current_node]: continue
            for neighbor, weight in self.graph[current_node]:
                new_dist = current_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    parent[neighbor] = current_node
                    heapq.heappush(pq, (new_dist, neighbor))
        return dist, parent

    def get_path(self, parent, target):
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path

# KOORDINAT MANUAL (Agar Peta Lebih Nyata) 
POSISI = {
    'A': (0, 10), 'B': (5, 12), 'C': (2, 8), 'D': (0, 6),
    'E': (3, 4), 'F': (6, 7), 'G': (5, 2), 'H': (8, 3),
    'I': (12, 2), 'J': (9, 6), 'K': (10, 10), 'L': (6, 9),
    'M': (11, 7), 'N': (13, 5), 'O': (8, 12), 'P': (12, 11),
    'Q': (15, 10), 'R': (15, 6)
}

def tampilkan_peta(edges, path, start, target, total_dist):
    plt.clf()
    # 1. Menggambar semua jalur dasar
    for u, v, w in edges:
        p1, p2 = POSISI[u], POSISI[v]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='lightgray', linestyle='--', alpha=0.5, zorder=1)   #jaringan jalan
        plt.text((p1[0]+p2[0])/2, (p1[1]+p2[1])/2, str(w), fontsize=7, color='gray')    #angka jarak

    # 2. Menggambar rute terpendek yang terpilih
    path_edges = list(zip(path, path[1:]))
    for u, v in path_edges:
        p1, p2 = POSISI[u], POSISI[v]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='red', linewidth=3, zorder=2)

    # 3. Menggambar semua titik kota
    for node, (x, y) in POSISI.items():
        # Logika Warna
        if node == start: color = 'lime'      # Awal
        elif node == target: color = 'red'    # Tujuan
        elif node in path: color = 'orange'   # Dilewati
        else: color = 'skyblue'               # Biasa
        
        plt.scatter(x, y, s=600, color=color, edgecolors='black', zorder=3)
        plt.text(x, y, node, ha='center', va='center', fontweight='bold')

    plt.title(f"Navigasi: {start} ke {target} | Jarak: {total_dist} km", fontsize=12)
    plt.axis('off')
    plt.draw()
    plt.pause(0.1)

# MAIN PROGRAM
if __name__ == "__main__":
    g = Graph()
    edges = [
        ("A", "B", 1.8), ("A", "C", 1.4), ("A", "D", 1.6), ("B", "L", 1.3),
        ("B", "K", 1.9), ("C", "L", 1.4), ("D", "E", 1.1), ("E", "F", 1.3),
        ("E", "G", 1.4), ("F", "B", 0.8), ("F", "J", 1.8), ("G", "H", 0.8),
        ("H", "I", 2.1), ("H", "J", 0.6), ("I", "N", 1.1), ("J", "M", 0.5),
        ("K", "P", 0.7), ("K", "R", 2.3), ("L", "K", 1.6), ("L", "O", 0.7),
        ("M", "K", 0.9), ("M", "N", 2.0), ("N", "R", 0.9), ("O", "P", 1.8),
        ("P", "Q", 2.0), ("Q", "R", 0.6),
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    plt.ion()
    print("SISTEM NAVIGASI KATERING (DIJKSTRA)")
    print("Ketik 'EXIT' untuk keluar.\n")

    while True: 
        start = input("\nLokasi saat ini  : ").upper()
        if start == 'EXIT': break
        target = input("Lokasi tujuan    : ").upper()
        if target == 'EXIT': break

        # Validasi Input
        if start not in POSISI or target not in POSISI:
            print("Error: Lokasi tidak terdaftar di peta!")
            continue
        
        if start == target:
            print("Kamu sudah berada di lokasi tujuan.")
            continue

        dist, parent = g.dijkstra(start)
        path = g.get_path(parent, target)

        print(f"Rute Ditemukan: {' -> '.join(path)}")
        print(f"Jarak Terpendek: {dist[target]} km")
        
        tampilkan_peta(edges, path, start, target, dist[target])

    print("\nProgram ditutup.")
    plt.ioff()
    plt.show()