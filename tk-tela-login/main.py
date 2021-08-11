from tkinter import *
import time

master = Tk()
master.title("Portal de alunos 2021")
master.geometry("490x560+610+153")
master.iconbitmap(default="icones\\ico.ico")
master.resizable(width=1, height=1)


# Funções
def nova_janela():
    master.destroy()
    time.sleep(0.3)

    master1 = Tk()
    master1.title("Nova Janela criada!!")
    master1.geometry("490x560+400+153")


# Variáveis globais
esconda_senha = StringVar()

# Importar imagens
img_fundo = PhotoImage(file="imagens\\fundo.png")
img_botao = PhotoImage(file="imagens\\bt-img.png")

# Criação de labels
lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

# Criação de caixas de entrada
en_token = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
en_token.place(width=392, height=45, x=49, y=138)

en_email = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
en_email.place(width=392, height=45, x=49, y=244)

en_senha = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
en_senha.place(width=392, height=45, x=49, y=355)


# Criação de botões
bt_entrar = Button(master, bd=0, image=img_botao, command=nova_janela)
bt_entrar.place(width=118, height=64, x=186, y=448)

master.mainloop()
