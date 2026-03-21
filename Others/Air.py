def simulasi_neraca_air(S_max, ET_p, data_hujan):
    # Menyimpan hasil perhitungan harian
    hasil_ETa = []
    hasil_S = []
    hasil_delta_S = []
    hasil_Limpasan = []
    
    # Asumsi awal: tanah terisi setengah dari kapasitas maksimal
    S_sebelumnya = S_max / 2.0  
    
    print(f"--- Memulai Simulasi Neraca Air ---")
    print(f"Kapasitas Maksimal (S_max): {S_max} mm")
    print(f"Evapotranspirasi Potensial (ET_p): {ET_p} mm/hari\n")
    print(f"{'Hari':<5} | {'Hujan':<5} | {'ET_aktual':<10} | {'Kelembapan (S)':<15} | {'ΔS':<6} | {'Limpasan':<10}")
    print("-" * 65)

    # Iterasi perhitungan untuk setiap hari
    for hari, P in enumerate(data_hujan, start=1):
        
        # Skenario 1: Hujan cukup untuk memenuhi kebutuhan evapotranspirasi
        if P >= ET_p:
            ET_a = ET_p
            air_tambahan = P - ET_p
            S_sementara = S_sebelumnya + air_tambahan
            
            # Cek apakah tanah sudah jenuh (melebihi kapasitas)
            if S_sementara > S_max:
                limpasan = S_sementara - S_max  # Sisa air menjadi limpasan
                S_sekarang = S_max              # Tanah penuh
            else:
                limpasan = 0.0
                S_sekarang = S_sementara
                
        # Skenario 2: Hujan tidak cukup, tanaman mengambil cadangan air tanah
        else:
            kebutuhan_air = ET_p - P
            # Air yang bisa diambil maksimal sebesar sisa air di tanah
            air_tersedia = min(kebutuhan_air, S_sebelumnya) 
            
            ET_a = P + air_tersedia
            S_sekarang = S_sebelumnya - air_tersedia
            limpasan = 0.0
            
        # Menghitung perubahan simpanan (Delta S)
        delta_S = S_sekarang - S_sebelumnya
        
        # Simpan hasil ke dalam list
        hasil_ETa.append(round(ET_a, 2))
        hasil_S.append(round(S_sekarang, 2))
        hasil_delta_S.append(round(delta_S, 2))
        hasil_Limpasan.append(round(limpasan, 2))
        
        # Tampilkan hasil per hari
        print(f"{hari:<5} | {P:<5} | {ET_a:<10.2f} | {S_sekarang:<15.2f} | {delta_S:<6.2f} | {limpasan:<10.2f}")
        
        # Update nilai S untuk hari berikutnya
        S_sebelumnya = S_sekarang

    return hasil_ETa, hasil_S, hasil_delta_S, hasil_Limpasan

# ==========================================
# Cara Menjalankan Program Dasar
# ==========================================

# Parameter DAS
kapasitas_tanah = 150.0  # mm
et_potensial = 4.5       # mm/hari

# Data curah hujan (10 hari sebagai contoh)
data_P = [0, 15, 20, 0, 0, 5, 50, 10, 0, 30]

# Panggil fungsi
simulasi_neraca_air(kapasitas_tanah, et_potensial, data_P)