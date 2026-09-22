"""TikTok gift/komen -> WebSocket ke game.html.
    pip install TikTokLive websockets
    python server.py @username_host
Lalu buka game.html di OBS Browser Source (tekan 1-9 buat tes tanpa TikTok)."""
import asyncio, json, random, re, sys
from collections import Counter
import websockets

HELP = {"rose", "tiktok", "heart", "heart me", "finger heart", "gg", "thumbs up", "ice cream cone"}  # gift "baik" -> bantuan, sisanya sabotase
LIKE_GOAL = 200   # like terkumpul tiap 3 detik -> dorongan naik

def tier(coins):  # total coin gift -> sabotase
    if coins >= 1000: return "reset"
    if coins >= 100:  return "vanish"
    if coins >= 30:   return "quake"
    if coins >= 5:    return "slip"
    return "wind"

def help_tier(coins):  # total coin gift HELP -> bantuan
    if coins >= 100: return "stair"
    if coins >= 10:  return "boost"
    return "shield"

if "--check" in sys.argv:
    assert [tier(c) for c in (1, 5, 30, 100, 1000)] == ["wind", "slip", "quake", "vanish", "reset"]
    assert [help_tier(c) for c in (1, 10, 100)] == ["shield", "boost", "stair"]
    print("ok"); sys.exit()

from TikTokLive import TikTokLiveClient
from TikTokLive.events import CommentEvent, GiftEvent, LikeEvent, FollowEvent, ShareEvent

url = lambda o: (getattr(o, "m_urls", None) or [None])[0]  # proto Image -> url pertama
clients, votes, likes = set(), {}, 0  # votes: user -> "kiri"|"kanan" (1 suara per orang)
client = TikTokLiveClient(unique_id=sys.argv[1] if len(sys.argv) > 1 else "@username")

async def send(ev):
    await asyncio.gather(*(c.send(json.dumps(ev)) for c in clients), return_exceptions=True)

@client.on(GiftEvent)
async def on_gift(e):
    if e.gift.streakable and e.streaking: return  # tunggu combo selesai
    coins = e.gift.diamond_count * e.repeat_count
    kind = help_tier(coins) if (e.gift.name or "").lower() in HELP else tier(coins)
    await send({"type": kind, "user": e.user.nickname, "gift": f"{e.gift.name} x{e.repeat_count}",
                "coins": coins, "dir": random.choice([-1, 1]),
                "avatar": url(getattr(e.user, "avatar_thumb", None)), "img": url(getattr(e.gift, "image", None))})

@client.on(LikeEvent)
async def on_like(e):
    global likes
    likes += getattr(e, "count", 1) or 1

@client.on(FollowEvent)      # follow baru = perisai
async def on_follow(e):
    await send({"type": "shield", "user": e.user.nickname, "gift": "follow baru", "coins": 0,
                "avatar": url(getattr(e.user, "avatar_thumb", None))})

@client.on(ShareEvent)       # share live = dorongan naik
async def on_share(e):
    await send({"type": "boost", "user": e.user.nickname, "gift": "share live", "coins": 0,
                "avatar": url(getattr(e.user, "avatar_thumb", None))})

@client.on(CommentEvent)
async def on_comment(e):
    m = re.search(r"\b(kiri|kanan)\b", e.comment.lower())
    if m: votes[e.user.unique_id] = m.group(1)

async def vote_loop():  # tiap 3 detik: mayoritas angin menang + panen like
    global likes
    while True:
        await asyncio.sleep(3)
        if votes:
            side, n = Counter(votes.values()).most_common(1)[0]
            votes.clear()
            await send({"type": "wind", "dir": -1 if side == "kiri" else 1, "user": f"{n} viewer", "gift": "vote", "coins": 0})
        if likes >= LIKE_GOAL:
            await send({"type": "boost", "user": "penonton", "gift": f"{likes} like", "coins": 0})   # satu nama, biar papan penolong gak penuh "213 like"
            likes = 0

async def ws_handler(ws, *_):
    clients.add(ws)
    try: await ws.wait_closed()
    finally: clients.discard(ws)

async def main():
    async with websockets.serve(ws_handler, "localhost", 8765):
        asyncio.create_task(vote_loop())
        while True:  # live putus / host rehat -> nyambung lagi sendiri, game jalan terus
            try: await client.connect()
            except Exception as e: print("TikTok putus:", e, "- nyoba lagi 15 detik", flush=True)
            await asyncio.sleep(15)

if __name__ == "__main__": asyncio.run(main())
