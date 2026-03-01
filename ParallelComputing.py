from multiprocessing import Pool
import time

# Parallel Computing - Proses bersama dalam waktu bersamaan
def proses_parallel(angka):
    time.sleep(1)  # Simulasi proses
    return f"Data {angka} diproses, hasil: {angka * 3}"

def parallel_computing():
    print("=== PARALLEL COMPUTING ===")
    print("Banyak proses dijalankan BERSAMAAN")
    
    data = [1, 2, 3, 4]
    
    start = time.time()
    with Pool() as pool:
        hasil = pool.map(proses_parallel, data)
    
    for h in hasil:
        print(h)
    
    print(f"Total waktu parallel: {time.time()-start:.2f} detik")

if __name__ == "__main__":
    parallel_computing()

#SERIAL COMPUTING
import time

# Serial Computing - Proses berurutan
def serial_computing():
    print("=== SERIAL COMPUTING ===")
    print("Proses dijalankan satu per satu secara berurutan")
    
    data = [1, 2, 3, 4]
    
    start = time.time()
    for angka in data:
        time.sleep(1)  # Simulasi proses 1 detik
        hasil = angka * 2
        print(f"Data {angka} -> Hasil: {hasil}")
    
    print(f"Total waktu: {time.time()-start:.2f} detik")

serial_computing()