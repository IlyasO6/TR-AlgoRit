import customtkinter as ctk #instalar
from tkinter import font
from PIL import Image,ImageTk # instalar
import ast # instalar
import pygame # instalar
import random 
import math
import numpy as np # instalar
import matplotlib.pyplot as plt #instalar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


login_done = False
# setting everything up: -------------------------------------------------------------------------------------------------

ctk.set_appearance_mode("Light") # options: light, dark  and system

# TONALITATS:
tonalitats={#            #  --> x
            "DM": ["SM", "FM", "Lm", "Mm", "Rm"],
            "SM": ["RM", "DM", "Mm", "Sim", "Lm"],
            "RM": ["LM", "Sol M", "Sim", "Fxm", "Mm"],
            "LM": ["MM", "RM", "Fxm", "Dxm", "Sim"],
            "MM": ["SiM", "LM", "Dxm", "Sxm", "Fxm"],
            "SiM": ["FxM", "MM", "Sxm", "Rxm", "Dxm"],
            "FxM": ["DxM", "SiM", "Rxm", "Lxm", "Sxm"],
            "DxM": ["RbM", "FM", "Lxm", "Sibm", "Rxm"],
            "FM": ["DM", "SibM", "Rm", "Lm", "Sm"],
            "SibM": ["FM", "MbM", "Sm", "Rm", "Dm"],
            "MbM": ["SibM", "LbM", "Dm", "Sm", "Fm"],
            "LbM": ["MbM", "RbM", "Fm", "Dm", "Sibm"],
            "RbM": ["LbM", "SbM", "Sibm", "Fm", "Mbm"],
            "SbM": ["RbM", "DbM", "Mbm", "Sibm", "Lbm"],
            "DbM": ["SbM", "SiM", "Lbm", "Mbm", "Sxm"],
            "Lm": ["Mm", "Rm", "DM", "SM", "FM"],
            "Mm": ["Sim", "Lm", "SM", "RM", "DM"],
            "Sim": ["Fxm", "Mm", "RM", "LM", "SM"],
            "Fxm": ["Dxm", "Sim", "LM", "MM", "RM"],
            "Dxm": ["Sxm", "Fxm", "MM", "SiM", "LM"],
            "Sxm": ["Rxm", "Dxm", "SiM", "FxM", "MM"],
            "Rxm": ["Lxm", "Sxm", "FxM", "DxM", "SiM"],
            "Lxm": ["Sibm", "Rxm", "DxM", "RbM", "FM"],
            "Rm": ["Lm", "Sm", "FM", "DM", "SibM"],
            "Sm": ["Rm", "Dm", "SibM", "FM", "MbM"],
            "Dm": ["Sm", "Fm", "MbM", "SibM", "LbM"],
            "Fm": ["Dm", "Sibm", "LbM", "MbM", "RbM"],
            "Sibm": ["Fm", "Mbm", "RbM", "LbM", "SbM"],
            "Mbm": ["Sibm", "Lbm", "SbM", "RbM", "DbM"],
            "Lbm": ["Mbm", "Sxm", "DbM", "SbM", "SiM"]
            }

widgets_gridforget = []
widgets_placeforget =[]

# Credits text:

with open('C:/Users/usuar/Downloads/Python/Main_PYfolder/TR/Text_Credits.txt','r') as f:
    credit_lines = f.readlines()

credits_text = ""
for line in credit_lines:
    print("merging...")
    credits_text += line

# print(credits_text)



# USER DATA: 
found_user = False

with open('C:/Users/usuar/Downloads/Python/Main_PYfolder/TR/Music_userdata.txt','r') as g:
    user_data = [line.strip()for line in g]
    
#print(user_data)

# ------------------

# DEFINE "MUSIC" CLASS (TO CREATE MUSIC OBJECTS, WHICH ARE THE SONGS)
class Music():
    def __init__(self,name,genre,url,author,lyrics,energy,tone,era):
        self.name = name
        self.genre = genre
        self.url = url
        self.author = author
        self.lyrics = lyrics
        self.energy = energy
        self.tone = tone
        self.era = era

##GET THE SONG DATA FROM THE TXT FILE:
with open('C:/Users/usuar/Downloads/Python/Main_PYfolder/TR/Infocançons.txt','r') as f:
    song_data = [line.strip()for line in f]

#with open('Music_userdata','r') as g:

# CREATE THE SONG_LIST AND APPEND ALL THE SONGS WITH THEIR RESPECTIVE DATA:
for index,items in enumerate(song_data):
    song_data[index] = items.split(",")

song_list = []
for song_info in song_data:
    new_name = song_info[0] # el nom de la cançó
    globals()[new_name] = Music(song_info[0],song_info[1],song_info[2],song_info[3],
                                song_info[4],song_info[5],song_info[6],song_info[7]) #defineix la cançó
    song_list.append(globals()[new_name]) # afegeix la cançó a la llista de cançons


# SORT SONGS BY THEIR GENRE, AUTHOR, URL AND lyrics
general_path = "C:/Users/usuar/Downloads/Python/Main_PYfolder/TR/Music/"
same_genre,same_lyrics,same_energy,same_tone,same_era,same_url= (dict() for i in range(6))

for song in song_list:
    if song.genre not in same_genre:
        same_genre[song.genre] = []
    if song.lyrics not in same_lyrics: 
        same_lyrics[song.lyrics] = []
    if song.energy not in same_energy:
        same_energy[song.energy] = []
    if song.tone not in same_tone:
        same_tone[song.tone] = []
    if song.era not in same_era:
        same_era[song.era] = []
    if general_path+song.url not in same_url:
        same_url[general_path+song.url]=[]

    same_genre[song.genre].append(song)
    same_lyrics[song.lyrics].append(song)
    same_energy[song.energy].append(song)
    same_tone[song.tone].append(song)
    same_era[song.era].append(song)
    same_url[general_path+song.url].append(song)



# CREATE LISTS TO PUT THE DIFERENT PARAMETERS, THE PREFERENCE OF THE USER AND THE PERCENTAGES:
genre_list = list(same_genre.keys())
lyrics_list = list(same_lyrics.keys())
energy_list = list(same_energy.keys())
era_list = list(same_era.keys())
genre_percent = list()
lyrics_percent = list()
energy_percent = list()
era_percent = list()

