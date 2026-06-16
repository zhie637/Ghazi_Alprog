#Data awal mahasiswa (menggunakan struktur list di dalam list)
data_mahasiswa = [
    ["viserys", 85],
    ["aegon", 78],
    ["rhaenyra", 90],
    ["daenarys", 85],
    ["daemon", 80],
]

while True:
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")
    print("====================================")
    
    pilihan = input("Pilih menu 1-8: ")
    print("------------------------------------")

    #1. TAMPILKAN DATA
    if pilihan == '1':
        if not data_mahasiswa:
            print("Data mahasiswa masih kosong.")
        else:
            print(f"{'No':<4}{'Nama Mahasiswa':<20}{'Nilai':<5}")
            print("-" * 30)
            for i, mhs in enumerate(data_mahasiswa, start=1):
                print(f"{i:<4}{mhs[0]:<20}{mhs[1]:<5}")

    #2. TAMBAH DATA
    elif pilihan == '2':
        nama = input("Masukkan nama mahasiswa baru: ")
        # Validasi input nilai berupa angka
        try:
            nilai = int(input("Masukkan nilai mahasiswa: "))
            data_mahasiswa.append([nama, nilai])
            print(f"Data {nama} berhasil ditambahkan!")
        except ValueError:
            print("Gagal! Nilai harus berupa angka.")

    #3. UBAH DATA
    elif pilihan == '3':
        nama_cari = input("Masukkan nama mahasiswa yang ingin diubah: ")
        ditemukan = False
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_cari.lower():
                print(f"Data ditemukan: {mhs[0]} - Nilai: {mhs[1]}")
                try:
                    nilai_baru = int(input("Masukkan nilai baru: "))
                    mhs[1] = nilai_baru
                    print(f"Data {mhs[0]} berhasil diperbarui!")
                except ValueError:
                    print("Gagal! Nilai harus berupa angka.")
                ditemukan = True
                break
        if not ditemukan:
            print(f"Mahasiswa dengan nama '{nama_cari}' tidak ditemukan.")

    # 4. HAPUS DATA
    elif pilihan == '4':
        nama_cari = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        ditemukan = False
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_cari.lower():
                data_mahasiswa.remove(mhs)
                print(f"Data {mhs[0]} berhasil dihapus!")
                ditemukan = True
                break
        if not ditemukan:
            print(f"Mahasiswa dengan nama '{nama_cari}' tidak ditemukan.")

    #5. CARI DATA
    elif pilihan == '5':
        nama_cari = input("Masukkan nama mahasiswa yang dicari: ")
        ditemukan = False
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_cari.lower():
                print(f"Data Ditemukan -> Nama: {mhs[0]}, Nilai: {mhs[1]}")
                ditemukan = True
                break
        if not ditemukan:
            print(f"Mahasiswa dengan nama '{nama_cari}' tidak ditemukan.")

    #URUTKAN DATA BERDASARKAN NILAI TERTINGGI
    elif pilihan == '6':
        if not data_mahasiswa:
            print("Data kosong, tidak bisa mengurutkan.")
        else:
            # Mengurutkan menggunakan fungsi sort berdasarkan elemen indeks ke-1 (Nilai) secara descending
            data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
            print("Data berhasil diurutkan berdasarkan nilai tertinggi!")
            # Langsung tampilkan hasil urutan
            print(f"\n{'No':<4}{'Nama Mahasiswa':<20}{'Nilai':<5}")
            print("-" * 30)
            for i, mhs in enumerate(data_mahasiswa, start=1):
                print(f"{i:<4}{mhs[0]:<20}{mhs[1]:<5}")

    # 7. HITUNG RATA-RATA NILAI
    elif pilihan == '7':
        if not data_mahasiswa:
            print("Data kosong, rata-rata adalah 0.")
        else:
            total_nilai = sum(mhs[1] for mhs in data_mahasiswa)
            rata_rata = total_nilai / len(data_mahasiswa)
            print(f"Jumlah Mahasiswa: {len(data_mahasiswa)}")
            print(f"Rata-rata Nilai : {rata_rata:.2f}")

    # 8. KELUAR
    elif pilihan == '8':
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-8.")