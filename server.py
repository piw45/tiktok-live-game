"""TikTok gift/komen -> WebSocket ke game.html.
    pip install TikTokLive websockets
    python server.py @username_host
Lalu buka game.html di OBS Browser Source (tekan 1-6 buat tes tanpa TikTok)."""
import asyncio, json, random, re, sys
from collections import Counter
import websockets

def tier(coins):  # total coin gift -> sabotase
    if coins >= 1000: return "reset"
    if coins >= 100:  return "vanish"
    if coins >= 30:   return "quake"
    if coins >= 5:    return "slip"
    return "wind"

if "--check" in sys.argv:
    assert [tier(c) for c in (1, 5, 30, 100, 1000)] == ["wind", "slip", "quake", "vanish", "reset"]
    print("ok"); sys.exit()

from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, GiftEvent

url = lambda o: (getattr(o, "m_urls", None) or [None])[0]  # proto Image -> url pertama
clients, votes = set(), {}  # votes: user -> "kiri"|"kanan" (1 suara per orang)
client = TikTokLiveClient(unique_id=sys.argv[1] if len(sys.argv) > 1 else "@username")

async def send(ev):
    await asyncio.gather(*(c.send(json.dumps(ev)) for c in clients), return_exceptions=True)

@client.on(GiftEvent)
async def on_gift(e):
    if e.gift.streakable and e.streaking: return  # tunggu combo selesai
    coins = e.gift.diamond_count * e.repeat_count
    await send({"type": tier(coins), "user": e.user.nickname, "gift": f"{e.gift.name} x{e.repeat_count}",
                "coins": coins, "dir": random.choice([-1, 1]),
                "avatar": url(getattr(e.user, "avatar_thumb", None)), "img": url(getattr(e.gift, "image", None))})

@client.on(CommentEvent)
async def on_comment(e):
    m = re.search(r"\b(kiri|kanan)\b", e.comment.lower())
    if m: votes[e.user.unique_id] = m.group(1)

async def vote_loop():  # tiap 3 detik, mayoritas menang
    while True:
        await asyncio.sleep(3)
        if votes:
            side, n = Counter(votes.values()).most_common(1)[0]
            votes.clear()
            await send({"type": "wind", "dir": -1 if side == "kiri" else 1, "user": f"{n} viewer", "gift": "vote", "coins": 0})

async def ws_handler(ws, *_):
    clients.add(ws)
    try: await ws.wait_closed()
    finally: clients.discard(ws)

async def main():
    async with websockets.serve(ws_handler, "localhost", 8765):
        asyncio.create_task(vote_loop())
        await client.connect()

asyncio.run(main())
