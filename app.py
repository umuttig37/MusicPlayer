from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import threading
import time
import tkinter.messagebox
from ttkthemes import themed_tk as tk
from mutagen.mp3 import MP3
from pygame import mixer
class MelodyPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Melody")
        self.root.iconbitmap(r'images/melody.ico')
        self.root.get_themes()
        self.root.set_theme("radiance")

        self.playlist = []
        self.paused = False

        mixer.init()
        self.create_widgets()
def create_widgets(self):
    # Status Bar
    self.statusbar = ttk.Label(self.root, text="Welcome to MusicApp!", relief=SUNKEN, anchor=W, font='Times new roman')
    self.statusbar.pack(side=BOTTOM, fill=X)

    # Menu Bar
    self.menubar = Menu(self.root)
    self.root.config(menu=self.menubar)

    # File Menu
    self.file_menu = Menu(self.menubar, tearoff=0)
    self.menubar.add_cascade(label="File", menu=self.file_menu)
    self.file_menu.add_command(label="Open", command=self.browse_file)
    self.file_menu.add_command(label="Exit", command=self.root.destroy)

    # Help Menu
    self.help_menu = Menu(self.menubar, tearoff=0)
    self.menubar.add_cascade(label="Help", menu=self.help_menu)
    self.help_menu.add_command(label="About Us", command=self.about_us)

    # Left Frame
    self.leftframe = Frame(self.root)
    self.leftframe.pack(side=LEFT, padx=30, pady=30)
    self.playlistbox = Listbox(self.leftframe)
    self.playlistbox.pack()
    self.addBtn = ttk.Button(self.leftframe, text="+ Add", command=self.browse_file)
    self.addBtn.pack(side=LEFT)
    self.delBtn = ttk.Button(self.leftframe, text="- Del", command=self.del_song)
    self.delBtn.pack(side=LEFT)

    # Right Frame
    self.rightframe = Frame(self.root)
    self.rightframe.pack(pady=30)

    # Top Frame
    self.topframe = Frame(self.rightframe)
    self.topframe.pack()
    self.lengthlabel = ttk.Label(self.topframe, text='Total Length : --:--')
    self.lengthlabel.pack(pady=5)
    self.currenttimelabel = ttk.Label(self.topframe, text='Current Time : --:--', relief=GROOVE)
    self.currenttimelabel.pack()

    # Middle Frame
    self.middleframe = Frame(self.rightframe)
    self.middleframe.pack(pady=30, padx=30)
    self.playPhoto = PhotoImage(file='kuvat/play.png')
    self.playBtn = ttk.Button(self.middleframe, image=self.playPhoto, command=self.play_music)
    self.playBtn.grid(row=0, column=0, padx=10)
    self.stopPhoto = PhotoImage(file='kuvat/stop.png')
    self.stopBtn = ttk.Button(self.middleframe, image=self.stopPhoto, command=self.stop_music)
    self.stopBtn.grid(row=0, column=1, padx=10)
    self.pausePhoto = PhotoImage(file='kuvat/pause.png')
    self.pauseBtn = ttk.Button(self.middleframe, image=self.pausePhoto, command=self.pause_music)
    self.pauseBtn.grid(row=0, column=2, padx=10)

    # Bottom Frame
    self.bottomframe = Frame(self.rightframe)
    self.bottomframe.pack()
    self.rewindPhoto = PhotoImage(file='kuvat/rewind.png')
    self.rewindBtn = ttk.Button(self.bottomframe, image=self.rewindPhoto, command=self.rewind_music)
    self.rewindBtn.grid(row=0, column=0)
    self.mutePhoto = PhotoImage(file='kuvat/mute.png')
    self.volumePhoto = PhotoImage(file='/volume.png')
    self.volumeBtn = ttk.Button(self.bottomframe, image=self.volumePhoto, command=self.mute_music)
    self.volumeBtn.grid(row=0, column=1)
    self.scale = ttk.Scale(self.bottomframe, from_=0, to=100, orient=HORIZONTAL, command=self.set_vol)
    self.scale.set(70)
    self.scale.grid(row=0, column=2, pady=15, padx=30)

    def browse_file(self):
        filename_path = filedialog.askopenfilename()
        self.add_to_playlist(filename_path)
        mixer.music.queue(filename_path)

    def add_to_playlist(self, filename):
        filename = os.path.basename(filename)
        self.playlistbox.insert(0, filename)
        self.playlist.insert(0, filename)

    def del_song(self):
        selected_song = self.playlistbox.curselection()
        selected_song = int(selected_song[0])
        self.playlistbox.delete(selected_song)
        self.playlist.pop(selected_song)
 def show_details(self, play_song):
        file_data = os.path.splitext(play_song)
        if file_data[1] == '.mp3':
            audio = MP3(play_song)
            total_length = audio.info.length
        else:
            a = mixer.Sound(play_song)
            total_length = a.get_length()

        mins, secs = divmod(total_length, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.lengthlabel['text'] = "Total Length" + ' - ' + timeformat

        t1 = threading.Thread(target=self.start_count, args=(total_length,))
        t1.start()

    def start_count(self, t):
        current_time = 0
        while current_time <= t and mixer.music.get_busy():
            if self.paused:
                continue
            else:
                mins, secs = divmod(current_time, 60)
                mins = round(mins)
                secs = round(secs)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                self.currenttimelabel['text'] = "Current Time" + ' - ' + timeformat
                time.sleep(1)
                current_time += 1