# Create a song_list to put all the urls
songs = list()
for sng in song_list:
    songs.append(general_path+sng.url)

songs_toplayx = [general_path+random.choice(same_genre["ROCK"]).url,
                general_path+random.choice(same_genre["ELECTRO"]).url,
                general_path+random.choice(same_genre["BLUES/JAZZ"]).url,
                general_path+random.choice(same_genre["RAP"]).url,
                general_path+random.choice(same_genre["CLASSICA"]).url,]
print(songs_toplayx)
second_songlist = songs

songs_toremove = songs_toplayx
for s in songs_toremove:
    if s in second_songlist:
        second_songlist.remove(s)


# --------------------------------------------------------------------------------------------------------------------------------


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # set properties of the window:
        self.title("My app")
        self.geometry("720x420")
        # import global variables:
        global widgets_gridforget, widgets_placeforget, user_data, found_user, songs_toplayx, second_songlist,general_path
        global same_energy,same_era,same_genre,same_tone,same_lyrics,same_url
        global song_list, genre_list,energy_list,era_list,lyrics_list
        global genre_percent, lyrics_percent, energy_percent,era_percent,songs
        global credits_text
        # define self variables:
        self.titles_font = "Bahnschrift Light Condensed"
        self.button_color = ("#b0726a","#5a5991")
        self.text_color = ("#260400","#d5d5f0")
        self.play_firsttime = True
        self.widgets_gridforget = widgets_gridforget # to keep track of the widgets to grid forget
        self.widgets_placeforget = widgets_placeforget# to keep track of the widgets to place forget
        self.songs_toplay = songs_toplayx # the songs to play list that will keep recieving new song
        self.first_songlist = songs # the original song list, which contains all the songs and doesn't remove any
        self.start_recomending_5 = 0 # start recomending after the fifth song
        self.second_songlist = second_songlist # the copy of the song list, which removes the songs that have been listened
        self.remove_songs = True # for now, but when we change to the first_songlist it'll be false
        self.getsongsfrom = second_songlist # from which list to we get the songs? later it'll change
        
        self.songs_forplaylist = list() # this will store the songs for playlist that are hearted
        self.playlist_songs = list() # this is the songs that will constitute the playlist (20)
        
        self.currentsong_index = 0 
        self.track_prev_or_next = 0 # keeps track of wether we clicked the prev button or the next button
        self.desired_position = ctk.DoubleVar()
        self.progress_var = ctk.DoubleVar() # the variable for the progress bar
        self.time_var = ctk.StringVar(value = "0:00") # the variable for the time
        self.update_music = False
        self.seconds = 0
        self.song_length = 0
        self.song_changed = False
        self.continue_updating = True
        self.hearted = False
        self.paused = True
        self.inplaylist = False
        self.value_per_song = dict()
        self.general_imagepath = "C:/Users/usuar/Downloads/Python/Main_PYfolder/TR/Images/"

        self.play_image = ctk.CTkImage(Image.open(self.general_imagepath+"playbutton_icon.png"))
        self.returnbutton_image = ctk.CTkImage(Image.open(self.general_imagepath+"returnbutton_icon.png"))

        self.return_button_info = ctk.CTkButton(self,text="",image=self.returnbutton_image,width=40,corner_radius=3,
                                                command=self.return_but_info, fg_color=self.button_color)

        self.automatic_next = False

        self.playlist_enabled = False
        self.count_toenable = 0

        self.charts_toForget = []
        self.exit_perfil = False
    
    def Nothing(self):
        pass

    def remove_widgets(self):
        for widget in self.widgets_gridforget:
            widget.grid_forget()
        self.widgets_gridforget.clear()
        for widget in self.widgets_placeforget:
            widget.place_forget()
        self.widgets_placeforget.clear()
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8),weight=0)
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8),weight=0)
    
    # loading screen functions and returns:
    def return_but_info(self):
        self.remove_widgets()
        self.load_homepage()

    def return_but_music(self):
        pygame.mixer.music.stop()
        self.continue_updating = False
        self.play_firsttime = True
        self.return_but_info()

    def return_but_playlist(self):
        self.return_but_info()

    def return_but_perfil(self,theframe):
        self.exit_perfil = True
        self.return_but_info()
        theframe.destroy()
        self.generalCharts("",[],[])
        self.exit_perfil = False
    
    def return_but_credits(self):
        self.return_but_info()

    def load_infoscreen(self):
        self.remove_widgets()
        self.grid_columnconfigure((0,1,2,3),weight=1)
        self.grid_rowconfigure((0,1,2,3),weight=1)

        self.info_label = ctk.CTkLabel(self,fg_color=self.button_color, text_color=self.text_color, font=("Calibri",17),
                                       text="El propòsit d'aquesta petita aplicació és de experimentar si un algoritme\n"
                                       "informàtic pot recomenar música adient a les preferènces de l'usuari. \n"
                                       "En la pantalla principal en trobaras 3 butons: un per reproduir, playlist i perfil.\n"
                                       "El primer butó et portarà al reproductor de música, on trobaràs una interfície \n"
                                       "senzilla per reproduir música. El segon botó (playlist), et portarà a una playlist\n"
                                       "feta per tú, però abans has d'escoltar 5 cançons mínim. Finalment, el terçer botó (perfil)\n"
                                       "et mostrarà gràfics amb les preferènces que ha calculat l'algoritme en cada paràmetre.",
                                       )
        self.info_label.grid(column=0,row=0,columnspan=4,rowspan=4,padx=50,pady=60,sticky="nsew")
        self.return_button_info.grid(column=0,row=0,columnspan=4,rowspan=4,sticky="ne")

        self.widgets_gridforget.extend([self.info_label,self.return_button_info])

    def load_homepage(self):
        Home.build(self)
    
    def reproductor_clicked(self):
        if self.inplaylist:
            self.currentsong_index = 0
            self.songs_toplay= list()
            self.songs_toplay.append(random.choice(self.getsongsfrom))
        self.inplaylist = False
        self.load_musicplayer()
    
    def playlist_play_clicked(self):
        self.inplaylist = True
        self.currentsong_index=0
        self.songs_toplay = self.playlist_songs
        self.load_musicplayer()

    def load_musicplayer(self):
        self.remove_widgets()
        music_player = MusicPlayer
        music_player.build(self)
        self.continue_updating=True

    def load_playlist(self):
        if self.playlist_enabled:
            self.remove_widgets()
            PlayList.build(self)
            PlayList.set_playlist(self)
        else:
            not_available_label = ctk.CTkLabel(self,text="Playlist not available.\nEscucha 5 canciones min.")
            not_available_label.grid(column=2,row=2,sticky="nw")
            widgets_gridforget.append(not_available_label)

    def load_perfil(self):
        self.remove_widgets()
        PerfilMusical.build(self)

    def load_credits(self):
        self.remove_widgets()
        Credits.build(self)
    # ---------- reproductor functions:
    def play_music(self):
        MusicPlayer.play(self)

    def pause_music(self):
        MusicPlayer.pause(self)
    
    def next_music(self):
        MusicPlayer.next(self)
    
    def prev_music(self):
        MusicPlayer.prev(self)

    def calc_percentages(self):
        MusicPlayer.calcpercentages2(self)
    def add_inter_songs(self,*args):
        arguments=args
        MusicPlayer.add_intersection_songs(self,arguments)
    
    def choose_music(self):
        if not self.inplaylist:
            MusicPlayer.choose_music2(self)
        else:
            pass

    def update_progress(self):
        progress = self.progress_var.get()
        if progress > self.song_length:
            self.automatic_next = True
            self.next_music()
        else:
            MusicPlayer.update_progress2(self)

    def new_song(self):
        MusicPlayer.new_song2(self)

    def progress_bar_clicked(self,event):
        MusicPlayer.progress_bar_clicked2(self,event)

    def study_user(self):
        MusicPlayer.study_user2(self)

    def heart(self):
        MusicPlayer.heart2(self)
    
    # perfil functions: 

    def generalCharts(self,title:str,parameters:list,values:list):

        if len(self.charts_toForget) != 0:
            for chart in self.charts_toForget:
                plt.close()
                chart.grid_forget()
        if self.exit_perfil:
            return
        new_chart = PerfilMusical.generalChart(self, title, parameters, values)
        new_chart.grid(row=1,column=0,columnspan=2, padx= 20,sticky="nsew")
        self.charts_toForget.append(new_chart)
   
