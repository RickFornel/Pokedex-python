from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from dados import *

# cores

cor0 = '#444466' # preto
cor1 = '#feffff' # branco
cor2 = '#6f9fbd' # azul
cor3 = '#38576b' # valor
cor4 = '#403d3d' # letras
cor5 = '#ef5350' # vermelho

# janela

janela = Tk()
janela.geometry('550x510')
janela.config(bg=cor1)
janela.title('')
janela.resizable(width=FALSE, height=FALSE)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use('clam')

# frames

frame_pokemon = Frame(janela, width=550, height=290, relief='flat', bg=cor1)
frame_pokemon.grid(row=1, column=0)

# funções

def trocar_pokemon(i):
    global im_pok, im_pok_1

    label_nome_pok['text'] = i
    frame_pokemon['bg'] = pokemon[i]['tipo'][3]
    label_tipo_pok['text'] = pokemon[i]['tipo'][1]
    label_id_pok['text'] = pokemon[i]['tipo'][0]
    label_hp_pok['text'] = pokemon[i]['status'][0]
    label_ataque_pok['text'] = pokemon[i]['status'][1]
    label_defesa_pok['text'] = pokemon[i]['status'][2]
    label_velocidade_pok['text'] = pokemon[i]['status'][3]
    label_total_pok['text'] = pokemon[i]['status'][4]
    label_hb1_pok['text'] = pokemon[i]['habilidades'][0]
    label_hb2_pok['text'] = pokemon[i]['habilidades'][1]

    label_nome_pok['bg'] = pokemon[i]['tipo'][3]
    label_tipo_pok['bg'] = pokemon[i]['tipo'][3]
    label_id_pok['bg'] = pokemon[i]['tipo'][3]



    im_pok = pokemon[i]['tipo'][2]
    im_pok = Image.open(im_pok)
    im_pok = im_pok.resize((238,238))
    im_pok = ImageTk.PhotoImage(im_pok)

    
    label_im_pok = Label(frame_pokemon, relief='flat', image=im_pok, bg=pokemon[i]['tipo'][3], fg=cor0)
    label_im_pok.place(x=60, y=50)

    label_tipo_pok.lift()

# labels

# nome
label_nome_pok = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font='Fixedsys 20', bg=cor1, fg=cor0)
label_nome_pok.place(x=12, y=15)

# Tipo 
label_tipo_pok = Label(frame_pokemon, text='Elétrico', relief='flat', anchor=CENTER, font='Ivy 10 bold', bg=cor1, fg=cor0)
label_tipo_pok.place(x=12, y=50)

# Id
label_id_pok = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font='Ivy 10 bold', bg=cor1, fg=cor0)
label_id_pok.place(x=12, y=75)

# status 
label_status_pok = Label(janela, text='Status', relief='flat', anchor=CENTER, font='Verdana 20', bg=cor1, fg=cor0)
label_status_pok.place(x=15, y=310)

# hp 
label_hp_pok = Label(janela, text='HP:  300', relief='flat', anchor=CENTER, font='Verdana 10 bold', bg=cor1, fg=cor0)
label_hp_pok.place(x=15, y=360)

# ataque 
label_ataque_pok = Label(janela, text='Ataque:  600', relief='flat', anchor=CENTER, font='Verdana 10 bold', bg=cor1, fg=cor0)
label_ataque_pok.place(x=15, y=385)

# defesa
label_defesa_pok = Label(janela, text='Defesa:  500', relief='flat', anchor=CENTER, font='Verdana 10 bold', bg=cor1, fg=cor0)
label_defesa_pok.place(x=15, y=410)

# velocidade
label_velocidade_pok = Label(janela, text='Velocidade:  300', relief='flat', anchor=CENTER, font='Verdana 10 bold', bg=cor1, fg=cor0)
label_velocidade_pok.place(x=15, y=435)

# total
label_total_pok = Label(janela, text= 'Total:  1700', relief='flat', anchor=CENTER, font='Verdana 10 bold', bg=cor1, fg=cor0)
label_total_pok.place(x=15, y=460)

# habilidades 
label_habilidades_pok = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font='Verdana 20', bg=cor1, fg=cor0)
label_habilidades_pok.place(x=180, y=310)

# habilidade 1 - hb1
label_hb1_pok = Label(janela, text='Choque do Trovão', relief='flat', anchor=CENTER, font='Verdana 10 bold', bg=cor1, fg=cor0)
label_hb1_pok.place(x=180, y=360)

# habilidade 2 - hb2 
label_hb2_pok = Label(janela, text='Cabeçada', relief='flat', anchor=CENTER, font='Verdana 10 bold', bg=cor1, fg=cor0)
label_hb2_pok.place(x=180, y=385)

Lambda:trocar_pokemon('Pikachu')

# criando botoes 

# botao pikachu
im_pok_1 = Image.open('cabeca-pikachu.png')
im_pok_1 = im_pok_1.resize((40,40))
im_pok_1 = ImageTk.PhotoImage(im_pok_1)

button_pok_1 = Button(frame_pokemon, command=lambda:trocar_pokemon('Pikachu'), image=im_pok_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font='Verdana 12 bold', bg=cor1, fg=cor0)
button_pok_1.place(x=375, y=10)

# botao bulbasaur
im_pok_2 = Image.open('cabeca-bulbasaur.png')
im_pok_2 = im_pok_2.resize((40,40))
im_pok_2 = ImageTk.PhotoImage(im_pok_2)

button_pok_2 = Button(frame_pokemon,command=lambda:trocar_pokemon('Bulbasaur'), image=im_pok_2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font='Verdana 12 bold', bg=cor1, fg=cor0)
button_pok_2.place(x=375, y=65)

# botao charmander
im_pok_3 = Image.open('cabeca-charmander.png')
im_pok_3 = im_pok_3.resize((40,40))
im_pok_3 = ImageTk.PhotoImage(im_pok_3)

button_pok_3 = Button(frame_pokemon,command=lambda:trocar_pokemon('Charmander'), image=im_pok_3, text='Charmander', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font='Verdana 12 bold', bg=cor1, fg=cor0)
button_pok_3.place(x=375, y=120)

# botao gyarados
im_pok_4 = Image.open('cabeca-gyarados.png')
im_pok_4 = im_pok_4.resize((40,40))
im_pok_4 = ImageTk.PhotoImage(im_pok_4)

button_pok_4 = Button(frame_pokemon, command=lambda:trocar_pokemon('Gyarados'),image=im_pok_4, text='Gyarados', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font='Verdana 12 bold', bg=cor1, fg=cor0)
button_pok_4.place(x=375, y=175)

# botao gengar
im_pok_5 = Image.open('cabeca-gengar.png')
im_pok_5 = im_pok_5.resize((40,40))
im_pok_5 = ImageTk.PhotoImage(im_pok_5)

button_pok_5 = Button(frame_pokemon, command=lambda:trocar_pokemon('Gengar'), image=im_pok_5, text='Gengar', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font='Verdana 12 bold', bg=cor1, fg=cor0)
button_pok_5.place(x=375, y=230)

# botao dragonite
im_pok_6 = Image.open('cabeca-dragonite.png')
im_pok_6 = im_pok_6.resize((40,40))
im_pok_6 = ImageTk.PhotoImage(im_pok_6)

button_pok_6 = Button(janela, command=lambda:trocar_pokemon('Dragonite'), image=im_pok_6, text='Dragonite', width=150, relief='raised', overrelief=RIDGE,compound=LEFT, padx=5, anchor=NW, font='Verdana 12 bold', bg=cor1, fg=cor0)
button_pok_6.place(x=375, y=285)



janela.mainloop()