import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

def adicionarContato():
    
    nome = nomeE.get().capitalize()
    telefone = telefoneE.get()
    email = emailE.get()
    
    contato = f"Nome: {nome}  Telefone: {telefone}  E-mail: {email}"
    if contato:
        lista_contatos.insert(0,contato)
        nomeE.delete(0, END) 
        telefoneE.delete(0, END) 
        emailE.delete(0, END) 
        salvarContato()
    else:
        messagebox.showerror('Error', 'Digite um contato !')
        
def removerContato():
   selecionada = lista_contatos.curselection()
   if selecionada:
       lista_contatos.delete(selecionada[0])    
       salvarContato()
   else:
       messagebox.showerror('Error', 'Escolha um contato para deletar ')
       
def salvarContato():
    with open('contatos.txt', 'w') as f:
        contato = lista_contatos.get(0, END)
        for x in contato:
            f.write(x + '\n')

def carregar_Contato():
    with open('contatos.txt', 'r') as f:
        contato = f.readlines()
        for x in contato:
            lista_contatos.insert(0, x.strip())

janela = ctk.CTk()
janela.minsize(530,500)
janela.maxsize(640,600)
janela.title('Agenda de Contatos')

ctk.CTkLabel(janela, text='Agenda de Contatos',font=("Arial", 16, "bold"), text_color='white').pack(pady=10)

adicionar_contato =  ctk.CTkButton(janela, font=("Arial", 12, "bold"), text='Adicionar contato',text_color='white',
fg_color= 'blue', corner_radius=5, width=120, command=adicionarContato)
adicionar_contato.place(x=150, y=80)

remover_contato =  ctk.CTkButton(janela, font=("Arial", 12, "bold"), text='Excluir contato',text_color='white',
fg_color= 'red', corner_radius=5, width=120, command=removerContato)
remover_contato.place(x=280, y=80)

nomeE = ctk.CTkEntry(janela, font=("Arial", 12, "bold"), text_color='black', fg_color='white', border_color='white', width=250 ,placeholder_text='Digite Nome')
nomeE.place(x=150, y= 130)

telefoneE = ctk.CTkEntry(janela, font=("Arial", 12, "bold"), text_color='black', fg_color='white', border_color='white', width=250 ,placeholder_text='Digite telefone')
telefoneE.place(x=150, y= 160)

emailE = ctk.CTkEntry(janela, font=("Arial", 12, "bold"), text_color='black', fg_color='white', border_color='white', width=250 ,placeholder_text='Digite Email')
emailE.place(x=150, y= 190)

lista_contatos = Listbox(janela, width=55, height=12, font=("Arial", 12, "bold"))
lista_contatos.place(x=14, y=230)

janela.mainloop()