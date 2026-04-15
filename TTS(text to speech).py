from gtts import gTTS
import os

# Matnni fayldan o‘qish
with open("men.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Til (o‘zbek uchun 'uz', ingliz uchun 'en')
language = 'uz'

# Ovozga o‘tkazish
speech = gTTS(text=text, lang=language, slow=False)

# Saqlash
speech.save("audio.mp3")

# Ochish (Windows uchun)
os.system("start audio.mp3")