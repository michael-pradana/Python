import random

welcome_message = "main game yuk!"
print(welcome_message)

# Input nama cukup dilakukan sekali di awal
nama_user = input("masukkan namamu : ")
print(f"\nhalo {nama_user}!")

# Perulangan game dimulai di sini
while True:
    # Posisi marmut diacak ulang di setiap ronde
    marmut_possesion = random.randint(1, 4)

    print(f'''
dimana si marmut?

[_]  [_]  [_]  [_]''')
    
    option_user = int(input("ada di 1/2/3/4 ?  "))
    print(f'''
kamu nebak {option_user}
''')
    # kamu nebak {type(option_user)}

    if option_user == marmut_possesion:
        print(f'''dan benar, tebakan kamu adalah {option_user} !
''')
    else:
        print(f'''haha salah cok, masak {option_user} !
''')
        
    print(f"yang bener {marmut_possesion}")

    # Pertanyaan apakah ingin lanjut bermain atau berhenti
    main_lagi = input("\nmau main lagi? (y/n) : ").lower()
    if main_lagi != 'y':
        print(f"\nterima kasih sudah bermain, {nama_user}! Sampai jumpa!")
        break
