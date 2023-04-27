import time
from pyrogram import Client
import uvloop

uvloop.install()

app = Client(
    "MySession",
    api_id=9534447,
    api_hash="f01a775392bd41dd0e118c1312470f0d")
with app:
    while True:
        time.sleep(60)
        time1 = time.localtime()
        soat = time.strftime("%H:%M", time1)
        kun = time.strftime("%d/%m/%Y", time1)
        if "00:00" <= soat <= "05:30":
            app.update_profile(first_name=f"𝐀𝐬𝐢𝐥𝐛𝐞𝐤 𝐌𝐢𝐫𝐨𝐥𝐢𝐦𝐨𝐯 🧑‍🎓💻",
                               bio=f"No bio 💤  ||  🗓 {kun}  ||  🕒 {soat}")
        else:
            app.update_profile(first_name=f"𝐀𝐬𝐢𝐥𝐛𝐞𝐤 𝐌𝐢𝐫𝐨𝐥𝐢𝐦𝐨𝐯 || {soat}",
                               bio=f"Student 👨‍🎓 ||  🗓 {kun}  ||  🕒 {soat}")
