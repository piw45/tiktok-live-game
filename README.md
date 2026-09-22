# Panjat Sengsara

Game manjat buat live TikTok. Lu manjat, penonton ngejatuhin lewat gift & komen.

```
game.html   game + overlay OBS (buka langsung, gak perlu server)
server.py   TikTok gift/komen -> WebSocket ke game
test.js     cek fisika tanpa browser
```

## Butuh

- Python 3.10+
- Browser (Firefox/Chrome) atau OBS
- Akun TikTok yang **lagi live** (buat nyambung ke chat)

## Install

```bash
pip install TikTokLive websockets
```

## Jalanin

**1. Coba tanpa TikTok** — buka `game.html` di browser, klik halaman, main:

| Tombol | Fungsi |
|---|---|
| `A/D` atau `←/→` | jalan |
| `Space` / `W` / `↑` | lompat |
| `1` `2` | tes angin kiri / kanan |
| `3` `4` `5` `6` | tes licin / gempa / pijakan hilang / reset |
| `M` | mute |

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

| Gift (total coin) | Efek |
|---|---|
| 1–4 | Angin 2.5 detik |
| 5–29 | Licin 5 detik |
| 30–99 | Gempa 3 detik, kontrol kebalik |
| 100–999 | Pijakan yang dipijak hilang |
| 1000+ | Reset ke bawah |

Komen `kiri` / `kanan` = vote angin tiap 3 detik, 1 suara per orang.

Siapa pun yang gift-nya bikin lu jatuh ≥3m dalam 4 detik masuk **Papan Penjatuh** (disimpan di browser, top 3 ditampilin).

Ubah angka tier di `server.py` → `tier()`. Durasi efek di `game.html` → `DUR`.

## Cek

```bash
python server.py --check   # tier gift
node test.js               # fisika: bisa manjat, platform kejangkau, sabotase jalan
```

## Masalah umum

- **Server gak nyambung ke TikTok** → pastiin akunnya lagi live dan username pakai `@`. Kalau kena rate limit, coba lagi beberapa menit.
- **Gak ada suara** → browser blokir audio sebelum ada klik. Klik halaman sekali. Di OBS, centang *Control audio via OBS*.
- **Keyboard gak jalan di OBS** → klik kanan source → *Interact*, main lewat jendela itu.
- **Font kotak-kotak gak muncul** → butuh internet (Google Fonts). Game tetap jalan tanpa itu.
