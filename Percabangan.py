def Konversi_ke_usd(jumlah_rupiah):
    return jumlah_rupiah / 15000  #1 USD = 15000 Rupiah

def Konversi_ke_yen(jumlah_rupiah):
    return jumlah_rupiah / 140  #1 Yen = 140 Rupiah

def Konversi_ke_ringgit(jumlah_rupiah):
    return jumlah_rupiah / 3800  #1 Ringgit = 3800 Rupiah

jumlah_rupiah = float(input("Masukkan jumlah Rupiah: "))

print("Pilih mata uang yang ingin dikonversikan:")
print("1. USD")
print("2. Yen")
print("3. Ringgit Malaysia")

choice = int(input("Masukkan pilihan: "))

if choice == 1:
    converted_amount = Konversi_ke_usd(jumlah_rupiah)
    print(f"Hasil konversi ke USD: {converted_amount:.2f}")
elif choice == 2:
    converted_amount = Konversi_ke_yen(jumlah_rupiah)
    print(f"Hasil konversi ke Yen: {converted_amount:.2f}")
elif choice == 3:
    converted_amount = Konversi_ke_ringgit(jumlah_rupiah)
    print(f"Hasil konversi ke Ringgit Malaysia: {converted_amount:.2f}")
else:
    print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.")
