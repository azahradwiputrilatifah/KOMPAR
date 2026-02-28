from multiprocessing import Process, Queue

def kali_matriks(start, end, C, D, q, pid):
    print(f"Proses {pid}: hitung baris {start} sampai {end-1}")
    hasil = []
    for i in range(start, end):
        baris = []
        for j in range(2):
            total = C[i][0]*D[0][j] + C[i][1]*D[1][j]
            baris.append(total)
        hasil.append((i, baris))
    q.put(hasil)

if __name__ == "__main__":
    # Matriks C (3x2) dan D (2x2)
    C = [[13, 8], [10, 9], [42, 23]]
    D = [[1, 8], [24, 4]]
    
    print("Matriks C =", C)
    print("Matriks D =", D)
    print("-" * 30)
    
    q = Queue()
    
    # Buat 2 proses
    p1 = Process(target=kali_matriks, args=(0, 2, C, D, q, 1))
    p2 = Process(target=kali_matriks, args=(2, 3, C, D, q, 2))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    # Kumpulkan hasil
    hasil = []
    for _ in range(2):
        hasil.extend(q.get())
    hasil.sort()
    
    print("-" * 30)
    print("Hasil C x D =")
    for baris in hasil:
        print(f"  {baris[1]}")
    
    # Verifikasi
    print("-" * 30)
    print("Verifikasi manual:")
    print("Baris 0: 13*1 + 8*24 = 205, 13*8 + 8*4 = 136")
    print("Baris 1: 10*1 + 9*24 = 226, 10*8 + 9*4 = 116")
    print("Baris 2: 42*1 + 23*24 = 594, 42*8 + 23*4 = 428")