from tkinter import *
from tkinter import filedialog
from tkinter import ttk


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