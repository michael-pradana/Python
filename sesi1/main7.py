import os
import random
import subprocess
import sys

# Memastikan terminal Windows mendukung karakter emoji UTF-8 tanpa error
sys.stdout.reconfigure(encoding='utf-8')

def bersihkan_layar():
    """Membersihkan tampilan terminal agar tidak menumpuk/scrolling."""
    os.system('cls' if os.name == 'nt' else 'clear')

def putar_suara(tipe):
    """Memutar efek suara sistem secara asinkron (non-blocking) di latar belakang."""
    if sys.platform == "darwin":  # Khusus macOS
        suara_map = {
            "benar": "/System/Library/Sounds/Glass.aiff",
            "salah": "/System/Library/Sounds/Basso.aiff",
            "buka": "/System/Library/Sounds/Pop.aiff",
            "game_over": "/System/Library/Sounds/Sosumi.aiff"
        }
        file_suara = suara_map.get(tipe)
        if file_suara and os.path.exists(file_suara):
            subprocess.Popen(["afplay", file_suara], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif sys.platform == "win32":  # Fallback untuk sistem Windows
        try:
            import winsound
            if tipe == "benar":
                winsound.Beep(1000, 150)
            elif tipe == "salah":
                winsound.Beep(400, 250)
            elif tipe == "game_over":
                winsound.Beep(300, 500)
        except Exception:
            pass

# Tampilan awal game
bersihkan_layar()
welcome_message = "main game yuk!"
print(welcome_message)

nama_user = input("masukkan namamu : ").strip()
print(f"\nhalo {nama_user}!")

# Data pilihan karakter hewan & icon
daftar_hewan = {
    1: {"nama": "Fox", "icon": "🦊"},
    2: {"nama": "Crab", "icon": "🦀"},
    3: {"nama": "Chicken", "icon": "🐤"}
}

# Menu Pemilihan Hewan
print("\n" + "=" * 40)
print("PILIH KARAKTER HEWAN YANG INGIN DITEBAK:")
print("=" * 40)
for nomor, data in daftar_hewan.items():
    print(f"[{nomor}] {data['nama']} {data['icon']}")

while True:
    pilihan = input("\nmasukkan nomor hewan pilihanmu (1-3): ").strip()
    try:
        nomor_pilihan = int(pilihan)
        if nomor_pilihan in daftar_hewan:
            hewan_terpilih = daftar_hewan[nomor_pilihan]
            break
        else:
            print("pilihan gak ada cok, pilih 1, 2, atau 3!")
    except ValueError:
        print("input harus angka 1-3 woi!")

nama_hewan = hewan_terpilih["nama"]
icon_hewan = hewan_terpilih["icon"]

putar_suara("buka")
print(f"\n🎉 Keren! Kamu memilih {nama_hewan} [{icon_hewan}]!")
input("\n👉 Tekan Enter untuk mulai bermain...")

# Inisialisasi Sistem Nyawa
nyawa_maksimal = 3
nyawa = nyawa_maksimal
ronde = 1

while True:
    # Bersihkan layar setiap kali ronde baru dimulai
    bersihkan_layar()
    posisi_hewan = random.randint(1, 4)

    # Tampilan Info Pemain, Target Hewan & Sisa Nyawa Terbaru
    tampilan_nyawa = "❤️ " * nyawa
    print("=" * 40)
    print(f"Ronde  : {ronde}")
    print(f"Pemain : {nama_user}")
    print(f"Target : {nama_hewan} {icon_hewan}")
    print(f"Nyawa  : {tampilan_nyawa} ({nyawa}/{nyawa_maksimal})")
    print("=" * 40)

    # Tampilan Awal Sebelum Menebak
    print(f'''dimana si {nama_hewan.lower()} {icon_hewan}?

   [1]     [2]     [3]     [4]
   [_]     [_]     [_]     [_]''')
    
    # Validasi input (angka 1-4, anti-crash, dan opsi 'exit')
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
    kotak[posisi_hewan - 1] = f"[{icon_hewan}]"

    # Pengecekan tebakan & logika nyawa
    if option_user == posisi_hewan:
        putar_suara("benar")
        print(f"dan benar, tebakan kamu adalah {option_user} !\n")
        
        if nyawa < nyawa_maksimal:
            nyawa += 1
            print(f"🎉 Mantap! Nyawamu bertambah 1! (Sekarang: {nyawa}/{nyawa_maksimal})")
        else:
            print("✨ Nyawamu masih penuh (3/3)!")
            
    else:
        putar_suara("salah")
        if 1 <= option_user <= 4:
            kotak[option_user - 1] = "[❌]"
        print(f"haha salah cok, masak {option_user} !\n")
        
        nyawa -= 1

    # Tampilkan kotak yang sudah terbuka
    tampilan_kotak = "     ".join(kotak)
    print("Kotak dibuka:")
    print("   [1]     [2]     [3]     [4]")
    print(f"   {tampilan_kotak}\n")
    print(f"yang bener nomor {posisi_hewan} ({icon_hewan})")

    # Cek jika nyawa habis (mati)
    if nyawa <= 0:
        putar_suara("game_over")
        print(f"\n💀 GAME OVER! Nyawamu habis cok, si {nama_hewan.lower()} kabur!\n")
        break

    # Jeda agar pemain bisa melihat hasil ronde sebelum layar dibersihkan
    ronde += 1
    input("\n👉 Tekan Enter untuk lanjut ke ronde berikutnya...")
