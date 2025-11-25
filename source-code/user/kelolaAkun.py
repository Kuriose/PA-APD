# Pengelolaan Akun & data Pribadi
from fungsi.utilitas import clear
import akun

# untuk sementara belum kubikin error handling nya yang lengkap
def ubah_data_akun():
    clear()
    print("=" * 75)
    print("UBAH DATA AKUN")
    print("=" * 75)
    print("[1] - Ubah Username")
    print("[2] - Ubah Password")
    print("[0] - Kembali ke Menu Sebelumnya")
    pilih = input("> ").strip()

    if pilih == "1":
        username_baru = input("Masukkan Username Yang Baru: ").strip
        if not username_baru:
            print("Username Tidak Boleh Kosong")

        elif username_baru == akun.daftarAkun["username"]:
            print("Username Tidak Boleh Sama Dengan Yang Lama")

        else:
            akun.daftarAkun['username'] = username_baru
            print("Username berhasil diubah!")

    elif pilih == "2":
        password = input("Masukkan Password: ")
        if password != akun.daftarAkun["password"]:
            print("Password Salah")

        else:
            password_baru = input("Masukkan Password Yang Baru: ").strip
            if not password_baru:
                print("Password Tidak Boleh Kosong")
            
            elif password_baru == akun.daftarAkun["password"]:
                print("Password Tidak Boleh Sama Dengan Password Lama")
            
            else:
                akun.daftarAkun["password"] == password_baru
                print("Password Berhasil Diubah")
    
    elif pilih == "0":
        return
    
    else:
        print("Pilihan Tidak Valid")

def ubah_data_pribadi():
    clear()
    print("=" * 75)
    print("UBAH DATA PRIBADI")
    print("=" * 75)
    print("[1] - Ubah Nama Lengkap")
    print("[2] - Ubah Email")
    print("[3] - Ubah Nomor Telepon")
    print("[0] - Kembali ke Menu Sebelumnya")
    pilih = input("> ").strip()

    if pilih == "1":
        nama_baru = input("Masukkan Nama Lengkap Baru: ").strip()
        if not nama_baru:
            print("Nama tidak boleh kosong")
        else:
            akun.daftarAkun["nama"] = nama_baru
            print("Nama berhasil diubah!")

    elif pilih == "2":
        email_baru = input("Masukkan Email Baru: ").strip()
        if not email_baru:
            print("Email tidak boleh kosong")
        elif "@" not in email_baru:
            print("Format email tidak valid")
        else:
            akun.daftarAkun["email"] = email_baru
            print("Email berhasil diubah!")

    elif pilih == "3":
        nohp_baru = input("Masukkan Nomor Telepon Baru: ").strip()
        if not nohp_baru:
            print("Nomor telepon tidak boleh kosong")
        elif not nohp_baru.isdigit():
            print("Nomor telepon hanya boleh berisi angka")
        else:
            akun.daftarAkun["telepon"] = nohp_baru
            print("Nomor telepon berhasil diubah!")

    elif pilih == "0":
        return

    else:
        print("Pilihan tidak valid")


# Menu Kelola Akun
def kelolaAkun():
    while True:
        clear
        print("=" * 75)
        print("KELOLA AKUN")
        print("=" * 75)
        print("[1] - Ubah Data pada Akun")
        print("[2] - Ubah Data Pribadi")
        print("[0] - Kembali ke Menu Sebelumnya")
        print("=" * 75)
        pilih = input("> ").strip()

        if pilih == "0":
            break

        elif pilih == "1":
            ubah_data_akun()
        
        elif pilih == "2":
            ubah_data_pribadi()
        
        else:
            print("Pilihan tidak valid")