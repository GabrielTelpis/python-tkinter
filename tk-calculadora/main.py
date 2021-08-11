from tkinter import *
master = Tk()
master.title("--  Calculadora 1.0 --")
master.iconbitmap(default="icones\\calc.ico")
master.geometry("521x411+625+293")  # LARGURA X ALTURA + DIST ESQUERDA + DIST TOPO
master.wm_resizable(width=False, height=False)


# funções
def clique_esquerdo_mouse(arg):
    global flag, x1, y1
    flag = not flag

    if flag:
        x1 = arg.x
        y1 = arg.y

    else:
        print(f'width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1}')


def calcular(op):
    global resposta, num1, num2, x

    try:
        float(num1.get())
        float(num2.get())

        if op == 1:
            x = float(num1.get()) + float(num2.get())

        elif op == 2:
            x = float(num1.get()) - float(num2.get())

        elif op == 3:
            try:
                x = float(num1.get()) / float(num2.get())

            except ZeroDivisionError:
                x = 999999999999

        elif op == 4:
            x = float(num1.get()) * float(num2.get())

        return resposta.config(text=round(x, 4))

    except ValueError:
        resposta.config(text="Só Números")


# Variáveis Globais
flag = x1 = y1 = x = 0

# Importação de imagens
calculadoraImg = PhotoImage(file="imagens\\calc.png")

# Criação de Labels
fundoCalculadora = Label(master, image=calculadoraImg)
resposta = Label(master, font="Arial 40", text="0")

# Posicionar Labels
fundoCalculadora.place(x=0, y=0)
resposta.place(width=398, height=56, x=61, y=67)

# Criação dos botões
bt1 = Button(master, text="+", font="Arial 30", command=lambda: calcular(1))
bt2 = Button(master, text="-", anchor=S, font="Arial 30", command=lambda: calcular(2))
bt3 = Button(master, text="/", font="Arial 30", command=lambda: calcular(3))
bt4 = Button(master, text="*", anchor=N, font="Arial 30", command=lambda: calcular(4))

# Posicionar botões
bt1.place(width=87, height=42, x=34, y=314)
bt2.place(width=87, height=42, x=153, y=314)
bt3.place(width=87, height=42, x=273, y=314)
bt4.place(width=87, height=42, x=392, y=314)

# Caixas de entrada
num1 = Entry(master, font="Arial 20", justify=CENTER)
num2 = Entry(master, font="Arial 20", justify=CENTER)

# Posicionar caixas de entrada
num1.place(width=155, height=34, x=46, y=201)
num2.place(width=155, height=34, x=311, y=201)

# Valores iniciais de entrada
num1.insert(END, 0)
num2.insert(END, 0)

# Eventos
master.bind("<Button-1>", clique_esquerdo_mouse)
master.mainloop()

