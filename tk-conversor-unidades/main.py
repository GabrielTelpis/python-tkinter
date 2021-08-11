from tkinter import *
from tkinter import ttk

master = Tk()
master.geometry("876x291+527+312")
master.iconbitmap(default="icones\\ico.ico")
master.wm_resizable(width=False, height=False)
master.title("Youtube  Gabriel Telpis  Programação & Eletrônica")

listaOp = [
    "Mili (m)",
    "Micro (u)",
    "Nano  (n)",
    "Pico  (p)",
    "Unidade",
    "Quilo (k)",
    "Mega  (M)",
    "Giga  (G)",
    "Tera  (T)",
]

listaPotencias = [
    10 ** -3,
    10 ** -6,
    10 ** -9,
    10 ** -12,
    1,
    10 ** 3,
    10 ** 6,
    10 ** 9,
    10 ** 12
]


def converter():
    try:
        op1 = menu1.get()
        op2 = menu2.get()
        entrada = float(num1.get())

        pos_op1 = listaOp.index(op1)
        pos_op2 = listaOp.index(op2)

        calculo = (listaPotencias[pos_op1] / listaPotencias[pos_op2]) * entrada

        resultado['text'] = str(format(calculo, '.1E'))

    except ValueError:
        resultado['text'] = "SÓ NÚMEROS"


def limpar():
    num1.delete(0, END)
    resultado["text"] = ""


imgFundo = PhotoImage(file="imagens\\img.png")

labelFundo = Label(master, image=imgFundo)
labelFundo.place(x=0, y=0)

info = Label(master, text="CONVERSOR DE UNIDADES", bg="#EA4335", fg="white", font=("Calibri", 24, "bold"))
info.place(width=815, height=46, x=30, y=12)

resultado = Label(master, text="SAÍDA", font=("Calibri", 20), bg="#E0E0E0")
resultado.place(width=353, height=39, x=494, y=82)

num1 = Entry(master, font=("Calibri", 20), justify=CENTER, bg="#E0E0E0")
num1.place(width=351, height=39, x=31, y=84)
num1.insert(END, 1)

menu1 = ttk.Combobox(master, value=listaOp, justify='center', font=("Calibri", 18))
menu1.place(width=207, height=38, x=105, y=151)
menu1.current(4)

menu2 = ttk.Combobox(master, value=listaOp, justify='center', font=("Calibri", 18))
menu2.place(width=209, height=38, x=566, y=151)
menu2.current(0)

bt1 = Button(master, text="LIMPAR", font=("Calibri", 14, "bold"), bg="#EA4335", fg="white", command=limpar)
bt1.place(width=142, height=41, x=135, y=220)

bt2 = Button(master, text="CONVERTER", font=("Calibri", 14, "bold"), bg="#EA4335", fg="white", command=converter)
bt2.place(width=143, height=42, x=599, y=221)

master.mainloop()
