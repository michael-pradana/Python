# 🦊 Game Tebak Hewan (Python CLI)

Game tebak-tebakan berbasis terminal (Command Line Interface) yang dibuat menggunakan bahasa pemrograman Python.

## 🎮 Fitur Game
- **Pilihan Karakter Hewan (Choose Your Fighter):**
  - 🦊 Fox
  - 🦀 Crab
  - 🐤 Chicken
- **🏆 Sistem Skor & Combo Streak:**
  - Setiap tebakan benar menghasilkan skor dasar +100 poin.
  - Berhasil menebak berturut-turut memicu pengali combo (`🔥 Combo x2`, `x3`, dst.).
  - Jika salah menebak, combo streak akan ter-reset ke 0.
- **👑 Penyimpanan High Score Otomatis:**
  - Rekor skor tertinggi dan nama juara disimpan otomatis ke file lokal `highscore.json`.
  - Juara bertahan dan skor tertinggi selalu ditampilkan di papan info setiap ronde.
- **🔊 Efek Suara Interaktif (macOS System Sounds):**
  - 🟢 Suara denting (*Glass*) saat tebakan benar.
  - 🔴 Suara bass (*Basso*) saat tebakan salah.
  - 📦 Suara letupan (*Pop*) saat memilih karakter.
  - 💀 Suara alarm (*Sosumi*) saat Game Over.
- **❤️ Sistem Nyawa:** Pemain dibekali 3 nyawa. Salah tebak mengurangi 1 nyawa, tebakan benar menambah 1 nyawa (maksimal 3).
- **🧹 Terminal Bersih (Auto-Clear Screen):** Layar dibersihkan di setiap ronde baru sehingga tampilan tidak menumpuk ke bawah.
- **🛡️ Validasi Input Anti-Crash:** Tahan error terhadap input huruf atau karakter tak valid.
- **🚪 Opsi Keluar:** Ketik `exit` kapan saja untuk keluar dan melihat ringkasan skor akhir.

## 🚀 Cara Memainkan
Pastikan kamu sudah menginstal Python di komputermu, lalu jalankan perintah:

```bash
python3 sesi1/main7.py
```
*(Atau `python main7.py` jika kamu berada di dalam folder `sesi1`)*