class Login(ctk.CTk):
    def __init__(self):
        super().__init__() ###get everything from CTkFrame
        self.geometry("720x420")
        self.title("Inici de sesió")
        ######## Set the grid for this screen
        self.grid_rowconfigure((0,1,2,3,4,5),weight=1)
        self.grid_columnconfigure((0,1,2),weight=1)

        self.nextfunction = 0 #variable that determines whether to check user or password

        self.found_user = False #by now, user is not found yet
        self.current_pass = "" #the password that later will be stored


        self.userentry_var = ctk.StringVar (value="user") #variable for the entry, at first it writes "user"
        self.user_entry = ""

        #the title, entry, wrong password and the continue button:
        self.title_label = ctk.CTkLabel(self,text="Inici de sessió",corner_radius=100,font=("Bahnschrift Light Condensed",70))
        self.user_entry = ctk.CTkEntry(self,textvariable=self.userentry_var)
        self.wrong_label = ctk.CTkLabel(self,text="Contraseña incorrecta",text_color="Red")
        self.continuebutton = ctk.CTkButton(self,text="Next",fg_color="white",text_color="Black",command=self.continuar)

        #grid them:
        self.title_label.grid(row=0,column=0,rowspan=2,columnspan=3,sticky="n", pady=20)
        self.user_entry.grid(row=1,column=0,columnspan=3,sticky="s")
        self.continuebutton.grid(row=3,column=2,rowspan=2,sticky="n")
        
    def continuar(self):
        if self.nextfunction == 0:
            self.checkuser()
        else:
            self.checkpass()

    def checkuser(self):
        global line_index,user,password
        global genre_preference,lyrics_preference,energy_preference,era_preference
        global found_user

        self.user_input = self.user_entry.get()
        user = self.user_input
        pass_text = ""
        user_info = dict()
        for line in user_data:
            parameters = line.split(";")
            if self.user_input == parameters[0]:
                line_index = user_data.index(line)
                self.found_user = True
                pass_text = "password"
                #replace <'> with <">, and convert to dictionaries
                password = parameters[1]
                genres = ast.literal_eval(parameters[2].replace("'", "\""))
                lyrics = ast.literal_eval(parameters[3].replace("'", "\""))
                energy = ast.literal_eval(parameters[4].replace("'", "\""))
                era = ast.literal_eval(parameters[5].replace("'", "\""))

                user_info = {"Genres": genres, "Lyrics": lyrics, "Energy": energy, "Era": era}
                genre_preference = user_info["Genres"]
                lyrics_preference = user_info["Lyrics"]
                energy_preference = user_info["Energy"]
                era_preference = user_info["Era"]
                break
            parameters = []
        if not self.found_user:
            genre_preference = dict()
            lyrics_preference = dict()
            energy_preference = dict()
            era_preference = dict()
            pass_text = "New password" 
            ######ASIGN EACH GENRE,LYRICS,ENERGY,ERA AND TONE A PREFERENCE NUMBER
            for i in genre_list:
                genre_preference[i] = (1/len(genre_list))
            lyrics_preference["0-0.4"] = 0.5
            lyrics_preference["0.5-0.9"] = 0.5
            for i in energy_list:
                energy_preference[i] = (round(1/len(energy_list),2))
            for i in era_list:
                era_preference[i] = (round(1/len(era_list),2))
        
        ##create the password entry, its variable and grid the entry:
        self.passentry_var = ctk.StringVar (value=pass_text)
        self.pass_entry = ctk.CTkEntry(self,textvariable=self.passentry_var)
        self.pass_entry.grid(row=3,column=0,columnspan=3,sticky="s")
        found_user = self.found_user
        self.nextfunction +=1  #we checked the user, we can get to the next function: checkpass
    
    def checkpass(self):
        global password, login_done
        pass_input = self.pass_entry.get()

        if self.found_user: #if it is not a new user:
            if pass_input == password:
                login_done = True
                self.destroy()
            else:
                #if password is wrong, warn the user with a label below:
                self.wrong_label.grid(row=4,column=0,columnspan=3,sticky="n")
        else: #if it is a new user:
            password = pass_input
            login_done = True
            self.destroy()

