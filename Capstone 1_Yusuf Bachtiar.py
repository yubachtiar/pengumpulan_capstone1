daftar_barang = [
    ['1A', 'Sekrup', 'Sparepart', 'G1', 50],
    ['1B', 'Pensil', 'ATK', 'G2', 20],
    ['1C', 'Kopi', 'Pantry Supplies', 'G3', 15],
    ['1D', 'Plat Besi', 'Sparepart', 'G1', 0]
]

def read_barang():
    def index_laporan(index, nilai):
        print("===Laporan Persediaan Barang===")
        print(f"{'Kode':<10}{'Nama':<15}{'Kategori':<20}{'Lokasi':<10}{'Jumlah Stok':<15}")
        for i in daftar_barang:
            if nilai is None or i[index] == nilai:
                print(f"{i[0]:<10}{i[1]:<15}{i[2]:<20}{i[3]:<10}{i[4]:<15}")
    while True:
        print('''
=== Menu Laporan ===
1. Laporan Persediaan Seluruh Barang
2. Laporan Persediaan Barang berdasarkan Kode Barang
3. Kembali ke Menu Utama
              ''')

        submenu_read = input("Masukkan pilihan (1-3): ")

        if submenu_read == '1':
            if daftar_barang:
                index_laporan(0,None)
            else:
                break
        elif submenu_read == '2':
            if daftar_barang:
                kode_barang = input("Masukkan kode barang yang ingin ditampilkan: ")
                ketemu = False
                for barang in daftar_barang:
                    if barang[0] is not None:
                        ketemu = True
                        index_laporan(0, kode_barang)
                        break
                if not ketemu:
                    print("Kode barang tidak ditemukan. Silahkan coba lagi.")
            else:
                print("Barang tidak ada (kosong)")
        elif submenu_read == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
def create_barang():
    while True:
        print('''
=== Menu Tambah Data Barang ===
1. Tambahkan data barang
2. Kembali ke Menu Utama
              ''')
        submenu_create = input("Masukkan pilihan (1-2): ")
        if submenu_create == '1':
            kode_barang = input("Masukkan kode barang: ")
            barang_sudah_ada = False
            for barang in daftar_barang:
                if barang[0] == kode_barang:
                    barang_sudah_ada = True
                    break
            if barang_sudah_ada:
                print(f"Kode barang {kode_barang} sudah ada. Tidak dapat menambahkan data.")
                continue
            nama_barang = input("Masukkan nama barang: ")
            kategori_barang = input("Masukkan kategori barang: ")
            lokasi_barang = input("Masukkan lokasi barang: ")
            while True:
                try:
                    jumlah_barang = int(input("Masukkan jumlah barang (angka):"))
                    break
                except ValueError:
                    print('Stok yang anda input harus angka')
            konfirmasi = input("Apakah Anda ingin menyimpan perubahan? (y/n): ")
            if konfirmasi == 'y':
                barang_baru = [kode_barang, nama_barang, kategori_barang, lokasi_barang, jumlah_barang]
                daftar_barang.append(barang_baru)
                print("Data barang berhasil ditambahkan.")
            else:
                print("Data barang batal ditambahkan.")
        elif submenu_create == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def update_barang():
    while True:
        print('''
=== Ubah Data Barang ===
1. Ubah data barang
2. Kembali ke Menu Utama
              ''')
        submenu_modify = input("Masukkan pilihan (1-2): ")
        if submenu_modify == '1':
            kode_barang = input("Masukkan kode barang: ")
            ketemu = False
            for i,barang in enumerate(daftar_barang):
                if barang [0] == kode_barang:
                    ketemu = True
                    print(f"Data yang akan diubah adalah barang dengan nama {barang[1]} dan memiliki stok dengan jumlah {barang[4]}")
                    konfirmasi = input("Apakah anda yakin ingin mengubah data barang tersebut? (y/n):")
                    if konfirmasi == 'y':
                        nama_baru = input("Masukkan nama barang yang baru :")
                        tipe_baru = input("Masukkan tipe barang yang baru :")
                        lokasi_baru = input("Masukkan lokasi barang yang baru :")
                        while True:
                            try:
                                jml_stok_baru = int(input("Masukkan jumlah stok yang baru :"))
                                break
                            except ValueError:
                                print("Stok yang anda input harus angka.")

                        konfirmasi2 = input("Apakah data yang anda input sudah benar?(y/n) :")
                        if konfirmasi2 == 'y':
                            daftar_barang[i][1]= nama_baru
                            daftar_barang[i][2]= tipe_baru
                            daftar_barang[i][3]= lokasi_baru
                            daftar_barang[i][4]= jml_stok_baru
                            print("Data barang berhasil diubah.")
                        else:
                            print("Pengubahan data batal")
                    else:
                        print("Pengubahan barang tidak tersimpan")
                    break
            if not ketemu:
                print("Kode barang tidak ditemukan. Silahkan coba lagi.")
        elif submenu_modify == '2':
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

