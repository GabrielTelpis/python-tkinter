from tkinter import *
from tkinter import colorchooser

master = Tk()

master.geometry("767x494+388+258")
master.title("Selecionador De Cores")
master.iconbitmap(default="icones\\pincel.ico")
master.resizable(width=False, height=False)

# Importar imagens
imgFundo = PhotoImage(file="imagens\\fundo.png")

# Criação de Labels
labelFundo = Label(master, image=imgFundo)
labelFundo.pack()

label_cor1 = Label(master, bg="#d9d9d9")
label_cor1.place(width=670, height=103, x=8, y=18)

label_cor2 = Label(master, bg="#d9d9d9")
label_cor2.place(width=670, height=103, x=8, y=196)

label_cor3 = Label(master, bg="#d9d9d9")
label_cor3.place(width=670, height=103, x=8, y=373)

# Caixas de entrada
info_cor1 = Entry(master,  bg="#e5e5e9", justify="center", font=("Calibri", 19))
info_cor1.place(width=226, height=34, x=230, y=52)

info_cor2 = Entry(master, bg="#e5e5e9", justify="center", font=("Calibri", 19))
info_cor2.place(width=226, height=34, x=230, y=230)

info_cor3 = Entry(master, bg="#e5e5e9", justify="center", font=("Calibri", 19))
info_cor3.place(width=226, height=34, x=230, y=408)


# Funções
def obter_cor1():
    cor1 = colorchooser.askcolor()
    hex_cor1 = cor1[1].upper()
    label_cor1["bg"] = hex_cor1

    info_cor1.delete(0, END)
    info_cor1.insert(0, hex_cor1)

    master.clipboard_clear()
    master.clipboard_append(hex_cor1)

    info_cor1["bg"] = "#93FE83"
    info_cor2["bg"] = "#d9d9d9"
    info_cor3["bg"] = "#d9d9d9"


def obter_cor2():
    cor2 = colorchooser.askcolor()
    hex_cor2 = cor2[1].upper()
    label_cor2["bg"] = hex_cor2

    info_cor2.delete(0, END)
    info_cor2.insert(0, hex_cor2)

    master.clipboard_clear()
    master.clipboard_append(hex_cor2)

    info_cor1["bg"] = "#d9d9d9"
    info_cor2["bg"] = "#93FE83"
    info_cor3["bg"] = "#d9d9d9"


def obter_cor3():
    cor3 = colorchooser.askcolor()
    hex_cor3 = cor3[1].upper()
    label_cor3["bg"] = hex_cor3

    info_cor3.delete(0, END)
    info_cor3.insert(0, hex_cor3)

    master.clipboard_clear()
    master.clipboard_append(hex_cor3)

    info_cor1["bg"] = "#d9d9d9"
    info_cor2["bg"] = "#d9d9d9"
    info_cor3["bg"] = "#93FE83"


# Criação de Botões
bt1 = Button(master, text="COR 1", command=obter_cor1)
bt1.place(width=63, height=59, x=693, y=39)

bt2 = Button(master, text="COR 2", command=obter_cor2)
bt2.place(width=63, height=59, x=693, y=217)

bt3 = Button(master, text="COR 3", command=obter_cor3)
bt3.place(width=63, height=59, x=693, y=395)

master.mainloop()
