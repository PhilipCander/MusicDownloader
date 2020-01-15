from youtube_dl import YoutubeDL


print("Kopiere den Youtube Link")

try:
    link = input(": ")
    ydl_opts = {}
    ydl = YoutubeDL(ydl_opts)
    ydl.download([link])
except:
    print("Irgendetwas ist schiefgelaufen, versuchs noch mal...")
print("Fertig...")