from tkinter import*
from tkinter import filedialog
import pygame
import os

root = Tk()
root.title("music Player")
root.geometry("500x300")



pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name ,ext = os.path.splitext(song)
        if ext == ',mp3':
            song.append(song)

    for somg in song:
        songlist.insert("end",song)

    songlist.selection_set(0)
    current_song = song[songlist.curselection()[0]]

def play_music():
    pass

def pause_music():
    pass

def next_music():
    pass

def prev_music():
    pass





organise_menu = Menu(menubar)
organise_menu.add_command(Label='Select Folder', command=load_music)
menubar.add_cascade(Label='organise', menu=organise_menu)


songlist = Listbox(root,bg="black",fg="white",width=100,height=15)
songlist.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next.png')
prev_btn_image = PhotoImage(file='previous.png')

Control_frame = Frame(root)
Control_frame.pack()

play_btn = Button(Control_frame, image= play_btn_image, borderwidth=0)
pause_btn = Button(Control_frame, image= pause_btn_image, borderwidth=0)
next_btn = Button(Control_frame, image= next_btn_image, borderwidth=0)
prev_btn = Button(Control_frame, image= prev_btn_image, borderwidth=0)


play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2 , padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0 , padx=7, pady=10)




root.mainloop()