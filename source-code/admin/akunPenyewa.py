from fungsi.utilitas import clear
from akun import dataPenyewa

def tambahPenyewa():
    clear()
    print("=" * 75)
    print("REGISTRASI PENYEWA BARU")
    print("=" * 75)

    # Input username & password
    username = input(f"{'Masukkan username':<40}: ").strip()
    password = input(f"{'Masukkan password':<40}: ").strip()

    # Validasi username dan password tidak boleh kosong
    if not username or not password:
        print("\nUsername dan password tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return False

    # Cek username double
    for info in dataPenyewa.values():
        if info.get("username") == username:
            print("\nUsername sudah digunakan! Silakan pilih yang lain.")
            input("Tekan Enter untuk kembali...")
            return False

    # Input data penyewa
    print("\n" + "=" * 75)
    print("LENGKAPI DATA PENYEWA")
    print("=" * 75)

    nama = input(f"{'Nama Lengkap':<40}: ")
    kontak = input(f"{'Kontak (No. HP)':<40}: ")
    email = input(f"{'Email':<40}: ")
    tanggal_gabung = input(f"{'Tanggal Gabung (contoh: 27 November 2025)':<40}: ")
    unit = input(f"{'Unit (contoh: KS01)':<40}: ")
    kamar = input(f"{'Nomor Kamar':<40}: ")

    # Semua data wajib diisi(bisa dibuat validasi satu satu kalau ketua mau)
    if not all([nama, kontak, email, tanggal_gabung, unit, kamar]):
        print("\nSemua data wajib diisi!")
        input("Tekan Enter untuk kembali...")
        return False

    # Menambahkan data penyewa ke dictionary
    id_baru = f"PENYEWA{len(dataPenyewa) + 1}"

    dataPenyewa[id_baru] = {
        "username": username,
        "password": password,
        "role": "MEMBER",
        "nama": nama,
        "kontak": kontak,
        "email": email,
        "tanggal_gabung": tanggal_gabung,
        "status": "AKTIF",
        "unit": unit,
        "kamar": kamar
    }

    print("\nRegistrasi berhasil! Silakan login dengan akun Anda.")
    input("Tekan Enter untuk melanjutkan...")
    clear()
    return True

def lihatPenyewa(): 
    print("=" * 75)
    print("LIHAT DATA PENYEWA")
    print("=" * 75)

    print(f"{'ID Penyewa':<15} {'Nama Lengkap':<25} {'Kontak':<15} {'Tanggal Gabung':<20} {'Status':<15} {'Unit':<10} {'Kamar':<10}")
    for id_penyewa, data in dataPenyewa.items(): 
        print(f"{str(id_penyewa):<15} {data['nama']:<25} {data['kontak']:<15} {data['tanggal_gabung']:<20} {data['status']:<15} {data['unit']:<10} {data['kamar']:<10}")
    
    print("=" * 75)
    input("Tekan Enter untuk kembali... ")
    # pass

def editPenyewa(): 
    while True: 
        try: 
            print("=" * 75)
            print("DATA PENYEWA")
            print("=" * 75)

            print(f"{'ID Penyewa':<15} {'Nama Lengkap':<25} {'Kontak':<15} {'Tanggal Gabung':<20} {'Status':<15} {'Unit':<10} {'Kamar':<10}")
            for id_penyewa, data in dataPenyewa.items(): 
                print(f"{str(id_penyewa):<15} {data['nama']:<25} {data['kontak']:<15} {data['tanggal_gabung']:<20} {data['status']:<15} {data['unit']:<10} {data['kamar']:<10}")

            print("=" * 75)
            print(f"{'0':<15} Keluar")
            print("=" * 75)

            print("Masukkan ID Pengguna yang Ingin Anda Ubah:")
            pilih_menu = input("> ")
            print("=" * 75)

            clear()
            if pilih_menu == "0": 
                break

            for id_penyewa, info_penyewa in dataPenyewa.items(): 
                if pilih_menu == id_penyewa: 
                    while True: 
                        print("=" * 75)
                        print("INFORMASI PENYEWA YANG DAPAT DIUBAH")
                        print("=" * 75)

                        print(f"{'1 - Nama Penyewa':<30}: {info_penyewa['nama']}")
                        print(f"{'2 - Kontak Penyewa':<30}: {info_penyewa['kontak']}")
                        print(f"{'3 - Tanggal Gabung':<30}: {info_penyewa['tanggal_gabung']}")
                        print(f"{'4 - Status Penyewa':<30}: {info_penyewa['status']}")

                        print("=" * 75)
                        print("0 - Keluar")
                        print("=" * 75)

                        print("Masukkan bagian yang ingin diubah :")
                        print("=" * 75)
                        pilih_edit = input("> ")
                        print("=" * 75)

                        clear()

                        if pilih_edit == "0": 
                            break
                        elif pilih_edit == "1": 
                            while True: 
                                print("=" * 75)
                                print("EDIT NAMA PENYEWA")
                                print("=" * 75)
                                
                                print(f"{'Nama Lama':<30} : {info_penyewa['nama']}")
                                ganti_nama = input(f"{'Masukkan nama baru':<30} : ")
                                print("=" * 75)

                                clear()

                                if len(ganti_nama) != 0: 
                                    dataPenyewa[id_penyewa].update({'nama': ganti_nama})
                                    break
                                else: 
                                    print("=" * 75)
                                    print("Tidak Boleh Kosong!")
                                    print("=" * 75)
                                    clear()
                        elif pilih_edit == "2": 
                            while True: 
                                print("=" * 75)
                                print("EDIT KONTAK PENYEWA")
                                print("=" * 75)
                                
                                print(f"{'Kontak Lama':<30} : {info_penyewa['kontak']}")
                                ganti_kontak = input(f"{'Masukkan kontak baru':<30} : ")
                                print("=" * 75)

                                clear()

                                if len(ganti_kontak) != 0: 
                                    dataPenyewa[id_penyewa].update({'kontak': ganti_kontak})
                                    break
                                else: 
                                    print("=" * 75)
                                    print("Tidak Boleh Kosong!")
                                    print("=" * 75)
                                    clear()
                        elif pilih_edit == "3": 
                            while True: 
                                print("=" * 75)
                                print("EDIT TANGGAL GABUNG PENYEWA")
                                print("=" * 75)
                                
                                print(f"{'Tanggal Gabung Lama':<30} : {info_penyewa['tanggal_gabung']}")
                                ganti_tanggal = input(f"{'Masukkan Tanggal Gabung baru':<30} : ")
                                print("=" * 75)

                                clear()

                                if len(ganti_tanggal) != 0: 
                                    dataPenyewa[id_penyewa].update({'tanggal_gabung': ganti_tanggal})
                                    break
                                else: 
                                    print("=" * 75)
                                    print("Tidak Boleh Kosong!")
                                    print("=" * 75)
                                    clear()
                        elif pilih_edit == "4": 
                            while True: 
                                print("=" * 75)
                                print("EDIT STATUS PENYEWA")
                                print("=" * 75)
                                
                                print(f"{'Status Sebelumnya':<45} : {info_penyewa['status']}")
                                ganti_status = input(f"{'Ubah Status Penyewa (AKTIF / TIDAK AKTIF)':<45} : ")
                                print("=" * 75)

                                clear()

                                if len(ganti_status) != 0 and (ganti_status == "AKTIF" or ganti_status == "TIDAK AKTIF"): 
                                    dataPenyewa[id_penyewa].update({'status': ganti_status})
                                    break
                                else: 
                                    print("=" * 75)
                                    print("Pastikan anda memasukkan data dengan benar!")
                                    print("=" * 75)
                                    clear()
                        else: 
                            clear()
                            raise ValueError("Pilihan Tidak Valid!")

        except ValueError as e: 
            print("=" * 75)
            print(e)
            print("=" * 75)

def hapusPenyewa(): 
    while True: 
        try: 
            global dataPenyewa
            selesai_delete = False
            print("=" * 75)
            print("HAPUS PENYEWA")
            print("=" * 75)

            print(f"{'ID Penyewa':<15} {'Nama Lengkap':<25} {'Kontak':<15} {'Tanggal Gabung':<20} {'Status':<15} {'Unit':<10} {'Kamar':<10}")
            for id_penyewa, data in dataPenyewa.items(): 
                print(f"{str(id_penyewa):<15} {data['nama']:<25} {data['kontak']:<15} {data['tanggal_gabung']:<20} {data['status']:<15} {data['unit']:<10} {data['kamar']:<10}")
            
            print("=" * 75)
            print(f"{'0':<5} Kembali")
            print("=" * 75)

            print("Masukkan ID akun yang ingin dihapus :")
            print("=" * 75)
            pilih_menu = input("> ")
            print("=" * 75)

            clear()

            if pilih_menu == "0": 
                break
            for id_penyewa, data_penyewa in dataPenyewa.items(): 
                if pilih_menu == id_penyewa: 
                    # Opsional -- Tambah Konfirmasi Hapus 
                    print("=" * 75)
                    print("KONFIRMASI HAPUS")
                    print("=" * 75)

                    del dataPenyewa[pilih_menu]
                    data_lama = dataPenyewa
                    data_baru = {}
                    nomor = 1

                    for _, data_akun in data_lama.items(): 
                        new_id = f"PENYEWA{nomor}"
                        data_baru[new_id] = data_akun
                        nomor += 1

                    dataPenyewa = data_baru
                    selesai_delete = True
                    break
                # break
            
            if selesai_delete == True: 
                break


        except ValueError as e: 
            print("=" * 75)
            print(e)
            print("=" * 75)
            
    # pass

def akunPenyewa(): 
    while True: 
        try: 
            clear()

            print("=" * 75)
            print("DATA DAN AKUN PENYEWA")
            print("=" * 75)

            print("[1] - Tambah Penyewa")
            print("[2] - Lihat Data Penyewa")
            print("[3] - Edit Data Penyewa")
            print("[4] - Hapus Data Penyewa")
            print("=" * 75)

            print("[0] - Keluar")
            print("=" * 75)

            print("Pilih menu yang anda inginkan")
            pilih_menu = input("> ")
            print("=" * 75)

            clear()

            if pilih_menu == "0": 
                break
            if pilih_menu == "1": 
                clear()
                tambahPenyewa()
            elif pilih_menu == "2": 
                clear()
                lihatPenyewa()
            elif pilih_menu == "3": 
                clear()
                editPenyewa()
            elif pilih_menu == "4": 
                clear()
                hapusPenyewa()
            else: 
                raise ValueError("Pilihan Tidak Valid")

        except ValueError as e: 
            print("=" * 75)
            print(e)
            print("=" * 75)
            clear()