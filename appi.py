#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#Author: Esko Viranko - EoAapp

import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import subprocess
import sys
from win32api import GetSystemMetrics
LARGE_FONT=("verdana",12)
NORM_FONT=("verdana",10)

def quit():
    quit()

#näytön resoluutio
WxH=str(GetSystemMetrics(0)) + "x" + str(GetSystemMetrics(1))
leveys=GetSystemMetrics(0)
korkeus=GetSystemMetrics(1)


class EoAapp (tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "EoAapp")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=2,minsize=100)
        container.grid_columnconfigure(0, weight=2,minsize=100)

        #menu
        menubar=tk.Menu(container)
        filemenu=tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Asetukset")
        filemenu.add_command(label="Exit",command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self,menu=menubar)
        
        #ikkunan lataaminen
        self.frames = {}


        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):


    #nappulat ja otsikot
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="EoAapp", font=LARGE_FONT)
        label.grid(row=1,column=0)

        tyhja = tk.Label(self, text="       ", font=LARGE_FONT)
        tyhja.grid(row=1,column=1)

        label2 = tk.Label(self, text="Puh. xxx xxxxxxx")
        label2.grid(row=1,column=2)

        butLasi = ttk.Button(self, text="Suurennuslasi")
        butLasi["command"]=self.lasi
        butLasi.place(x=120,y=int(korkeus*0.95-110),height=100,width=100)

        butLehti = ttk.Button(self, text="Päivänlehti")
        butLehti["command"]=self.lehti
        butLehti.place(x=10,y=int(korkeus*0.95-110),height=100,width=100)

        butDuuni = ttk.Button(self, text="DuuniTori")
        butDuuni["command"]=self.duuni
        butDuuni.place(x=230,y=int(korkeus*0.95-110),height=100,width=100)

		
        butRemote = ttk.Button(self, text="TARVITSETKO APUA?")
        butRemote["command"] = self.kysely
        butRemote.place(x=10,y=int(korkeus/3),height=100,width=int(leveys/2-20))

    #nappuloiden funktiot
    def lasi(self):
            
            os.startfile("C:\Windows\System32\magnify.exe")


    def lehti(self):
            webbrowser.open("www.iltalehti.fi/")
	
	
    def duuni(self):
            webbrowser.open("www.duunitori.fi/")
			
    #etakaytton vahvistus ikkuna
    def kysely(StartPage):
        ikkuna = tk.Tk()

        ikkuna.wm_title("Tarvitsetko apua?")
        
        label = ttk.Label(ikkuna,text="Tarvitsetko apua?",font=LARGE_FONT)
        label.grid(row=0,column=0)
        
        label2 = ttk.Label(ikkuna,text="Puh. xxx xxxxxx",font=LARGE_FONT)
        label2.grid(row=1,column=0)
        
        label3 = ttk.Label(ikkuna,text="Kuvaile lyhyesti ongelmaa.",font=NORM_FONT)
        #label3.grid(row=2,column=0)
        label3.place(x=10,y=int(korkeus/11))

        ent = Entry(ikkuna)
        ent.place(x=10,y=int(korkeus/8),height=100,width=int(leveys/4-20))

        butLaheta= ttk.Button(ikkuna,text="Lähetä",command=lambda: ok())
        butLaheta.place(x=10,y=int(korkeus/4),height=80,width=int(leveys/4-20))
      
        def ok():
                teksti=ent.get()
                file = open("vika.txt","w")
                file.write(teksti)
                file.close()
                ikkuna.destroy()
                

        ikkuna.geometry("720x1060")
        ikkuna.maxsize(width=int(leveys/4), height=int(korkeus/3))
        ikkuna.minsize(width=int(leveys/4), height=int(korkeus/3))
        ikkuna.mainloop()





#ikkunan koko ja lukitus
app = EoAapp()
app.geometry("720x1060")
app.maxsize(width=int(leveys/2), height=int(korkeus*0.95))
app.minsize(width=int(leveys/2), height=int(korkeus*0.95))
app.mainloop()
