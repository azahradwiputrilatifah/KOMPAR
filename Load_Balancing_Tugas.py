class RoundRobinBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        # Mengambil server berdasarkan indeks saat ini
        server = self.servers[self.index]
        # Menggeser indeks ke server berikutnya (memutar balik ke 0 jika sudah di akhir)
        self.index = (self.index + 1) % len(self.servers)
        return server

# Simulasi
if __name__ == "__main__":
    # Daftar server yang tersedia
    daftar_server = ["Server_A", "Server_B", "Server_C"]
    balancer = RoundRobinBalancer(daftar_server)

    # Simulasi 10 permintaan (requests) masuk
    print(f"Memulai Load Balancer dengan server: {daftar_server}\n")
    for i in range(1, 11):
        target = balancer.get_next_server()
        print(f"Request #{i:02} diarahkan ke: {target}")