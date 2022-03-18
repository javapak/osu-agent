import osrparsing as osr
import osuparsing as osu
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import ntpath as nt
import numpy as np
import pandas as pd




root = tk.Tk()
root.title('deepsu! osu + osr to csv for training')
root.geometry('400x400')



def select_file_osu():
    ftype = (
        ('osu! beatmap file', '*.osu'),
        ('all files', '*.*')
    )

    fname = fd.askopenfilename(
        title='Load a .osu file.',
        initialdir='C:/Users/apaki/Desktop/replaysandbeatmaps/',
        filetypes=ftype
    )
    if (fname != ''):
        messagebox.showinfo("osu! beatmap loaded.", "Beatmap loaded successfully")
        global mapname
        mapname = nt.basename(fname)
        global fnameosu
        fnameosu = fname
    
def select_file_osr():
    ftype = (
        ('osu! replay file', '*.osr'),
        ('all files', '*.*')
    )

    fname = fd.askopenfilename(
        title='Load a .osr file.',
        initialdir='C:/Users/apaki/Desktop/replaysandbeatmaps/',
        filetypes=ftype
    )
    if (modcheck(fname) == True):
        global fnameosr
        fnameosr = fname
    
def modcheck(dotosr):
    flag = osr.modcheck(dotosr)
    if (flag == False):
        messagebox.showerror("Mods present in replay.", "Mods are not currently supported as training data for deepsu!")
        select_file_osr()
    else:
        messagebox.showinfo("File successfully loaded", "No mods detected, osr is compatible.")
    return flag

def convert2csv(fnameosu, fnameosr):
    print(fnameosu)
    print(fnameosr)
    parsedosu = osu.parseosu(fnameosu)
    parsedosr = osr.parseosr(fnameosr)
    data_x = np.array(parsedosu.xytimetype, dtype = "float")
    data_y = np.array(parsedosr.xytimetimedeltakeys, dtype = "float")
    data_x = np.append(data_x, np.repeat(np.nan, (data_y.size-data_x.size)))
    df = pd.DataFrame({"beatmap": data_x, "replay": data_y})
    df.to_csv("C:/Users/apaki/Documents/combinedosuosr" + mapname + ".csv")
    messagebox.showinfo("csv written", "File was written successfully!")
    
    
open_button = ttk.Button(
    root,
    text='Open a .osu file',
    command=select_file_osu
)

open_button2 = ttk.Button(
    root,
    text='Open a .osr file',
    command=select_file_osr
)

convert_button = ttk.Button(
    root,
    text ='Convert to concatenated .csv',
    command= lambda: convert2csv(fnameosu, fnameosr)
   )


label = tk.Label(root, text="deepsu! dataset utility", font="Calibri 22")
label.pack()
open_button.pack(expand=True)
open_button2.pack(expand=True)
convert_button.pack(expand=True)
root.mainloop()

    
    
        




