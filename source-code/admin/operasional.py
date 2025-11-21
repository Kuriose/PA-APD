# Operasional Kos / Kontrakan
from fungsi.utilitas import clear

def buatTagihan():
    pass

def lihatKamar_kosong():
    pass

def lihatTagihan_lunas():
    pass

def lihatKeluhan_penyewa():
    pass

def editStatus():
    pass

def cetakLaporan():
    pass

def operasional():
    while True:
        clear() 
        print("=" * 75)
        print("OPERASIONAL KOS & KONTRAKAN")
        print("=" * 75)
        print("[1] - Buat Tagihan Bulanan")
        print("[2] - Lihat Berapa Kamar Yang Kosong")
        print("[3] - Lihat Tagihan Yang Belum Lunas")
        print("[4] - Lihat Keluhan dari Penyewa")
        print("[5] - Edit status pembayaran penyewa")
        print("[6] - Cetak Laporan Keuangan")
        print("[0] - Kembali ke Menu Sebelumnya")
        pilih = input("> ").strip()

        if pilih == "0":
            break
        
        elif pilih == "1":
            buatTagihan()

        elif pilih == "2":
            lihatKamar_kosong()

        elif pilih == "3":
            lihatTagihan_lunas()
        
        elif pilih == "4":
            lihatKeluhan_penyewa()

        elif pilih == "5":
            editStatus()

        elif pilih == "6":
            cetakLaporan()
        
        else:
            print("Pilihan Tidak Valid")
            input("Tekan Enter Untuk Kembali...")