import fungsi
from akun import dataPenyewa

from fungsi.utilitas import clear

user_login = None

def login():
    while True: 
        global user_login, role_login, id_login, login_password, nama_login
        berhasil_login = False
        clear()
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        for id_penyewa, info_penyewa in dataPenyewa.items(): 
            if username == info_penyewa['username'] and password == info_penyewa['password']: 
                user_login = username
                login_password = password
                role_login = info_penyewa['role']
                id_login = id_penyewa
                berhasil_login = True
                nama_login = info_penyewa['nama']

                print("Login Berhasil")

        if berhasil_login == True: 
            break
        else: 
            print("Login gagal, silahkan coba lagi!")

def register():
    clear()
    print("=== REGISTER ===")
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

# ini buat ngecek kosong atau ngga nya data login
    if not username or not password:
        print("Username dan password tidak boleh kosong!")
        return False

    id_penyewa = f"PENYEWA{len(dataPenyewa) + 1}"

    dataPenyewa[id_penyewa] = {
    "username": username,
    "password": password,
    "role": "MEMBER",

    # Data tambahan penyewa (isi dengan input atau default)
    "nama": "",
    "kontak": "",
    "email": "",
    "tanggal_gabung": "",
    "status": "AKTIF",
    "unit": "",
    "kamar": ""
    }

    print("Data penyewa berhasil ditambahkan!")
    print(f"ID Penyewa: {id_penyewa}")

    # user[username] = password
    print("Akun berhasil dibuat! Silakan login.")

    clear()
    return True

#ini biarin aja kah fitur logout nya dipisah atau nanti mau di gabung di function lain?
def logout():
    global user_login
    user_login = None
    print("Berhasil logout.")