class Home(App):
    def __init__(self, master):
        super().__init__(master)
        self.music_player = MusicPlayer
        self.app = App

    def build(self):
        self.grid_columnconfigure((0,2),weight=2)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure((0,1,2),weight=1)

        self.chart_image = ctk.CTkImage(Image.open(self.general_imagepath+"chart_icon.png"))
        self.reproduce_image = ctk.CTkImage(Image.open(self.general_imagepath+"playbutton_icon.png"))

        self.reproduce_button = ctk.CTkButton(self,text= "Reproduir",command=self.reproductor_clicked,fg_color=self.button_color,
                                              text_color=self.text_color,image=self.reproduce_image,compound="right")
        self.reproduce_button.grid(column=1,row=1,sticky="s")

        self.title_label = ctk.CTkLabel(self,text="AlgoRit", font=("Lucida Sans",80),text_color=self.text_color)
        self.title_label.grid(column=0,row=0,columnspan=3)

        self.perfil_button = ctk.CTkButton(self,text="Perfil",command=self.load_perfil,fg_color=self.button_color,
                                              text_color=self.text_color, image= self.chart_image,compound="right")
        self.perfil_button.grid(column=0,row=1,sticky="se")

        self.playlist_button = ctk.CTkButton(self,text="Playlist",command=self.load_playlist,fg_color=self.button_color,
                                              text_color=self.text_color)
        self.playlist_button.grid(column=2,row=1,sticky="ws")

        self.info_button = ctk.CTkButton(self,text="i",corner_radius=200,width=2,border_width=5,border_color="",fg_color=self.button_color,
                                              text_color=self.text_color, command=self.load_infoscreen)
        self.info_button.grid(column=2,row=2,sticky="es")

        self.credits_button = ctk.CTkButton(self,text="Credits",fg_color="transparent",hover_color="grey", text_color=self.text_color,
                                            command=self.load_credits)
        self.credits_button.grid(column=0,row=2,sticky="sw")
    
        self.widgets_gridforget.extend([self.reproduce_button,self.title_label,self.perfil_button,self.playlist_button,self.info_button,self.credits_button])