def delete_barang():
    while True:
        print('''
=== Hapus Data Barang ===
1. Hapus data barang
2. Kembali ke Menu Utama
              ''')
        submenu_hapus = input("Masukkan pilihan (1-2): ")
        if submenu_hapus == '1':
            kode_barang = input('Masukkan kode barang yang ingin dihapus: ')

            ketemu = False
            for barang in daftar_barang:
                if barang[0] == kode_barang:
                    ketemu = True
                    print(f"Data yang akan dihapus adalah barang dengan nama {barang[1]} dan memiliki stok dengan jumlah {barang[4]}")
                    konfirmasi = input("Apakah anda yakin ingin menghapus data barang tersebut?(y/n): ")
                    if konfirmasi == 'y':
                        daftar_barang.remove(barang)
                        print("Data barang berhasil dihapus.")
                    else:
                        print("Data barang gagal dihapus.")
            if not ketemu:
                print('Kode barang tidak ditemukan')
        elif submenu_hapus == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
def ambil_barang():
    while True:
        print('''\n=== Pengambilan Barang ===
              1. Ambil barang
              2. Kembali ke Menu Utama
              ''')
        submenu_ambil = input("Masukkan pilihan (1-2): ")
        if submenu_ambil == '1':
            kode_barang = input("Masukkan kode barang yang ingin diambil: ")
            found = False
            for i, barang in enumerate(daftar_barang):
                if barang[0] == kode_barang:
                    found = True
                    print(f"Data barang yang akan diambil: {barang[1]} - Jumlah stok: {barang[4]}")
                    while True:
                        try:
                            jumlah_diambil = int(input("Masukkan jumlah barang yang ingin diambil: "))
                            if jumlah_diambil <= barang[4]:
                                konfirmasi = input("Apakah anda yakin ingin mengambil data barang tersebut?(y/n): ")
                                if konfirmasi == 'y':
                                    daftar_barang[i][4] -= jumlah_diambil
                                    print(f"{jumlah_diambil} {barang[1]} berhasil diambil. Jumlah stok tersisa: {barang[4]}")
                                    break
                                else:
                                    print("Barang tidak jadi diambil.")
                            else:
                                print("Jumlah yang diambil melebihi stok yang tersedia.")
                                break
                        except ValueError:
                            print("Jumlah yang anda input harus angka.")
            if not found:
                print("Kode barang tidak ditemukan. Sila1kan coba lagi.")
        elif submenu_ambil == '2':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        
while True:
    menu_utama = input('''
        Semangat Pagi!\n
        Ini adalah program manajemen data persediaan barang gudang.
        Apa yang ingin anda lakukan?\n
        Pilihan Menu :
        1. Laporan Persediaan Barang
        2. Tambah Barang Baru
        3. Ubah Data Barang
        4. Hapus Barang
        5. Pengambilan Barang
        6. Keluar
        Masukkan menu yang ingin anda pilih (1-6) :''')
    if menu_utama == '1':
        read_barang()
    elif menu_utama == '2':
        create_barang()
    elif menu_utama == '3':
        update_barang()
    elif menu_utama == '4':
        delete_barang()
    elif menu_utama == '5':
        ambil_barang()
    elif menu_utama == '6':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
