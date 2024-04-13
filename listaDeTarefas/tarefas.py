import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

# Funções ---------------------


def adicionarTarefa():
    tarefa = tarefa_entrada.get().capitalize()
    if tarefa:
        lista_tarefas.insert(0, tarefa) #Para inserir algo
        tarefa_entrada.delete(0, END) # Limpando o Input depois de adicionar a tarefa
        salvarTarefas()
    else:
        messagebox.showerror('Error', 'Digite uma Tarefa !')
        

def apagarTarefa():
   selecionada = lista_tarefas.curselection()
   if selecionada:
       lista_tarefas.delete(selecionada[0]) # Apaga na localização selecionada
       salvarTarefas()
   else:
       messagebox.showerror('Error', 'Escolha uma tarefa para deletar ')
    
def salvarTarefas():
    with open('tarefas.txt', 'w') as f:
        tarefas = lista_tarefas.get(0, END)
        for x in tarefas:
            f.write(x + '\n')

def carregar_tarefas():
    with open('tarefas.txt', 'r') as f:
        tarefas= f.readlines()
        for x in tarefas:
            lista_tarefas.insert(0, x.strip())
# Interface -------------------

janela = ctk.CTk("#09112e")
janela.minsize(350,450)
janela.maxsize(350,500)
janela.title('Lista de Tarefas V1.0')

# Reserva de fontes ------------

font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 10, 'bold')

#  ----------------------------

ctk.CTkLabel(janela, text='Lista de Tarefas V1.0', font=font1, text_color='white').pack(pady=10)

add_botao = ctk.CTkButton(janela, text='Adicionar Tarefa', font=font2,text_color='white',
fg_color= 'blue', cursor='heart', corner_radius=5, width=120, command=adicionarTarefa)
add_botao.place(x=20, y=80)

remove_botao = ctk.CTkButton(janela, text='Excluir Tarefa', font=font2,text_color='white',
fg_color= 'darkred', cursor='heart', corner_radius=5, width=120, command=apagarTarefa)
remove_botao.place(x=195, y=80)

tarefa_entrada = ctk.CTkEntry(janela, font=font2, text_color='black', fg_color='white', border_color='white', width=250,placeholder_text='Digite a sua tarefa')
tarefa_entrada.place(x=50, y= 130)

lista_tarefas = Listbox(janela, width=45, height=15, font=font3)
lista_tarefas.place(x=15.5, y=180)

janela.mainloop()