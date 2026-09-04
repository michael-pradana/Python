# 🦊 Game Tebak Hewan (Python CLI)

Game tebak-tebakan berbasis terminal (Command Line Interface) yang dibuat menggunakan bahasa pemrograman Python.

## 🎮 Fitur Game
- **Pilihan Karakter Hewan:** Pemain bisa memilih karakter yang ingin ditebak:
  - 🦊 Fox
  - 🦀 Crab
  - 🐤 Chicken
- **Efek Suara Interaktif (macOS System Sounds):**
  - 🟢 Suara denting (*Glass*) saat tebakan benar.
  - 🔴 Suara bass (*Basso*) saat tebakan salah.
  - 📦 Suara letupan (*Pop*) saat memilih karakter.
  - 💀 Suara alarm (*Sosumi*) saat Game Over.
- **Sistem Nyawa (❤️):** Pemain dibekali 3 nyawa. Salah tebak mengurangi nyawa, tebakan benar menambah nyawa (maksimal 3).
- **Terminal Bersih (Auto-Clear Screen):** Layar terminal dibersihkan di setiap ronde baru sehingga tidak menumpuk ke bawah (*anti-scrolling*).
- **Visual Kotak Interaktif:** Membuka kotak dengan tampilan emoji hewan yang dipilih serta penanda `[❌]` jika tebakan salah.
- **Validasi Input:** Tahan crash terhadap input huruf/karakter aneh dan peringatan otomatis jika salah format.
- **Opsi Keluar:** Ketik `exit` kapan saja untuk menyudahi permainan.

## 🚀 Cara Memainkan
Pastikan kamu sudah menginstal Python di komputermu, lalu jalankan perintah:

```bash
python3 main7.py
```
*(Atau `python main7.py` tergantung konfigurasi komputermu)*