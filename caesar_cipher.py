def caesar_enkripsi(teks, kunci):
    hasil = ""
    for huruf in teks:
        if huruf.isalpha():
            dasar = ord('A') if huruf.isupper() else ord('a')
            hasil += chr((ord(huruf) - dasar + kunci) % 26 + dasar)
        else:
            hasil += huruf
    return hasil

def caesar_dekripsi(teks_sandi, kunci):
    return caesar_enkripsi(teks_sandi, -kunci)

if __name__ == "__main__":
    print("=== APLIKASI CAESAR CIPHER ===")
    while True:
        print("\nMENU:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        pilihan = input("Pilih menu [1-3]: ")

        if pilihan == "1":
            pesan = input("Masukkan pesan: ")
            kunci = int(input("Masukkan kunci (angka): "))
            hasil = caesar_enkripsi(pesan, kunci)
            print(f"✅ Hasil Enkripsi: {hasil}")

        elif pilihan == "2":
            sandi = input("Masukkan teks sandi: ")
            kunci = int(input("Masukkan kunci (angka): "))
            hasil = caesar_dekripsi(sandi, kunci)
            print(f"✅ Hasil Dekripsi: {hasil}")

        elif pilihan == "3":
            print("Selesai. Terima kasih!")
            break
        else:
            print("❌ Pilihan tidak benar, coba lagi.")