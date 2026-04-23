from multiprocessing import Process, Queue

# Data suhu tiap sensor (dalam °C)
sensor_data = [32, 28, 35, 30]

def baca_sensor(sensor_id, queue):
    suhu = sensor_data[sensor_id]
    print(f"Sensor {sensor_id} membaca suhu: {suhu}°C")
    queue.put(suhu)

if __name__ == "__main__":
    processes = []
    queue = Queue()
    num_sensors = 4

    # Jalankan tiap sensor sebagai proses terpisah
    for i in range(num_sensors):
        p = Process(target=baca_sensor, args=(i, queue))
        processes.append(p)
        p.start()

    # Kumpulkan hasil dari semua sensor
    total = 0
    for _ in range(num_sensors):
        total += queue.get()
    
    for p in processes:
        p.join()

    rata_rata = total / num_sensors
    print(f"\nRata-rata suhu semua sensor: {rata_rata:.1f}°C")