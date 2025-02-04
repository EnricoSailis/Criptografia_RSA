
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("600x800")
window.configure(bg = "#3413FF")
window.title("Programma di Cifratura RSA - Versione 02")

canvas = Canvas(
    window,
    bg = "#3413FF",
    height = 800,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,

    command=lambda: decriptaTesto(),

    relief="flat"
)
button_1.place(
    x=338.0,
    y=687.0,
    width=135.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: criptaTesto(),
    relief="flat"
)
button_2.place(
    x=138.0,
    y=684.0,
    width=135.0,
    height=40.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    302.0,
    607.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=47.0,
    y=574.0,
    width=510.0,
    height=64.0
)

canvas.create_text(
    40.0,
    558.0,
    anchor="nw",
    text="Testo criptato",
    fill="#FBF8F8",
    font=("Inter ExtraBold", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    302.0,
    487.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=47.0,
    y=454.0,
    width=510.0,
    height=64.0
)

canvas.create_text(
    42.0,
    437.0,
    anchor="nw",
    text="Testo in chiaro",
    fill="#FBF8F8",
    font=("Inter ExtraBold", 14 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    302.0,
    376.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#8676EC",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=47.0,
    y=343.0,
    width=510.0,
    height=64.0
)

canvas.create_text(
    42.0,
    326.0,
    anchor="nw",
    text="Modulo n",
    fill="#FBF8F8",
    font=("Inter ExtraBold", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    300.0,
    266.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#8676EC",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=45.0,
    y=233.0,
    width=510.0,
    height=64.0
)

canvas.create_text(
    40.0,
    216.0,
    anchor="nw",
    text="Chiave Pubblica",
    fill="#FBF8F8",
    font=("Inter ExtraBold", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    300.0,
    152.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#8676EC",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=45.0,
    y=119.0,
    width=510.0,
    height=64.0
)

canvas.create_text(
    42.0,
    99.0,
    anchor="nw",
    text="Chiave Privata",
    fill="#FBF8F8",
    font=("Inter ExtraBold", 14 * -1)
)

canvas.create_text(
    155.0,
    40.0,
    anchor="nw",
    text="Interfaccia grafica creata con Tkinter Designer",
    fill="#FBF8F8",
    font=("Inter ExtraBold", 14 * -1)
)

# FUNZIONI

# Trasforma una stringa di caratteri ascii in un numero intero 
def DaStringaANumero(testo):
    n=0
    for c in testo:
        n=n*256+ord(c)
    return n

# Trasforma un numero intero in una stringa di caratteri ASCII esteso 
def DaNumeroAStringa(m):
    testo = ''
    n=int(m)
    while n > 0 :
        r = n % 256
        c = chr(r)
        testo = c + testo
        n = n // 256
    return testo

def criptaTesto():
    text_content = entry_2.get("1.0", "end")
    b = int(DaStringaANumero(text_content))
    K = int(entry_5.get("1.0", "end"))
    n = int(entry_3.get("1.0", "end"))
    # Calcola la potenza b^K in Zn
    x=b
    y=K
    z=1
    while y>0:
        if y%2==1:
            z=z*x
            z=z%n
            y=y-1
        x=x*x
        x=x%n
        y=y//2

    # carica la potenza z=b^K modulo(n) nell'area criptata 
    entry_1.delete("1.0","end")
    entry_1.insert("1.0",z)

def decriptaTesto():
    b = int(entry_1.get("1.0", "end"))
    H = int(entry_4.get("1.0", "end"))
    n = int(entry_3.get("1.0", "end"))
    # Calcola la potenza b^H in Zn
    x=b
    y=H
    z=1
    while y>0:
        if y%2==1:
            z=z*x
            z=z%n
            y=y-1
        x=x*x
        x=x%n
        y=y//2

    # carica la potenza  z=b^H modulo(n) nell'area in chiaro 
    # dopo averla trasformata in testo
    testo_in_chiaro=DaNumeroAStringa(z)
    entry_2.delete("1.0","end")
    entry_2.insert("1.0",testo_in_chiaro)



window.resizable(False, False)
window.mainloop()
