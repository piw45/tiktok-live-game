# Panjat Sengsara

Game manjat 3D buat live TikTok. Lu manjat, penonton ngejatuhin lewat gift & komen.

```
game.html     game 3D (three.js) + overlay OBS, buka langsung gak perlu server
three.min.js  three.js r158, offline
server.py     TikTok gift/komen -> WebSocket ke game
app.py        server + game dalam satu jendela (bahan .exe)
build.bat     bikin dist\PanjatSengsara.exe
test.js       cek fisika tanpa browser
```

## Butuh

- Python 3.10+
- Browser (Firefox/Chrome) atau OBS
- Akun TikTok yang **lagi live** (buat nyambung ke chat)

## Install

```bash
pip install TikTokLive websockets
pip install pywebview pyinstaller   # cuma kalau mau bikin .exe
```

## Jalanin (.exe)

Double-click `PanjatSengsara.exe`, ketik username host (atau `PanjatSengsara.exe @username`). Jendela game + server jalan bareng, gak perlu Python.
Masukin ke OBS lewat **Window Capture**. Bikin exe-nya: `build.bat` → `dist\PanjatSengsara.exe` (~20 MB, butuh WebView2 = bawaan Windows 10/11).

## Jalanin (manual)

**1. Coba tanpa TikTok** — buka `game.html` di browser, klik halaman, main:

| Tombol | Fungsi |
|---|---|
| `A/D` atau `←/→` | jalan |
| `Space` / `W` / `↑` | lompat |
| `1` `2` | tes angin kiri / kanan |
| `3` `4` `5` `6` | tes licin / gempa / pijakan hilang / reset |
| `7` `8` `9` | tes bantuan: perisai / dorong naik / tangga darurat |
| `M` | mute (musik latar + efek) |

**2. Sambung ke live:**

```bash
python server.py @username_host
```

Dot di pojok kanan bawah jadi hijau "live" kalau nyambung. Server harus jalan terus selama live.

**3. Masukin ke OBS / TikTok LIVE Studio:**

Sources → `+` → Browser → centang **Local file** → pilih `game.html`.
Lebar/tinggi samain dengan canvas (portrait 1080×1920 paling pas). Centang **Control audio via OBS** kalau mau suara game masuk stream.

Klik dulu di Browser Source (Interact) supaya keyboard masuk ke game.

## Aturan main

Penonton punya dua kubu: yang ngejatuhin dan yang nolongin.

**Sabotase** — semua gift selain daftar bantuan di bawah:

| Gift (total coin) | Efek |
|---|---|
| 1–4 | Angin 4 detik, hembusannya naik-turun |
| 5–29 | Licin 6 detik, rem hampir gak ada |
| 30–99 | Gempa 4 detik: kontrol kebalik + bisa kepleset sendiri |
| 100–999 | Pijakan yang dipijak **dan** satu di atasnya runtuh |
| 1000+ | Reset ke bawah + nyungsep 1.2 detik |

**Bantuan** — gift yang namanya ada di `HELP` (`server.py`): mawar, heart, GG, finger heart, dst.

| Sumber | Efek |
|---|---|
| gift HELP 1–9 coin, follow baru | Perisai 8 detik (nangkis sabotase, tiap tangkisan potong 1.2 detik) |
| gift HELP 10–99 coin, share live, 200 like | Didorong naik |
| gift HELP 100+ coin | Tangga darurat: 3 pijakan di atas kepala |

Komen `kiri` / `kanan` = vote angin tiap 3 detik, 1 suara per orang.

Siapa pun yang gift-nya bikin lu jatuh ≥3m dalam 4 detik masuk **Papan Penjatuh**; yang ngasih bantuan masuk **Papan Penolong** (dua-duanya disimpan di browser, top 3 ditampilin).

Target sesi naik per 100m — meter di kiri atas itu progres ke target, bukan rekor. Makin tinggi, pijakan makin nakal (geser, rapuh, pegas). Jatuh jauh = slow-mo + nyungsep sebentar.

Ubah angka tier & daftar gift baik di `server.py` → `tier()`, `help_tier()`, `HELP`, `LIKE_GOAL`. Durasi efek di `game.html` → `DUR`, target sesi → `goal`.

## Cek

```bash
python server.py --check   # tier gift (sabotase + bantuan)
node test.js               # fisika: bisa manjat, platform kejangkau, sabotase & bantuan jalan
```

## Masalah umum

- **Jendela .exe putih kosong + error `in use`** → instance sebelumnya belum tutup total. Tunggu beberapa detik, buka lagi.
- **Server gak nyambung ke TikTok** → pastiin akunnya lagi live dan username pakai `@`. Kalau kena rate limit, coba lagi beberapa menit.
- **Gak ada suara / musik** → browser blokir audio sebelum ada klik. Klik halaman sekali (musik latar mulai dari situ). Di OBS, centang *Control audio via OBS*.
- **Keyboard gak jalan di OBS** → klik kanan source → *Interact*, main lewat jendela itu.
- **Font kotak-kotak gak muncul** → butuh internet (Google Fonts). Game tetap jalan tanpa itu.
