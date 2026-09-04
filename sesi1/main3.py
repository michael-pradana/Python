import random
import sys

# Memastikan terminal Windows mendukung karakter emoji UTF-8 tanpa error
sys.stdout.reconfigure(encoding='utf-8')

welcome_message = "main game yuk!"
print(welcome_message)

nama_user = input("masukkan namamu : ")
print(f"\nhalo {nama_user}!")

while True:
    marmut_possesion = random.randint(1, 4)

    print(f'''
dimana si marmut?

[_]  [_]  [_]  [_]''')
    
    option_user = int(input("ada di 1/2/3/4 ?  "))
    print(f'''
kamu nebak {option_user}
''')

    # Logika visualisasi kotak
    # 1. Mulai dengan 4 kotak tertutup
    kotak = ["[_]", "[_]", "[_]", "[_]"]
    
    # 2. Tampilkan marmut di posisi yang benar (indeks list mulai dari 0, jadi dikurangi 1)
    kotak[marmut_possesion - 1] = "[🐹]"

    # 3. Cek hasil tebakan
    if option_user == marmut_possesion:
        print(f"dan benar, tebakan kamu adalah {option_user} !\n")
    else:
        # Jika salah dan nomornya valid (1-4), tandai kotak tebakan pemain dengan silang
        if 1 <= option_user <= 4:
            kotak[option_user - 1] = "[❌]"
        print(f"haha salah cok, masak {option_user} !\n")

    # 4. Tampilkan visualisasi kotak yang sudah terbuka
    tampilan_kotak = "  ".join(kotak)
    print(f"Kotak dibuka:\n{tampilan_kotak}\n")
    print(f"yang bener nomor {marmut_possesion}")

    # Konfirmasi main lagi
    main_lagi = input("\nmau main lagi? (y/n) : ").lower()
    if main_lagi != 'y':
        print(f"\nterima kasih sudah bermain, {nama_user}! Sampai jumpa!")
        break