class MusicPlayer(App):
    def __init__(self, master):
        super().__init__(master)

    def update_progress2(self):
        if self.continue_updating:
            print("Progreso...")
            progress = self.progress_var.get()
            progress += 1

            self.progress_var.set(progress)
            self.seconds = progress
            minutes = 0
            if self.update_music:
                pygame.mixer.music.set_pos(self.seconds)
                self.update_music = False
            while self.seconds >= 60:
                minutes+=1
                self.seconds-=60
            self.seconds = round(self.seconds)
            self.time_var.set(f"{minutes}:{str(self.seconds).zfill(2)}")
            self.after(1000,self.update_progress)
        else:
            pass

    def new_song2(self):
        self.seconds = 0
        if self.songs_toplay[self.currentsong_index] in self.songs_forplaylist:
            self.hearted = True
            self.heart_button.configure(image=self.heart_image2)
        else:
            self.hearted = False
            self.heart_button.configure(image=self.heart_image1)
        self.progress_bar.configure(to=self.song_length)
        self.progress_var.set(0)
        self.time_var.set("0:00")
    def play(self):
        self.paused = False
        pygame.mixer.music.load(self.songs_toplay[self.currentsong_index])
        self.song_length= pygame.mixer.Sound(self.songs_toplay[self.currentsong_index]).get_length()
        length = self.song_length/60
        minutes_song = round(length)
        seconds_song = abs(round((length-minutes_song)*100))
        self.total_time_label.configure(text=f"{minutes_song}:{str(seconds_song).zfill(2)}")
        self.new_song()
        pygame.mixer.music.play(start=int(self.desired_position.get()))
        
        if self.continue_updating:
            self.update_progress()
        else:
            self.continue_updating = True
        
        if self.automatic_next:
            self.update_progress()
            self.automatic_next = False

    def pause(self):
        if self.play_firsttime:
            self.play_music()
            self.play_firsttime = False
            self.play_button.configure(image=self.unpaused_image)
        else:
            if self.paused:
                self.continue_updating = True
                self.play_button.configure(image=self.unpaused_image)
                pygame.mixer.music.unpause()
                self.update_progress()
                self.paused = False
            else:
                self.continue_updating = False
                self.play_button.configure(image=self.play_image)
                pygame.mixer.music.pause()
                self.paused = True 
    def next(self):
        self.continue_updating = False
        if self.track_prev_or_next < 0:
            self.track_prev_or_next +=1
        else:
            if self.start_recomending_5 > 3:
                self.choose_music()
                print("EMPEZAR A RECOMENDAR")
                self.playlist_enabled = True
            else:
                self.start_recomending_5 += 1
            if not self.inplaylist:
                self.study_user()
            else:
                pass
        if self.paused:
            self.continue_updating = True
        if self.currentsong_index == (len(self.songs_toplay) - 1):
            self.currentsong_index = 0
        else:
            self.currentsong_index +=1
        print(self.currentsong_index)
        self.play_music()
        self.play_button.configure(image=self.unpaused_image)
        
        current_song = same_url[self.songs_toplay[self.currentsong_index]][0]
        author = current_song.author
        song_name = current_song.name
        self.song_author_label.configure(text=f"{song_name}\n{author}")
    
    def prev(self):
        self.continue_updating = False
        if self.currentsong_index==0:
            self.continue_updating = True
            return
        if self.paused:
            self.continue_updating = True
        self.track_prev_or_next -=1
        self.currentsong_index -= 1
        self.play_music()
        self.play_button.configure(image=self.unpaused_image)
        
        current_song = same_url[self.songs_toplay[self.currentsong_index]][0]
        author = current_song.author
        song_name = current_song.name
        self.song_author_label.configure(text=f"{song_name}\n{author}")

    def calcpercentages2(self):
        global genre_list,lyrics_list, energy_list, era_list
        global genre_preference,lyrics_preference, energy_preference, era_preference
        global genre_percent,lyrics_percent, energy_percent, era_percent
        suma = 0

        genre_percent,lyrics_percent,energy_percent,era_percent = ([] for i in range(4))
        genre_dict = {"list":genre_list,"preference":genre_preference,"percent":genre_percent} #genre_dict for later use
        lyrics_dict = {"list":["0-0.4","0.5-0.9"],"preference":lyrics_preference,"percent":lyrics_percent} #lyrics_dict for later use
        energy_dict = {"list":energy_list,"preference":energy_preference,"percent":energy_percent} #energy_dict for later use
        era_dict = {"list":era_list,"preference":era_preference,"percent":era_percent} #era_dict for later use
        order = [genre_dict,lyrics_dict,energy_dict,era_dict]
        for dictn in order:  
            suma = sum(dictn["preference"].values()) #sums every value of the current picked dictionary's preference (ex: genre_dict->genre_pref.)
            for i in range(len(dictn["list"])): #for i in the range of the lenght of the current picked list
                number = dictn["preference"][dictn["list"][i]] #number = value of the current item in the preference dict. (current item is list[i])
                dictn["percent"].append(round(number*100/suma)/100) #appends to the current percent_list the percentage
    
    def add_intersection_songs(self,*args):
        global chosen_songs
        intersections_tocheck = list(args)
        for intersection in intersections_tocheck:
            for song_object in intersection:
                if len(song_object)==0:
                    pass
                else:
                    chosen_songs.append(song_object)
        # print("CHOSEN SONGS BEFORE:",chosen_songs)
        # flat_list = self.flatten_chosensong_list(chosen_songs)
        flat_list = []
        for i in chosen_songs:
            flat_list.extend(list(i))
        chosen_songs = flat_list
        #print("\nCHOSEN SONGS AFTER:",chosen_songs)
        chosen_songs = [s for s in chosen_songs if s in self.getsongsfrom]
    def choose_music2(self):
        global genre_list,lyrics_list, energy_list, era_list
        global genre_preference,lyrics_preference, energy_preference, era_preference
        global genre_percent,lyrics_percent, energy_percent, era_percent
        global same_genre,same_lyrics,same_energy,same_era,same_tone
        global tonalitats,chosen_songs
        if len(self.songs_toplay) > 55:
            self.getsongsfrom = self.first_songlist
            self.remove_songs = False
        
        self.calc_percentages()##calculate the percentages

        #choose the parameters:
        chosen = {"Genre":random.choices(genre_list,genre_percent)[0],"Lyrics":random.choices(["0-0.4","0.5-0.9"],lyrics_percent)[0],
                "Energy":random.choices(energy_list,energy_percent)[0],"Era":random.choices(era_list,era_percent)[0]}
        print("Chosen parameters:",chosen)
        #you can get rid of this, this only to test:
        current_song = random.choice(song_list)
        current_tone = current_song.tone

        #init the sets:
        genre_set,lyrics_set,energy_set,era_set = (set() for i in range(4))
        
        ###set up of the lyrics_set:
        lyrics_range = 0
        count_torange = 0
        lyrics_listtoset = list()
        
        if chosen["Lyrics"] == "0-0.4":
            lyrics_range = 0.4
        elif chosen["Lyrics"] == "0.5-0.9":
            lyrics_range = 0.9
            count_torange=0.5
        else:
            print("ERROR EN EL LYRICS RANGE")
            exit()
        while not count_torange > lyrics_range:
            lyrics_listtoset.extend((same_lyrics[str(count_torange)]))
            lyrics_set = set(lyrics_listtoset)
            count_torange += 0.1
            count_torange = round(count_torange,1)
    ##########the other sets:
        genre_set = set(same_genre[chosen["Genre"]])
        tone_set = set(same_tone[current_tone])
        energy_set = set(same_energy[chosen["Energy"]])
        era_set = set(same_era[chosen["Era"]])
        
        enough = 0 #variable that when reaches 3, stops all the process and choses the song
        chosen_songs = [] #the raw list that contains the songs without checking the tune
        songs_toplay = [] #after checking the tune, this list will have only 3 songs

    #define the intersections:
        genre_energy = genre_set.intersection(energy_set)
        lyrics_era = lyrics_set.intersection(energy_set)
        complete_inter = genre_energy.intersection(lyrics_era)
        
        genre_era = genre_set.intersection(era_set)
        genre_lyrics = genre_set.intersection(lyrics_set)
        energy_lyrics = energy_set.intersection(lyrics_set)
        energy_era = energy_set.intersection(era_set)
        perfect_inter = genre_era.intersection(genre_lyrics,energy_lyrics,energy_era)

        genre_energy_lyrics = genre_set.intersection(energy_set,lyrics_set)
        energy_lyrics_era = energy_set.intersection(lyrics_set,era_set)
        genre_energy_era = genre_set.intersection(energy_set,era_set)
        genre_lyrics_era = genre_set.intersection(lyrics_set,era_set)
        #add the songs in the intersections to the chosen_songs:
        self.add_inter_songs(perfect_inter,complete_inter,genre_energy_lyrics,energy_lyrics_era,genre_energy_era,genre_lyrics_era,genre_energy,
                            lyrics_era,genre_era,genre_lyrics,energy_lyrics,energy_era)

        for sng in chosen_songs:
            if enough == 2:
                break
            if sng.tone == current_tone:
                songs_toplay.append(sng.url)
                enough +=1
        songs_toplay = set(songs_toplay)
        
        if len(songs_toplay) < 2:
            for sng in chosen_songs:
                if enough==2:
                    break
                if sng.tone in tonalitats[current_tone]:
                    songs_toplay.add(sng.url)
                    enough+=1
        
        if len(songs_toplay)<2:
            try:
                songs_toplay = list(list(songs_toplay).extend(same_tone[current_tone]))
                songs_toplay = set(songs_toplay)
            except:
                pass
            for tones in tonalitats[current_tone]:
                if enough ==2:
                    break
                try:
                    songs_toplay = list(songs_toplay).extend(same_tone[tones])
                    songs_toplay = set(songs_toplay)
                except:
                    pass
        
        if songs_toplay == None:
            songs_toplay = set()
        count_forglitching = 0
        
        if len(songs_toplay)<2:
            while len(songs_toplay) < 2:
                if count_forglitching > 20:
                    break
                try:
                    random_song = random.choice(chosen_songs)
                    song_url = random_song.url
                except:
                    random_song = random.choice(song_list)
                    song_url = random_song.url
                if song_url not in songs_toplay:
                    songs_toplay.add(song_url)
                    print("One song was added randomly")
                else:
                    print(f"The song was already in the songs to play list: {song_url}")
                count_forglitching +=1
        
        while len(songs_toplay)<2:
            songs_toplay.add(random.choice(song_list))

        songs_toplay = list(songs_toplay)

        for i,songs in enumerate(songs_toplay):
            if isinstance(songs_toplay[i],str):
                pass
            else:
                songs_toplay[i] = songs_toplay[i].url
        print("\nSongs to play: ",songs_toplay,"\n",len(songs_toplay))

        for sngo in songs_toplay:
            self.songs_toplay.append(general_path+sngo)
        if self.remove_songs:
            for s in songs_toplay:
                try:
                    print("SONG TO REMOVE:",s)
                    self.getsongsfrom.remove(general_path+s)
                    print("\nBorrada con exito")
                except:
                    print("\nNo se ha podido borrar ¿?")
        else:
            pass
        
        print("\nLENGHT SONGS TO PLAY:",len(self.songs_toplay))
    def study_user2(self):
        global genre_preference,lyrics_preference, energy_preference, era_preference
        try:
            max_percentage = 79
            num_to_add = 0
            percentage_listened = round(self.seconds*100/self.song_length)
            if percentage_listened > max_percentage:
                num_to_add +=0.09
            else:
                num_to_add += percentage_listened*0.09/max_percentage
            
            if self.hearted:
                num_to_add += 0.09
            
            current_song_url = self.songs_toplay[self.currentsong_index]
            current_song = same_url[current_song_url]
            for e in current_song:
                current_song = e
            lyrics = ""
            if float(current_song.lyrics) < 0.5:
                lyrics = "0-0.4"
            else:
                lyrics = "0.5-0.9"
            genre_preference[current_song.genre] += num_to_add
            lyrics_preference[lyrics] += num_to_add
            energy_preference[current_song.energy] += num_to_add
            era_preference[current_song.era] += num_to_add

            if current_song_url not in self.value_per_song:
                self.value_per_song[current_song_url] = num_to_add
            else:
                if self.value_per_song[current_song_url] < num_to_add:
                    self.value_per_song[current_song_url] = num_to_add
                else:
                    pass
            print("\n",self.value_per_song)
        except:pass

    def heart2(self):
        if self.hearted:
            self.heart_button.configure(image=self.heart_image1)
            self.hearted = False
            self.songs_forplaylist.remove(self.songs_toplay[self.currentsong_index])
            print(self.songs_forplaylist)
        else:
            self.heart_button.configure(image=self.heart_image2)
            self.hearted = True
            if self.songs_toplay[self.currentsong_index] not in self.songs_forplaylist:
                self.songs_forplaylist.append(self.songs_toplay[self.currentsong_index])
            print(self.songs_forplaylist)

    def progress_bar_clicked2(self,event):
        self.update_music=True
    def build(self):
        self.grid_columnconfigure((0,1,2,3,4),weight=1)
        self.grid_rowconfigure((0),weight=3)
        self.grid_rowconfigure((1,2,3),weight=1)

        #first song and author text:
        first_song = same_url[self.songs_toplay[self.currentsong_index]][0]
        author = first_song.author
        song_name = first_song.name

        #images:
        self.next_image = ctk.CTkImage(Image.open(self.general_imagepath+"nextbutton_icon.png"))
        self.prev_image = ctk.CTkImage(Image.open(self.general_imagepath+"prevbutton_icon.png"))
        self.unpaused_image = ctk.CTkImage(Image.open(self.general_imagepath+"pausedbutton_icon.png"))
        #self.cover_image = ctk.CTkImage(Image.open(self.general_imagepath+"portada_image.png"))
        self.heart_image1 = ctk.CTkImage(light_image=Image.open(self.general_imagepath+"heart_icon1light.png"),
                                         dark_image=Image.open(self.general_imagepath+"heart_icon1.png"))
        self.heart_image2 = ctk.CTkImage(Image.open(self.general_imagepath+"heart_icon2.png"))

        cover_image = Image.open(self.general_imagepath+"portada_image.png")
        resized_image = cover_image.resize((250,250),Image.LANCZOS)
        self.cover_image = ImageTk.PhotoImage(resized_image)

        if self.songs_toplay[self.currentsong_index] in self.songs_forplaylist:
            first_heart_image = self.heart_image2
        else:
            first_heart_image = self.heart_image1
        #widgets:
        self.play_button = ctk.CTkButton(self,text="",width=50,height=40,image=self.play_image,command=self.pause_music, 
                                         fg_color=self.button_color)
        self.play_button.place(relx=0.5,rely=0.8, anchor="center")
        
        self.next_button = ctk.CTkButton(self,text="",width=50,height=40,image=self.next_image,command=self.next_music, 
                                         fg_color=self.button_color)
        self.next_button.place(relx=0.6,rely=0.8, anchor="center")
        
        self.prev_button = ctk.CTkButton(self,text="",width=50,height=40,image = self.prev_image,command=self.prev_music, 
                                         fg_color=self.button_color)
        self.prev_button.place(relx=0.4,rely=0.8, anchor="center")
        
        self.progress_bar = ctk.CTkSlider(self,variable=self.progress_var,width=560,from_=0,to=200,button_color=self.button_color,
                                          button_hover_color=("black","white"))
        self.progress_bar.place(relx=0.5,rely=0.7, anchor="center")
        self.progress_bar.bind("<Button-1>", self.progress_bar_clicked)
        
        self.cover_label = ctk.CTkLabel(self,text="",font=('Helvetica',70),bg_color="White",image=self.cover_image)
        self.cover_label.place(relx=0.5,rely=0.35, anchor="center")
        
        self.song_author_label = ctk.CTkLabel(self,text=f"{song_name}\n{author}",justify="left", text_color=self.text_color)
        self.song_author_label.place(relx=0.12,rely=0.6)
        
        self.current_time_label = ctk.CTkLabel(self,textvariable=self.time_var, text_color=self.text_color)
        self.current_time_label.place(relx=0.11,rely=0.72)
        
        self.total_time_label = ctk.CTkLabel(self,text="0:00", text_color=self.text_color)
        self.total_time_label.place(relx=0.88,rely=0.72,anchor="ne")
        
        self.heart_button = ctk.CTkButton(self,text="",image=first_heart_image,fg_color="transparent",text_color="black",width=20,command=self.heart)
        self.heart_button.place(relx=0.85,rely=0.64, anchor="center")

        self.return_button_music = ctk.CTkButton(self,text="",image=self.returnbutton_image,width=40,corner_radius=3,
                                                 command=self.return_but_music, fg_color=self.button_color)
        self.return_button_music.grid(column=2,columnspan=3,row=0,rowspan=3,sticky="ne")     

        widgets_gridforget.extend([
                                   self.return_button_music])
        widgets_placeforget.extend([self.play_button,self.next_button,self.prev_button,self.progress_bar,self.cover_label,self.heart_button,
                                    self.song_author_label,self.current_time_label,self.total_time_label])

