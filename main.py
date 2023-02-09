from tkinter import *
from tkinter import filedialog, messagebox
from pygame import mixer
import os
from PIL import Image, ImageTk
from Modules import *
# create doubly linked list
aa = cdll()
# create tkinter window
Music_Player = Tk()
# create image
try:
    original = Image.open('E:\\my projects\\media player using ds\\pp.png')
    a = original.resize((50, 50))
    Image_play = ImageTk.PhotoImage(a)
    original = Image.open('E:\\my projects\\media player using ds\\pa.png')
    b = original.resize((50, 50))
    Image_pause = ImageTk.PhotoImage(b)
    original = Image.open('E:\\my projects\\media player using ds\\ff.png')
    c = original.resize((50, 50))
    Image_for = ImageTk.PhotoImage(c)
    original = Image.open('E:\\my projects\\media player using ds\\bb.png')
    d = original.resize((50, 50))
    Image_back = ImageTk.PhotoImage(d)
    original = Image.open('E:\\my projects\\media player using ds\\ff11.png')
    e = original.resize((50, 50))
    Image_add = ImageTk.PhotoImage(e)
    original = Image.open('E:\\my projects\\media player using ds\\f.png')
    f = original.resize((50, 50))
    Image_logo = ImageTk.PhotoImage(f)
except:
    messagebox.showerror("Error", "Image Not Found")

# title of project
Music_Player.title('Music player ')
# backgraoud of project
Music_Player.configure(bg="#333333")
# size of window
Music_Player.geometry("486x620")
Music_Player.iconphoto(False, Image_logo)
# set not change window size
Music_Player.resizable(False, False)
# initilaze mixer
mixer.init()
# Functions of project


def Add_Music():
    # return path of folder
    path = filedialog.askdirectory()
    if path:
        f = 1
        os.chdir(path)
        # return list of files
        songs = os.listdir(path)
        Playlist.insert(
            END, "                      List of Songs")
        Playlist.insert(
            END, "________________________________________________________")
        Playlist.insert(END, "")

        for song in songs:
            # check which .mp3 file
            if song.endswith(".mp3"):
                s = Node(song)
                # insert .mp3 file in Linked list
                aa.insert_at_end(s)
                # insert .mp3 file for listbox
                Playlist.insert(END, " "+str(f)+") " + song)
                f += 1
        aa.display()


def resume():
    mixer.music.unpause()
    Button_pause = Button(Music_Player, activebackground="grey",
                          bg="silver", image=Image_pause, command=pause).place(x=260, y=550)


def pause():
    mixer.music.pause()
    Button_resume = Button(Music_Player, activebackground="grey",
                           bg="silver", image=Image_play, command=resume).place(x=260, y=550)


def Play_Music():
    try:
        # first node of linked list
        global s
        s = aa.first
        mixer.music.load(s.data)
        mixer.music.play()
        Button_pause = Button(Music_Player, activebackground="grey",
                              bg="silver", image=Image_pause, command=pause).place(x=260, y=550)

    except:
        messagebox.showerror("Error", "Select Data")


def playnext():
    try:
        # next node of linked list
        global s
        s = s.next
        mixer.music.load(s.data)
        mixer.music.play()
        Button_pause = Button(Music_Player, activebackground="grey",
                              bg="silver", image=Image_pause, command=pause).place(x=260, y=550)

    except:
        messagebox.showerror("Error", "Select Data")


def playpri():
    try:
        # previous node of linked list
        global s
        s = s.prev
        mixer.music.load(s.data)
        mixer.music.play()
        Button_pause = Button(Music_Player, activebackground="grey",
                              bg="silver", image=Image_pause, command=pause).place(x=260, y=550)
    except:
        messagebox.showerror("Error", "Select Data")


def ask():
    try:
        if 1:
            w = takecom()
            if w == "":
                speak("say again")
            elif "next" in w:
                playnext()
            elif "back" in w:
                playpri()
            elif "stop" in w:
                pause()
            elif "play" in w:
                Play_Music()
            elif "start" in w:
                resume()
            elif "bye" or "quit" or "exit" in w:
                speak("Thanks for used AI")
                Music_Player.quit()

    except:
        messagebox.showerror("Error", "AI Not Working")


# create frame for listbox
Frame_Music = Frame(Music_Player)
Frame_Music.place(x=10, y=10, width=640, height=520)
# Button of projects
Button_Add = Button(Music_Player, activebackground="grey", bg="silver",
                    image=Image_add, command=Add_Music).place(x=10, y=550)
Button_Play = Button(Music_Player, activebackground="grey", bg="silver",
                     image=Image_play, command=Play_Music).place(x=260, y=550)
Button_Playn = Button(Music_Player, activebackground="grey", bg="silver",
                      image=Image_for, command=playnext).place(x=320, y=550)
Button_Playp = Button(Music_Player, activebackground="grey", bg="silver",
                      image=Image_back, command=playpri).place(x=200, y=550)
Button_AI = Button(Music_Player, text="AI", font=("mono", 20, "bold"),
                   activebackground="grey", bg="silver", command=ask).place(x=80, y=550)

# scrollbar for listbox
Scroll = Scrollbar(Frame_Music)
# listbox
Playlist = Listbox(Frame_Music, width=50, font='arial 12 bold',
                   bg="black", fg="white", yscrollcommand=Scroll.set)
# return display all file in listbox
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)
# end of window
Music_Player.mainloop()
