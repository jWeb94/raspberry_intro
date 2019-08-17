#!/usr/bin/python3

from tkinter import *
from PIL import ImageTk, Image
import os
from termcolor import colored
import sys

def callback1(entry_object):
    print(entry_object.get())

def callback2():
    print(1 + 1)

def create_window(window_name, color="black"):

    root = Tk() # Fenster erstellen -> Zugriff ueber die Variable root
    root.wm_title(window_name) # Fenster Titel
    if color == "black":
        root.config(background = "#000000") # Hintergrundfarbe des Fensters in RGB-Hex -> kann man googeln
    elif color == "white":
        root.config(background = "#FFFFFF")
    else:
        print(colored('ERROR: No valid color for the background of the window.', 'red')) # colors.red('ERROR: No valid color for the background of the window'))
        sys.exit()
    return root

def create_frame(window, heigh_frame, width_frame, row_frame, col_frame):
    frame_handle = Frame(window, width=width_frame, height=heigh_frame) # Frame initialisieren -> zugriff ueber frame_handle als Variable
    frame_handle.grid(row=row_frame, column=col_frame, padx=2, pady=2) # Relative Position und Seitenabstand (padding) angeben
        # padx und pady definiert den Abstand zum Rand des Fensters
    return frame_handle


def create_label(frame, text_label, row_label, col_label, caption=False):

    if caption == True:
        label_handle = Label(frame, text=text_label, font=("Helvetica", 16), fg="red")  # Label sind quasi Beschriftungen
        label_handle.grid(row=row_label, column=col_label, padx=10, pady=3)       # Grid-Einstellungen
            # padx und pady sind relativ zu bisher im frame existierenden labels
    elif caption == False:
        label_handle = Label(frame, text=text_label)  # Label sind quasi Beschriftungen
        label_handle.grid(row=row_label, column=col_label, padx=10, pady=3)       # Grid-Einstellungen
    else:
        print(colored('ERROR: No valid caption specification for the background of the window.', 'red')) # colors.red('ERROR: No valid color for the background of the window'))
        #print(colors.red('ERROR: No valid caption specification for the background of the window'))
        sys.exit()
    return label_handle

def create_entry(frame, width_entry, row_entry, col_entry):
        # Entry = Eingabefeld
        E1 = Entry(frame, width=width_entry)    # Breite wird in Zeichen angegeben
        E1.grid(row=row_entry, column=col_entry, padx=10, pady=3)
        return E1

def create_button(frame, button_text, color, callback, row_button, col_button, parameter_callback=False):
    # Callbacks = function-pointers in C++ -> ich uebergebe die Funktion an die Funktion weiter. Die Funktion die den Callback aufruft entscheidet dann was sie mit dem Function-Pointer anfaengt
    # https://effbot.org/zone/tkinter-callbacks.htm -> Erklaerung callbacks und callbacks mit Uebergabeparametern
    if color == "red":
        color_rgb = "#FF0000"
    elif color == "yellow":
        color_rgb = "#FFFF00"
    else:
        color_rgb = "#8a2be2"

    if parameter_callback == False:
        B2 = Button(frame, text=button_text, bg=color_rgb, width=15, command=callback)
        B2.grid(row=row_button, column=col_button, padx=10, pady=3)
    else:
        B1 = Button(frame, text=button_text, bg=color_rgb, width=15, command=lambda: callback1(parameter_callback))
        B1.grid(row=row_button, column=col_button, padx=10, pady=3)


def insert_image(frame, row_frame, col_frame, path_to_img, size_w, size_h):
        # lade bild mit PIL
    img = Image.open(path_to_img)
    img = img.resize((size_w, size_h), Image.ANTIALIAS)
        # rescale image
    imageEx = ImageTk.PhotoImage(img)
        # erstelle Tkinter bild-objekt
    Label(frame, image=imageEx).grid(row=row_frame, column=col_frame, padx=10, pady=3)

def main():
    # Fuer das gui-image
    rescale_size_w = 200
    rescale_size_h = 150

    window = create_window("Test GUI")

    left_frame = create_frame(window, 200, 400, 0, 0)
    right_frame = create_frame(window, 400, 400, 0, 1)

    label_left_1 = create_label(left_frame, "Hier kommt die GUI", 0, 0, True)
    label_left_2 = create_label(left_frame, "Dieses Bild zeigt\nden neuen Audi R8:", 1, 0)

    img = Image.open("/home/jens/Schreibtisch/rasperry_pi/software/2019-audi-r8-v10-performance-looks-brutal-in-yellow-130641_1.jpg")
    img = img.resize((200, 150), Image.ANTIALIAS)
        # rescale image
    imageEx = ImageTk.PhotoImage(img)
        # erstelle Tkinter bild-objekt
    Label(left_frame, image=imageEx).grid(row=2, column=0, padx=10, pady=3)
    #insert_image(left_frame, 2, 0, "/home/jens/Schreibtisch/rasperry_pi/software/2019-audi-r8-v10-performance-looks-brutal-in-yellow-130641_1.jpg", 200, 150)

    E1 = create_entry(right_frame, 50, 0, 0)

    # erstelle Frame fuer Button in Frame vorhandenem Frame
    button_frame = Frame(right_frame)
    button_frame.grid(row=1, column=0, padx=1, pady=3)

    create_button(button_frame, "Button 1", "red", callback1, 0, 0, parameter_callback=E1)
    create_button(button_frame, "Button 2", "yellow", callback2, 0, 1)

    Slider = Scale(right_frame, from_=0, to=100, resolution=0.1, orient=HORIZONTAL, length=400)
    Slider.grid(row=2, column=0, padx=10, pady=3)

    window.mainloop() # GUI wird upgedated. Danach keine Elemente setzen



if __name__== "__main__": main()
# Das wird nur beim Aufrufen des Skripts ausgefuerht!