class PlayList(App):
    def __init__(self, master):
        super().__init__(master)
    
    def set_playlist(self):
        self.playlist_songs.extend(self.songs_forplaylist)
        song_per_values = {value: key for key, value in self.value_per_song.items()}

        sorted_values = sorted(list(song_per_values.keys()),key=float)
        song_ammount = 20-len(self.playlist_songs)

        self.playlist_songs = set(self.playlist_songs)
        for i in range(song_ammount):
            try:
                self.playlist_songs.add(song_per_values[sorted_values[i]])
            except:
                break
        l = list(self.playlist_songs)
        for i,s in enumerate(l):
            shortened_s = s.replace("C:/Users/usuar/Downloads/Python/Main_PYfolder/TR/Music/","")
            shortened_s = shortened_s.replace(".wav","")
            if len(shortened_s)>35: shortened_s = shortened_s[:34] + "..."
            l[i]= str(i+1) + ". " + shortened_s
        first_10_songs = l[:10] + ["-"] * (10 - len(l[:10]))
        next_10_songs = l[10:20] + ["-"] * (10 - len(l[10:20]))

        first_10_text = "\n".join(first_10_songs)
        next_10_text = "\n".join(next_10_songs)

        self.first10_songs.configure(text=first_10_text)
        self.next10_songs.configure(text=next_10_text)

        self.playlist_songs = list(self.playlist_songs)

        # print(l)
        # self.first10_songs.configure(text=f"{l[0]}\n{l[1]}\n{l[2]}\n{l[3]}\n{l[4]}\n{l[5]}\n{l[6]}\n{l[7]}\n{l[8]}\n{l[9]}")
        # self.next10_songs.configure(text=f"{l[10]}\n{l[11]}\n{l[12]}\n{l[13]}\n{l[14]}\n{l[15]}\n{l[16]}\n{l[17]}\n{l[18]}\n{l[19]}")
        

    def build(self):
        self.grid_columnconfigure((0,1,2),weight=1)
        self.grid_rowconfigure((0,1,2,3),weight=1)

        self.playlist_title = ctk.CTkLabel(self,text="PLAYLIST:",font=(self.titles_font,50), text_color=self.text_color)
        self.playlist_title.grid(column=0,row=0,columnspan=3,sticky="nw",pady=20,padx=20)

        self.first10_songs = ctk.CTkLabel(self,justify="left", text_color=self.text_color,
                                          text="Song1\nSong2\nSong3\nSong4\nSong5\nSong6\nSong7\nSong8\nSong9\nSong10",
                                          fg_color=self.button_color)
        self.first10_songs.place(relx=0.02,rely=0.28,relheight=0.7,relwidth=0.35)

        self.next10_songs = ctk.CTkLabel(self,justify="left", text_color=self.text_color,
                                         text="Song11\nSong12\nSong13\nSong14\nSong15\nSong16\nSong17\nSong18\nSong19\nSong20",
                                         fg_color=self.button_color)
        self.next10_songs.place(relx=0.37,rely=0.28,relheight=0.7,relwidth=0.35)

        self.playlist_play = ctk.CTkButton(self,text="",image=self.play_image,corner_radius=200,command=self.playlist_play_clicked,
                                           fg_color=self.button_color)
        self.playlist_play.place(relx=0.85,rely=0.65,relwidth=0.1,relheight=0.1,anchor = "center")

        self.return_button_playlist = ctk.CTkButton(self,text="",image=self.returnbutton_image,width=40,corner_radius=3,
                                                    command=self.return_but_playlist, fg_color=self.button_color)
        self.return_button_playlist.place(relx=1,rely=0,anchor="ne")

        self.widgets_gridforget.append(self.playlist_title)
        self.widgets_placeforget.extend([self.first10_songs,self.next10_songs,self.playlist_play, self.return_button_playlist])

