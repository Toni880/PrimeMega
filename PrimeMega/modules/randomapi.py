import requests
from PrimeMega.events import register
from PrimeMega import telethn as tbot


@register(pattern="^/ptl ?(.*)")
async def asupan(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        asupannya = f"{resp['url']}"
        return await tbot.send_file(event.chat_id, asupannya)
    except Exception:
        await event.reply("`Error 404 not found...`")


@register(pattern="^/chika ?(.*)")
async def chika(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        chikanya = f"{resp['url']}"
        return await tbot.send_file(event.chat_id, chikanya)
    except Exception:
        await event.reply("`Error 404 not found...`")


@register(pattern="^/hilih ?(.*)")
async def _(hilih):
    kuntul = hilih.pattern_match.group(1)
    if not kuntul:
        await hilih.reply("Usage: /hilih <text>")
        return
    try:
        resp = requests.get(f"https://tede-api.herokuapp.com/api/hilih?kata={kuntul}").json()
        hilihnya = f"{resp['result']}"
        return await hilih.reply(hilihnya)
    except Exception:
        await hilih.reply("Something went wrong LOL...")