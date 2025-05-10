import math

def hitung_titik_sampling(diameter_cm, jumlah_titik):
    radius_cm = diameter_cm / 2
    titik_posisi = []

    print(f"\nTitik Sampling (jarak dari tepi cerobong, dalam cm):")
    for i in range(1, jumlah_titik + 1):
        # Rumus distribusi titik sampling isokinetik (EPA Method 1)
        posisi = radius_cm * math.sqrt((i - 0.5) / jumlah_titik)
        jarak_dari_tepi = radius_cm - posisi
        titik_posisi.append(round(jarak_dari_tepi, 2))
        print(f"Titik {i}: {round(jarak_dari_tepi, 2)} cm")

    return titik_posisi

# ==== INPUT ====
try:
    diameter = float(input("Masukkan diameter cerobong (dalam cm): "))
    jumlah_titik = int(input("Masukkan jumlah titik sampling (4, 6, 8, dst): "))

    hitung_titik_sampling(diameter, jumlah_titik)
except ValueError:
    print("Input tidak valid. Pastikan memasukkan angka.")