class PerfilMusical(App):
    def __init__(self, master):
        super().__init__(master)
    
    def generalChart(self,title:str, parameters:list,values:list):
        global ax, fig
        categories = parameters
        data = values  
        print(title,categories)
        print(title,data)
        num_vars = len(categories)
        print(f"{title}: {categories}")
        # Create an array of evenly spaced angles to represent each variable
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]  # Repeat the first angle to create a 'closed' shape

        # Ensure the data list has the same length as angles
        data += data[:1]  # Repeat the first data point to match the number of angles

        # Create a Matplotlib figure and axis
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, polar=True)

        # Plot the data points
        ax.fill(angles, data, 'b', alpha=0.1)  # Fill the area under the curve with blue
        
        # Add labels for each axis
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)

        # Set the title
        ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.config(width=100,height=100)

        data.pop(-1)

        return canvas_widget

    def build(self):
        self.grid_columnconfigure((0,1,2,3),weight=1)
        self.grid_rowconfigure(1,weight=4)
        self.grid_rowconfigure((0,2),weight=1)

        # chart categories and data:
        self.genreChart_categories = list(genre_preference.keys())
        self.genreChart_data = list(genre_preference.values())

        self.lyricsChart_categories = list(lyrics_preference.keys())
        self.lyricsChart_data = list(lyrics_preference.values())
        self.lyricsChart_categories.append("")
        self.lyricsChart_data.append(0.5)

        self.energyChart_categories = list(energy_preference.keys())
        self.energyChart_data = list(energy_preference.values())

        self.eraChart_categories = list(era_preference.keys())
        self.eraChart_data = list(era_preference.values())
        #self.graphic_label = ctk.CTkLabel(self,text="GRAFICO",fg_color="red")
        #self.graphic_label.grid(row=1,column=0,columnspan=2, padx= 20,sticky="nsew")
        self.return_button_perfil = ctk.CTkButton(self,text="",image=self.returnbutton_image,width=40,corner_radius=3,
                                                  command= lambda: self.return_but_perfil(self.graphic_selecter), fg_color=self.button_color)
        self.return_button_perfil.place(relx=1,rely=0,anchor="ne")

        self.graphic_selecter = ctk.CTkFrame(self,fg_color=self.button_color)
        self.graphic_selecter.grid_rowconfigure((0,1,2,3),weight=1)

        radio_var = ctk.IntVar(value=0)
        self.genreChart_button = ctk.CTkRadioButton(self.graphic_selecter, text="Perfil respecte el genere", variable= radio_var,value=1,
                                                    command= lambda: self.generalCharts("Generes",self.genreChart_categories,self.genreChart_data))
        self.genreChart_button.grid(column=0, row=0, sticky="w", padx = 10)

        self.lyricsChart_button = ctk.CTkRadioButton(self.graphic_selecter, text="Perfil respecte la lletra", variable= radio_var, value=2,
                                                     command= lambda: self.generalCharts("Lletra",self.lyricsChart_categories,self.lyricsChart_data))
        self.lyricsChart_button.grid(column=0, row=1, sticky="w", padx = 10)

        self.energyChart_button = ctk.CTkRadioButton(self.graphic_selecter,text="Perfil respecte l'energia", variable= radio_var, value=3,
                                                     command= lambda: self.generalCharts("Energia",self.energyChart_categories,self.energyChart_data))
        self.energyChart_button.grid(column=0, row=2, sticky="w", padx = 10)

        self.eraChart_button = ctk.CTkRadioButton(self.graphic_selecter,text="Perfil respecte l'era", variable= radio_var, value=4,
                                                  command= lambda: self.generalCharts("Era",self.eraChart_categories,self.eraChart_data))
        self.eraChart_button.grid(column=0, row=3, sticky="w", padx = 10)

        self.graphic_selecter.place(relx= 0.8, rely = 0.5, relheight= 0.7, relwidth= 0.3,anchor = "center")

        self.widgets_gridforget.extend([self.genreChart_button, self.lyricsChart_button, self.energyChart_button, self.eraChart_button,
                                        self.graphic_selecter])
        self.widgets_placeforget.extend([self.return_button_perfil])

