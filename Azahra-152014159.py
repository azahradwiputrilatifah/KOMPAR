import random

# List server yang tersedia
servers = ['Server_Pusat_A', 'Server_Pusat_B', 'Server_Pusat_C']

# Simulasi beban kerja (misal: ukuran request dalam MB atau waktu proses dalam ms)
# Data ini diibaratkan trafik yang masuk ke sistem
incoming_requests = [15, 42, 28, 10, 55, 30, 18, 45]

def dynamic_load_balancing():
    print(f"=== SIMULASI DYNAMIC DISTRIBUTION (NRP: 159) ===")
    
    # Inisialisasi beban awal semua server adalah 0
    server_status = {s: 0 for s in servers}
    
    print("Mulai mendistribusikan beban secara dinamis...\n")
    
    for i, load in enumerate(incoming_requests):
        # LOGIKA DINAMIS: Mencari server dengan total beban terendah saat ini
        selected_server = min(server_status, key=server_status.get)
        
        # Update beban server yang dipilih
        server_status[selected_server] += load
        
        print(f"Request ke-{i+1} (Beban: {load}) dialokasikan ke -> {selected_server}")
        print(f"Status Beban Saat Ini: {server_status}\n")

    # Menentukan Expected Optimal Time
    # Optimal time tercapai ketika server yang paling sibuk menyelesaikan tugasnya
    optimal_time = max(server_status.values())
    
    print("-" * 45)
    print(f"HASIL AKHIR DISTRIBUSI: {server_status}")
    print(f"STATUS: Expected Optimal Time tercapai pada {optimal_time}ms.")
    print("-" * 45)

if __name__ == "__main__":
    dynamic_load_balancing()