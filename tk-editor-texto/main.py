from tkinter import *
from tkinter import filedialog

master = Tk()
master.title("Editor de Texto 1.0")
master.iconbitmap(default="icones\\lapis.ico")
master.geometry("954x905+317+34")
master.wm_resizable(width=False, height=False)


def limpar():
    textoDescricao.delete("1.0", END)
    textoTitulo.delete("1.0", END)
    textoTags.delete("1.0", END)

    contDescricao.config(text=0)
    contTitulo.config(text=0)
    contTags.config(text=0)


def contar():
    a = len(textoTitulo.get('1.0', END))
    a = a - 1

    b = len(textoDescricao.get('1.0', END))
    b = b - 1

    c = len(textoTags.get('1.0', END))
    c = c - 1

    contTitulo.config(text=a)
    contDescricao.config(text=b)
    contTags.config(text=c)


def salvar():
    arquivo = filedialog.asksaveasfile(defaultextension='.txt',
        filetypes=[("Documento de Texto", ".txt")])
    titulo = str(textoTitulo.get(1.0, END))
    descricao = str(textoDescricao.get(1.0, END))
    tag = str(textoTags.get(1.0, END))

    arquivo.write(titulo + "\n")
    arquivo.write(descricao + "\n")
    arquivo.write(tag + "\n")


# Importar imagens
fundoImg = PhotoImage(file="imagens\\fundo.png")

# Criação de labels
fundoInterface = Label(master, image=fundoImg)
fundoInterface.place(x=0, y=0)

contTitulo = Label(master, text="", font=("Calibri", 14), background="#FFFFFF")
contTitulo.place(width=98, height=67, x=836, y=504)

contDescricao = Label(master, text="", font=("Calibri", 14), background="#FFFFFF")
contDescricao.place(width=98, height=67, x=836, y=583)

contTags = Label(master, text="", font=("Calibri", 14), background="#FFFFFF")
contTags.place(width=97, height=66, x=836, y=664)

# Criação de frames
frameTitulo = Frame(master)
frameTitulo.place(width=802, height=42, x=12, y=21)

frameDescricao = Frame(master)
frameDescricao.place(width=801, height=579, x=12, y=73)

frameTag = Frame(master)
frameTag.place(width=803, height=222, x=12, y=663)

# Criação da barra lateral
barraLateral1 = Scrollbar(frameDescricao)
barraLateral1.pack(side=RIGHT, fill=Y)

barraLateral2 = Scrollbar(frameTag)
barraLateral2.pack(side=RIGHT, fill=Y)

# Criação de caixas de texto
textoTitulo = Text(frameTitulo, font=("Calibri", 20), selectbackground="#F5F799", selectforeground="black")
textoTitulo.place(width=802, height=42, x=0, y=0)

textoDescricao = Text(frameDescricao, font=("Calibri", 16), selectbackground="#F5F799", selectforeground="black",
                      wrap=WORD, undo=True, yscrollcommand=barraLateral1.set)
textoDescricao.place(width=784, height=579, x=0, y=0)

textoTags = Text(frameTag, font=("Calibri", 16), selectbackground="#F5F799", selectforeground="black",
                 yscrollcommand=barraLateral2.set)
textoTags.place(width=786, height=222, x=0, y=0)

# Configura a barra lateral
barraLateral1.config(command=textoDescricao.yview)
barraLateral2.config(command=textoTags.yview)

# Criação dos Botões
bt1 = Button(master, text="Salvar", font=("Calibri", 16), background="white", command=salvar)
bt1.place(width=100, height=51, x=834, y=22)

bt2 = Button(master, text="Limpar", font=("Calibri", 16), background="white", command=limpar)
bt2.place(width=100, height=52, x=834, y=123)

bt3 = Button(master, text="Contar", font=("Calibri", 16), background="white", command=contar)
bt3.place(width=100, height=51, x=834, y=228)

bt4 = Button(master, text="+", font=("Calibri", 17), background="white")
bt4.place(width=101, height=53, x=833, y=329)

# Fim
master.mainloop()