class Credits(App):
    def __init__(self, master):
        super().__init__(master) 
    
    def build(self):
        
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=6)
        self.grid_rowconfigure(2,weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5),weight=1)

        self.credits_title = ctk.CTkLabel(self, text="CREDITS", font=(self.titles_font,65))
        self.credits_title.grid(column=1, row = 0, columnspan=4, sticky="n", pady=20)

        self.return_button_credits = ctk.CTkButton(self, text = "",image=self.returnbutton_image, width=40,corner_radius=3,
                                                   command=self.return_but_credits, fg_color=self.button_color)
        self.return_button_credits.place(relx=1, rely=0, anchor="ne")

        self.credits_text = ctk.CTkTextbox(master=self, width=400, corner_radius=0)
        self.credits_text.grid(row=1, column=1,columnspan=4, sticky="nsew")
        self.credits_text.tag_config("center", justify="center")
        self.credits_text.insert("0.0", credits_text, tags="center")
        self.credits_text.configure(state="disabled")

        self.widgets_gridforget.extend([self.credits_title, self.credits_text])
        self.widgets_placeforget.extend([self.return_button_credits])



login = Login()
login.resizable(False, False)
login.mainloop()

pygame.init()
pygame.mixer.init()

app = App()
app.configure(fg_color=("#f0ebeb","#16161a"))
app.resizable(False, False)
app.load_homepage()

# since when opening a graphic the code runs infinitely, we must force closing the window:

def on_closing():
    app.quit()
    app.destroy()
app.protocol("WM_DELETE_WINDOW", on_closing)

if login_done:
    app.mainloop()

# write data in 'Music_userdata.txt':

    with open('C:/Users/usuar/Downloads/Python/Main_PYfolder/TR/Music_userdata.txt','r') as file:
        lineas = file.readlines()

    if not found_user: 
        with open('C:/Users/usuar/Downloads/Python/Main_PYfolder/TR/Music_userdata.txt','a') as a: 
            a.write(f"\n{user};{password};{genre_preference};{lyrics_preference};{energy_preference};{era_preference}")

    else:
        lineas[line_index] = f"{user};{password};{genre_preference};{lyrics_preference};{energy_preference};{era_preference}\n"
        with open('C:/Users/usuar/Downloads/Python/Main_PYfolder/TR/Music_userdata.txt','w') as w:
            w.writelines(lineas)