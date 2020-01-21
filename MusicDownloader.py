from youtube_dl import YoutubeDL
from tkinter import *
window = Tk()

window.title("MusicDownloader")

window.geometry('350x200')

lbl = Label(window, text="Type your Link Here")
lbl.grid(column=0, row=0)
txt = Entry(window, width=25)
txt.grid(column=1, row=0)


def clicked():
    link = txt.get()
    ydl_opts = {}
    ydl = YoutubeDL(ydl_opts)
    ydl.download([link])


btn = Button(window, text="Download", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
