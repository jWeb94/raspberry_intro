#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk, Image
import os

def callback2():
    print(1 + 1)

def main():
    # Fuer das gui-image
    rescale_size_w = 200
    rescale_size_h = 150


    root = Tk() # Fenster erstellen -> Zugriff ueber die Variable root
    root.wm_title("Raspberry Pi GUI") # Fenster Titel
    root.config(background = "#000000") # Hintergrundfarbe des Fensters in RGB-Hex -> kann man googeln

    # Frames -> Rahmen innerhalb deren man schreiben oder Elemente erstellen kann

    # Left Frame:
    leftFrame = Frame(root, width=200, height=400) # Frame initialisieren -> zugriff ueber leftFrame als Variable
    leftFrame.grid(row=0, column=0, padx=1, pady=3) # Relative Position und Seitenabstand (padding) angeben
        # padx und pady definiert den Abstand zum Rand des Fensters

    # Hier kommen die Elemente des linken Frames rein
    leftLabel1 = Label(leftFrame, text="Hier kommt die GUI", font=("Helvetica", 16), fg="red")  # Label sind quasi Beschriftungen
    leftLabel1.grid(row=0, column=0, padx=10, pady=3)       # Grid-Einstellungen
    leftLabel2 = Label(leftFrame, text="Dieses Bild zeigt\nden neuen Audi R8:")
    leftLabel2.grid(row=1, column=0, padx=10, pady=3)

        # lade bild mit PIL
    img = Image.open("/home/jens/Schreibtisch/rasperry_pi/software/2019-audi-r8-v10-performance-looks-brutal-in-yellow-130641_1.jpg")
    img = img.resize((rescale_size_w, rescale_size_h), Image.ANTIALIAS)
        # rescale image
    imageEx = ImageTk.PhotoImage(img)
        # erstelle Tkinter bild-objekt
    Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=3)
        # fuege Bild ein

    # Right Frame:
    rightFrame = Frame(root, width=400, height = 400)
    rightFrame.grid(row=0, column=1, padx=1, pady=3)
    # Hier kommen die Elemente des rechten Frames rein
        # Entry = Eingabefeld
    E1 = Entry(rightFrame, width=50)    # Breite wird in Zeichen angegeben
    E1.grid(row=0, column=0, padx=10, pady=3)

    def callback1():
        print(E1.get())

    buttonFrame = Frame(rightFrame)
    buttonFrame.grid(row=1, column=0, padx=10, pady=3)

    B1 = Button(buttonFrame, text="Button 1", bg="#FF0000", width=15, command=callback1)
    B1.grid(row=0, column=0, padx=10, pady=3)

    B2 = Button(buttonFrame, text="Button 2", bg="#FFFF00", width=15, command=callback2)
    B2.grid(row=0, column=1, padx=10, pady=3)

    Slider = Scale(rightFrame, from_=0, to=100, resolution=0.1, orient=HORIZONTAL, length=400)
    Slider.grid(row=2, column=0, padx=10, pady=3)

    root.mainloop() # GUI wird upgedated. Danach keine Elemente setzen



if __name__== "__main__": main()
# Das wird nur beim Aufrufen des Skripts ausgefuerht!
