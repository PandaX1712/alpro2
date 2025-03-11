# Program menghitung total belanja dengan berbagai kompleksitas algoritma
import time

def hitung_total_o1(daftar_belanja):
    """
    Menghitung total belanja dengan kompleksitas O(1)
    Hanya bisa digunakan jika total sudah dihitung sebelumnya
    """
    return daftar_belanja["total"]

def hitung_total_on(daftar_belanja):
    """
    Menghitung total belanja dengan kompleksitas O(n)
    n adalah jumlah item dalam daftar belanja
    """
    total = 0
    for item in daftar_belanja:
        total += item["harga"] * item["jumlah"]
    return total

def hitung_total_on2(daftar_belanja):
    """
    Menghitung total belanja dengan kompleksitas O(n²)
    Implementasi yang tidak efisien - hanya untuk demonstrasi
    """
    total = 0
    for i in range(len(daftar_belanja)):
        for j in range(1):  # Loop yang tidak perlu untuk demonstrasi O(n²)
            total += daftar_belanja[i]["harga"] * daftar_belanja[i]["jumlah"]
    return total

# Fungsi untuk mengukur waktu eksekusi
def ukur_waktu(fungsi, *args):
    waktu_mulai = time.time()
    hasil = fungsi(*args)
    waktu_selesai = time.time()
    waktu_eksekusi = waktu_selesai - waktu_mulai
    return hasil, waktu_eksekusi

# Contoh penggunaan
if __name__ == "__main__":
    # Data belanja
    belanja = [
        {"nama": "Beras", "harga": 12000, "jumlah": 5},
        {"nama": "Telur", "harga": 25000, "jumlah": 1},
        {"nama": "Minyak Goreng", "harga": 20000, "jumlah": 2},
        {"nama": "Gula", "harga": 15000, "jumlah": 1},
        {"nama": "Kecap", "harga": 8000, "jumlah": 3}
    ]
    
    # Menghitung total yang benar terlebih dahulu
    total_benar = hitung_total_on(belanja)
    
    # Contoh O(1) - menggunakan total yang sudah dihitung dengan benar
    belanja_dengan_total = {"items": belanja, "total": total_benar}
    
    # Ukur waktu eksekusi O(1)
    hasil_o1, waktu_o1 = ukur_waktu(hitung_total_o1, belanja_dengan_total)
    print(f"Total belanja (O(1)): {hasil_o1}, Waktu: {waktu_o1:.10f} detik")
    
    # Ukur waktu eksekusi O(n)
    hasil_on, waktu_on = ukur_waktu(hitung_total_on, belanja)
    print(f"Total belanja (O(n)): {hasil_on}, Waktu: {waktu_on:.10f} detik")
    
    # Ukur waktu eksekusi O(n²)
    hasil_on2, waktu_on2 = ukur_waktu(hitung_total_on2, belanja)
    print(f"Total belanja (O(n²)): {hasil_on2}, Waktu: {waktu_on2:.10f} detik")