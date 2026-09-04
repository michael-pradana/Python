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
    print("\n" + "-" * 40)
    print(f"Pemain : {nama_user}")
    print(f"Nyawa  : {tampilan_nyawa} ({nyawa}/{nyawa_maksimal})")
    print("-" * 40)

    # Tampilan Awal Sebelum Menebak (Opsi 1)
    print('''dimana si marmut?

   [1]     [2]     [3]     [4]
   [_]     [_]     [_]     [_]''')
    
    # Validasi input anti crash
    while True:
        tebakan = input("\nada di 1/2/3/4 ?  ")
        try:
            option_user = int(tebakan)
        except ValueError:
            option_user = 0
            
        if option_user == 0:
            print("\ngoblok, pake angka inputannya woi!")
            continue
        break

    print(f"\nkamu nebak {option_user}\n")

    # Logika visualisasi kotak
    kotak = ["[_]", "[_]", "[_]", "[_]"]
    kotak[marmut_possesion - 1] = "[🐹]"

    # Pengecekan tebakan & logika nyawa
    if option_user == marmut_possesion:
        print(f"dan benar, tebakan kamu adalah {option_user} !\n")
        
        # Jika menang: nyawa bertambah 1 jika sebelumnya berkurang (maksimal 3)
        if nyawa < nyawa_maksimal:
            nyawa += 1
            print(f"🎉 Mantap! Nyawamu bertambah 1! (Sekarang: {nyawa}/{nyawa_maksimal})")
        else:
            print("✨ Nyawamu masih penuh (3/3)!")
            
    else:
        # Jika salah: nyawa berkurang 1
        if 1 <= option_user <= 4:
            kotak[option_user - 1] = "[❌]"
        print(f"haha salah cok, masak {option_user} !\n")
        
        nyawa -= 1

    # Tampilkan kotak yang sudah terbuka
    tampilan_kotak = "     ".join(kotak)
    print(f"Kotak dibuka:")
    print("   [1]     [2]     [3]     [4]")
    print(f"   {tampilan_kotak}\n")
    print(f"yang bener nomor {marmut_possesion}")

    # Cek jika nyawa habis (mati)
    if nyawa <= 0:
        print("\n💀 GAME OVER! Nyawamu habis cok, kamu mati!\n")
        break

    # Konfirmasi lanjut jika masih ada nyawa
    main_lagi = input("\nmau lanjut main? (y/n) : ").lower()
    if main_lagi != 'y':
        print(f"\nterima kasih sudah bermain, {nama_user}! Sisa nyawamu: {nyawa}")
        break
