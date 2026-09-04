import random
import sys

# Memastikan terminal Windows mendukung karakter emoji UTF-8 tanpa error
sys.stdout.reconfigure(encoding='utf-8')

welcome_message = "main game yuk!"
print(welcome_message)

nama_user = input("masukkan namamu : ")
print(f"\nhalo {nama_user}!")

# Inisialisasi Sistem Nyawa
nyawa_maksimal = 3
nyawa = nyawa_maksimal

while True:
    marmut_possesion = random.randint(1, 4)

    # Tampilan Info Pemain & Sisa Nyawa
    tampilan_nyawa = "❤️ " * nyawa
    print("\n" + "=" * 40)
    print(f"Pemain : {nama_user}")
    print(f"Nyawa  : {tampilan_nyawa} ({nyawa}/{nyawa_maksimal})")
    print("=" * 40)

    # Tampilan Awal Sebelum Menebak
    print('''dimana si marmut?

   [1]     [2]     [3]     [4]
   [_]     [_]     [_]     [_]''')
    
    # Validasi input (angka 1-4, anti-crash, dan opsi 'exit')git i
    keluar = False
    while True:
        tebakan = input("\nada di 1/2/3/4 (atau ketik 'exit' untuk keluar) ?  ").strip()
        
        # Fitur keluar game dengan string 'exit'
        if tebakan.lower() == 'exit':
            keluar = True
            break
            
        try:
            option_user = int(tebakan)
        except ValueError:
            option_user = 0
            
        if option_user == 0:
            print("\ngoblok, pake angka inputannya woi!")
            continue
        break

    # Jika pemain memilih 'exit', hentikan game
    if keluar:
        print(f"\nkamu memilih keluar. Terima kasih sudah bermain, {nama_user}! Sisa nyawamu: {nyawa}\n")
        break

    print(f"\nkamu nebak {option_user}\n")

    # Logika visualisasi kotak
    kotak = ["[_]", "[_]", "[_]", "[_]"]
    kotak[marmut_possesion - 1] = "[🐹]"

    # Pengecekan tebakan & logika nyawa
    if option_user == marmut_possesion:
        print(f"dan benar, tebakan kamu adalah {option_user} !\n")
        
        if nyawa < nyawa_maksimal:
            nyawa += 1
            print(f"🎉 Mantap! Nyawamu bertambah 1! (Sekarang: {nyawa}/{nyawa_maksimal})")
        else:
            print("✨ Nyawamu masih penuh (3/3)!")
            
    else:
        if 1 <= option_user <= 4:
            kotak[option_user - 1] = "[❌]"
        print(f"haha salah cok, masak {option_user} !\n")
        
        nyawa -= 1

    # Tampilkan kotak yang sudah terbuka
    tampilan_kotak = "     ".join(kotak)
    print("Kotak dibuka:")
    print("   [1]     [2]     [3]     [4]")
    print(f"   {tampilan_kotak}\n")
    print(f"yang bener nomor {marmut_possesion}")

    # Cek jika nyawa habis (mati)
    if nyawa <= 0:
        print("\n💀 GAME OVER! Nyawamu habis cok, kamu mati!\n")
        break

    # Langsung lanjut ke ronde berikutnya tanpa konfirmasi (y/n)!
