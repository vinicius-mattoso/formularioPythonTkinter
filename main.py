# import libs
from tkinter import*
from tkcalendar import Calendar, DateEntry
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

# Criação de uma janela do tkinter

janela  = Tk()

# Título da janela
janela.title("Vinicius Mattoso Support")

# Geometria da janela
janela.geometry('1043x453')

# Colocando um fundo na janela
janela.configure(background=co9)

# Limitar que o usuário mude o tamanho da janela
janela.resizable(width=False, height=False)


############ Criação dos Frames da Janela #########
#_________________________________________________
# |            |                                 |
# |     CIMA   |                                 |
# |____________|             DIREITA             |
# |            |                                 |
# |    BAIXO   |                                 |
# |            |                                 |
#--------------------------------------------------

# Frame de cima é um frame que vai estar dentro da janela e definimos o tamanho, cor de fundo e estilo
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')

# Posicionando o frame_cima
frame_cima.grid(row=0, column=0)

# Criando um frame para parte de baixo
frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

# Criando um frame para parte de baixo
frame_direita = Frame(janela, width=310, height=403, bg=co1, relief='flat')
# Nesse caso queremos que ele se expanda por duas linhas
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Criação do Label do formulério
app_nome = Label(frame_cima, text='Formulário de Consultoria',anchor=NW, font=('Ivy 13 bold'), bg=co2,fg = co1, relief='flat')
app_nome.place(x=30, y=10)

########## Criando os Labels de input no Frame de Baixo ###########
############
# NOME 
############
var_nome = Label(frame_baixo, text='Nome:',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg = co4, relief='flat')
var_nome.place(x=30, y=10)
input_nome = Entry(frame_baixo,width=40,justify='left',bg=co1, relief='solid')
input_nome.place(x=30, y=30)

############
# EMAIL
#############
var_email = Label(frame_baixo, text='Email:',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg = co4, relief='flat')
var_email.place(x=30, y=70)
input_email = Entry(frame_baixo,width=40,justify='left',bg=co1, relief='solid')
input_email.place(x=30, y=100)

############
# TELEFONE
############
var_telefone = Label(frame_baixo, text='Telefone:',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg = co4, relief='flat')
var_telefone.place(x=30, y=130)
input_telefone = Entry(frame_baixo,width=40,justify='left',bg=co1, relief='solid')
input_telefone.place(x=30, y=160)

############
# Data da Consulta
############
var_data = Label(frame_baixo, text='Data da Consulta:',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg = co4, relief='flat')
var_data.place(x=30, y=190)
input_data = DateEntry(frame_baixo,width=15,background='darkblue', foregrounf='white',borderwidth=2, year=2023)
input_data.place(x=30, y=210)

############
# Estado
#! Atualizar para isso ser um drawdwon com: Marcado, Confirmado, Ausente, Realizada
############
var_estado = Label(frame_baixo, text='Estado da Consulta:',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg = co4, relief='flat')
var_estado.place(x=160, y=190)
input_estado = Entry(frame_baixo,width=20,justify='left',bg=co1, relief='solid')
input_estado.place(x=160, y=210)

############
# Sobre
############
var_nome = Label(frame_baixo, text='Informação Extra:',anchor=NW, font=('Ivy 10 bold'), bg=co1,fg = co4, relief='flat')
var_nome.place(x=30, y=250)
input_nome = Entry(frame_baixo,width=40,justify='left',bg=co1, relief='solid')
input_nome.place(x=30, y=280)

############
# Botão Inserir
############
# Overrelief é semelhante ao rover
button_inserir = Button(frame_baixo, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
button_inserir.place(x=15, y = 320)

############
# Botão Editar
############
# Overrelief é semelhante ao rover
button_editar = Button(frame_baixo, text='Editar', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
button_editar.place(x=120, y = 320)

############
# Botão Excluir
############
# Overrelief é semelhante ao rover
button_excluir = Button(frame_baixo, text='Excluir', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
button_excluir.place(x=220, y = 320)

# main loop da janela
janela.mainloop()
