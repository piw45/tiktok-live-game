"""Satu jendela: server TikTok + game 3D (pywebview/WebView2). Buat .exe: jalanin build.bat
    python app.py @username_host     (tanpa argumen -> ditanya)"""
import asyncio, os, sys, threading, webview

if len(sys.argv) < 2: sys.argv.append(input("username host TikTok (contoh @fajararif895): ").strip() or "@username")
import server  # baca sys.argv[1] waktu import

def run():
    try: asyncio.run(server.main())
    except Exception as e: print("server TikTok mati:", e, "\ngame tetap jalan offline, tekan 1-6 buat tes", flush=True)

threading.Thread(target=run, daemon=True).start()
here = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))  # _MEIPASS = folder extract PyInstaller
webview.create_window("Panjat Sengsara", os.path.join(here, "game.html"), width=540, height=960)
webview.start(private_mode=False)  # private_mode False = localStorage (rekor, papan penjatuh) kesimpan
