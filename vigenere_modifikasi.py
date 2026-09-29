def vigenere_mod_enkripsi(teks, kunci):
    teks = teks.upper()
    kunci = kunci.upper()
    hasil = ""
    for i in range(len(teks)):
        geser = ord(kunci[i % len(kunci)]) - ord('A')
        hasil += chr((ord(teks[i]) - ord('A') + geser) % 26 + ord('A'))
    return hasil

def vigenere_mod_dekripsi(teks_sandi, kunci):
    teks_sandi = teks_sandi.upper()
    kunci = kunci.upper()
    hasil = ""
    for i in range(len(teks_sandi)):
        geser = ord(kunci[i % len(kunci)]) - ord('A')
        hasil += chr((ord(teks_sandi[i]) - ord('A') - geser) % 26 + ord('A'))
    return hasil

if __name__ == "__main__":
    print("=== Vigenère Cipher Modifikasi ===")
    pesan = input("Masukkan pesan (tanpa spasi): ")
    kata_kunci = input("Masukkan kunci: ")
    
    enkripsi = vigenere_mod_enkripsi(pesan, kata_kunci)
    dekripsi = vigenere_mod_dekripsi(enkripsi, kata_kunci)
    
    print(f"\nHasil Enkripsi: {enkripsi}")
    print(f"Hasil Dekripsi: {dekripsi}")